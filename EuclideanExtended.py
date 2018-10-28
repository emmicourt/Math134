
def euclideanLinearRec(a, b, u1, u2, v1, v2):
        r = a%b
        q = a//b

        print(repr(a)+ " = " +repr(q)+ " * " +repr(b)+ " + " +repr(r)+  "       ui=" + repr(u2) + " vi =" +repr(v2))
        if r == 0:
                print("==> u = " + repr(u2)+"  v = "+ repr(v2))
                return r
        else:
                return euclideanLinearRec(b, r, u2, u1 -(u2*q), v2, v1-(v2*q) )

def euclideanLinear(a, b):
        print("u and v of " + repr(a) + " and " +repr(b)+ ":")
        u1 = 1
        u2 = 0
        v1 = 0
        v2 = 1
        q = 0
        if a > b:
                result = euclideanLinearRec(a, b, u1, u2, v1, v2)
        else:
                result = euclideanLinearRec(b, a, u1, u2, v1, v2)



x = int(input("Enter a: ")) 
y = int(input("Enter b: ")) 

euclideanLinear(x, y)
