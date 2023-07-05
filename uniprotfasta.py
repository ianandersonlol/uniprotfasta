import sys
import os
import requests

def fetch_protein_sequence(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    response.raise_for_status()
    lines = response.text.strip().split('\n')
    header = uniprot_id  # Use UniProt ID as the header
    sequence = ''.join(lines[1:])
    return header, sequence

def txt_to_fasta(txt_file):
    fasta_file = os.path.splitext(os.path.basename(txt_file))[0] + ".fasta"
    
    with open(txt_file, 'r') as file:
        uniprot_ids = [line.strip() for line in file if line.strip()]

    print("Fetching protein sequences...")
    with open(fasta_file, 'w') as file:
        for i, uniprot_id in enumerate(uniprot_ids, start=1):
            try:
                header, sequence = fetch_protein_sequence(uniprot_id)
                file.write(f">{header}\n{sequence}\n")
                print(f"[{i}/{len(uniprot_ids)}] Fetched sequence for UniProt ID: {uniprot_id}")
            except requests.exceptions.HTTPError:
                print(f"[{i}/{len(uniprot_ids)}] Error fetching sequence for UniProt ID: {uniprot_id}")

    print("Conversion complete.")
    print(f"FASTA file saved as: {fasta_file}")

# Usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input.txt")
    else:
        input_file = sys.argv[1]
        txt_to_fasta(input_file)
