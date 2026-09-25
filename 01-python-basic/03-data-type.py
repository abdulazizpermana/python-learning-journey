x = 7
print(type(x))  # Output: <class 'int'>

x = 6.0
print(type(x))  # Output: <class 'float'>

x = 1+2j
print(type(x))  # Output: <class 'complex'>


# tipe data number bersifat immutable, artinya nilainya tidak dapat diubah setelah dibuat.
y = 10
print(y)  # Output: 10
print(id(y))  # Output: (misalnya) 140711234567456

y = 2
print(y)  # Output: 2
print(id(y))  # Output: (misalnya) 140711234567488


# boolean
is_active = True
print(type(is_active))  # Output: <class 'bool'>

is_active = False
print(type(is_active))  # Output: <class 'bool'>


# string
name = "John Doe"
print(type(name))  # Output: <class 'str'>