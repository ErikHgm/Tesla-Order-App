

def showCarModels():

    print('Which car model would you like to order? Choose between option 1-4. \n\n1. Model S \n2. Model X \n3. Model 3 \n4. Model Y \n')
    car_model = input('Enter your option here: ')
    print(f'\nYou picked car model: {car_model}')       
    return car_model

def main():
    print('Hello! Welcome to the Tesla Ordering app. \n\n')

    showCarModels()

main()
