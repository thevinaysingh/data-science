# DATA-TYPES

## common methods or properties

len()
type(): `<class 'list'>`
str()
int()
float()
list()
input()
tuple()
set()
map()
print()
None: None is used to define a null value. It is not the same as an empty string, False, or a zero. It is a data type of the class NoneType object. Assigning a value of None to a variable is one way to reset it to its original, empty state.

## Array

Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable\*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered\*\* and changeable. No duplicate members.
\*Set items are unchangeable, but you can remove and/or add items whenever you like.
\*\*As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

### List (Array) helper functions

Check if Item Exists:

```
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

Looping Using List Comprehension:

```
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
```

```
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

//Or

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
```

append() Adds an element at the end of the list
clear() Removes all the elements from the list
copy() Returns a copy of the list
count() Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list
