# kwagrs = Key Word Arguments

def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)

# ----

def named2(name, age):
    print(name, age)

details = { "name": "Bob", "age": 25 }

named2(**details)

# ----

def print_nacely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nacely(name="Bob", age=25)

# ----

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 2, 3, name="Bob", age=25)

# ----

def myfunc(**kwargs):
    print(kwargs)

myfunc(**"Bob")  # Error, must be mapping
myfunc(**None)   # Error