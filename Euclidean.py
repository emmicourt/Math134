
def euclideanRec(a, b):
	r = a%b 
	q = a//b
	print(repr(a)+ " = " +repr(q)+ " * " +repr(b)+ " + " +repr(r))  
	if r == 0: 
		return b
	else: 
		return euclideanRec(b, r) 

def euclidean(a, b):
	print("Euclidean Algorithm of " + repr(a) + " and " +repr(b)+ ":") 
	result = 0
	if a > b: 
		result = euclideanRec(a, b)
	else:
		result = euclideanRec(b, a) 
	print("==>  gcd(" +repr(a)+ ", " +repr(b)+") = " + repr(result)) 
	print()

x = int(input("Enter a: "))
y = int(input("Enter b: "))
euclidean(x, y) 

