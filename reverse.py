# Revision

# Multiple data
# x,y,w, = 10,15,20
# print(f'This will give me all the number above such as: {x, y,w }')

# List
# Fruit = ['Apple', 'Mango', 'Orange', 'Paneapple', 'Strawberry', 'Pawpaw', 'Cucumber']
# print(f'All data will be display accordingly {Fruit}')
# print(f'Getting only first index {Fruit[6]}')
# for fruits in Fruit:
#     print(f'{fruits}')
# Dictionary
# info = {
#     'name': 'Akinola',
#     'age': 20,
#     'state': 'Lagos',
#     'country': 'Nigeria'
# }
# print(info.values())


# text = [1,2,3,4,5,6,7,8,9,10]
# for getText in text:
#     print(f'I love you {getText}')

company = {
    'Companys': 'Google',
    'Founded': 23, 
    'founder': 'known',
}
# for getOnlyKeys, getOnlyValues in company.items():
#     print(f'{getOnlyKeys} : {getOnlyValues}')
# company.pop('Founded')
company.update({'founder': 'Akinola'})
print(company) 

for companies in company:
    print(f'This {companies}')

if company.get('Founded'):
    print(f'Founded is path of Company data')
else :
    print('Company does not have Founded in their data')
# for onlyKeys in company.values():
#     print(onlyKeys)

# for onlyKeys in company.keys():
#     print(onlyKeys)