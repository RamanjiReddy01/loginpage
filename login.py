storage = {}
class user:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email=email
class check_condition:
    def username_check(self, username):
        if len(username) > 6:
            return True
        else:
            return False
    def password_check(self, password):
        if len(password)>8:
            return True
        else:
            return False
    def email_check(self, email):
        if email[-10:] == '@gmail.com' or email[-10:] == '@yahoo.com':
            return True
        else:
            return False
    
class verify:
    def user_name(self, username):
        if username in storage:
            return True
        else:
            return False
    def user_password(self, password):
        if password in storage:
            return True
        else:
            return False
    def user_email(self, email):
        if email in storage:
            return True
        else:
            return False

def main():
    while True:
        print (' press 1 To register : ')
        print(' press 2 To login : ')
        print(' press 3 To exit : ')
        choice = int(input('Enter your choice : '))
        if choice==1:
            username=input('Enter your username : ')
            password=input('Enter your password : ')
            email=input('Enter your email : ')
            check=check_condition()
            if check.username_check(username) and check.password_check(password) and check.email_check(email):
                if username in storage:
                    print('Username already exists')
                    main()
                    break
                elif email in storage:
                    print('Email already exists')
                    main()
                    break
                else:
                    storage[username]=user(username, password, email)
                    print('Registration successful')
                    #break
                    
                
                
            else:
                if check.username_check(username)==False:
                    print('Invalid username')
                if check.password_check(password)==False:
                    print('Invalid password')
                if check.email_check(email)==False:
                    print('Invalid email')
                main()
                break
                
        if choice == 2:
            username = input('Enter your username : ')
            password = input('Enter your password : ')
            verif = verify()
            if verif.user_name(username) and verif.user_password(password):
                print('Login successful')
            else:
                print('Login failed')
                print('Invalid username or password')
                main()
                break
        if choice == 3:
            break

main()
#written by : ramanji reddy
