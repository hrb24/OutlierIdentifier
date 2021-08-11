#This program identifies any outlier data points from a given input file

def main():
    # ------------------------------------------------------------- #
    # The below block of code is for testing purposes only and      #
    # should be commented out when the program is being used for a  #
    # data set other than testData.txt                              #
    # --------------------------------------------------------------#
    
    file = open("testData.txt","r")
    
    print("Line 1 is: ")
    print(file.readline())
    
    print("Line 2 is: ")
    print(file.readline())
       
    print("Line 3 is: ")
    print(file.readline())
    
    file.close()
    
if (__name__ == "__main__"):
    main()
