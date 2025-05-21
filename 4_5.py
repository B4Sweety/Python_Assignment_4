from functools import reduce

Prime = lambda iNo : iNo > 1 and all(iNo % iCnt != 0 for iCnt in range (2, iNo))

Multiplication = lambda iNo : iNo*2

Maximum = lambda iNo, iMax: iNo if iNo > iMax else iMax

def main():
    Data = []
    print("Enter number of elements : ")
    iSize = int(input())

    print("Please eneter numeric values : ")
    for iCnt in range (iSize):
        iValue = int(input())
        Data.append(iValue)

    print("Input Data : ",Data)    

    FData = list(filter(Prime, Data))
    print("Filter Output : ",FData)

    MData = list(map(Multiplication, FData))
    print("Map Output : ",MData)

    RData = reduce(Maximum, MData)
    print("Reduce Output : ",RData)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_4>python 4_5.py
Enter number of elements :
8
Please eneter numeric values :
2
70
11
10
17
23
31
77
Input Data :  [2, 70, 11, 10, 17, 23, 31, 77]
Filter Output :  [2, 11, 17, 23, 31]
Map Output :  [4, 22, 34, 46, 62]
Reduce Output :  62

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_4>

'''