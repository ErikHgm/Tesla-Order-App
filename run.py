

def show_car_models():
    """
    Shows user the different car models. 
    Stores the option that the user chose.
    """
    print('Which car model would you like to order? Choose between option 1-4. \n\n1. Model S \n2. Model X \n3. Model 3 \n4. Model Y \n')
    car_model = input('Enter your option here: ')
    print(f'\nYou picked car model: {car_model}') 
    price = 0
    model = ''
    if car_model == '1':
        price = 89000
        model = 'Model S' 
    elif car_model == '2':
        price = 95000
        model = 'Model X' 
    elif car_model == '3':
        price = 49000
        model = 'Model 3' 
    else:
        price = 55000
        model = 'Model Y'      
    return price, model


def show_color_options():
    """
    Shows user the different options for colors. 
    Stores the color that the user chose.
    """
    print()
    print('Which color would you like? Choose between option 1-3. \n\n1. Pearl White \n2. Titanium Grey \n3. Black \n')
    color = input('Enter your option here: ')
    print(f'\nYou picked color: {color}')       
          
    return color


def show_drivetrain_options():
    """
    Shows user the different drivetrain options. 
    Stores the answer that the user chose.
    """
    print()
    print('Which drivetrain option would you like? Choose between option 1-2. \n\n1. 2WD \n2. 4WD \n')
    drivetrain = input('Enter your option here: ')
    print(f'\nYou picked drivetrain: {drivetrain}')       
    return drivetrain

def show_interior_options():
    """
    Shows user the different interior options. 
    Stores the answer that the user chose.
    """
    print()
    print('Which interior color would you like? Choose between option 1-2. \n\n1. White \n2. Black \n')
    interior = input('Enter your option here: ')
    print(f'\nYou picked interior: {interior}')       
    return interior


def main():
    print('Hello! Welcome to the Tesla Ordering app. \n\n')

    show_car_models()
    show_color_options()
    show_drivetrain_options()
    show_interior_options()

main()