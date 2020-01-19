'''
App for creating customer account,
Checking the balance for an existing account, 
Depositing money into an existing account,
Withdrawing money from an existing account,
Transfering money from an existing account to another existing account
Note: The user password created during creation must be unique for proper functioning of the App
To run the App via command line or Terminal run (py bank.py)

'''

# dict of users, sample users are already registered for testing 
users = [\
    {'email':'first@gmail.com', 'password':'first_password', 'balance':250},\
    {'email':'second@gmail.com', 'password':'second_password', 'balance':20}, \
    {'email':'third@gmail.com', 'password':'third_password', 'balance':0}\
        ]

# This function checks if user with a given attribute and corresponding value exist
def check_user(attr, value):
    for item in users:
        if item[attr] == value:
            return item
    return False

# function to deposit money
def deposit_money(user):
    # amount to be deposited
    amount = input('please enter the deposit amount\n')
    while(True) :
        try:
            user_amount = float(amount)
            if user_amount > 0.0:
                break
            else:
                print('invalid amount\n')
                amount = input('please enter the deposit amount\n')
        except ValueError:
            print('invalid amount\n')
            amount = input('please enter the deposit amount\n')
    new_balance = float(user['balance']) + user_amount
    print('you just deposited {deposit}, your balance is now {balance}'.format(deposit = user_amount, balance = new_balance))

# function to check a given users account balance
def check_balance(user):
    print('Your account balance is {}'.format(user['balance']))

# function to withdraw money given the user
def withdraw(user):
    amount = input('please enter the amount you want to withdraw\n')
    while(True) :
        try:
            user_amount = float(amount)
            if user_amount > 0.0:
                break
            else:
                print('invalid amount\n')
                amount = input('please enter the amount you want to withdraw\n')
        except ValueError:
            print('invalid amount\n')
            amount = input('please enter the amount you want to withdraw\n')
    if user['balance'] == 0.0:
        print('insufficent balance')
        deposit_money(user)
    elif user['balance'] < user_amount:
        print('insufficient balance\n')
    else:
        new_balance = float(user['balance']) - user_amount
        print('your have successfully withdrawn {withdrawn_amount}, your balance is {balance}'.format(withdrawn_amount = user_amount, balance = new_balance))

# function to transfer money given user        
def tranfer(user):
    amount = input('please enter the amount you want to transfer\n')
    while(True) :
        try:
            user_amount = float(amount)
            if user_amount > 0.0:
                break
            else:
                print('invalid amount\n')
                amount = input('please enter the amount you want to transfer\n')
        except ValueError:
            print('invalid amount\n')
            amount = input('please enter the amount you want to transfer\n')
    if float(user['balance']) < user_amount:
        print('insufficent balance')
    else:
        receiver = input('please enter beneficiary\'s email address \n')
        while(True):
            beneficiary = check_user('email',receiver.lower())

            if beneficiary:
                break
            print('No account is associated with the given email\n')
            receiver = input('please enter beneficiaries email address\n')
        
        beneficiary_balance = float(beneficiary['balance']) + user_amount
        sender_balance = user['balance'] - user_amount
        beneficiary['balance'] = beneficiary_balance
        user['balance'] = sender_balance
        print('you have successfully transfered {sent_amount} to {reciever}, your balance is now {new_balance}'.format(sent_amount = user_amount, reciever = beneficiary['email'], new_balance = user['balance']))
        

# function creates a new user
def create_user():
    user_email = input('please enter an email\n')
    # loop checks if user with the given email or identity already exist
    while(True):
        if not check_user('email',user_email.lower()):
            break
        else:
            print('An account with the email or username you provided already exist.\n')
            user_email = input('please enter an email\n')
    
    user_password = input('please choose a password:\n')
    # loop makes sure user chooses a character at least 4 character long
    while(True):
        if len(user_password) > 4 and not check_user('password', user_password):
            break
        else:
            print('password must be four characters or more and unique\n')
            user_password = input('please choose a password:\n')
    # add new user to users
    new_user = {'email':user_email.lower(), 'password':user_password, 'balance': 0.0}
    users.append(new_user)
    print('{customer} created successfully!'.format(customer = user_email.lower()))


def main():
    # This variable holds an authenticated user
    user_authicated = False

    user_input = input('press 1: create account \npress 2: transaction\n')

    # loop ensures that the user input is 1 or 2
    while(True):
        if user_input == '1' or user_input == '2':
            break
        else:
            print('incorrect input, press either 1 or 2\n')
            user_input = input('press 1: create account \npress 2: transaction \n')
        
    # creat user
    if user_input == '1':
        create_user()
    else:
        #ask user for  password
        password = input('please enter your password\n')
        # check if password is correct
        user = check_user('password', password)
        # if password is not correct return to first set of options
        if not user:
            print('password incorrect, you are not authorized!')
            main()
        # if password is correct
        else:
            # authicate user
            user_authicated = True
            user_option = input('press 1: check balance\npress 2: deposit\npress 3: withdraw\npress 4: transfer\npress 0: go back\n')
            # makes sure user chooses from available options
            while True:
                if user_option == '0' or user_option == '1' or user_option == '2' or user_option == '3' or user_option == '4':
                    break
                else:
                    print('please choose one the following options\n')
                    user_option = input('press 1: check balance\npress 2: deposit\npress 3: withdraw\npress 4: transfer\npress 0: go back\n')
            
            if user_option == '0':
                main()
            elif user_option == '1':
                check_balance(user)
            elif user_option == '2':
                deposit_money(user)
            elif user_option == '3':
                withdraw(user)
            else:
                tranfer(user)

if __name__ == "__main__":
    main()