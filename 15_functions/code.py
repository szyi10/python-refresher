def hello():
    print("Hello!")

hello()

# ----

def user_age_in_seconds():
    user_age = int(input("Enter you age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age is seconds is{age_seconds}.")

user_age_in_seconds()
