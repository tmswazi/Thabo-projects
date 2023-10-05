#program to track animal ordinates logged in by user
#Thabo Mswazi
#MSWTHA010
#26 July 2023

def main():
    
    animal_list = [] #list to store the animal codes
    ordinates_dict = {} #dictionery to store animal codes as keys and animal ordinates as values
    i = 1
    print('Please enter the animal identity codes. (Press return when done.)')
    while True: 
        animal_code = input('Animal no. ' + str(i)+ ':' + '\n')
        animal_list.append(animal_code)
        ordinates_dict[animal_code] = 'cannot be located.'
        if animal_code == '':
            break
        i += 1
        print(ordinates_dict)
       
    #prompt the user to enter the commands (Commands: print, log <animal id> <x ord> <y ord>, quit.)
    print('Commands: print, log <animal id> <x ord> <y ord>, quit.')
    while True:
        command = input('>').removesuffix(" ")
        code = command[4:command.find(' ' , 4)] #code entered by the user for a specific animal when logging ordinates
        if command == 'quit':
            break
        
        if command != 'print' and len(command) <= 8:
                print('Could not interpret command.\nCommands: print, log <animal id> <x ord> <y ord>, quit.')
            
        if command == 'print':
            for animal in animal_list[0:-1]:
                print('Animal ' + animal + ' ' + str(ordinates_dict[animal]))
                
        if code not in animal_list and command.count(' ') > 2:
            print('That animal identity code is unknown.')  
            
        if 'log' in command and len(command) > 8 and code in animal_list:
            ordinates = command[command.find(' ' , 4):]
            ordinate1 = ordinates[1:ordinates.find(' ' , 1 , -1)]
            ordinate2 = ordinates[ordinates.find(' ' , 1 , -1)+1:]
            if not ordinate1.isnumeric() or not ordinate2.isnumeric():
                print('The ordinates should be integers.\nCommands: print, log <animal id> <x ord> <y ord>, quit.')
            else:
                ordinates_dict[code] = 'last seen at (' + str(int(ordinate1)) + ', ' + str(int(ordinate2)) + ')' + '.'

main()