"""
date = '23/04/2021'
modified_date = '23/04/2021'
author = 'vishnu'
description = 'A program with cubic running time. Read in N integers and counts the   number of triples that sum to exactly 0.'
"""

def WindCalculation(Temperature, Speed):
    try:
        # calculation part
        w=35.74+(0.6215*Temperature)+((0.4275*Temperature)-35.75)*pow(Speed, 0.16)

        print('wind chill: ')
        print(w)
    except Exception as e:
        print(e)

# input values
Temperature= int(input('enter the value of temperature in Fahrenheit less then 50: '))
if Temperature>50:
    print('Please enter value less then 50')
Speed= int(input('enter wind speed in miles per hour from 3 to 120: '))
if Speed<3 or Speed>120:
    print('enter value from 3 to 120')
WindCalculation(Temperature, Speed)