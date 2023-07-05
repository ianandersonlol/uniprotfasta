# Documentation for uniprotfasta.py

`uniprotfasta.py` is a Python script that fetches protein sequences from the UniProt database using their UniProt IDs and converts the sequences into FASTA format.

## Table of Contents

1. [Dependencies](#dependencies)
2. [Functions](#functions)
    - [fetch_protein_sequence](#fetch_protein_sequence)
    - [txt_to_fasta](#txt_to_fasta)
3. [Usage](#usage)

## Dependencies <a name="dependencies"></a>

This script requires Python, along with the `os`, `sys`, and `requests` modules.

## Functions <a name="functions"></a>

### fetch_protein_sequence <a name="fetch_protein_sequence"></a>

```python
def fetch_protein_sequence(uniprot_id):
```

This function fetches protein sequences from the UniProt database. It uses the `requests` module to send a GET request to the UniProt database's API.

**Parameters:**

- `uniprot_id`: A string representing the UniProt ID of the protein sequence to fetch.

**Returns:**

- `header`: A string representing the UniProt ID of the fetched protein sequence.
- `sequence`: A string representing the fetched protein sequence.

### txt_to_fasta <a name="txt_to_fasta"></a>

```python
def txt_to_fasta(txt_file):
```

This function reads a text file containing UniProt IDs, fetches the corresponding protein sequences using `fetch_protein_sequence`, and writes them to a new FASTA file.

**Parameters:**

- `txt_file`: The path to the input text file containing UniProt IDs.

**Returns:**

None. But it saves a new .fasta file in the current working directory.

## Usage <a name="usage"></a>

To use this script, run it from the command line with the path to the input text file as an argument:

```bash
python uniprotfasta.py input.txt
```

Replace `input.txt` with the path to your input text file. The input text file should contain one UniProt ID per line. The script will create a new FASTA file in the same directory as the input text file.

**Example:**

If your input text file looks like this:

```
P12345
Q67890
```

And you run this command:

```bash
python uniprotfasta.py input.txt
```

The script will create a new file called `input.fasta` with the fetched protein sequences.
