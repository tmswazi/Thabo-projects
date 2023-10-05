#Program for a game of frogs and toads
#Thabo Mswazi
#MSWTHA010
#28 July 2023

def main():
    num_frogs = int(input('Enter the number of frogs:\n'))  
    num_toads = int(input('Enter the number of toads:\n'))
    
    state1 = ['Frog']*num_frogs+['    ']+['Toad']*num_toads #list to store the state of the game in the beginning
    i = 1
    #prints the number of squares in the game
    for animal in state1: 
        if i > 9:
            print('' , str(i)+'.' , end = " ")
        else:
            print(" " , str(i)+'.' , end = '')
        i += 1
    print()
    
    #places the frogs, toads and space in the square numbers
    for value in state1:
        print(value , end = "")
    print() 
    while True:
        move = input('>')
        if move == 'quit':
            break
        else:
            move = int(move)
            move -= 1
        #accounts for each scenario for a move entered by user and moves the frog or toad from the position specified in the move to the space
        if state1[move] == 'Frog' and state1[move + 1] == '    ': 
            state1[move] , state1[move + 1] = state1[move + 1] , state1[move]
        elif state1[move] == 'Frog' and state1[move + 1] == 'Toad' and state1[move + 2] == '    ':
            state1[move] , state1[move + 2] = state1[move + 2] , state1[move]
        elif state1[move] == 'Frog' and state1[move + 1] == 'Frog' and state1[move + 2] == '    ':
            state1[move] , state1[move + 2] = state1[move + 2] , state1[move]    
        elif state1[move] == 'Toad' and state1[move - 1] == '    ':
            state1[move] , state1[move - 1] = state1[move - 1] , state1[move]
        elif state1[move] == 'Toad' and state1[move - 1] == 'Frog' and state1[move - 2] == '    ':
            state1[move] , state1[move - 2] = state1[move - 2] , state1[move]
        elif state1[move] == 'Toad' and state1[move - 1] == 'Toad' and state1[move - 2] == '    ':
            state1[move] , state1[move - 2] = state1[move - 2] , state1[move]
            
        #prints the number of squares in the game
        i = 1    
        for animal in state1:
            if i > 9:
                print('' , str(i)+'.' , end = " ")
            else:
                print(" " , str(i)+'.' , end = '')
            i += 1
            
        print()
        state2 = [] #list to store state of frogs, toads and space after the latest move by user
        
        #places the frogs, toads and space in the square numbers
        for value in state1:
            print(value , end = "")
            state2.append(value) #to check state of list if you have won
            
        print()
        if state2 == ['Toad']*num_toads+['    ']+['Frog']*num_frogs: #checks if the user won the game
            print('Congratulations, you\'ve won!')
            break
        
        #to account for cases where the user has lost the game
        elif state2[0] == 'Frog' and state2[1:num_toads+1] >= ['Toad']*2 and state2[-1] == '    ':
            print('Sorry, you\'ve lost.')
            break
        elif state2[0] == 'Toad' and state2[1:num_frogs+1] == ['Frog']*2 and state2[-1] == '    ':
            print('Sorry, you\'ve lost.')
            break
        elif state2[0] == '    ' and state2[1:num_frogs+1] == ['Frog']*2:
            print('Sorry, you\'ve lost.')
            break
        elif state2[0] == '    ' and state2[-1:-(num_toads)-1:-1] == ['Toad']*2:
            print('Sorry, you\'ve lost.')
            break
        elif state2[-1] == '    ' and state2[0:num_frogs] == ['Frog']*2:
            print('Sorry, you\'ve lost.')
            break
        elif state2[-1] == '    ' and state2[-2:-(num_toads)-1:-1] == ['Toad']*2:
            print('Sorry, you\'ve lost.')
            break
        elif state2[-1] == 'Frog' and state2[-2:-(num_toads)-1:-1] == ['Toad']*2:
            print('Sorry, you\'ve lost.')
            break
        elif state2[0] == '    ' and state2[1:4] == ['Toad']+['Frog']*2:
            print('Sorry, you\'ve lost.')
            break            
main()
    

    

    

        
    
    
  


    
        
    
