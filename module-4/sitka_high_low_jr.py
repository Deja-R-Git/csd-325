#Juedeja Richard 4/6/25 Module 4.2
#This program will show a graph of temperatures from
# Sitka based on the User choice from an imported file

print("To see different temperatures please Enter: 'Highs' or 'Lows' Below")
print("Enter 'EXIT' to end the program")
import csv, sys
from datetime import datetime

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, highs and lows from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)


while True:  # Main game loop.
    # Place your bet:
    print('What temperatures do you want to see? (Highs, Lows or EXIT)')
    while True:
        temperature = input()
        if temperature.upper() == 'EXIT':
            print('No more weather for you!')
            sys.exit()
        elif temperature == 'Highs':
            print("Here are the high temperatures")
            break
        elif temperature == "Lows":
            print("Here are the Low temperatures")
            break


#Make two separate figures for high and low temps
#plt.style.use('seaborn')
    fig1, ax1 = plt.subplots()
    ax1.plot(dates, highs, c='red')

    fig2, ax2 = plt.subplots()
    ax2.plot(dates, lows, c='blue')

# Format plots
    ax1.set_title("Daily high temperatures - 2018", fontsize=24)
    ax1.set_xlabel('', fontsize=16)
    fig1.autofmt_xdate()
    ax1.set_ylabel("Temperature (F)", fontsize=16)
    ax1.tick_params(axis='both', which='major', labelsize=16)

    ax2.set_title("Daily Low temperatures - 2018", fontsize=24)
    ax2.set_xlabel('', fontsize=16)
    fig2.autofmt_xdate()
    ax2.set_ylabel("Temperature (F)", fontsize=16)
    ax2.tick_params(axis='both', which='major', labelsize=16)

#draw plots on figures and display the chosen temperatures
    if temperature == 'Highs':
        plt.close(fig2)
        plt.figure(fig1.number)
        plt.show()
    elif temperature == 'Lows':
        plt.close(fig1)
        plt.figure(fig2.number)
        plt.show()

