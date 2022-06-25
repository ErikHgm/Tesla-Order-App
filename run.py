

def show_car_models():
    """
    Shows user the different car models. 
    Stores the option that the user chose.
    """
    print('Which car model would you like to order? Choose between option 1-4. \n\n1. Model S \n2. Model X \n3. Model 3 \n4. Model Y \n')
    car_model = input('Enter your option here: ')
    print(f'\nYou picked car model: {car_model}')       
    return car_model

def show_color_options():
    """
    Shows user the different options for colors. 
    Stores the color that the user chose.
    """
    print()
    print('Which color would you like? Choose between option 1-4. \n\n1. Pearl White \n2. Titanium Grey \n3. Black \n')
    color = input('Enter your option here: ')
    print(f'\nYou picked color: {color}')       
    return color


def main():
    print('Hello! Welcome to the Tesla Ordering app. \n\n')

    show_car_models()
    show_color_options()

main()