from functools import wraps

user_logged_in=False
def requires_login(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not user_logged_in:
            raise PermissionError("User not authenticated")
        return func(*args,**kwargs)
    return wrapper

@requires_login
def access_dashboard(username):
    print(f"Welcome to your dashboard, {username}!")

def main():
    global user_logged_in
    print("===Attempt without login===")
    try:
        access_dashboard("Pete")
    except PermissionError as e:
        print("Error: ",e)
    print("\n---Logging in---")
    user_logged_in=True
    access_dashboard("Pete")

if __name__=="__main__":
    main()