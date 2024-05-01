## Project Description
The Peptide Length Calculator is a Python-based tool designed to approximate the total length of a peptide chain from a sequence of amino acids. This tool accounts for the distances between the N-terminal of one amino acid to the peptide bond of the next and the distance from the last peptide bond to the C-terminal. The lengths calculated by this tool are approximate and not exact measurements, suitable for theoretical and modeling purposes.

## Features
- Approximate the total length from the N-terminal of the first amino acid to the C-terminal of the last in a sequence.
- Uses standard distance measures for peptide bonds and terminal connections, emphasizing that the results are approximations.
- Simple command-line interface for ease of use.

## Installation
This project does not require any external libraries to run the main script. It is written in Python 3.x. To set it up, follow these steps:

1. Ensure that Python 3.x is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/M15160058/peptidelengthcalculator.git
## Requirements
You need a FASTA sequence to calculate the length of the extended peptide of a protein. This format allows the tool to accurately parse and process the sequence data necessary for length calculations.
## Usage
To run the calculator, execute the script from the command line by navigating to the project directory and running:
```bash
python calculate_peptide_length.py

Modify the script calculate_peptide_length.py to input your peptide sequence, or import the function into another script to use programmatically.
