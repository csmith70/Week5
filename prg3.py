## Christopher Smith
## This is a program to count to a user defined limit.
## 9/6/19

#Initializing Varibales
n=1 
end=0
total = 0
while end < 3 or end > 10: #Validating User Input
	end = input('Enter a number between 3 and 10: ')
	end = float(end)

while n<= end: #Print the counter
	print('hello world: {0}'.format(n))
	total = total + n
	print('The Total Sum is: {0}'.format(total))
	n+=1
ave = total/end

print('The Average is {0}'.format(round(ave, 1)))
