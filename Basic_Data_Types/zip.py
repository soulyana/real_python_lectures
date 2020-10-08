countries = ['France', 'Tanzania', 'Canada']
contients = ['Europe', 'Africa', 'North America']


merged = []
for i in range(len(countries)):
    # print(countries[i], contients[i])
    merged.append((countries[i], contients[i]))

print(merged)

# ZIP - used to merge lists
# zip()	Creates an iterator that aggregates elements from iterables
merged_2 = zip(countries, contients)
print(merged_2)

# ITER AND NEXT


