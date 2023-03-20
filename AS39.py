import random

artists = [    [0, 'Adele', 'Hello', 'Rolling in the Deep', 'Someone Like You', 'Set Fire to the Rain', 'Chasing Pavements', 'Skyfall', 'Send My Love (To Your New Lover)', 'When We Were Young', 'Rumour Has It', 'Water Under the Bridge'],
    [1, 'Beyoncé', 'Crazy in Love', 'Formation', 'Single Ladies (Put a Ring on It)', 'Drunk in Love', 'Irreplaceable', 'Halo', 'Love on Top', 'Run the World (Girls)', 'If I Were a Boy', 'Partition'],
    [2, 'Ed Sheeran', 'Shape of You', 'Thinking Out Loud', 'Photograph', 'Castle on the Hill', 'Perfect', 'Galway Girl', 'The A Team', 'Bloodstream', 'Sing', 'I See Fire'],
    [3, 'Lady Gaga', 'Bad Romance', 'Shallow', 'Poker Face', 'Born This Way', 'Just Dance', 'Paparazzi', 'Telephone', 'Alejandro', 'The Edge of Glory', 'Applause'],
    [4, 'Michael Jackson', 'Billie Jean', 'Thriller', 'Beat It', 'Smooth Criminal', 'Black or White', 'Don\'t Stop \'Til You Get Enough', 'Man in the Mirror', 'Bad', 'Rock with You', 'The Way You Make Me Feel'],
    [5, 'Rihanna', 'Umbrella', 'Work', 'We Found Love', 'Diamonds', 'Stay', 'Only Girl (In the World)', 'Love on the Brain', 'SOS', 'Disturbia', 'Take a Bow'],
    [6, 'Taylor Swift', 'Shake It Off', 'Love Story', 'Blank Space', 'You Belong with Me', 'I Knew You Were Trouble', 'Style', 'Bad Blood', 'Wildest Dreams', 'Mean', 'Mine'],
    [7, 'The Beatles', 'Hey Jude', 'Yesterday', 'Let It Be', 'Twist and Shout', 'Come Together', 'All You Need Is Love', 'Help!', 'A Hard Day\'s Night', 'She Loves You', 'I Want to Hold Your Hand'],
    [8, 'The Rolling Stones', '(I Can\'t Get No) Satisfaction', 'Sympathy for the Devil', 'Paint It Black', 'Jumpin\' Jack Flash', 'Start Me Up', 'Brown Sugar', 'Gimme Shelter', 'Wild Horses', 'You Can\'t Always Get What You Want', 'Honky Tonk Women'],
    [9, 'Whitney Houston', 'I Will Always Love You', 'I Wanna Dance with Somebody (Who Loves Me)', 'Greatest Love of All', 'How Will I Know', 'So Emotional', 'I Have Nothing', 'One Moment in Time', 'Saving All My Love for You', 'Where Do Broken Hearts Go', 'All the Man That I Need']
]

randomlist = []
count = 0
twice = 0
start = True
secondartist = -1
while count != 10:
    randomnum = random.randint(0, 9)
    if twice == 2 or start == True:
        twice = 0
        start = False
        secondartist = randomnum
    else:
        if randomnum != secondartist:
            randomlist.append(randomnum)
            count += 1
            twice += 1

for randomnumber in randomlist:
    print(artists[randomnumber][random.randint(2, 11)] + " by: " + artists[randomnumber][1])
