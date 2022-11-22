# this is a number
a = 1
b = 3
print(a+b)
type(a+b)
type(2.1)

# this is a string
c = "Network Security"
print(c)

# this is a multi line string
d = '''Network Security
is fun'''
print(d)

e = "Network Security \nis Fun \n"
print(e)

data_a = 1
data_b = 3.4
print(data_a + data_b)

data_c = "Network Security"
data_d = " is fun!"
print(data_c + data_d)

flag = False
type(flag)

# if else
if(flag):
    print("Hello World")
else:
    print("Goodnight World")

# OSI Layer
osi_layer = ["physical", "data link", "network", "transport", "presentation", "session", "application"]
print(osi_layer)
print(osi_layer[1])

# operation in list
import numpy as np
list_a = [1,2,3]
list_b = [4,5,6]

print((list_a + list_b))

numpy_list_a = np.array(list_a)
numpy_list_b = np.array(list_b)

print(type(numpy_list_a))

print(numpy_list_a + numpy_list_b)

osi_layer = ["layer 1", "physical",
             "layer 2", "data link",
             "layer 3", "network",
             "layer 4", "transport",
             "layer 5", "presentation",
             "layer 6", "session",
             "layer 7", "application"]

# {} used for dict
osi_layer_dict = {"layer 1": "physical",
             "layer 2": "data link",
             "layer 3": "network",
             "layer 4": "transport",
             "layer 5": "presentation",
             "layer 6": "session",
             "layer 7": "application"}

print(osi_layer_dict["layer 7"])
