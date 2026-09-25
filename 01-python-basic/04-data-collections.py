# ============================================================= LISTS =============================================================

# x = [1, 2.2, 'Hello', True]
# print(type(x))  # Output: <class 'list'>

# x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

# print(x[0])
# print(x[2])
# print(x[-1])
# print(x[-3])

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']

"""

# ============================================================= TUPLES ============================================================
x = (1, "Dicoding", 1+3j)
print(type(x))

"""
Output:
<class 'tuple'>
"""

x = (5, 'program', 1+3j)
# x[0] = 10  # This will raise an error because tuples are immutable
print(x[1])
print(x[0:3])

""" 
Output:
program
(5, 'program', (1+3j))
"""
# ============================================================== SETS =============================================================
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

"""
Output:
{1, 2, 3, 7, 13}
<class 'set'>
"""

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

"""
Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}

"""

# ============================================================== DICTIONARIES =======================================================
x = { 'name': 'Perseus Evans',
    'age': 20, 'isMarried': False, }

print(type(x))

"""
Output:
<class 'dict'>
"""

print(x['name'])
x['job'] = 'Software Engineer'
print(x)

del x['isMarried']
print(x)

x['name'] = 'John Doe'
print(x)


# ============================================================= Convert ============================================================
# Convert int to float
print(float(10))  # Output: 10.0

# Convert float to int
print(int(10.5))  # Output: 10

# Convert int to str
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

"""
Output:
25
25
25.0
25.6
"""

# convert summary
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))

"""
Output:
{1,2,3}
(5,6,7)
['h','e','l','l','o']
"""