"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'vishnu'
description = 'Leap Year'
"""
class LeapYear:
    def year(self):
        print("Enter the year")
        # taking the year as input
        year = int(input())
        # if given year is greater than 999 and less than 9999 to make the condition that 4 digits
        if year>999 and year<9999:
            # checking the condition if the given year is leap year or not
            if(year % 4==0 or year % 400==0 or year % 100!=0):
                if(year % 4==0 or year % 400==0):
                    print(year, "is a leap year")
                else:
                    print(year, "is not a leap year")
            else:
                print(year, "is not a leap year")
        else:
            print("Given number is less than 4 digits")
# creating object for the class and calling the method
yearnum = LeapYear()
yearnum.year()