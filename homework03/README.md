### Homework 3
## Exercise 1

In this exercize I took the file `ProteinList.json` convert the data into a python dictionary and then load the elements into the list `proteins`. 
I use many functions that take in this list of dictionaries:
  + `find_total_mass()`: This function returns the total mass of the proteins in the list
  + `find_large_proteins()`: This function returns a list of proteins greater than or equal to 1,000 Daltons
  + `find_non_eukaryotes()`: This function returns all proteins not from Eukaryotes

## Exercise 2

In this exercize I took the file `ProteinList.json` and load it into a python dictionary and then flatten the nested dictionary with a created function `flatten_dict()`.

This function recursively looks inside of a dictionary and adds keys to a new dictionary. Any nested keys have the form *(parent key)_(key)*.

This flattened dictionary is then loaded into the `proteins.csv` file.

## Exercise 3

The `ProteinList.json` file is loaded as a python dictionary, and then it is given a put into a nested dictionary with a root key of `data`. This "rooted" dictionary is then loaded into the `proteins.xml` file.

## Exercise 4

The `ProteinList.json` file is loaded as a python dictionary, and is loaded directly into the `proteins.yaml` file, with explicit starts and ends. I also set `sort_keys` to False for readability.
