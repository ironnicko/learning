a=['Tim', 'Nikhil', 'Harold']
b=[25,17,17]
#keep em related
#g = [f'{i[0]}:{i[1]}\n' for i in list(zip(a,b))]
print(*[i for i in [f'{i[0]}:{i[1]}\n' for i in list(zip(a,b))]])
g = {i:i**100 for i in range(1,21)}
print(*[i for i in [f'{i}:{g[i]}\n' for i in g]])
print(f'{22/7:.100f}')
for i,names in enummerate(a):
  print(f'{i+1}:{name}')#index
