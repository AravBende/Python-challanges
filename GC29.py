import random

comments = ["asks a lot of question", "works very hard", "doesnt listen", "doesnt work at all", "messes around", "works well in groups"]

studentnum = int(input("how many students are in your class? "))

for i in range (studentnum):
    print(random.choice(comments))
