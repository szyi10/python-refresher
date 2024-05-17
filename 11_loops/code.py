# -- While Loop --

number = 7

while True:
    user_input = input("Would you like to play? (Y/n) ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

# -- For Loop --

friends = ['Ralph', 'Jen', 'Bob', 'Anne']

for friend in friends:
    print(f"{friend} is my frined.")

# -- Sum Function, instead of for loop --

grades = [35, 67, 98, 100, 100]
total = sum(grades) # total = 0 -> in case of using for loop
amount = len(grades)

# for grade in grades:
#     total += grade

print(total / amount)