import requests
import hashlib
import zipfile

url = 'https://archive.ics.uci.edu/static/public/109/wine.zip'
response = requests.get(url)

expected_hash_wine_index = 'c24d1f17df97bdde234913bb0a3334227215eefd0ad3d6a9988151d49971cba7'
expected_hash_wine_data = '6be6b1203f3d51df0b553a70e57b8a723cd405683958204f96d23d7cd6aea659'
expected_hash_wine_names = 'f1b84f2ef845e0bdebf13e14fa7a213e56de4f1baa40c5974dbd1ee51c5ae710'

response = requests.get(url)

with zipfile.ZipFile('wine.zip',mode = 'r') as archive:
    archive.extractall(path='data/wine')

index = 'data/wine/index'
data = 'data/wine/wine.data'
names = 'data/wine/wine.names'

def hash_compare(filename, hash_value):
    try:
        with open(filename, mode='rb') as file:
            data = file.read()
            sha256hash = hashlib.sha256(data).hexdigest()
            return sha256hash == hash_value
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False

result1 = hash_compare(index, expected_hash_wine_index)
result2 = hash_compare(data, expected_hash_wine_data)
result3 = hash_compare(names, expected_hash_wine_names)
print("wine_index hash match:", result1)
print("wine_data hash match:", result2)
print("wine_names hash match:", result3)
