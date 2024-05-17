def add(x, y):
    return x + y

result = add(5, 8)

print(result)

# ----

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"
    
div_result = divide(15, 3)
print(div_result)