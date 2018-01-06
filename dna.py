# Functions for DNA data


def isDNANucleotide(letter):
    """Determines if letter is a DNA nucleotide or there's empty space"""
    if letter == 'A' or letter == 'C' or letter == 'G' or letter == 'T':
        return True
    return False


def DNAparser(text):
    """Parses text to create valid DNA sequence"""
    upper_text = text.upper()
    DNAsequence = ""
    # Splits text into an array of no whitespace text
    no_space_text_array = upper_text.split()
    # Parse through all the text in the text within the array, adding nucleotide letters to DNA sequence
    for no_space_sequence in no_space_text_array:
        for letter in no_space_sequence:
            if isDNANucleotide(letter):
                DNAsequence += letter
            # If there exists invalid DNA nucleotide, then the text file must not be a DNA sequence
            if not isDNANucleotide(letter):
                return ""
    # Otherwise return a DNA sequence with no blank spaces
    return DNAsequence


def adenosine_count(DNAsequence):
    """Counts the number of adenosines"""
    adenosines = 0
    for nucleotide in DNAsequence:
        if nucleotide == 'A':
            adenosines += 1
    return adenosines


def guanosine_count(DNAsequence):
    """Counts the number of guanosines"""
    guanosine = 0
    for nucleotide in DNAsequence:
        if nucleotide == 'G':
            guanosine += 1
    return guanosine


def cytosine_count(DNAsequence):
    """Counts the number of cytosines"""
    cytosine = 0
    for nucleotide in DNAsequence:
        if nucleotide == 'C':
            cytosine += 1
    return cytosine


def thymine_count(DNAsequence):
    """Counts the number of thymines"""
    thymine = 0
    for nucleotide in DNAsequence:
        if nucleotide == 'T':
            thymine += 1
    return thymine


def complement_DNA(DNAsequence):
    """Returns complement of DNA"""
    complement = ""
    for nucleotide in DNAsequence:
        if nucleotide == "A":
            complement += "T"
        if nucleotide == "C":
            complement += "G"
        if nucleotide == "G":
            complement += "C"
        if nucleotide == "T":
            complement += "A"
    return complement


def reverse_complement_DNA(DNAsequence):
    """Returns reverse complement of DNA"""
    complement = ""
    for nucleotide in DNAsequence:
        if nucleotide == "A":
            complement = "T" + complement
        if nucleotide == "C":
            complement = "G" + complement
        if nucleotide == "G":
            complement = "C" + complement
        if nucleotide == "T":
            complement = "A" + complement
    return complement