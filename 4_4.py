from functools import reduce

FilteredData = lambda iNo : iNo % 2 == 0

Increase = lambda iNo : iNo**2

Multiplication = lambda iNo1, iNo2: iNo1 + iNo2      

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

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_4>python 4_4.py
Enter number of elements :
10
Please eneter numeric values :
5
2
3
4
3
4
1
2
8
10
Input Data :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
Filter Output :  [2, 4, 4, 2, 8, 10]
Map Output :  [4, 16, 16, 4, 64, 100]
Reduce Output :  204

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_4>

'''