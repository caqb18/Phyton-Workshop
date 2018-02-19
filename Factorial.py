#Write a phython program that computes the factorial of an integer

fact = 1
num = input ("Enter an integer: ")
for x in range (0, num):
    fact = fact * num
print "Factorial" , num , "is ", fact

