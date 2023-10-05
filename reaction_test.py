#Program to get the average reaction time of an individual
#Thabo Mswazi
#MSWTHA010
#22 September 2023

import time
#import random
#from leader_board import *

#reactions_list = []
##records the reaction time of the user
#def reaction_time():
    #print("Press 'enter' NOW!", end='')
    #start_time = time.time()
    #reaction = input()
    #final_time = time.time()
    #reaction_time = final_time - start_time
    #reaction_time = '{0:.6f}'.format(reaction_time)
    #reactions_list.append(reaction_time)
    #return reaction_time    
    
##records the reactions of the user throgh every test   
#def record_reaction(num_of_tests):
    #if num_of_tests == 0:
        #return print('Tests complete') 
    #print('Get ready...', flush=True) #prompts the user to get ready to press enter button
    #time.sleep(random.randrange(5)) #random time lapse between 1-5 seconds before testing reaction
    #print('Reaction time:', reaction_time())
    #return record_reaction(num_of_tests-1)

##calculates the average reaction time       
#def average(num_of_tests):
    #total = 0
    #for num in reactions_list:
        #total += float(num)
    #average = total/num_of_tests
    #reactions_list.clear()
    #return average

#def flush_input():
    #try:
        #import msvcrt
        #while msvcrt.kbhit():
            #msvcrt.getch()
    #except ImportError:
        #import sys, termios
        #termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        
#def main():
    #file_name = input('Enter the name of the output file:\n')
    #output_file = open(file_name, "w")
    #subject_name = input("Enter subject name (or press 'enter' to quit):\n")
    #while subject_name != '':
        #reactions_list = []
        #try:
            #num_of_tests = int(input('Enter the number of tests:\n'))
            #record_reaction(num_of_tests)
            #average1 = average(num_of_tests)
            #print('Average reaction time: ' + '{0:.6f}'.format(average1))
            #print()
            #test_results = subject_name + " " + str(num_of_tests) + " " + '{0:.6f}'.format(average1)
            #print(test_results, file=output_file)
            #subject_name = input("Enter subject name (or press 'enter' to quit):\n")
        #except ValueError:
            #print('Error, please enter a integer value')
            
#if __name__=='__main__':
    #main()
def ds():
    for i in range(5):
        time.sleep(1)
        print(i)

def main():
    time1 = time.time()
    ds()
    t2 = time.time()
    tt = t2 - time1
    print(tt)
main()


