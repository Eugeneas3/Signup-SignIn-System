def main():
    signIn()

def signup():
    print("Create your account")
    username = input("Enter your user name: ")
    password = input("Enter your password: ")
    password_01 = input("Please Confirm your password: ")
    
    while password_01 != password:
            print("Password Mismatch!!!")
            password = input("Enter your password:")
            password_01 = input("Confirm your password: ")
            if password == password_01:
                break
    print("Account Created!")
    details = [f"{username}", f"{password}"]
    return details

def signIn():
    variable = signup()
    print("LOGIN....")
    username1 = input("Enter your username to LogIn: ")
    password1 = input("enter your password to LogIn: ")
    username, password = variable
    while username1 != username or password1 != password:
        print("Details Mismatch!!!")
        username1 = input("Enter your username: ")
        password1 = input("enter your password: ")
        if username1 == username and password1 == password:
            print("LogIn Successfull......")
            break 
    if username1 == username and password == password:
        print("Logged in Successful!")   
if __name__ == "__main__":       
    signIn()
    