import numpy as np

usermass = []

lm = ['222', '222', '333']
print(len(usermass))

def unique(usermass):
    x = np.unique(np.array(usermass))
    return len(x)

print("the unique values from 1st list is")
print(unique(usermass))