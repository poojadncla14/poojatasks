
# def addNums(nu1 , nu2):
# 	ans = nu1 + nu2 
# 	print("sum of numbers is " +str(ans))
# 	return ans 

# def subNums(nu1 , nu2):
# 	ans = nu1 - nu2
# 	print("diff of numbers is " +str(ans))
# 	return ans

# def mulNums(nu1 , nu2):
# 	ans = nu1 * nu2
# 	print("mul of numbers is " +str(ans))
# 	return ans


# def divNums(nu1 , nu2):
# 	ans = nu1 // nu2
# 	print("quo of numbers is " +str(ans))
# 	return ans



# def optionSelect():
# 	'''
# 	1. Arith
# 	2. Logical
# 	3. Bitwise '''
# 	option = int(input("enter your option "))
# 	if option == 1:
# 		arith()
# 	elif option == 2:
# 		logical()
# 	elif option == 3:
# 		bitwise()
# 	else:
# 		print("Enter given options only")
# def arith():
# 	'''
# 	1. Add
# 	2. Sub
# 	3. Mul
# 	4. Div '''
# 	print(arith.__doc__)
# 	operation = int(input("enter your operation"))
# 	num1 = int(input("enter your number "))
# 	num2 = int(input("enter your number "))
# 	if operation == 1:
# 		addNums(num1 , num2)
# 	elif operation == 2:
# 		subNums(num1 , num2)
# 	elif operation == 3:
# 		mulNums(num1 , num2)
# 	elif operation == 4:
# 		divNums(num1 , num2)
# 	else:
# 		print("Enter given operation only")

# print(optionSelect.__doc__)
# def logical():
# 	'''
# 	1.and
# 	2.or
# 	3.not'''
# 	print(logical.__doc__)
# 	operation =int(input('enter your operation'))
# 	num1 = int(input("enter your number "))
# 	num2 = int(input("enter your number "))
# 	if operation == 1:
# 		andNums(num1 , num2)
# 	elif operation == 2:
# 		orNums(num1 , num2)
# 	elif operation == 3:
# 		notNums(num1 , num2)
# 	else:
# 		print("Enter given operation only")

# def andNums(nu1 , nu2):
# 	ans = nu1 and nu2 
# 	print("logical operation is" +str(ans))
# 	return ans 
# def orNums(nu1 , nu2):
# 	ans = nu1 or nu2 
# 	print("logical operation is" +str(ans))
# 	return ans 
# def notNums(nu1 , nu2):
# 	ans = not(nu1 and nu2) 
# 	print("logical operation is" +str(ans))
# 	return ans 	
# def bitwise():
# 	'''
# 	1.bitwiseand
# 	2.bitwiseor
# 	3.bitwisexor
# 	4.binary ones complement
# 	5.binary left shift
# 	6.binary right shift'''
# 	print(bitwise.__doc__)
# 	operation =int(input('enter your operation'))
# 	num1 = int(input("enter your number "))
# 	num2 = int(input("enter your number "))
# 	if operation == 1:
# 		bandNums(num1 , num2)
# 	elif operation == 2:
# 		borNums(num1 , num2)
# 	elif operation == 3:
# 		bxorNums(num1 , num2)
# 	elif operation == 1:
# 		bonecNums(num1 , num2)
# 	elif operation == 2:
# 		bleshNums(num1 , num2)
# 	elif operation == 3:
# 		brishNums(num1 , num2)	
# 	else:
# 		print("Enter given operation only")

# def bandNums(nu1 , nu2):
# 	ans = nu1 & nu2 
# 	print("bitwise operation is" +str(ans))
# 	return ans 
# def borNums(nu1 , nu2):
# 	ans = nu1 | nu2 
# 	print("bitwise operation is" +str(ans))
# 	return ans 
# def bxorNums(nu1 , nu2):
# 	ans = nu1 ^ nu2
# 	print("bitwise operation is" +str(ans))
# 	return ans 	
# def bonecNums(nu1):
# 	ans = ~(nu1) 
# 	print("bitwise operation is" +str(ans))
# 	return ans 	
# def bleshNums(nu1):
# 	ans = nu1 <<2 
# 	print("bitwise operation is" +str(ans))
# 	return ans 	
# def brishNums(nu1):
# 	ans = nu1>>2 
# 	print("bitwise operation is" +str(ans))
# 	return ans 	
# optionSelect()

# def avgNums(*args):
#     ans=0
#     for i in args:
#     	ans=ans+i
#     print(ans//len(args))
# # avgNums(10)

# mean median and max of mean and median:
# ----------------------------------------

# n=int(input('enter the value'))
# b=0
# for i in range(n):
#    	p=int(input('enter your num'))
#    	b=b+p
# def meanNums():
#    mean=b/n   
#    print('mean='+str(mean))
#    return mean
# meanNums()
# l=[]
# for i in range(n):
#    	p=int(input('enter your num'))
#    	l.append(p)
# l.sort()
# print(l)   
# def medNums(): 
#     if len(l)%2==0:
#        median=(l[int(n/2)-1]+l[int(n/2+1)-1])/2
#        print('median='+str(median))
#     else:
#        median=l[int(n/2)]  
#        print('median='+str(median)) 
#     return median
# medNums()
# def maxNums():
# 	median=medNums()
# 	mean=meanNums()
# 	if (int(median)>int(mean)):
# 		print('max='+str(median))
# 	else:
# 		print('max='+str(mean))
# maxNums()

# l1=[1,2,4,5,6]
# l2=[2,5,7,8,5]
# l3=[]
# for i in range(len(l1)):
# 		w=l1[i]+l2[i]
# 		l3.append(w)
# print(l3)		


# l4=[1,4,6,78,98]
# ans=0
# for i  in l4:
# 	ans=ans+i
# print(ans)





# def var(a,coll):
# 	l=[]
# 	c=0
# 	for i in range((a)):
# 		n=int(input('enter the number'))
# 		if(coll=="l"):
# 			l.append(n)
# 			print(l)
# 		elif(coll=="t"):
# 			# n=int(input('enter the number'))
# 			l.append(n)
# 			b=tuple(l)
# 			print(b)
# 		else:
# 			l.append(n)
# 			print(l)
# 		c=c+n
# 	mean=c/(a)
# 	print('mean='+str(mean))
# 	return mean
# var(4,"l")

# def medNums(a,coll):
# 	l=[]
# 	for i in range((a)):
# 		n=int(input('enter the number'))
# 		if(coll=="l"):
# 			l.append(n)
# 			l.sort()
# 			print(l)
# 		elif(coll=="t"):
# 			# n=int(input('enter the number'))
# 			l.append(n)
# 			l.sort()
# 			b=tuple(l)
# 			print(b)  
# 		else:
# 			l.append(n)
# 			l.sort()
# 			print(l)	
# 	if len(l)%2==0:
# 		median=(l[int(n/2)-1]+l[int(n/2+1)-1])/2
# 		print('median='+str(median))
# 	else:
# 		median=l[int(n/2)]  
# 		print('median='+str(median)) 
# 	return median
# medNums(4,"l")
# def maxNums():
# 	median=print(medNums(4,'l'))
# 	mean=print(var(4,'l'))
# 	if (int(median)>int(mean)):
# 		print('max='+str(median))
# 	else:
# 		print('max='+str(mean))
# maxNums()


d={name:pooja,age:21,mobile:9652021971}
print(d)



















