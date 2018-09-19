import random
while True:
	x=int(input("press 1 to roll the dice and 0 to quit"))
	if(x==1):
		print(random.randint(1,6))
	elif(x==0):
		print("bye!")
		break
	else:
		print("press either 1 or 0")
		
		
		
	