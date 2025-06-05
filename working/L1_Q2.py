"""Part1"""

names = ["Mary", "John", "Sarah"]
age = [21, 56, 98]

for x, y in zip(names, age):
    print("{} is {} years old".format(x, y))


""" Part2 """

import random

random_list = []
start = 0
end = 9

for i in range(10):
    random_list.append(random.randint(start, end))


for index, number in enumerate(random_list):
    print("Match: {} and {}".format(number, index))
