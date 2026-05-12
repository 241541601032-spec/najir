empty_tuple = ()
int_tuple = (1, 2, 3)
string_tuple = ("apple", "banana", "berry")
float_tuple = (1.1, 2.2, 3.3)
nested_tuple = (1, (2, 3), ["a", "b", "c"])

print("Empty tuple:", empty_tuple)
print("Integer tuple:", int_tuple)
print("String tuple:", string_tuple)
print("Float tuple:", float_tuple)
print("Nested tuple:", nested_tuple)

print("In Indexing:")
print("First element of int_tuple:", int_tuple[0])
print("Second element of string_tuple:", string_tuple[1])

print("In Nested Tuple Indexing")
print("Second element of nesting_tuple:", nested_tuple[1])

print("In Negative Indexing:")
print("Last element of string_tuple:", string_tuple[-1])
print("Second last element of float_tuple:", float_tuple[-2])

print("In Slicing:")
print("First two elements of int_tuple:", int_tuple[:2])
print("Last two elements of string_tuple:", string_tuple[-2:])

print("In Modifying list inside tuple:")
nested_tuple[2].append("d")
print("Modified Nested Tuple:", nested_tuple)

sample_tuple = (1, 2, 3, 4, 4, 2, 5)
print("Count of 2 in sample_tuple:", sample_tuple.count(2))
print("Index of first occurrence of 4:", sample_tuple.index(4))

del_tuple = (10, 20, 30)
print("Tuple before deletion:", del_tuple)
del del_tuple
try:
    print(del_tuple)
except NameError:
    print("Tuple deleted successfully.")
