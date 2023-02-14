MyArray = [12, 14, 13, 11]
n = len(MyArray) -1
flag = 1

while flag != 0:
    flag = 0
    for i in range(n):
        if MyArray[i]> MyArray[i+1]:
            temp = MyArray[i]
            MyArray[i] = MyArray[i+1]
            MyArray[i+1] = temp
            flag = 1

print(MyArray)
