'''
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
'''

animals = ['lion', 'tiger', 'bear', 'elephant', 'giraffe']
animals.pop(2) # Delete the animal at the 3rd index (bear)
print(animals)
animals.append('zebra')  # Append a new animal at the end of the list
print(animals)
animals.pop(0)  # Delete the animal at the beginning of the list (lion)
print(animals)  # Print all the animals
print(animals[:3])  # Print only the first 3 animals