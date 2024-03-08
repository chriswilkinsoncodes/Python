import random

with open('dog_names.txt', 'r') as file:
    names_list = [name.strip() for name in file]
    
# print(*names_list, sep="\n")
print(random.choice(names_list))