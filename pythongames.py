start= '''
You decide to take up babysitting. You think "hey its kids, money and love. what could go wrong?"
You are babysitting a five year old boy named James. He asks you to take him to the park.
Type the options to play.
'''


print("start")
print ("You decide to take up babysitting. You think 'hey its kids, money and love. what could go wrong?'' You are babysitting a five year old boy named James. He asks you to take him to the park. Type the options to play. Choose your options wisely. Each decision will lower or raise James' hapiness. Get 10 happy points to win!")

print("Do you want to drive or walk to the park? Type 'drive' to drive and 'walk' to walk")
user_input = input()
if user_input == "drive":
    print("You decide to drive. Would you like to take the highway or residential streets? Type 'highway' or 'residential'")
    user_input1=input()# finished the story by writing what happens
    if user_input1== "highway":
        print("minus 2 happy points! The highway is loud and fast, James prefers to be outdoors.")
    if user_input1== "residential":
        print("minus 3 happy points! Residential driving takes longer, the faster to the park, the better.")
if user_input== "walk":
    print ("You decide to walk. Do you take the long way on the sidewalk or do you trepass through lawns to get there faster? Type 'trespass' or 'sidewalk'")
    user_input2=input()
    if user_input2== "trespass":
        print("minus 1 happy point! James ALWAYS follows the rules")
    if user_input2== "sidewalk":
        print("gain 1 happy point! Taking the sidewalk is the right thing to do but it is also a longer walk")

print("You have finally arrived at the park. How happy is James? Don't worry if it's low! You are allowed to pick up to 4 park equipments for James to play on to raise his happiness! Remember: choose carefully!")
print("Pick 'south', 'west', 'east")

user_input3 = input()
if user_input = "south":
    print ("Go on the slide? or go on the monkey bars? Type 'MB' for monkey bars and 'slide' for slide")
    user_input4 == input()
    if user_input4 == "slide":
        print("Yay! The Slide is one of James' favorites! Gain 2 happy points1")
    if user_input4 == "MB":
        print("Eh, the monkey bars are good but not thattt good. Gain 1 happy point.")
if user_input3 == "west":
    print("Go on the sprinklers or go in the sand pit? Type 'sprinkler' or 'sandpit'")
    user_input5 == input()
    if user_input5 == "sprinkler"
        print("EWWWW, water is gross! Gain 0 happy points!")
    if user_input5 == "sadnpit"
        print("sandpits are fun!!!! Gain 3 happy points!")
