# There are 100 Cars
cars = 100
# There is space in the car for 4 people
space_in_a_car = 4
# There are 30 drivers
drivers = 30
# There are 90 passengers to take
passengers = 90
# Cars not driven = 100 Cars - 30 Drivers = 70 Cars not Driven
cars_not_driven = cars - drivers
# Cars Driven = Number of Drivers = 30
cars_driven = drivers
# Carpool Capacity = Cars Driven 30 * Space in a Car 4 = 120
carpool_capacity = cars_driven * space_in_a_car
# Average Passengers per car = Passengers 90 / Cars driven 30 = 3 
# Written as 3.0 in some cases, and 3 in others.
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers avalable.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")