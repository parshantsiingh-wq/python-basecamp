p={3,4,6,"parshant","singh"}
print(type(p))
print(len(p))
# print(max(p))
n="parshant"
s = set([3,4,5,6,7,8])
m=set(n)

l=tuple(n)
print(l)

print(s)
print(m)

print(type(s))
print(type(m))

# some operations

s.add(1)  # add method takes only one argument
s.add(1)  # it is not working because in set repetition will not perform
s.add(2)
print(s)

print(p.union(s))
print(s.union(p))
print(s.union({5,"aman"}))

print(p.intersection(s))
s2=s.intersection({3,4,6,8,9})

print(s.isdisjoint({3,4,5,6}))


s.remove(3)
print(s)










