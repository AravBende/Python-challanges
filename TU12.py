# excersize 1

list = ["mangoes", "apples", "pinnaples", "cucumber", "tomatoes"]

print(*list[0:4], sep=", ")

# excersize 2

count = 1

charecters = ["superman", "spiderman", "Captain america"]

for charecter in charecters:
    print(str(count) + ": " + charecter)
    count += 1

chosenchar = int(input("please input the chosen charecters number: ")) - 1

item = input("please input item you want to give the charecter: ")

charecters[chosenchar] += ", " + item

print(charecters[chosenchar])
