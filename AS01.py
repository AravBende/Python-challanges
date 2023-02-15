import random
MyArray = []
for i in range(10):
    randomnum = random.randint(1, 99)
    MyArray.append(randomnum)
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
