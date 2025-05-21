from functools import reduce

FilteredData = lambda iNo : 70 <= iNo <= 90

Increase = lambda iNo : iNo + 10

Multiplication = lambda iNo1, iNo2: iNo1 * iNo2      

def main():
    Data = []
    print("Enter number of elements : ")
    iSize = int(input())

    print("Please eneter numeric values : ")
    for iCnt in range (iSize):
        iValue = int(input())
        Data.append(iValue)

    print("Input Data : ",Data)    

    FData = list(filter(FilteredData, Data))
    print("Filter Output : ",FData)

    MData = list(map(Increase, FData))
    print("Map Output : ",MData)

    RData = reduce(Multiplication, MData)
    print("Reduce Output : ",RData)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_4>python 4_3.py
Enter number of elements :
12
Please eneter numeric values :
4
34
36
76
68
24
89
23
86
90
45
70
Input Data :  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
Filter Output :  [76, 89, 86, 90, 70]
Map Output :  [86, 99, 96, 100, 80]
Reduce Output :  6538752000

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_4>

'''