def passwordcheck():
    password = input("Enter password: ")
    if password == 'python123':
        print('Access granted')
    else:
        print('Access denied')
def main():
    passwordcheck()
main()