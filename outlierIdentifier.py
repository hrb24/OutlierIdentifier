#This program identifies any outlier data points from a given input file

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
    outlierMethod()
    file.close()

def introductionScreen():
    print("Welcome to the Outlier Identifier Program")
    print("This program identifies and outputs any outliers that may be found in a data set")
    print("You can connect to the data set of interest via pathname or filename")

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
    
    def outlierMethod()
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
                number = input()
                outliersIQR(number)
                outlierDone = True
            else:
                print("Your input is invalid")
    
    def outliersIQR(number):
        # Measure data and output outliers based on IQR approach
        
    def outlierSTDV(number):
        # Measure data and output outliers based on STDV approach
        
    
    
if (__name__ == "__main__"):
    main()
