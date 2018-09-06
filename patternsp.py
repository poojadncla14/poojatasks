# n=int(input('enter any number'))
# l=len(str(n**3))	
# for i in range(1,n+1):
#    print("%s %s %s"%(str(i).zfill(l), str(i**2).zfill(l) , str(i**3).zfill(l)))


##to find whether a number is prime or composite
# -------------------------------------------------
# n = int(input('enter a number'))
# count = 0
# for i in range(1,n+1):
# 	if(n%i == 0 ):
# 		count += 1

# if(count > 2):
# 	print("composite")
# else:
# 	print("prime")



# #to give the range of numbers if they are prime or not 
# ---------------------------------------------------------

# s=int(input('enter any number'))
# e=int(input('enter any number'))
# count = 0
# for j in range(s,e):
# 	for i in range(1,j+1):
# 		if(j%i == 0 ):
# 			count += 1

# 	if(count > 2):
# 		print("%d is composite"%(j))
# 	else:
# 		print("%d is prime"%(j))






# # task 2-->tables
# # ---------------
# n=int(input('enter any number'))
# for i in range(1,11):
# #     print(n,'x',i,'=',n*i)
#       print("%d x %d=%d"%(n,i,n*i))










# task3-->string pattern
# -----------------------
# for i in range(1,6):
# 	for j in range (97,97+i):
#    	   a= char(j)
#     print(a)
  
#    print()




## task4--->pattern for small letters
# -------------------------------------

# n=int(input('enter any number'))
# num=97
# for i  in range(1,n+1):
# 	a = chr(num)
# 	print(a * i,end="")
# 	num=num+1
# 	print()    
      
   










## task5--->pattern for capital letters 
# ----------------------------------------


# n=int(input('enter any number'))
# num=65
# for i in range(1,n+1):
#    a=chr(num)
#    print(a *i,end="")
#    num=num+1
#    print()








##task6------>anagram
# ------------------------- 

# tech='i am a girl with two eyes'
# for i in tech:
#   print(i,end="")
#   # break




# # task pascal triangle
# # ------------------------
# n=6
# for i in range(1,6):
#     n=n-1
#     for j in range(0,1):
#         print(n*" ",end="")
#         for k in range(0,i):
#             print("* ",end="")
#     print()  

























