def login():
    username=input("Enter the username :")
    password=input("Enter your password :")

    valid_users=["Mohitsharma","Karan","Lucky","Salman","Praduman"]
    valid_Passwords=["Mohitsh","Karan111","Lucky222","Salman333","Praduman444"]

    if username in valid_users and password == valid_Passwords [valid_users.index(username)]:
        print("Login successfully")
    else:
        print("Invalid user name or Password")
login()
