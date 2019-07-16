s=int(input())
if (s%4==0):
	if (s%100==0):
		if (s%400==0):
			print ("yes")
		else:
			print ("no")
	else:
		print ("yes")
else:
	print("no")
