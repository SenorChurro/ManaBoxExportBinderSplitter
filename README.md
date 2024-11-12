# ManaBox Export CSV Binder Splitter

I use [ManaBox](https://manabox.app/) for cataloguing my MTG Collection and [Moxfield](https://www.moxfield.com/) for managing my decks and sharing with friends.

Manabox has an export CSV feature that exports everything with binder information. While Moxfield can import the CSV, it can not read the binder information and manage new binders.

So I wrote this quick python script to break out the files.

## Requirements
Python 3.3 or greater

## How to use
- Clone the repo or copy the python file.
- Place the python file and the ManaBox export CSV in the same directory
- Run the following command
  - ``` py split_csv_by_binder.py PATH_TO_CSV```
- An output directy will be made where the python script is, inside will be individual CSVs per binder name.

Afterwards I just import them into the corresponding binders on Moxfield.

## Notes
I had a rather large collection of 14k+ cards catalogued for the first time with ManaBox, With over 12 "Binders" which were really storage boxes.
After Looking for solutions that might work with Moxfield and their suggestion board, I made this quick solution that worked for me.

Hoping to help someone out there who might be in the same boat.
