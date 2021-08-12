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
    populateArray(file)
    outlierMethod()
    file.close()

# ----------------------------------------------------------------- #
#                   Method introductionScreen()                     #
# This method is responsible for outputting some initial welcome    #
# statements to introduce the user to the program and prompt them   #
# to choose how they will connect the program to their data source  #
# ----------------------------------------------------------------- #
def introductionScreen():
    print("Welcome to the Outlier Identifier Program")
    print("This program identifies and outputs any outliers that may be found in a data set")
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
            pathname = input()
            file = open(pathname,"r")
            inputDone = True
        elif (inputMethod == 'F' or inputMethod == 'f'):
            print("Please enter the filename: ")
            filename = input()
            file = open(filename,"r")
            inputDone = True
        else:
            print("Your input is invalid")
    return file
    
# ----------------------------------------------------------------- #
#                       Method populateArray                        #
# This method populates an array with the data from the inputted    #
# data file                                                         #
# ----------------------------------------------------------------- #
def populateArray(file):
    array = np.array(file.readlines())
    print("Here is the first element! Should be 20.00: ")
    print(array[0])
    print("There are this many elements in the array. Should be 1020: ")
    print(array.size)
    print("Now we will print array")
    for x in array:
        print(x)
        
# ----------------------------------------------------------------- #
#                       Method outlierMethod()                      #
# This method prompts the user as to which outlier method they want #
# to use as well as what they want their cutoff (No. of STDV/IQRs)  #
# to be                                                             #
# ----------------------------------------------------------------- #
def outlierMethod():
    outlierDone = False
    print("Next, select how you want to define an outlier. You can use the data's Standard Devation")
    print("or Inter Quartile Range (IQR) to do this")
    while (not outlierDone):
        print("To choose, enter one of the options below: ")
        print("S - For Standard Deviation")
        print("I - For Inter Quartile Range")
            
        outlierMethod = input()
        if (inputMethod == 'S' or inputMethod == 's'):
            print("Please enter the number of standard deviations away from the mean you would like")
            print("to be consider an outlier: ")
            print("Note: 3 standard deviations is a typical cutoff value")
            number = input()
            outlierSTDV(number)
            outlierDone = True
        elif (inputMethod == 'I' or inputMethod == 'i'):
            print("Please enter the number of IQRs away from the first or third quartiles you would like")
            print("to be consider an outlier: ")
            print("Note: 1.5 IQRs is a typical cutoff value")
            number = input
            outlierIQR(number)
            outlierDone = True
        else:
            print("Your input is invalid")
# ----------------------------------------------------------------- #
#                   Method outlierIQR(number)                      #
# This method is the implementation for identifying outliers using  #
# the IQR method. The parameter 'number' is the number of IQRs      #
# above/below the third/first quartile that qualify as an outlier   #
# ----------------------------------------------------------------- #
def outlierIQR(number):
    # Measure data and output outliers based on IQR approach
    print("Hello")
    
# ----------------------------------------------------------------- #
#                   Method outlierSTDV(number)                      #
# This method is the implementation for identifying outliers using  #
# the STDV method. The parameter 'number' is the number of STDVs    #
# above/below the sample mean that qualify as an outlier            #
# ----------------------------------------------------------------- #
def outlierSTDV(number):
    # Measure data and output outliers based on STDV approach
    print("Hello")
    
    
if (__name__ == "__main__"):
    main()
