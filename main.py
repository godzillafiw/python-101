import value_operations
from value_operations import swap
from fizzbuzz import find_fizzbuzz

number = 3
name = "Q"

print(number)
print(name)

if number == 3:
    print("Number is 3")
    print("Inside IF")

print("Outside IF")

fruits = ["Orange", "Apple", "Durain"]
print(fruits[0])

# Bad
for i in range(0,len(fruits)):
    print(i, fruits[i])

# Good
for fruit in fruits:
    print(fruit)

# Good
for i,fruit in enumerate(fruits):
    print(i, fruit)

company = ("Github", "SF", "USA")
print(company)
# company_name, location = company
# print(company_name, location)

a = 5
b = 10

# print(a,b)
# print(b,a)

a, b = b , a

print(a,b)

print(swap(5,1))

print(__name__)

if __name__ == "__main__":
    results = value_operations.swap(5,1)
    print(results)

    for number in range(0,16):
        print(number, find_fizzbuzz(number))
    