name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#Adding Weight in kilos to show off a bit. 
weight_kilos = weight * 0.4535924

#Also adding length in centimeters to really show off... Fuck the Imperial System of measurement.
height_cm = height * 2.54


print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "My weight in kilos is: %.2f kilos" % weight_kilos
print "My height in centimeters is: %d cm" % height_cm