"""
Flatonacci secuence is a secuence which is result from the same given secuence 
plus the sum of the last 3 numbers of the secuence. 
The challenge is to create a flatonacci function that given a signature returns the first 
n elements - signature included of the so seeded sequence. So, if we are to 
start our Flatonacci sequence with [1, 1, 1] as a starting input (AKA signature) and n = 8,
we have this sequence:
[1, 1 ,1, 3, 5, 9, 17, 31]
Another example; if signature is the secuence [0, 0, 1] we should get some thing
like:
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
- Signature will always contain 3 numbers 
- n will always be a non-negative number
- if n == 0, then return an empty list and be ready for anything else which is not
clearly specified ;)
Note. Please note that we are gonna test the funcion against a lot of different signatures and n's
"""

def validateInteger(var):
	try:
		int(var)
		return True
	except:
		return False


def flatonacci(signature: list, n: int) -> list:
    
    if(n == 0):
        signature = []
        return signature
    
    a = signature[0]
    b = signature[1]
    c = signature[2]
    
    if(validateInteger(a) and validateInteger(b) and validateInteger(c)):

        for _ in range(n-len(signature)):
            d = a + b + c
            signature.append(d)
            a = b
            b = c
            c = d
    else: 
        signature = []
        print("An error has ocurred,you did not pass a number")
        return signature

    print(signature)

    # happy coding
    pass 
    return signature

flatonacci([0, 1,1],8)