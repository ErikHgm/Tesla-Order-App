class CustomerOrder:
    """
    Class that creates the customer order summary that is used by 
    the main function to display the order to the customer.
    """
    
    def __init__(self, model, color, drivetrain, interior):
        self.model = model
        self.color = color
        self.drivetrain = drivetrain
        self.interior = interior

    def order_summary(self):
        print(f'Thank you for you order!\nYour order details:\n{self.model}\n{self.color}\n{self.drivetrain}\n{self.interior}\n')

def show_car_models():
    """
    Shows user the different car models. 
    Returns the price and model that the user chose.
    """
    while True:
        print('Which car model would you like to order? Choose between option 1-4. \n\n1. Model S ($89000)\n2. Model X ($95000)\n3. Model 3 ($49000)\n4. Model Y ($55000)\n')
        user_choice = input('Enter your option here: ')
        options = ['Model S', 'Model X', 'Model 3', 'Model Y']

        if validate_user_choice(user_choice, len(options)):
            model = options[int(user_choice)-1]
            print(f'\nYou have selected model: {model}\n')
            break

    return model

def show_color_options():
    """
    Shows user the different options for colors. 
    Returns the price and color that the user chose.    
    """
    while True:
        print('Which color would you like? Choose between option 1-3. \n\n1. Black (standard)\n2. Titanium Grey (+ $500)\n3. Pearl White (+ $1000)\n')
        user_choice = input('Enter your option here: ')
        options = ['Black', 'Titanium Grey', 'Pearl White']
        
        if validate_user_choice(user_choice, len(options)):
            color = options[int(user_choice)-1]
            print(f'\nYou have selected color: {color}\n') 
            break
     
    return color

def show_drivetrain_options():
    """
    Shows user the different drivetrain options. 
    Returns the price and drivetrain that the user chose.    
    """
    while True:
        print('Which drivetrain option would you like? Choose between option 1-2. \n\n1. 2WD (standard)\n2. 4WD (+ $2000)\n')
        user_choice = input('Enter your option here: ')
        options = ['2WD', '4WD']
        if validate_user_choice(user_choice, len(options)):
            drivetrain = options[int(user_choice)-1]
            print(f'\nYou have selected drivetrain: {drivetrain}\n')  
            break

    return drivetrain

def show_interior_options():
    """
    Shows user the different interior options. 
    Returns the price and interior that the user chose.
    """
    while True:
        print('Which interior color would you like? Choose between option 1-2. \n\n1. Black (standard)\n2. White (+ $2000) \n')
        user_choice = input('Enter your option here: ')
        options = ['Black', 'White']
        if validate_user_choice(user_choice, len(options)):
            interior = options[int(user_choice)-1]
            print(f'\nYou have selected interior: {interior}\n')  
            break

    return interior

def validate_user_choice(choice, length):
    """
    Checks and validates that the input user makes is correct.
    If incorrect it asks the user to try again.
    """ 
    if int(choice) > length or int(choice) < 1:
        print(f'Your answer should be a number between 1 and {length}, please try again!\n\n')
     
    else:
        return True

def main():
    """
    Main function that runs the program by calling the other functions in order. 
    """
    print('Hello! Welcome to the Tesla Ordering app. \n\n')

    model = show_car_models()
    color = show_color_options()
    drivetrain = show_drivetrain_options()
    interior = show_interior_options()
    order = CustomerOrder(model, color, drivetrain, interior)

    print(order.order_summary())

while True:
    main()
    end_message = input('\nWould you like to place another order? Please enter (Y/N): ')
    if end_message.lower() == 'y':
        continue
    else:
        print('\nHave a great day!')
        break




