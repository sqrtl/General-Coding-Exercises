def add(a, b):
    print ("ADDING %d + %d" %(a,b) )
    return a + b

def subtract(a, b):
    print ("SUBTRACTING %d - %d" %(a,b) )
    return a - b

def multiplication(a, b):
    print ("MULTIPLYING %d X %d" %(a,b) )
    return a * b

def division(a, b):
    print ("DIVIDING %d + %d" %(a,b) )
    return a / b

print ("Lets do some math with just functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiplication(90, 2)
iq = division(100, 2)

print("Age: %d, Height: %d, Weight %d, IQ: %d" %(age, height, weight, iq))

# A puzzle for extra credit, type it in any. 
print ("Here's a puzzle you ungreatful bitch.")

what = add(age, subtract(height, multiplication(weight, division(iq, 2))))

print ("That becomes: ", what, "Can you do it by hand?")