it_companies = {'facebook','google','microsoft','apple','IBM','oracle','amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
len(it_companies)
print(len(it_companies))
it_companies.add('twitter')
print(it_companies)
it_companies.update(['AT%T','cisco','spaceX','paramount'])
print(it_companies)
it_companies.remove('twitter')
print(it_companies)
C = A.union(B)
print(C)
A.intersection(B)
print(A.intersection(B))
print(A.issubset(B))
print(A.difference(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(A))