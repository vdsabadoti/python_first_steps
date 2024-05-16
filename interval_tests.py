from Interval import Interval

test = Interval.createInterval(1, 2)
seconde = Interval.createInterval(4, 7)
sum = test + seconde
done = seconde + test
intersection = seconde.intersection(test)
print("Intersection btw {} and {}".format(seconde, test))
print(intersection)
print("Sum of {} and {}".format(seconde, test))
print(sum)
print("Trying to set the min of {} to 10, the result is : ".format(test))
test.min = 10
print(test)
print("Trying to set the min of {} to 1, the result is :".format(test))
test.min = 1
print(test)

print(sum == done)