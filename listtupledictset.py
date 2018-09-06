# t=1,2,2,3,
# print(type(t))
# print(t)

# import sys
# print(sys.argv[1]) # 10 
# count = 0 
# if len(sys.argv) > 2:
# 	print("Enter only one number next time ")
# 	for i in range(0,int(sys.argv[1])+1):
# 		count += i
# else:
# 	for i in range(0,int(sys.argv[1])+1):
# 		count += i
# print(count)


# d={1:'hey',2:'you',3:'are',4:'beautiful'}
# print(d.keys())
# print(d.items())
# print(d.values())
# d={}
# l=[1,2,3,4]
# r=['hey','you','are','beautiful']
# for i in range(0,len(l)):
#     d[l[i]]=r[i]
# print(d)    

# p={}
# l=[2,3,4,5,6,8]
# p=['hey','i','was','doin','fine','whem','poo']
# for i in range(0,len(l)):
# 	p[l[i]]=l[i]**2
# print(p)


# o=zip(l,p)
# print(o)
# d=dict(o)
# print(d)


# def par():
#     d1={1:2,2:3,3:4}
#     d2={4:5,5:6,6:7,7:8}
#     d1.update(d2)
#     print(d1)

# # def par():
# # d1={1:2,2:3,3:4,4:5}
# #d2={4:5,5:6,6:7,7:8}}
# # for i in range(len(d1)):
# # 	d2.update(d1)
# # print(d2)
# par()

# task:dictionaries
# -------------------
# question1: 
# a={i:i+2 for i in range(10)}
# print(a)

#q2:
# d1={1:'p',2:'y',3:'t'}
# d2={4:'h',5:'o',6:'n'}
# d1.update(d2)
# print(d1)

# q3:
# d={}
# l=[1,4,7,9,3,5]
# q=[2,3,4,5,6,7]
# for i in range(len(l)):
#     d[l[i]]=q[i]
# print(d)

# q4:
# n=int(input('enter any number'))
# d={i:i*i for i in range(n)}
# print(d)

# #q5:
# d={1:2,2:3,3:4,4:5,5:6,6:7}
# for i in range(1,len(d)+1):
# 	d.pop(i)
# print(d)

# # q6
# d={1:2,2:3,3:4,4:5,5:6,6:7}
# k=(list(d.keys()))
# l=(list(d.values()))
# print(k)
# print(l)
# k.sort(reverse=True)
# l.sort(reverse=True)
# # print(list.sort.__doc__)
# print(k)
# print(l)
# e={}
# for i in range(len(l)):
#     e[k[i]]=l[i]
# print(e)











# tasks-----sets
# ----------------
# # question5
# a=set((1,2,3,4,6,1,2,3))
# a.add(7)
# print(a)

# question4
# a=frozenset([1,2,3,47,8,9,5,2])
# print(a)

# c=set(('blue','pink','orange'))
# print(c)


# question3
# a=set((7,3,4,8,9,2))
# b=set((1,2,3,4,5,6))
# print((a-b).union(b-a))


# question2
# p=(input('enter any string'))
# v=0
# # print(p)
# for letter in p:
# 	if letter in set(('aeiou')):
# 	   v=v+1
# print(v)	   




l=[1,2,3,5,6,7]
p=[2,3,5,7,8,9]
l1=zip(l,p)
d=dict(l1)
print(d)






















