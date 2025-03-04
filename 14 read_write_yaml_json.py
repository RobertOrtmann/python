import yaml
import json

# yaml.safe_load is a single function call provided by the PyYAML library.This function takes a YAML document (either as a string or a file object)
# and parses it into a Python dictionary (or other corresponding Python data structures, such as lists).

with open('14_network_config.yml', "r") as file:
    network_config = yaml.safe_load(file)
print(network_config)

network_data = {
    'switch' : 'Switch1',
    'ports' : [
        {'name' : 'FastEthernet0/1', 'vlan' : '10'},
        {'name' : 'FastEthernet0/2', 'vlan' : '20'},
    ]
}
with open('14_new_network_config.json' , 'w') as file:
    json.dump(network_data, file, indent=4)

# The json.dump function in Python is used to serialize a Python object and write it as a JSON formatted stream to a file.
# json.dump(obj, fp, indent=None)   -   
# obj: The Python object (e.g., dictionary, list) you want to serialize.
# fp: The file-like object to which the JSON data will be written.
# indent: Specifies the indentation level for pretty-printing the JSON data. 
# If None, the most compact representation is used. If an integer, it specifies the number of spaces to use for indentation


# Termin "serializować" (ang. "serialize") oznacza proces przekształcania obiektu danych w formę, która może być łatwo przechowywana lub przesyłana,
#  a następnie odtworzona w późniejszym czasie. Odbywa się za pomocą funkcji json.dump lub json.dumps
# W kontekście programowania, serializacja często odnosi się do konwersji obiektów do formatu tekstowego,
#  takiego jak JSON, XML, lub binarny, aby można je było zapisać do pliku lub przesłać przez sieć
# Proces przekształcania obiektu danych (np. słownika w Pythonie) do formatu, 
# który można zapisać do pliku lub przesłać przez sieć. W powyższym przykładzie, obiekt data jest serializowany do formatu JSON

# json.dump
# Cel: Serializuje obiekt Python do formatu JSON i zapisuje go bezpośrednio do pliku (lub innego obiektu obsługującego metodę write()).
# Użycie: Używane, gdy chcesz zapisać dane JSON bezpośrednio do pliku

# json.dumps
# Cel: Serializuje obiekt Python do formatu JSON i zwraca go jako ciąg znaków (string).
# Użycie: Używane, gdy chcesz uzyskać dane JSON jako ciąg znaków, na przykład do wysłania przez sieć lub zapisania do zmiennej.
# szczególnie przydatne w komunikacji między różnymi systemami lub usługami  na przykład w aplikacjach webowych, API.

data = {
    'name': 'Jan Kowalski',
    'age': 30,
    'city': 'Warszawa'
}

# Serializacja do ciągu znaków (string) JSON
json_string = json.dumps(data, indent=4)
print("Serialized JSON string:")
print(json_string)

# Serializacja do pliku JSON
with open('14_data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data has been written to data.json")