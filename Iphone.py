''' Program that propts the user for his/her amount of money, then reports
how many iphone the person can afford, and how much more money will he/she
need to afford an additional iphone
'''

import sys

iphone = 50000
salary = 0
qty = 0

print ("Reminder: An iphone costs P50000\n")
salary = input ("How much is your money? ")
qty = salary/iphone
mmoney = iphone - salary%iphone

if qty < 1:
    print "You need P", mmoney, "to buy an Iphone"
    
else:
    print "You can buy", qty, "Iphone/s"
    print "To buy another iphone you need P", mmoney
