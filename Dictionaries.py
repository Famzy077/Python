Country = {
    'USA': 'Idaoh',
    'Nigeria': 'Lagos State',
    'India': 'Delhi'
}
# print(Country.get('Nigeria'))
# print(Country.get('India'))
# print(Country.get('USA'))
# if Country.get('Nigeria'):
#     print('Lagos  state state is exist inside Country data')
# else:
#     print('Country does not exist')
Country.update({'China': 'I love china'})
# Country.pop('Nigeria')
# Country.popitem()
# Country.clear()
# print(Country)
# data = 
data1 = Country.keys()
# print(data)
# print(data1)

for dataValue in Country.keys():
    print(dataValue)
# print(Country.items())
# for keys, values in Country.items():
#     print(f'{keys}: {values}')