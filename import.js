a = {
  "discoveries": [],
  "elements": [
    {
      "text": "Water",
      "emoji": "\ud83d\udca7"
    },
    {
      "text": "Fire",
      "emoji": "\ud83d\udd25"
    },
    {
      "text": "Wind",
      "emoji": "\ud83c\udf2c\ufe0f"
    },
    {
      "text": "Earth",
      "emoji": "\ud83c\udf0d"
    },
    {
      "text": "Steam",
      "emoji": "\ud83d\udca8"
    },
    {
      "text": "Lava",
      "emoji": "\ud83c\udf0b"
    },
    {
      "text": "Mud",
      "emoji": "\ud83d\udca9"
    },
    {
      "text": "Volcano",
      "emoji": "\ud83c\udf0b"
    },
    {
      "text": "Clay",
      "emoji": "\ud83c\udffa"
    },
    {
      "text": "Stone",
      "emoji": "\ud83e\udea8"
    },
    {
      "text": "Pottery",
      "emoji": "\ud83c\udffa"
    },
    {
      "text": "Sand",
      "emoji": "\ud83c\udfd6\ufe0f"
    }
  ]
};

window.$nuxt.$root.$children[2].$children[0].$children[0]._data.elements = a.elements;
window.$nuxt.$root.$children[2].$children[0].$children[0]._data.discoveries = a.discoveries;
alert(`${a.elements.length} elements unlocked in total.`);