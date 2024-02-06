import json

def generate_js_code(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

    merged_json = {"discoveries": [], "elements": []}

    for element1, element2 in zip(json1["elements"], json2["elements"]):
        if element1 != element2:
            merged_json["elements"].append(element1)
            merged_json["elements"].append(element2)
        else:
            merged_json["elements"].append(element1)

    js_code = (
        f'a = {json.dumps(merged_json, indent=2)};\n\n'
        'window.$nuxt.$root.$children[2].$children[0].$children[0]._data.elements = a.elements;\n'
        'window.$nuxt.$root.$children[2].$children[0].$children[0]._data.discoveries = a.discoveries;\n'
        'alert(`${a.elements.length} elements unlocked in total.`);'
    )

    return js_code

if __name__ == "__main__":
    file1 = "json1.json"
    file2 = "json2.json"

    js_code = generate_js_code(file1, file2)

    with open("import.js", 'w') as output:
        output.write(js_code)

    print("JavaScript code saved to import.js")