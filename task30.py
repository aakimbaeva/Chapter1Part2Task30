text = input('Write something: ')
elem = input('What character do you want to count: ')
q = 0
for i in text:
    if i == elem:
        q += 1

print(q)
