'''
author = Zoltan Veres
'''

############# FUNCTIONS ################
# read cars parameters from files
def read_parameters(index):
    file_nanme = str(index) + '.txt'
    file = open(file_nanme, 'r+')
    file.seek(0)
    d1 = {'ID' : index}
    for line in file:
        parameter = (line.strip('\n')).split('=')
        d1.update({ parameter[0] : parameter[1]})
     #file.close()
    #print(d1)
    return d1
#########################################
# read cars id's from files
def cars(file):
    file = open(file, 'r+')
    file.seek(0)
    car = []
    for i in file:
        car += i.strip('\n')
    file.close()
    return car

#########################################
# print car parameters
def print_parameter(profile):
    print('=' * 41)
    for j in profile.items():
        print('| {:<17} | {:^17} |'.format(*j))
    print('=' * 41)

#########################################
# update rented.txt file
def update_rented_file(id):
    file = open('rented.txt', 'a')
    file.write('{}\n'.format(id))
    file.close()

#########################################
# update not_rented.txt file

def update_not_rented_file(number):
    file = open('not_rented.txt')
    content = file.read()
    file.seek(0)
    content1 = file.readlines()
    file.close()
    content1.remove(str(number)+'\n')
    file = open('not_rented.txt', 'w')
    file.writelines(content1)
    file.close()

#####################################################
# ask user to fill conditions for searching cars
def read_conditions():
    conditions = {}
    conditions['brand'] = input("Brand: ").lower()
    conditions['model year'] = input("Model year: ")
    conditions['transmission'] = input("Transmission(automatic/manual): ").lower()
    conditions['price'] = input("Price: ")

#remove conditions which are not filled
    conditions_test = {}
    for i in conditions.keys():
        if conditions[i] != '':
            conditions_test.update({ i : conditions[i]})

    return conditions_test

#####################################################
# read car parameters from files and format them(keys of dictionary)
def car_parameters(index, conditions_test):
    car_parameters = read_parameters(index)
    car_parameters_update ={}
    for i in car_parameters.keys():
         j = i.strip(' ')
         car_parameters_update.update({ j : car_parameters[i]})

# create new dictiponary with items which is the same as was added by user in conditions
    car_parameters_test= {}
    for i in car_parameters_update.keys():
        if i in conditions_test:
            car_parameters_test.update({i : car_parameters_update[i]})

    return car_parameters_test

#####################################################
# check if the contions match with parameters

def compare2(conditions_test, car_parameters_test ):
    prem = 0
    for i in list(conditions_test.keys()):
        try:
            condition1 = (conditions_test[i][0] != '<' and conditions_test[i][0] != '>' and car_parameters_test[i].lower() == conditions_test[i])
            condition2 = (conditions_test[i][0] == '<' and int(car_parameters_test[i]) < int(conditions_test[i][1:]))
            condition3 = (conditions_test[i][0] == '>' and int(car_parameters_test[i]) > int(conditions_test[i][1:]))

        except:
            continue

        if condition1 or condition2 or condition3:
            prem += 1


    return prem


################# MAIN PROGRAM ########################

print('''Welcome to the CAR RENT,
place where people can rent their dream car''')

while True:
    print('=' * 40)

    print('''
    MENU:
    L - show all availible cars
    S - search cars
    R - rent a car
    X - exit the program
    ''')
    option = str(input('Choose option from menu: '))


    print('=' * 40)

    if option == 'X':
        exit()

    elif option == 'L':
        not_rented_cars = cars('not_rented.txt')
        for i in not_rented_cars:
            car_profile = read_parameters(i)
            print_parameter(car_profile)

    elif option == 'R':
        value = True
        while value:
            car_to_rent = input("Fot rent the car, add the car's ID(Back to tha main Menu press X): ")
            if car_to_rent == 'X':
                value = False
            else:
                not_rented_cars = cars('not_rented.txt')
                rented_cars = cars('rented.txt')
                if car_to_rent in not_rented_cars:
                    update_rented_file(car_to_rent)
                    update_not_rented_file(car_to_rent)
                    print("You successfully rented our car wird ID {}:".format(car_to_rent))
                    car_profile = read_parameters(car_to_rent)
                    print_parameter(car_profile)
                    print("You can get it in our car park.")
                    value = False

                elif car_to_rent in rented_cars:
                    print("Car with iD {} is already rented. Choose another car.".format(car_to_rent))

                else:
                    print("Wrong ID")

    elif option == 'S':
        print('''Search a car basod on condition - brand, model year, transmission and price.
For model year and price you can use '<' and '>' - "find models newer than 2000" = "<2000"
If condition doesn't matter for you, leave it blank(hit Enter):      ''' )
        conditions = read_conditions()
        all_cars = cars('not_rented.txt') + cars('rented.txt')
        matched_cars = 0
        for i in all_cars:
            parameters = car_parameters(i, conditions)
            prem = compare2(conditions, parameters)
            if len(conditions) == prem:
                car_profile = read_parameters(i)
                rented_cars = cars('rented.txt')
                if car_profile['ID'] in rented_cars:
                    car_profile['ID'] = 'NOT AVAILABLE'
                print_parameter(car_profile)
                matched_cars += 1
        if matched_cars == 0:
            print("Cannot found any cars, which match to your conditions.")


    else:
        print("Wrong option.")
