![Static Badge](https://img.shields.io/badge/Alpha%20Phase-FF0000)
# inventore It! Inventory manager

####################
---**WORK IN PROGRESS**---
####################

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
	        ├── Items
	            ├── some_item.itm
	            ├── another_one.itm
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
==marked==
2<sup>10</sup>
H<sup>2</sub>O
`Inline monospace`
> Quote

[Link to Google](https://google.com/)
Image:  ![Alt text](img.jpg =60x50)

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
