#Program to determine the number of days in a particular month of a specific year
#Thabo Mswazi
#MSWTHA010
#8 May 2023

def main():
    months_list = ['January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December']

    month = int(input('Enter number of month (1 is January):\n'))-1
    year = int(input('Enter year:\n'))

    leap_year_test1 = year%4
    leap_year_test2 = year%100
    leap_year_test3 = year%400

    month_string = months_list[month]
    
    if month <= -1 or month > 12 or year < 0:
        print('Sorry, invalid input(s).')
        return
    elif month == 3 or month == 5 or month == 8 or month == 10:
        number_of_days = '30'
    elif month == 0 or month == 2 or month == 4 or month == 6 or month == 7 or month == 9 or month == 11:
        number_of_days = '31'  
    elif month == 1 and leap_year_test1 == 0 and leap_year_test2 != 0 or leap_year_test3 == 0:
        number_of_days = '29'
    elif month == 1:
        number_of_days = '28'
          
    print('In the year' , str(year) + ', ' + month_string + ' has ' + number_of_days + ' days.')

main()




    

