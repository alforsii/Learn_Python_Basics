friends = ['Kevin', 'Karen', 'Jim', 'Ashraf']
new_friends = ['Tom', 'ASH']
print(friends)

# concat in py
friends.extend(new_friends)
print(friends)

# push into array a new elem in py
friends.append('Nodir')
print(friends)

# insert in the middle somewhere
friends.insert(1, 'Kelly')
print(friends)

# remove elem
friends.remove('Karen')
print(friends)

# remove all
# friends.clear()
# print(friends)

# pop()
friends.pop()
print(friends)

# count elem
print(friends.count('Ashraf'))

# sort
friends.sort()
print(friends)

# reverse
friends.reverse()
print(friends)

# copy
friends2 = friends.copy()



