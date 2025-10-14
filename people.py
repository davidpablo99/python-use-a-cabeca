import pprint

people = {}
people['Ford'] = {
    'Name' : 'Ford Prefect',
    'Gender' : 'Male',
    'Occupation' : 'Researcher',
    'Home Planet' : 'Betelgeuse Seven'
}
people['Arthur'] = {
    'Name' : 'Arthur Dent',
    'Gender' : 'Male',
    'Occupation' : 'Sandwich-Maker',
    'Home Planet' : 'Earth'
}
pprint.pprint(people['Arthur']['Occupation'])