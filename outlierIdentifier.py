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
    
    inputMethod = input()
    if (inputMethod == 'P' or inputMethod == 'p'):
        print("Please enter the pathname: ")
        pathname = input()
        file = open(pathname,"r")
        
    elif (inputMethod == 'F' or inputMethod == 'f'):
        print("Please enter the filename: ")
        filename = input()
        file = open(filename,"r")
        
    print("Line 2 is: ")
    print(file.readline())
       
    print("Line 3 is: ")
    print(file.readline())
    
    file.close()
    

def introductionScreen():
    print("Welcome to the Outlier Identifier Program")
    print("This program identifies and outputs any outliers that may be found in a data set")
    print("You can connect to the data set of interest via pathname or filename")
    print("To begin, enter one of the following: ")
    print("P - For Pathname")
    print("F - For Filename (Note: Must be in current directory")
    
if (__name__ == "__main__"):
    main()
