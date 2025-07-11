![inventore It! logo](./assets/icon.svg) ![Static Badge](https://img.shields.io/badge/Alpha%20Phase-FF0000)  ![Static Badge](https://img.shields.io/badge/Python-3.10.11-00CC00)  ![Static Badge](https://img.shields.io/badge/CustomTKinter-5.2.2-0088CC)

TODO
- [X] DB Structure
- [X] Reading them
- [X] Show their content in the interface
- [ ] Import items/inventories
- [ ] Edit and save DBs
- [ ] Tabs with different interfaces (to test and improve)
- [X] Panned window

Later
- [ ] Undo, Redo, whatever other important functionalities
- [ ] Exports to many formats
- [ ] Reading other formats
- [ ] Import from many formats
- [ ] API
- [ ] Extensions 

# inventore It! Inventory manager

####################</br>
---**WORK IN PROGRESS**---</br>
####################</br>

Based on Python and CustomTKinter

# Getting started

## Installation
Extract the content of the zipfile, the app is a standalone, or use an installer from [link to releases].







# Here comes the docs~

## Database

In inventore It!, **databases** are zipfiles containing json files. Databases are splitted into multiples **inventories**, containing your **items**. A `.info` file is present in every folder. To prevent items name-dependancy, an individual ID is created with the creation date of the db, inventory or item, add a magic number and multiply it with another. (details in app/logics/id_creator.py) 

#### Fig 1: Global Structure:
```
	DB/
	├── db.info
	├── log.state
	├── logs/
	    ├── date.log
	    ├── date.log
	├── Inventories/
	    ├── inventory1/
	        ├── ivt.info
	        ├── log.state
	        ├── logs/
	        ├── Items/
	            ├── some_item/
                        ├── some_item.itm
                        ├── logs/
	            ├── another_one/
	    ├── inventory2/
	        ├── ivt.info
	        ├── log.state
	        ├── logs/
```
---
### File structure
#### db .info

The `db.info` (json file) contains every basic information about the database:
```json
{
  "id":"0123456789abcdef"
  "name":"DB",
  "created":20250619192250,
  "updated":20250619231600,
  "owner":"Yakari_68",
  "format": "inventore It! Database (v1)",
}
``` 

---
#### ivt .info

The `ivt.info` (json file) contains every basic information about the inventory its in. 
```json
{
  "id":"0123456789abcdef"
  "name":"Inventory 1",
  "created":20250619192250,
  "updated":20250619231600,
  "owner":"Yakari_68",
  "columns":[
      "name",
      "created",
      "updated",
      "number",
      "type",
      "storage"
      ]
}
``` 

---
#### my_item .itm
`.itm` files contain informations about an item. Required fields are defined in the `ivt.info`.
```json
{
  "id":"0123456789abcdef"
  "name":"some item",
  "created":20250619192250,
  "updated":20250619231600,
  "number":15,
  "type":"My item type",
  "storage": "Antartica"
}
```
## API
One can easily create an extension for inventore It!, get to your IDE and start coding!



# Syntax memo

```mylanguage
Some code
blocks
```
**bold**,*italic*,~~strikethrough~~,
- some list
  * more
     + More...
       1. More!
       2. MORE!!!
- some more lines
- [ ] Checkbox unchecked
- [x] Checkbox checked 

Separator:

---
2<sup>10</sup>
H<sub>2</sub>O
`Inline monospace`
> Quote

[Link to Google](https://google.com/)

Image:  ![Alt text](img.jpg)

<!-- Commented text -->

Tables:

|Stick Left       |Center                           |Right                        |
|:----------------|:-------------------------------:|--------------------------------------:|
|Row 1            |Some content                     |Hey guys                     |
|Row 2 is quite long           |Some content but larger so you can see everything is centered                     |Have you ever heard          |
|Row 3            |Some content                     |About Lord Vraxx???          |

Notes:

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

Badges: https://shields.io/badges/static-badge
