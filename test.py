# from mymodule import greet
import mymodule
# from math import sqrt, pi
from math import sqrt  as sq
from my_package import greet

print(mymodule.greet("Filan"))

cal = mymodule.Calculator()

print(cal.add(5, 3))
print(cal.substrack(10, 4))

# result = math.sqrt(25)
# print("Square root of 36 is:", sqrt(36))
# print("Value of pi is:", pi)
print("Square root of 36 is:", sq(36))
print(greet("Filan2"))