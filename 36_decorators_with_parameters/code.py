import functools

user = { "username": "jose", "access_level": "guest" }


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*agrs, **kwargs):
            if user["access_level"] == access_level:
                return func(*agrs, **kwargs)
        
        return secure_function
    
    return decorator


@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"
    

print(get_admin_password())
print(get_dashboard_password())

print('-- User changed --')
user = { "username": "anna", "access_level": "admin" }

print(get_admin_password())
print(get_dashboard_password())
