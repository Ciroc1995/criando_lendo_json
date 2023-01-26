import json


# Criar ou ler JSON
usuarios_json = """{
    "name": "John Smith",
    "age": 30,
    "city": "New York",
    "isStudent": true,
    "gpa": 3.5
}"""


# Salvar um string JSON -> Arquivo JSON
with open('desafio.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(usuarios_json, arquivo_json)


with open('desafio.json', encoding='utf-8') as arquivo_json:
    string_desafio_json = json.load(arquivo_json)
    dicionario_desafio_json = json.loads(string_desafio_json)
    print(dicionario_desafio_json['name'])
