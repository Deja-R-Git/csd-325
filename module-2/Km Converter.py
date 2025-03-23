#Juedeja Richard- 12/26/25- Module4.2
    #This is a Program that converts Miles to Kilometers


def start():
    try:
        miles = float(input('How many miles do you want to convert?'))
        # user will input the number of miles they want to become kilometers

        conversion_multiplier: float = 1.609344
        #This is the number used to convert miles to km

        km: float = miles * conversion_multiplier
        #this executes the process of multiplying the two statements together

        print(miles,'in miles is', km, 'in kilometers')
    except ValueError:
        print('Input must be numerical - Try again')
        #if input is not written numerically, give error message and do not execute function

start()
#calls the start function to execute

#Gaddis, T. (2020). Starting out with Python (5th ed.). Pearson.
