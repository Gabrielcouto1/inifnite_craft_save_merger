import json

def merge_and_sort_jsons(json1, json2):
    merged_json = {"discoveries": [], "elements": []}

    # Merge elements without duplicates
    for element in json1["elements"]:
        if element not in merged_json["elements"]:
            merged_json["elements"].append(element)

    for element in json2["elements"]:
        if element not in merged_json["elements"]:
            merged_json["elements"].append(element)

    # Sort elements by the "text" field in ascending order
    # Comment next line if you dont want to rearrange elements in alphabetical order
    merged_json["elements"] = sorted(merged_json["elements"], key=lambda x: x.get("text", ""))

    return merged_json

with open('json1.json', 'r') as file1, open('json2.json', 'r') as file2:
    json1 = json.load(file1)
    json2 = json.load(file2)

# Merge and sort the JSONs
merged_json = merge_and_sort_jsons(json1, json2)

with open('import.js', 'w') as output_file:
    js_code = (
        f'a = {json.dumps(merged_json, indent=2)};\n\n'
        'window.$nuxt.$root.$children[2].$children[0].$children[0]._data.elements = a.elements;\n'
        'window.$nuxt.$root.$children[2].$children[0].$children[0]._data.discoveries = a.discoveries;\n'
        'alert(`${a.elements.length} elements discovered!`);'
    )
    output_file.write(js_code)

print("Javascript code to paste on terminal saved in 'import.js'")
