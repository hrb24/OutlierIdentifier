# OutlierIdentifier

Program Description

The program inputs a .txt file of values, provided by the user. The file should contain no other information aside from the values
and each value should be separated by a new line character (\n).

File Descriptions by Name

testData.txt:
Sample Data (For Testing Purposes)
This data was generated using the website:
https://www.socscistatistics.com/utilities/normaldistribution/default.aspx

The data points should produce a normal distribution with the following distribution characteristics:
Population Mean (μ):            50
Sample Mean (x):                49.94695
Standard Deviation (σ):         10
First Quartile (Q1):            43.35
Third Quartile (Q3):            56.83
Inter Quartile Range (IQR):     13.48
Size of Dataset:                1000


The first 10 values are: 20,10,0,-10,-20,80,90,100,110,120
These fall -3,-4,-5,...,3,4,5,... standard deviations (approximately) away from the sample mean

The next 10 values are: 29.87,23.13,16.39,9.65,2.91,70.31,77.05,83.79,90.53,97.27
These fall -1,-1.5,-2,...,1,1.5,2,... IQRs below/beyond the first/third quartile

Depending on the users inputs, a subset of these 20 values will be flagged as outliers


