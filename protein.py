# Dictionaries to lookup transcriptions

# Protein table converts single-lettered amino acid to triple-lettered amino acid
PROTEIN_TABLE = {
    'C': 'CYS', 'D': 'ASP', 'S': 'SER', 'Q': 'GLN', 'K': 'LYS',
    'I': 'ILE', 'P': 'PRO', 'T': 'THR', 'F': 'PHE', 'N': 'ASN',
    'G': 'GLY', 'H': 'HIS', 'L': 'LEU', 'R': 'ARG', 'W': 'TRP',
    'A': 'ALA', 'V': 'VAL', 'E': 'GLU', 'Y': 'TYR', 'M': 'MET', '_': ''
}
# Protein table converts single-lettered amino acid to fully-named amino acid
PROTEIN_TABLE_FULL = {
    'C': 'Cysteine', 'D': 'Aspartate', 'S': 'Serine', 'Q': 'Glutamine', 'K': 'Lysine',
    'I': 'Isoleucine', 'P': 'Proline', 'T': 'Threonine', 'F': 'Phenylalanine', 'N': 'Asparagine',
    'G': 'Glycine', 'H': 'Histidine', 'L': 'Leucine', 'R': 'Arginine', 'W': 'Tryptophan',
    'A': 'Alanine', 'V': 'Valine', 'E': 'Glutamate', 'Y': 'Tyrosine', 'M': 'Methionine', '_': 'STOP'
}
# Protein table contains chemical properties of amino acids
PROTEIN_CHARACTERISTIC = {
    'C': 'disulfide',
    'D': 'negative',
    'S': 'polar',
    'Q': 'polar',
    'K': 'positive',
    'I': 'nonpolar',
    'P': 'nonstandard',
    'T': 'polar',
    'F': 'aromatic',
    'N': 'polar',
    'G': 'nonstandard',
    'H': 'positive',
    'L': 'nonpolar',
    'R': 'positive',
    'W': 'aromatic',
    'A': 'nonpolar',
    'V': 'nonpolar',
    'E': 'negative',
    'Y': 'aromatic',
    'M': 'nonpolar',
    '_': ''
}


# Class for proteins


class AminoAcid:
    """Class containing Amino Acid Characteristics"""

    def __init__(self, aa_letter, aa_position):
        self.aa_letter = aa_letter
        self.aa_tripleletter = PROTEIN_TABLE[aa_letter]
        self.aa_fullname = PROTEIN_TABLE_FULL[aa_letter]
        self.aa_characteristic = PROTEIN_CHARACTERISTIC[aa_letter]
        self.aa_position = aa_position


class Sequence:
    """Class containing Sequence of Amino Acid Characteristics"""

    def __init__(self, sequence, position):
        self.sequence = sequence
        self.position = position


class Protein:
    """Class containing Protein Characteristics"""

    def __init__(self):
        self.C = 0
        self.D = 0
        self.S = 0
        self.Q = 0
        self.K = 0
        self.I = 0
        self.P = 0
        self.T = 0
        self.F = 0
        self.N = 0
        self.G = 0
        self.H = 0
        self.L = 0
        self.R = 0
        self.W = 0
        self.A = 0
        self.V = 0
        self.E = 0
        self.Y = 0
        self.M = 0
        self.count = 0
        self.total = 0

    # Function for updating protein counts per newly added amino acid
    def add_counts(self, proteinsequence):
        # Updates each amino acid count and total count in object
        for aa_letter in proteinsequence:
            if aa_letter == "C":
                self.C += 1
                self.total += 1
            elif aa_letter == "D":
                self.D += 1
                self.total += 1
            elif aa_letter == "S":
                self.S += 1
                self.total += 1
            elif aa_letter == "Q":
                self.Q += 1
                self.total += 1
            elif aa_letter == "K":
                self.K += 1
                self.total += 1
            elif aa_letter == "I":
                self.I += 1
                self.total += 1
            elif aa_letter == "P":
                self.P += 1
                self.total += 1
            elif aa_letter == "T":
                self.T += 1
                self.total += 1
            elif aa_letter == "F":
                self.F += 1
                self.total += 1
            elif aa_letter == "N":
                self.N += 1
                self.total += 1
            elif aa_letter == "G":
                self.G += 1
                self.total += 1
            elif aa_letter == "H":
                self.H += 1
                self.total += 1
            elif aa_letter == "L":
                self.L += 1
                self.total += 1
            elif aa_letter == "R":
                self.R += 1
                self.total += 1
            elif aa_letter == "W":
                self.W += 1
                self.total += 1
            elif aa_letter == "A":
                self.A += 1
                self.total += 1
            elif aa_letter == "V":
                self.V += 1
                self.total += 1
            elif aa_letter == "E":
                self.E += 1
                self.total += 1
            elif aa_letter == "Y":
                self.Y += 1
                self.total += 1
            elif aa_letter == "M":
                self.M += 1
                self.total += 1
            elif aa_letter == "_":
                self.count += 1


# Functions for proteins


def protein_parser(text):
    """Returns a string of amino acids from text"""
    # Accomodates lower-cased words
    upper_text = text.upper()
    protein = ""
    # Splits text into an array of no whitespace text
    no_space_text_array = upper_text.split()
    # Parse through all the text in the text within the array, adding nucleotide letters to protein sequence
    for no_space_sequence in no_space_text_array:
        for letter in no_space_sequence:
            # Only adds valid amino acid single-letters as accepted by biologists and bioinformaticians in FASTA files or underline to symbolize stop (by a stop codon)
            if letter.isalpha() or letter == '_':
                if letter == "B" or letter == "J" or letter == "O" or letter == "U" or letter == "X" or letter == "Z":
                    return ""
                else:
                    protein += letter
            else:
                return ""
    # End protein sequence with ending character if user failed to provide one
    if protein[len(protein) - 1] != '_':
        protein += '_'
    return protein


def translate_protein(protein):
    """Returns an array of amino acid characteristics in protein"""
    proteinsequence = []
    for index in range(len(protein)):
        proteinsequence.append(AminoAcid(protein[index], index))
    return proteinsequence


def new_Protein():
    """Returns a Protein object"""
    return Protein()


def Single_to_Triple_Protein(proteinsequence):
    """Converts a single-lettered protein sequence to a triple-lettered protein sequence"""
    # Begins protein string with N terminal specification
    protein = "N terminal - "
    index = 0
    while index < len(proteinsequence):
        # Print new protein strand if stop indicator is present
        if proteinsequence[index] == '_':
            # Ends protein string with C terminal specification
            protein += "C terminal"
            # Check if more amino acids after an ending sequence to create a new protein strand
            if index + 1 < len(proteinsequence):
                protein += " | N terminal - "
        else:
            # Utilizes protein table to print normal amino acid
            protein += PROTEIN_TABLE[proteinsequence[index]] + " - "
        index += 1
    return protein


def Single_to_Full_Protein(proteinsequence):
    """Converts a single-lettered protein sequence to a fully-named protein sequence"""
    protein = ""
    # Utilizes protein table
    for aa_letter in proteinsequence:
        protein += PROTEIN_TABLE_FULL[aa_letter] + " "
    return protein


def seperate_protein_sequence(proteinsequence):
    """Returns protein sequence as an array of independent sequences and their sequence number split by the stop codon indicator"""
    splitsequence = proteinsequence.split("_")
    number = 1
    splitsequence_array = []
    for sequence in splitsequence:
        # Ensures non-empty sequence is appended to dataset
        if sequence != "":
            splitsequence_array.append(Sequence(sequence, number))
            number += 1
    return splitsequence_array