values = [1, 2, 'rahul', 4, 5]
# List is data type that allows multiple values and can be different data types
print(values[0])

print(values[3])

print(values[-1])

print(values[1:3])

values.insert(3, 'shetty')

print(values)

values.append("End")

print(values)

values[2] = 'RAHUL'

print(values)

del values[0]

print(values)

# Tuple - same as list data type but immutable

val = (1, 2, 'rahul', 4.5)

print(val[1])

# Dictionary

dic = {"a": 2, 4: "bcd", "c": "Hello world"}

print(dic["c"])
