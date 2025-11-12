import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Break problem into 3 loops:
#1:Pick a letter & store them:-
# STEP 1: start with an empty list to collect characters (easier to extend/shuffle later)
pass_charac = []
# STEP 2: add letters FIRST (exactly nr_letters of them)
# hint: use random.choice(letters) to get ONE random letter each loop
for l in range(nr_letters):
    #random.choice(letters) for addition of letters.
    pass_charac.append(random.choice(letters))
#print(pass_charac)

# STEP 3: add symbols NEXT (exactly nr_symbols of them)
# hint: same idea as letters, just pull from symbols list
for s in range(nr_symbols):
    pass_charac.append(random.choice(symbols))
#print(pass_charac)

#step 4 : adding numbers now:
for n in range(nr_numbers):
    pass_charac.append(random.choice(numbers))
#print(pass_charac)
#step-5: joining all of them
lev1 = "".join(pass_charac)
print(f"Your level one password is: {lev1}")

#level-2 thing
random.shuffle(pass_charac)
lev2 = "".join(pass_charac)
print(f"Your level 2 password is: {lev2}")

#----------Got The Logic!!!-----------------------4 step thing for level 1 & 5 step for level 2-------------------------------------------------------