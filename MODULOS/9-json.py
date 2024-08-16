import json

# 1 - Converter Strings para Dicionários
person = '{"name": "Claysson", "languagens": ["Python", "JavaScript"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languagens'])

# 2 - Converter Dicionário para Json
person_json= json.dumps(person_dict)
print(person_json)

# 3 - Formatar json
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Salvando json em txt
with open("person.txt", "w") as json_file:
    json.dump(person_dict, json_file)