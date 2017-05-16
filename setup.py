from ipwhois import IPWhois
from pprint import pprint

#ip=input("skriv ip:")
obj = IPWhois("212.214.217.4")
print (type(obj))
results = obj.lookup_rdap(depth=1)

print(results['network']['name'])
pprint(results)
