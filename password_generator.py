import string
import random
def password_genreator(length,digits=True,specials=True):
    digit=string.digits
    special=string.punctuation
    letters=string.ascii_letters
    charcters=''
    if digits:
        charcters+=digit
    if specials:
        charcters+=special
    charcters+=letters
    password=''
    isdigit=False
    isspecial=False
    meetcriteria=False
    while len(password)<length and meetcriteria==False :
        for i in range(length):
            password+=random.choice(charcters)
            if password[i] in digit:
                isdigit=True
            if password[i] in special:
                isspecial=True
        if isdigit and isspecial:
            meetcriteria=True
        else:
            password=''
    return password
def main():
    while True:
        print('enter length of password : ')
        length=int(input())
        print('Do you want digits in password y/n: ')
        digits=input()
        print('Do you want special characters in password y/n: ')
        specials=input()
        if digits=='y':
            digits=True
        else:
            digits=False
        if specials=='y':
            specials=True
        else:
            specials=False
        print('     ' ,password_genreator(length,digits,specials))
        print('Do you want to continue y/n: ')
        choice=input()
        if choice=='n':
            break    
        else:
            continue
main()

