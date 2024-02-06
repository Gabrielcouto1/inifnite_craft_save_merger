a = {
  "discoveries": [],
  "elements": [
    {
      "text": "Earth",
      "emoji": "\ud83c\udf0d"
    },
    {
      "text": "Fire",
      "emoji": "\ud83d\udd25"
    },
    {
      "text": "Water",
      "emoji": "\ud83d\udca7"
    },
    {
      "text": "Wind",
      "emoji": "\ud83c\udf2c\ufe0f"
    },
    {
      "text": "Yellowstone",
      "emoji": "\ud83c\udf0b"
    }
  ]
};

window.$nuxt.$root.$children[2].$children[0].$children[0]._data.elements = a.elements;
window.$nuxt.$root.$children[2].$children[0].$children[0]._data.discoveries = a.discoveries;
alert(`${a.elements.length} elements discovered!`);