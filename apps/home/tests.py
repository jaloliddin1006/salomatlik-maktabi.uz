from django.test import TestCase

import types
 
code_string = """

a = 5
a += 6
b = 10

c = a + b

s = sqrt(16)

"""
my_namespace = types.SimpleNamespace()
exec(code_string, my_namespace.__dict__)
print(my_namespace.c)  # 11
print(my_namespace.s)  # 4.0
print(my_namespace)  # 11