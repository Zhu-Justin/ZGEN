# Functions for RNA data


def isRNANucleotide(letter):
    """Determines if letter is an RNA nucleotide"""
    if letter == 'A' or letter == 'C' or letter == 'G' or letter == 'U':
        return True
    return False


def RNAparser(text):
    """Parses text to create valid RNA sequence"""
    upper_text = text.upper()
    RNAsequence = ""
    # Splits text into an array of no whitespace text
    no_space_text_array = upper_text.split()
    # Parse through all the text in the text within the array, adding nucleotide letters to RNA sequence
    for no_space_sequence in no_space_text_array:
        for letter in no_space_sequence:
            if isRNANucleotide(letter):
                RNAsequence += letter
            # If there exists invalid RNA nucleotide, then the text file must not be a RNA sequence
            if not isRNANucleotide(letter):
                return ""
    # Otherwise return a RNA sequence with no blank spaces
    return RNAsequence


def uracil_count(RNAsequence):
    """Counts the number of Uracils"""
    uracil = 0
    for nucleotide in RNAsequence:
        if nucleotide == 'U':
            uracil += 1
    return uracil


def complement_RNA(RNAsequence):
    """Returns complement of RNA"""
    complement = ""
    for nucleotide in RNAsequence:
        if nucleotide == "A":
            complement += "U"
        if nucleotide == "C":
            complement += "G"
        if nucleotide == "G":
            complement += "C"
        if nucleotide == "U":
            complement += "A"
    return complement


def reverse_complement_RNA(RNAsequence):
    """Returns reverse complement of RNA"""
    complement = ""
    for nucleotide in RNAsequence:
        if nucleotide == "A":
            complement = "U" + complement
        if nucleotide == "C":
            complement = "G" + complement
        if nucleotide == "G":
            complement = "C" + complement
        if nucleotide == "U":
            complement = "A" + complement
    return complement