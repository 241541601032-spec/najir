empty_list = []
int_list = [1, 2, 3]
string_list = ["apple", "banana", "berry"]
float_list = [1.1, 2.2, 3.3]
nested_list = [1, [2, 3], ["a", "b", "c"]]

print("Empty list:", empty_list)
print("Integer list:", int_list)
print("String list:", string_list)
print("Float list:", float_list)
print("Nested list:", nested_list)
print("In Indexing:")
print("First element of int_list:", int_list[0])
print("Second element of string_list:", string_list[1])
print("In Nested List Indexing")
print("Second element of nested_list:", nested_list[1])
print("In Negative Indexing:")
print("Last element of string_list:", string_list[-1])
print("Second last element of float_list:", float_list[-2])
print("In Slicing:")
print("First two elements of int_list:", int_list[:2])
print("Last two elements of string_list:", string_list[-2:])
nested_list[2].append("d")
print("Modified Nested List:", nested_list)
sample_list = [1, 2, 3, 4, 4, 2, 5]
print("Count of 2 in sample_list:", sample_list.count(2))
print("Index of first occurrence of 4:", sample_list.index(4))
del_list = [10, 20, 30]
print("List before deletion:", del_list)
del del_list
try:
    print(del_list)
except NameError:
    print("List deleted successfully.")
