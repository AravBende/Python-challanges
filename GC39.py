import random

#  excerize 1

insults = [",you were born on the highway, where all accidents happen ", ", your lazy", ", just look in the mirror", ", If I wanted to kill myself, I'd climb up your ego and jump to your IQ.", ", You're the best at all you do -- and all you do is make people hate you." ]

name = input("whats the students name: ")

print(name + random.choice(insults))
