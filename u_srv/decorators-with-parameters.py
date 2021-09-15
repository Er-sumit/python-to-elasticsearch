'''
get admin password shall be accessible by admins
get dashboard password shall be accessible by all users
and guest can access anything

create function that will return decorator to allow us check access level
create another decorator -> the new decorator wrapping existing decorator & the new decorator accepts an argument. Fundametally the new decorator is no more decorator but a function returning make_secure. This function used to create a decorator.

so while using this
the function call happens first and the function is returning a decorator which is applied to next line defined function
'''

import functools

user = { "username":"sumit", "access_level":"guest" }

#make_secure function returns decorator
def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, *kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "1234"

@make_secure("user")
def get_dashboard_password():
    return "dashboard_pass"

print(get_admin_password())
print(get_dashboard_password())

user = { "username":"sumits", "access_level":"admin" }
print(get_admin_password())
print(get_dashboard_password())
