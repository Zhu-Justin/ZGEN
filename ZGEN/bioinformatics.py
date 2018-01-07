# Constants for bioinformatics calculations

START_CODON = "AUG"
STOP_CODON_1 = "UAA"
STOP_CODON_2 = "UAG"
STOP_CODON_3 = "UGA"

# Dictionaries to lookup transcriptions

CODON_TABLE = {
    "AUA": "I", "AUC": "I", "AUU": "I", "AUG": "M",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
    "AAC": "N", "AAU": "N", "AAA": "K", "AAG": "K",
    "AGC": "S", "AGU": "S", "AGA": "R", "AGG": "R",
    "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
    "CAC": "H", "CAU": "H", "CAA": "Q", "CAG": "Q",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
    "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
    "GAC": "D", "GAU": "D", "GAA": "E", "GAG": "E",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGU": "G",
    "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
    "UUC": "F", "UUU": "F", "UUA": "L", "UUG": "L",
    "UAC": "Y", "UAU": "Y", "UAA": "_", "UAG": "_",
    "UGC": "C", "UGU": "C", "UGA": "_", "UGG": "W",
}


# Classes


class Motifs:
    """Class for obtaining data concerning motifs"""

    def __init__(self, count, indices):
        self.count = count
        self.indices = indices


class FastaData:
    """Class for FASTA data"""

    def __init__(self, fasta_identifier, fasta_sequence, index):
        self.fasta_identifier = fasta_identifier
        self.fasta_sequence = fasta_sequence
        self.index = index


# Functions for bioinformatics calculations


def calculate_percentages(count, total):
    """Calculates the percentage of count over total"""
    percent = 100.0 * count / total
    return percent


def DNA_to_RNA(DNAsequence):
    """Transcribes DNA to RNA"""
    RNAsequence = ""
    for nucleotide in DNAsequence:
        # Switches Thymine for Uracil
        if nucleotide == "T":
            RNAsequence += "U"
        else:
            RNAsequence += nucleotide
    return RNAsequence


def RNA_to_DNA(RNAsequence):
    """Translates RNA to DNA"""
    DNAsequence = ""
    for nucleotide in RNAsequence:
        # Switches Uracil for Thymine
        if nucleotide == "U":
            DNAsequence += "T"
        else:
            DNAsequence += nucleotide
    return DNAsequence


def DNA_to_Protein(DNAsequence):
    """Translates DNA to Protein"""
    # Initialize variables
    protein = ""
    index = 0
    if len(DNAsequence) > 2:
        # Translate until no more nucleotides in DNA sequence
        while index < len(DNAsequence) - 2:
            # Search for a start codon to begin translations
            if DNA_to_RNA(DNAsequence[index:index + 3]) == START_CODON:
                protein += CODON_TABLE[DNA_to_RNA(DNAsequence[index:index + 3])]
                index += 3
                # Continue translation until a stop codon is read
                while index + 3 <= len(DNAsequence) and DNA_to_RNA(DNAsequence[index:index + 3]) != STOP_CODON_1 and DNA_to_RNA(DNAsequence[index:index + 3]) != STOP_CODON_2 and DNA_to_RNA(DNAsequence[index:index + 3]) != STOP_CODON_3:
                    protein += CODON_TABLE[DNA_to_RNA(DNAsequence[index:index + 3])]
                    index += 3
                # Underline indicates end of amino acid strand
                protein += "_"
            index += 1
    return protein


def RNA_to_Protein(RNAsequence):
    """Translates RNA to Protein"""
    # Initialize variables
    protein = ""
    index = 0
    if len(RNAsequence) > 2:
        # Translate until no more nucleotides in RNA sequence
        while index < len(RNAsequence) - 2:
            # Search for a start codon to begin translations
            if RNAsequence[index:index + 3] == START_CODON:
                protein += CODON_TABLE[RNAsequence[index:index + 3]]
                index += 3
                # Continue translation until a stop codon is read
                while index + 3 <= len(RNAsequence) and RNAsequence[index:index + 3] != STOP_CODON_1 and RNAsequence[index:index + 3] != STOP_CODON_2 and RNAsequence[index:index + 3] != STOP_CODON_3:
                    protein += CODON_TABLE[RNAsequence[index:index + 3]]
                    index += 3
                # New line indicates new amino acid strand
                protein += "_"
            index += 1
    return protein


def find_motifs(motifs, sequence):
    """Finds positions of motifs in sequence"""
    # Initialize variables
    motif = []
    index = 0
    counter = 1
    # Search for positions of motifs located within sequence
    while index < len(sequence):
        index = sequence.find(motifs, index)
        # Break if no motifs are found
        if index == -1:
            break
        motif.append(Motifs(counter, index + 1))
        index += 1
        counter += 1
    # Returns an array of positions of motifs in sequence
    return motif


def FASTAparser(fastatext):
    """Parsing through FASTA files"""
    # Initialize variables
    fasta = []
    # Split data based off of ">" delimiter
    fasta_raw = fastatext.split(">")
    if len(fasta_raw) > 0:
        # Search through data for identifiers and sequence info for DNA, RNA, and protein
        for index in range(1, len(fasta_raw)):
            fasta_array = fasta_raw[index].split("\n")
            fasta_identifier = fasta_array[0]
            fasta_sequence = ""
            if len(fasta_array) > 0:
                for sequenceindex in range(1, len(fasta_array)):
                    fasta_sequence += fasta_array[sequenceindex]
            fasta.append(FastaData(fasta_identifier, fasta_sequence, index))
    # Returns an array of FastaData objects
    return fasta
