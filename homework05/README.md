# Homework 5- *Best Practices in Python (Code Organization, Documentation, Logging, Error Handling)*

Description here.

### Project Files
1. `mmcif_summary.py` - Main program file
2. .cif input file

### Necessary Libraries
+ `MMCIFParser` from Bio.PDB.MMCIFParser  

## Usage
The main program file is `mmcif_summary.py`
Within this file the user assigns the path to the input .cif file as `INPUT_FILE`, and the name of the output .json file as `OUTPUT_FILE`.
The Output file should appear within the directory `output_files`, but if not present the program will create the output within the working directory.



This file is an input file and needs to be directed to within the constants section
```{python}
# -------------------------
# Constants (configuration)
# -------------------------
INPUT_FILE = "PATH/TO/INPUT.cif"
OUTPUT_FILE = "NAMEOFOUTPUT.json"
```

Next we can initiate the file in Python 3.x.
When running in terminal by adding the `-l` flag we can get more information about the run's progress.

| Command | Description |
| :---    | :--- |
| `ERROR` | User is only warned of program ending failures |
| `INFO`  | The user is given updates about the stages of the programs workflow |
| `DEBUG` | The user is told every step being taken by the program to check for small problems and debugging the program |

### Example of Use
In this example I use the file `4HHB.cif` which you are able to download with this command:
```
wget https://files.rcsb.org/download/4HHB.cif.gz
gunzip 4HHB.cif.gz
```

In the file under constants:
```{python}
# -------------------------
# Constants (configuration)
# -------------------------
INPUT_FILE = "4HHB.cif"
OUTPUT_FILE = "4HHB_summary.json"
```

**Command**:
```
python3 mmcif_summary.py -l INFO
```

**Output**:
```
[2026-02-13 02:28:10,125 mbs-337-2] mmcif_summary.py:main:139 - INFO: Beginning mmCIF Summary workflow
[2026-02-13 02:28:10,319 mbs-337-2] mmcif_summary.py:open_input_file:52 - INFO: Successfully opened 4HHB.cif
[2026-02-13 02:28:10,320 mbs-337-2] mmcif_summary.py:parse_file:75 - INFO: Beginning to parse file
[2026-02-13 02:28:10,321 mbs-337-2] mmcif_summary.py:parse_file:103 - INFO: Finished parsing 4HHB.cif have 4 chains
[2026-02-13 02:28:10,321 mbs-337-2] mmcif_summary.py:generate_output_file:122 - INFO: Writing to 4HHB_summary.json
[2026-02-13 02:28:10,321 mbs-337-2] mmcif_summary.py:main:143 - INFO: mmCIF Summary workflow is complete!
```

**Example Output File**:
```
$head output_files/4HHB_summary.json
...
{
  "chains": [
    {
      "chain_id": "A",
      "total_residues": 198,
      "standard_residues": 141,
      "hetero_residues": 57
    },
    {
```

