# tuple is immutable (element of tuple cannot be change)
# bounded by paranthesis '()'

t1=(1,2,3,1,2,4,5,2,6)
print(type(t1))
print(len(t1))

# methods of tuple
# indexing
print(t1.index(3))

#count
print(t1.count(2))
print(t1.count(1))

#tuple of list
tol=([1,2],[3,4],[5,6])
print(tol)
print(tol[-1][-1])

#list of tuple
lot=[(1,2),(3,4),(5,6)]
print(lot)
