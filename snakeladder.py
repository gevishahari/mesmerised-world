#write a program to play snake and ladder
import random
c=0
while True:
	r=random.randint(1,6)
while(c<=100):
	n=input("press r to roll the dice")
	if(n=='r'):
		c=c+r
		print("u got ",r)
		print("new position is",c)

		if(c==8):
			c=37
			print("climb the ladder")
		elif(c==11):
			c=2
			print("snake has bitten u")	
		elif(c==13):
			c=34
			print("climb the ladder")
		elif(c==25):
			c=4
			print("snake has bitten u")
		elif(c==38):
			c=9
			print("snake has bitten u")
		elif(c==40):
			c=68
			print("climb the ladder")
		elif(c==52):
			c=81
			print("climb the ladder")
		elif(c==65):
			c=46
			print("snake has bitten u")
		elif(c==76):
			c=97
			print("climb the ladder")
		elif(c==89):
			c=70
			print("snake has bitten u")
		elif(c==93):
			c=64
			print("snake has bitten u")
		elif(c==100):
			c=100
			print("u won the game")

