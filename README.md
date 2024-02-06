# inifnite_craft_save_merger
Program to merge 2 (or more) saves from infinite craft (neal.fun)

To export your 2 saves data, you need to paste the code in the "export.js" file in the console of your browser with the game open. You then will save each one of them in the json1.json and json2.json.

The JSON inputs are of the following format:

```
{
  "discoveries": [],
  "elements": [
    {
      "text": "Water",
      "emoji": "💧"
    },
    {
      "text": "Fire",
      "emoji": "🔥"
    },
    {
      "text": "Wind",
      "emoji": "🌬️"
    },
    {
      "text": "Earth",
      "emoji": "🌍"
    },
    {
      "text": "Yellowstone",
      "emoji": "\ud83c\udf0b"
    }
  ]
}
```

Then you simply run the merge.py program. The output script will be saved in "import.js". You'll copy this code and paste in the terminal. For it to work, you have to click the reset button to erase all your stuff before pasting the import code.

The output code in the import.js is of the following format:

```
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
```

There is one little issue i'm trying to figure out: the search no longer works lol. If someone knows what to do please pull request.

In order to save the merged stuff in your browser, you have to craft one new element. After you do that, it autosaves and there is no further problems.

