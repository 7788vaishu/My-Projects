#SET
s1={1,2,3,4,2,4,2}
print(s1)

s2={5,6,7,8}

#methods of set 
# UNION
print(s1.union(s2))

# intersection
print(s1.intersection(s2))

#difference
print(s1.difference(s2))
print(s2.difference(s1))

# symentric_difference
print(s1.symmetric_difference(s2))