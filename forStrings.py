# num = 5
# 000 000 000
# 001 001 001 
# 002 004 016
# 003 009 027
# 004 016 064
# 005 025 125

# n = int(input("enter a number")) # 4
# l = len(str(n**3)) # 2
# for i in range(1,n+1):
# 	# print("%d %d %d"%(i , i**2 , i**3))
# 	print("%s %s %s"%(str(i).zfill(l) , str(i**2).zfill(l) , str(i**3).zfill(l)))

# 1
# 12
# 123
# 1234
# 12345

# 123
# for i in range(1,4):
# 	print(i , end="")
# print()
# # 1234  
# for i in range(1,5):
# 	print(i , end ="")
# print() # next 
# # 12345  
# for i in range(1,6):
# 	print(i , end ="")

# for j in range(1,6):
# 	for i in range(1,j+1):
# 		print(i , end="")
# 	print()

# num = 5
# 5 X 1 = 5
# .
# .
# .
# 5 X 10 = 50

# composite / prime 
# -----------------
# 12 --> composite --> 1,2,3,4,6,12
# 13 --> prime --> 1,13
# 9  --> composite --> 1,3,9

# n = 9
# 9%1 == 0 -
# 9%2 != 0
# 9%3 == 0 -
# 9%4 != 0
# .
# .
# 9%9 == 0 - 
# n = 130
# count = 0
# for i in range(1,n+1):
# 	if(n%i == 0 ):
# 		count += 1

# if(count > 2):
# 	print("composite")
# else:
# 	print("prime")

# s = 20 
# e = 60 
# for j in range(s,e+1): 
# 	count = 0
# 	for i in range(1,j+1):
# 		if(j%i == 0 ):
# 			count += 1

# 	if(count > 2):
# 		print("%d is Composite"%(j))
# 	else:
# 		print("%d is Prime"%(j))

# 20 - composite
# 21 - composite
# 22 - composite
# 23 - prime
# .
# .
# . 
# 60 - composite

# strings 
# -------
# string --> array of chars --> iterate
# tech = "python"
# print(tech[0])
# print(tech[1])
# print(tech[2])
# print(tech[3])
# print(tech[4])
# for i in range(0,len(tech)):
# 	print(tech[i]) # indexing using i (number)

# for <dummy> in <string>:
# 	<statements>

# for i in tech:
# 	print(i)
# for i in "python":
# 	print(i)

# for i in "Python and Data ScIEces I N HyDe":
# 	if(i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u"):
# 		print(i)

# n = 5
# a
# bb
# ccc
# dddd
# eeeee

# p = "iam in hyd in class of dl "
# n = 1

# n = 2
# iam in 
# in. hyd 
# hyd in 
# in class
# class of
# of dl

# n = 3
# iam in hyd
# hyd in class 













