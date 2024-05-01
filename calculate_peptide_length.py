# Write Python 3 code in this online editor and run it.
def calculate_peptide_length(num_residues):
    if num_residues < 1:
        return 0  # No length for a sequence with no residues
    elif num_residues == 1:
        return 0  # Only one residue, no peptide bonds

    # Calculate lengths
    n_terminal_to_first_peptide = 3.5  # Distance from the N-terminal to the first peptide bond
    peptide_to_peptide = 3.5 * (num_residues - 2)  # Distance from the first peptide bond to the last peptide bond
    last_peptide_to_c_terminal = 2.4  # Distance from the last peptide bond to the C-terminal

    total_length = n_terminal_to_first_peptide + peptide_to_peptide + last_peptide_to_c_terminal
    return total_length

# Example
sequence = "MHHHHHHSSLIEVEKPLYGVEVFVGETAHFEIELSEPDVHGQWKLKGQPLTASPDCEIIEDGKKHILILHNCQLGMTGEVSFQAANAKSAANLKVKEL"
num_residues = len(sequence)
total_length = calculate_peptide_length(num_residues)
print(f"Total length of the sequence '{sequence}' is: {total_length} Å")
