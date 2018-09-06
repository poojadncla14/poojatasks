# Python class - 2 Online 21-05-2018

# Python -- uses 
# features , introduction 

# main compenents in Python programming 
# -------------------------------------

# Keywords and identifers
# -----------------------
# library of words (Keywords)
# 	pre defined
# 	cannot be changed 
# 	should only purpose defined 
# 	cannot be deleted 
# Python 2.7 --> 31 Keywords
# Python 3.6 --> 33 Keywords
# mostly small case --> None , True , False

# get keywords
# ------------
# import keyword 
# keyword.kwlist

# identifers
# ----------
# library of words given by user/developer
# names of compenents(datatypes , functions , classes , objects , files )
# rules 
# 	cannot use keyword
# 	start with letter
# 	cannot start with number or special char
# 	start with small case ( recommended )
# 	can start with an underscore ( _ , __)(special)
# Input - output 
# --------------
# > a = 10 ALLOWED
# >>> 1 = "khan" not ALLOWED
#   File "<stdin>", line 1
# SyntaxError: can't assign to literal
# >>> 1name = "Python" not ALLOWED
#   File "<stdin>", line 1
#     1name = "Python"
#         ^
# SyntaxError: invalid syntax
# >>> name = "Python" ALLOWED
# >>> NAME = "Python" ALLOWED but not recommended
# >>> @name = "Python" not ALLOWED
#   File "<stdin>", line 1
#     @name = "Python"
#           ^
# SyntaxError: invalid syntax
# >>> name@ = "python" not ALLOWED
#   File "<stdin>", line 1
#     name@ = "python"
#           ^
# SyntaxError: invalid syntax
# >>> _name = "python" ALLOWED but special case
# >>> __name = "python" ALLOWED but special case
# ----------------------------------------------
# Variable 
# --------
# -> mini bucket to store values / data
# 	-> name (identifier)
# 	-> data ( many types)
# 	-> memory location ( address where it is stored )
# -> var_name = < value >

# -> datatypes--> type(var_name)
# -> memory --> id(var_name)

# var_name --> identifier
# value --> data 
# = -> assignment operator 
# ---------------------------------------------
# Data Types 
# ----------
# 5 datatypes 
# 	2 independent --> numbers , Strings 
# 	3 derived --> lists , tuples and dictionaries 

# Numbers --> integer , float , long , complex 
# int class
# maximum possible integer in python