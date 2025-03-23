#Juedeja Richard - 3/22/25 - Module1.3
#This program will take the input and count backwards to 1
    #while displaying the number of remaining bottles of beer on the wall.
    #Once the count is down to 1, change lyrics to show "1 bottle of beer..."
    #At the end of the countdown,remind the user to buy more beer

print("Listen to my Bottle Song")

def main():
    bottle(b)

#get the number of bottles from the User
def bottle(b):
    if b > 1:
#if number of bottles is greater than 1 print this statement
        print(b,"bottles of beer on the wall,", b, "bottles of beer,",
        "Take one down and pass it around,", b-1, " bottles of beer on the wall")
        bottle(b-1)
    elif b == 1:
        print(b,"bottle of beer on the wall,", b, "bottle of beer,",
        "Take one down and pass it around,", b-1, " bottles of beer on the wall")
#when number of bottles(b) is 1, change bottle(s) to bottle
    elif b == 0:
        print('We need more Beer Bottles')
#when number of bottles(b) reaches 0 print this

b = int(input("How Many Bottles do we have?:"))
if __name__ =='__main__':
    main()
#call the main function