rivers = {'Nile': 'Egypt','Yangtze': 'China', 'Ganges': 'India'}
for river, country in rivers.items():
    print (f"the {river} River runs through {country}.")
for river in rivers:
    print (river)
for river, country in rivers.items():
    print (country)