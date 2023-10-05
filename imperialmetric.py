#Program that computes and displays a conversion table for feet and inches to metres.
#Thabo Mswazi
#MSWTHA010
#9 May 2023

def main():        
 feet_min = int(input('Enter the minimum number of feet (not less than 0):\n'))
 feet_max = int(input('Enter the maximum number of feet (not more than 30):\n'))

 #code to print the first line (skeleton) of the table
 print('    |' , end = ' ') #prints the vertical bar on the first line 
 for inches in range(0 , 12):
  if inches < 10:
   print('  ' , str(inches) + '"' , end = ' ') #prints all the inches from 0 to 9
  else:
   print(' ' , str(inches) + '"' , end = ' ') #prints the inches 10 and 11
          
 for feet in range(feet_min , feet_max + 1):
  print('\n{0:4}'.format(str(feet) + "'") + '|' , end = ' ') #prints all the feet conversions required by the user in a column with a vertical bar after each number
  for inches in range(0 , 12):
   meters = (feet*12+inches)*0.0254 #formula to convert feet and inches to meters
   print('{0:0.3f}'.format(meters) , end = ' ') #prints all the meters in a row to 3 decimal places

main()
