A primitive script made for listing all possible products of items in multiple lists. Run via a terminal, like this:
```bash
python python-unique-combinations.py <input-file> <output-file>
```

Takes in a JSON-formatted file, like this:
```json
{
  "fruits": [
    "Apples",
    "Oranges",
    "Tangerines",
    "Pears"
  ],
  "desserts": [
    "Pie",
    "Cake",
    "Sorbet"
  ]
  ...
}
```
Note that it accepts a multiple of lists, but amount of calculations grow exponentially.
