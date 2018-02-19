#Write a phython program that computes the factorial of an integer


num = input ("Enter an integer:")
fact = 1

if num < 0:
    print "Must be a positive integer"

elif num == 0:
    print "Factorial = 1"

else:
    for i in range (1, num+1):
        fact = fact*i
    print"Factorial number is",num,"and value is" ,fact
