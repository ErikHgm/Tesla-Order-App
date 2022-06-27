

def show_car_models():
    """
    Shows user the different car models. 
    Returns the price and model that the user chose.
    """
    print('Which car model would you like to order? Choose between option 1-4. \n\n1. Model S ($89000)\n2. Model X ($95000)\n3. Model 3 ($49000)\n4. Model Y ($55000)\n')
    user_choice = input('Enter your option here: ')
    model_options = ['Model S', 'Model X', 'Model 3', 'Model Y']
    model = model_options[int(user_choice)-1]
    print(f'\nYou have selected model: {model}\n')  

    return model


def show_color_options():
    """
    Shows user the different options for colors. 
    Returns the price and color that the user chose.    
    """
    print('Which color would you like? Choose between option 1-3. \n\n1. Black (standard)\n2. Titanium Grey (+ $500)\n3. Pearl White (+ $1000)\n')
    user_choice = input('Enter your option here: ')
    color_options = ['Black', 'Titanium Grey', 'Pearl White']
    color = color_options[int(user_choice)-1]
    print(f'\nYou have selected color: {color}\n')  

    return color


def show_drivetrain_options():
    """
    Shows user the different drivetrain options. 
    Returns the price and drivetrain that the user chose.    
    """
    print('Which drivetrain option would you like? Choose between option 1-2. \n\n1. 2WD (standard)\n2. 4WD (+ $2000)\n')
    user_choice = input('Enter your option here: ')
    drivetrain_options = ['2WD', '4WD']
    drivetrain = drivetrain_options[int(user_choice)-1]
    print(f'\nYou have selected drivetrain: {drivetrain}\n')  

    return drivetrain


def show_interior_options():
    """
    Shows user the different interior options. 
    Returns the price and interior that the user chose.
    """
    print('Which interior color would you like? Choose between option 1-2. \n\n1. Black (standard)\n2. White (+ $2000) \n')
    user_choice = input('Enter your option here: ')
    interior_options = ['Black', 'White']
    interior = interior_options[int(user_choice)-1]
    print(f'\nYou have selected interior: {interior}\n')  

    return interior


def print_receipt(car, color, drivetrain, interior):
    """
    Prints the costs and option selected by the user for each item.
    Calculate and prints total cost for the order.
    """
    print('Your order summary:')
    print(car)
    print(color)
    print(drivetrain)
    print(interior)

    total_price = car[0]+color[0]+drivetrain[0]+interior[0]
    print(total_price)




def main():
    """
    Main function that runs the program by calling the other functions in order. 
    """
    print('Hello! Welcome to the Tesla Ordering app. \n\n')

    car_option = show_car_models()
    color_option = show_color_options()
    drivetrain_option = show_drivetrain_options()
    interior_option = show_interior_options()


main()

