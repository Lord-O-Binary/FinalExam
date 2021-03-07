#find all numbers which are divisible by 7 but are not multiples of 5
# and are numbers between 2000 and 3200

number_space = range(2000,3200)
div7less5 = []
for n in number_space:
    #nested if statements in loop iterating for every number between 2,000 and 3,200
    if n % 5 != 0:
        if n % 7 == 0:
            #adds number to array if qualifying
            div7less5.append(n)

#outputs array for validation
print(div7less5)
