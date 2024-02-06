import json

def merge_jsons(json1, json2):
    merged_json = {"discoveries": [], "elements": []}

    # Merge elements from the first JSON
    for element in json1["elements"]:
        if element not in merged_json["elements"]:
            merged_json["elements"].append(element)

    # Merge elements from the second JSON
    for element in json2["elements"]:
        if element not in merged_json["elements"]:
            merged_json["elements"].append(element)

    return merged_json

# Ler os JSONs dos arquivos
with open('json1.json', 'r') as file1, open('json2.json', 'r') as file2:
    json1 = json.load(file1)
    json2 = json.load(file2)

# Mesclar os JSONs
merged_json = merge_jsons(json1, json2)

# Escrever o JSON mesclado em um novo arquivo
with open('import.js', 'w') as output_file:
    js_code =(
        f'a = {json.dumps(merged_json, indent=2)};\n\n'
        'window.$nuxt.$root.$children[2].$children[0].$children[0]._data.elements = a.elements;\n'
        'window.$nuxt.$root.$children[2].$children[0].$children[0]._data.discoveries = a.discoveries;\n'
        'alert(`${a.elements.length} elements discovered!`);'
    )
    output_file.write(js_code)

print("Javascript code to paste on terminal saved in 'import.js'")
