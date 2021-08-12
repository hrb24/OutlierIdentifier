#This program identifies any outlier data points from a given input file

import numpy as np

def main():
    introductionScreen()
        
        # ------------------------------------------------------------- #
        # The below block of code is for testing purposes only and      #
        # should be commented out when the program is being used for a  #
        # data set other than testData.txt                              #
        # --------------------------------------------------------------#
       
        # file = open("testData.txt","r")
        # print("Line 1 is: ")
        # print(file.readline())
        # print("Line 2 is: ")
        # print(file.readline())
        # print("Line 3 is: ")
        # print(file.readline())
        # file.close()
       
    file = inputMethod()
    array = populateArray(file)
    outlierMethod(array)
    file.close()

# ----------------------------------------------------------------- #
#                   Method introductionScreen()                     #
# This method is responsible for outputting some initial welcome    #
# statements to introduce the user to the program and prompt them   #
# to choose how they will connect the program to their data source  #
# ----------------------------------------------------------------- #
def introductionScreen():
    print("Welcome to the Outlier Identifier Program")
    print("Author: hrb24")
    print("Last edit: 08/12/2021")
    print("This program identifies and outputs any outliers that may be found in a data set")
    print("Note: Each numeric datum should be on its own line in the .txt file and there should be at least 10 points")
    print("You can connect to the data set of interest via pathname or filename")

# ----------------------------------------------------------------- #
#                   Method inputMethod()                            #
# This method prompts the user to enter their input method along    #
# with a file name or pathname before opening the file of choice    #
# ----------------------------------------------------------------- #
def inputMethod():
    inputDone = False
    while (not inputDone):
        print("To begin, enter one of the following: ")
        print("P - For Pathname")
        print("F - For Filename (Note: Must be in current directory")
        inputMethod = input()
        if (inputMethod == 'P' or inputMethod == 'p'):
            print("Please enter the pathname: ")
            while True:
                try:
                    pathname = input()
                    file = open(pathname,"r")
                    break
                except:
                    print("Oops! That was not a valid pathname. Try again...")
            inputDone = True
        elif (inputMethod == 'F' or inputMethod == 'f'):
            print("Please enter the filename: ")
            while True:
                try:
                    filename = input()
                    file = open(filename,"r")
                    break
                except:
                    print("Oops! That was not a valid Filename. Try again...")
            inputDone = True
        else:
            print("Your input is invalid")
    return file
    
# ----------------------------------------------------------------- #
#                       Method populateArray                        #
# This method populates an array with the data from the inputted    #
# data file and converts all values from NumPy strings to float     #
# variables                                                         #
# ----------------------------------------------------------------- #
def populateArray(file):
    arrayTemp = np.array(file.readlines())
    array = arrayTemp.astype(np.float)
    return array
        
# ----------------------------------------------------------------- #
#                       Method outlierMethod()                      #
# This method prompts the user as to which outlier method they want #
# to use as well as what they want their cutoff (No. of STDV/IQRs)  #
# to be                                                             #
# ----------------------------------------------------------------- #
def outlierMethod(array):
    outlierDone = False
    print("Next, select how you want to define an outlier. You can use the data's Standard Devation")
    print("(STDV) or Inter Quartile Range (IQR) to do this")
    while (not outlierDone):
        print("To choose, enter one of the options below: ")
        print("S - For Standard Deviation")
        print("I - For Inter Quartile Range")
            
        outlierMethod = input()
        if (outlierMethod == 'S' or outlierMethod == 's'):
            print("Please enter the number of standard deviations away from the mean you would like")
            print("to be consider an outlier: ")
            print("Note: 3 standard deviations is a typical cutoff value")
            number = input()
            outlierSTDV(number,array)
            outlierDone = True
        elif (outlierMethod == 'I' or outlierMethod == 'i'):
            print("Please enter the number of IQRs away from the first or third quartiles you would like")
            print("to be consider an outlier: ")
            print("Note: 1.5 IQRs is a typical cutoff value")
            number = input()
            outlierIQR(number,array)
            outlierDone = True
        else:
            print("Your input is invalid")
            
# ----------------------------------------------------------------- #
#                   Method outlierIQR(number)                       #
# This method is the implementation for identifying outliers using  #
# the IQR method. The parameter 'number' is the number of IQRs      #
# above/below the third/first quartile that qualify as an outlier.  #
# The parameter 'array' is the array of data values                 #
# ----------------------------------------------------------------- #
def outlierIQR(number,array):
    # Sort the array read in from text file in ascending order
    sortedArray = np.sort(array)
    # Use the array size to determine the first and third quartile indices
    
    # Start with the first quartile index
    indexQ1 = (sortedArray.size) * 0.25
    # Check to see if quartile index needs to be rounded up or down
    if (indexQ1 > (int(indexQ1) + 0.5)):
        indexQ1 = int(indexQ1) + 1
    else:
        indexQ1 = int(indexQ1)
        
    # Now third quartile index
    indexQ3 = (sortedArray.size) * 0.75
    # Check to see if quartile needs to be rounded up or down
    if (indexQ3 > (int(indexQ3) + 0.5)):
        indexQ3 = int(indexQ3) + 1
    else:
        indexQ3 = int(indexQ3)
        
    # Calculate IQR
    firstQuartile = sortedArray[indexQ1]
    thirdQuartile = sortedArray[indexQ3]
    IQR = thirdQuartile - firstQuartile
        
    # Create and populate an array for outliers
    # Note: The array is initialized using the third quartile value
    # This can then be used to see if the array should be 'empty'
    
       
    print("Here is the array of your outliers: ")
    #if (arrayOutliers[0] = sortedArray[thirdQuartile]):
     #   print("No outliers in data set")
    
    
        
# ----------------------------------------------------------------- #
#                   Method outlierSTDV(number)                      #
# This method is the implementation for identifying outliers using  #
# the STDV method. The parameter 'number' is the number of STDVs    #
# above/below the sample mean that qualify as an outlier. The       #
# parameter 'array' is the array of data values                     #
# ----------------------------------------------------------------- #
def outlierSTDV(number,array):
    # Measure data and output outliers based on STDV approach
    print("Hello")
    
    
if (__name__ == "__main__"):
    main()
