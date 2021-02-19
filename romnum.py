# practice with dictionaries: month conversions and roman numerals

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# print(month_conversions["Mar"])
# print(month_conversions.get("Sat", "Invalid key"))

# Roman numeral calculator
# no invalidation logic yet --
#       you can put in any letter and it will try to calculate
#       nonstandard numerals like IIIV would still be tested (needs to be fixed)
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
num = input("Enter Roman Numeral: ")

# size for how much to loop
size = len(num)
print("size is set to " + str(size))

# for total num equivalent to user numeral
total = 0
print("total is " + str(total))

# i for where loop is
i = 0
print("i is set to " + str(i))

# XXXIII
while size > 0:
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
    print("total is now " + str(total))
    print("i is now " + str(i))
    # repeat

# Create a for loop -- it'll look and work better!

print(num + " is " + str(total) + " in roman numerals.")