# list is mutable in nature(element of list can be change)
# bounded by square brackets'[]'

l1=[1,2,3,4,5,6,7]
print(l1)

print(l1.index(2))

print(type(l1))

print(len(l1))

print(l1.append([1,2]))
print(l1)

print(l1.extend([99,100]))
print(l1)

l2=[1,2,3,1,4,5,1,3,1]
print(l2.append(8))
print(l2)

print(l2.insert(1,6))
print(l2)

print(l2.count(1))

print(l2.remove(6))
print(l2)

print(l2.pop(0))
print(l2)

print(l2.sort(reverse=True))
print(l2)

print(l2[::-1])


