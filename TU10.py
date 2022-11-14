import random

#excersize 1

print(random.uniform(0.1, 9.9))

#excersize 2

Choose_Name = ["James","John","Mark","Rick"]
for i in range(1,5):
    chosen = random.choice(Choose_Name)
    print(chosen)
    yorn = input("would you like to keep this name in the list(y/n)? ")
    if yorn.casefold() == "n":
        Choose_Name.remove(chosen)
print(Choose_Name)
