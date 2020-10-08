#downloading files
#one way function of summary of context what it's been passed
#print(hash(123)) #value of int
#print(hash('hello from real python!')) #bbigger hash
#print(hash('hello from real python.'))

with open('moby_dick.txt', 'r') as file_obj:
    moby_list = file_obj.readlines()

moby_1 = ''.join(moby_list)
moby_2 = ''.join(moby_list)


print(hash(moby_1) == hash(moby_2)) #if they're the same; true

moby_2 += ' '
print(hash(moby_1) == hash(moby_2)) #hash is different
len(moby_1)
len(moby_2)