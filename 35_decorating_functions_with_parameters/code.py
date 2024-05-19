import functools

user = { "username": "jose", "access_level": "admin" }


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*agrs, **kwargs):
        if user["access_level"] == "admin":
            return func(*agrs, **kwargs)
    
    return secure_function


@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'super_secure_password'
    

print(get_password('billing'))
