"""
fruits = ["orange","banana","mango"]
for x in fruits:
    print(x)
"""
"""
for x in "banana":
    print(x)
    if x == "n":
        break
"""
"""
for x in "banana":
    if x == "n":
        break
    print(x)
"""

"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
"""
"""
fruits = ["orange","banana","mango","apple","guava"]

for fruit in fruits[0:3]:
    print(fruit)
"""
fruits = ["orange","banana","mango","apple","guava"]

for fruit in fruits:
    if fruit == "mango":
        print("{} is my favourite".format(fruit))
    else:
        print(fruit)


