# Steffen "Ya Boi" Riener
# Roman numeral calculator
# BUG -- nonstandard numerals like IIIV would still be tested

roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# print(roman_numerals.get(test[x + 1], "Invalid numeral"))
num = input("Enter Roman Numeral: ").upper()

# print(list(enumerate(num)))

# size for how much to loop
size = len(num)
#print("size is set to " + str(size))

# for total num equivalent to user numeral
total = 0
#print("total is " + str(total))

# i for where loop is
i = 0
#print("i is set to " + str(i))

# XXXIII
while size > 0:
    try:
        temp = roman_numerals.get(num[i], "Invalid roman numeral") # read index 0 of user string
        # FIND WAY TO GET CONSOLE TO SAY INVALID AT ANY POINT IN THE NUMERAL
        if i == len(num) - 1:
            total += roman_numerals[num[i]]  # add to total
            break
        elif temp < roman_numerals.get(num[i + 1], "Invalid roman numeral"): # CHECK IF NEXT is greater than index 0
            total -= temp # subtract from total
        else:
            total += roman_numerals[num[i]] # add to total
        size -= 1 # shift index up 1
        i += 1
        #print("total is now " + str(total))
        #print("i is now " + str(i))
        # repeat
    except TypeError:
        total = 0
        print("Invalid Roman Numeral")
        break

# Create a for loop if you can!
# Figure out how to use enumerate()

if total > 0:
    print(num + " is " + str(total) + " in roman numerals.")
else:
    pass