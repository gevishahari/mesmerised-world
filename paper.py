#rock paper sizer
import random

print("================================")
print("welcome to rock paper sizer")
print("remember 1 s stone")
print("remember 2 s paper")
print("remember 3 s sizer")
print("================================")

#user input
def useinp():
	r=random.randint(1,3)
	return r

while True:
	r=useinp()
	x=int(input("what do u wanna throw"))
	if(x==1 and r==2):
		print("u loose bec stone wins against paper")
	elif(x==2 and r==1):
		print("u win bec paper wins against stone")
	elif(x==1 and r==3):
		print("u win bec stone wins against sizer")
	elif(x==3 and r==1):
		print("u loose bec sizer wins against paper")
	elif(x==2 and r==3):
		print("u loose bec stone wins against paper")
	elif(x==3 and r==2):
		print("u won bec stone wins against paper")
	else:
		print("u ant the computer put same value..so it is a draw")