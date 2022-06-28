import time
from pyfiglet import Figlet


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

        pricing = {
           'Model S': '89000',
           'Model X': '95000',
           'Model 3': '49000',
           'Model Y': '55000',
           'Blue': '0',
           'Titanium Grey': '500',
           'Pearl White': '1000',
           '2WD': '0',
           '4WD': '2000',
           'Black': '0',
           'White': '2000'
        }
        print("\nCreating your order...\n")
        time.sleep(2)
        print('------------------------------------------')
        print(f'Thank you for your order!')
        print('------------------------------------------')
        print('See your order details below:\n')
        print(f'Model: {self.model:>15} Price: ${pricing[self.model]:>5}')
        print(f'Color: {self.color:>15} Price: ${pricing[self.color]:>5}')
        print(f'Drivetrain: {self.drivetrain:>10} Price: ${pricing[self.drivetrain]:>5}')
        print(f'Interior: {self.interior:>12} Price: ${pricing[self.interior]:>5}')

        order_total = int(pricing[self.model])+int(pricing[self.color])+int(pricing[self.drivetrain])+int(pricing[self.interior])
        print(f'\nOrder Total: ${order_total}')
        print(f'Tax rebates: $5000')
        print(f'Your Totals: ${order_total-5000}\n')


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
        print('Which color would you like? Choose between option 1-3. \n\n1. Blue (standard)\n2. Titanium Grey (+ $500)\n3. Pearl White (+ $1000)\n')
        user_choice = input('Enter your option here: ')
        options = ['Blue', 'Titanium Grey', 'Pearl White']

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
        time.sleep(2)
    else:
        return True


def main():
    """
    Main function that runs the program by calling the other functions in order.
    """
    logo = Figlet(font="slant")
    print(logo.renderText("TESLA"))
    print('Welcome to the Tesla ordering app!\n')

    model = show_car_models()
    color = show_color_options()
    drivetrain = show_drivetrain_options()
    interior = show_interior_options()
    order = CustomerOrder(model, color, drivetrain, interior)

    print(order.order_summary())


while True:
    main()
    end_message = input('\nWould you like to place another order? Please enter (y): ')
    if end_message.lower() == 'y':
        continue
    else:
        print('\nThank you for your order.\nHave a great day!')
        break
