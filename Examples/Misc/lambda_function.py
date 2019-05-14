
# Different ways of using a lamba function

# 1st way of using lambda
x = lambda a : a + 1
print(x(5))


# 2nd way of using lambda
x = lambda a,b : a * b
print(x(3,5))


# 3rd way of using lambda
x = lambda a,b=4 : a * b
print(x(3))

# 4th way of using lambda
x = lambda a,b,c = 4 : a + b + c
print(x(1,b = 5))


# 3rd way of using lambda
def lambda_using_func(n):
	return lambda a : a + n

x = lambda_using_func(2) 
print(x(5))
