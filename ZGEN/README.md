# ZGEN

ZGEN is a bioinformatics toolkit used for analyzing DNA, RNA, and Protein data

It was released on December 7th, 2017

## Getting Started

These instructions will get ZGEN up and running. Skip to [Getting started with CS50 IDE](README.md#getting-started-with-CS50-IDE) if using ZGEN on CS50 IDE.

### Installing ZGEN

To install ZGEN, you can simply download ZGEN from this GitHub page and store ZGEN in a path of your choosing, which will be
denoted here in this README file as ```~/yourpathdirectory/```

### Installing Flask

Documentation and more details here: http://flask.pocoo.org/docs/0.12/installation/

```
$ sudo pip install virtualenv
$ pip install Flask
```

## Launching application

Export the FLASK_APP environment variable

### Windows

Type the commands into you terminal window for the application to work.

```
$ cd ~/yourpathdirectory/ZGEN
$ set FLASK_APP=application.py
$ flask run
```

Your terminal should display something like

```
 * Serving Flask app "application"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Type the URL outputted by your terminal ```http://127.0.0.1:5000/``` in the address bar to now access ZGEN.

### Mac

Type the commands into you terminal window for the application to work.

```
$ cd ~/yourpathdirectory/ZGEN
$ export FLASK_APP=application.py
$ flask run
```

Your terminal should display something like

```
 * Serving Flask app "application"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Type the URL outputted by your terminal ```http://127.0.0.1:5000/``` in the address bar to now access ZGEN.

## Getting started with CS50 IDE

If you are using CS50 IDE, certain environmental variables have already been established.

Simply execute the following commands

```
$ cd ~/yourpathdirectory/ZGEN
$ flask run
```

The CS50 terminal should display something like

```
 * Serving Flask app "application"
 * Forcing debug mode on
 * Running on http://ide50-yourusername.cs50.io:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
```

Type the URL outputted by the CS50 terminal ```http://ide50-yourusername.cs50.io:8080/``` in the address bar to now access ZGEN.

## Tutorials

To understand how to use ZGEN, go to the tutorials page by clicking the button 'Let's Begin!' or 'ZGEN' in the top left corner

## ZGEN : DNA

### Input file formats

ZGEN can take in DNA data from either a text file or from the user typing in the DNA sequence into the text box.
If both are present, the text file will take precedence over the typed sequence in the text box.

ZGEN is very sensitive to DNA-specific data.  Because ZGEN is specifically interested in analyzing nucleotides, it is imperative
that your file or your text box includes only nucleotides.  Valid nucleotide characters are 'A', 'a', 'G', 'g', 'C', 'c', 'T', 't'.
This is because only four DNA nucleotides exist: adenine ('A' or 'a'), guanine ('G', 'g'), cytosine ('C', 'c'), and thymine ('T', 't').

ZGEN does, however, handle and ignore whitespaces that comes in the form of spaces and line breaks, so it is fine for you to accidentally insert
a whitespace in your text file or text box.

Please check out the file ```ZGEN_dna_1.txt``` under the ```inputfiles``` folder.

This shows the most standard format of a DNA text file where all DNA nucleotides are positioned next to each other with no whitespace in the text file.

Please check out the file ```ZGEN_dna_2.txt``` under the ```inputfiles``` folder.

This shows a format of a DNA text file where line breaks exist.  ZGEN still reads in all nucleotides, displaying the same results as the ```ZGEN_dna_1.txt```

Please check out the file ```ZGEN_dna_3.txt``` under the ```inputfiles``` folder.

This shows a format of a DNA text file where spaces, line breaks, and all shorts of messy white space exist.  ZGEN still reads in all nucleotides, displaying the same results as the ```ZGEN_dna_1.txt``` and ```ZGEN_dna_2.txt```

Any other file not following the specifications of this DNA text format will not be analyzed, and a page displaying the error message 'invalid text file' or 'invalid characters in text area' will appear.
See and test ```ZGEN_invalid_file.text``` for an example.

### Analyzing DNA data

ZGEN provides several options for users in analyzing DNA data.
The following data is presented when a user checks the box (checkbox is checked when it changes color from gray to blue):

Nucleotide counts -- Displays the number of adenines, guanines, cytosines, and thymines in the DNA sequence inputted

Nucleotide percentages -- Displays the percentages of adenines, guanines, cytosines, and thymines in the DNA sequence in relation to the total number of nucleotides in the DNA

This data is particularly important in comparing genomic deviations between different eukaryotes and prokaryotes.
The 'GC' content (number of guanines and cytosines) is something evolutionary biologists look for when categorizing animal phyla and identifying speciation.

### Transcribing DNA data

ZGEN is able to transcribe DNA into RNA and Protein sequences.
Users have the option of analyzing those transcribed sequences with the functions in [ZGEN : RNA](README.md#zgen-:-rna) and [ZGEN : Protein](README.md#zgen-:-protein) respectively.

### Obtaining complementary strands

ZGEN also is able to process and present complementary DNA and RNA sequences, which is particularly important in validation and verification tests with
control groups involving a single DNA sequence and in identifying mutations between different strands of DNA.

### Finding motifs

ZGEN also finds motifs of certain nucleotide sequences of interest by the user.
These nucleotide sequences specified by the user could be a promoter region that stimulates tumor creation, thus
searching specifically for the positions of these nucleotide sequences may help locate possible regions of DNA that code for cancer.

## ZGEN : RNA

### Input file formats

ZGEN can take in RNA data from either a text file or from the user typing in the RNA sequence into the text box.
If both are present, the text file will take precedence over the typed sequence in the text box.

ZGEN is very sensitive to RNA-specific data.  Because ZGEN is specifically interested in analyzing RNA nucleotides, it is imperative
that your file or your RNA text box includes only nucleotides.  Valid nucleotide characters are 'A', 'a', 'G', 'g', 'C', 'c', 'U', 'u'.
This is because only four RNA nucleotides exist: adenine ('A' or 'a'), guanine ('G', 'g'), cytosine ('C', 'c'), and uracil ('U', 'u').

ZGEN does, however, handle and ignore whitespaces that comes in the form of spaces and line breaks, so it is fine for you to accidentally insert
a whitespace in your text file or text box.  In other words, the same styling for RNA text files still applies to RNA text files.

Please check out the file ```ZGEN_rna_1.txt``` under the ```inputfiles``` folder.

This shows the most standard format of a RNA text file where all RNA nucleotides are positioned next to each other with no whitespace in the text file.

Please check out the file ```ZGEN_rna_2.txt``` under the ```inputfiles``` folder.

This shows a format of a RNA text file where line breaks exist.  ZGEN still reads in all nucleotides, displaying the same results as the ```ZGEN_rna_1.txt```

Please check out the file ```ZGEN_rna_3.txt``` under the ```inputfiles``` folder.

This shows a format of a RNA text file where spaces, line breaks, and all shorts of messy white space exist.  ZGEN still reads in all nucleotides, displaying the same results as the ```ZGEN_rna_1.txt``` and ```ZGEN_rna_2.txt```

Any other file not following the specifications of this RNA text format will not be analyzed, and a page displaying the error message 'invalid text file' or 'invalid characters in text area' will appear.
See and test ```ZGEN_invalid_file.text``` for an example.

### Analyzing RNA data

ZGEN provides several options for users in analyzing RNA data.
The following data is presented when a user checks the box (checkbox is checked when it changes color from gray to blue):

Nucleotide counts -- Displays the number of adenines, guanines, cytosines, and uracil in the RNA sequence inputted

Nucleotide percentages -- Displays the percentages of adenines, guanines, cytosines, and thymines in the RNA sequence in relation to the total number of nucleotides in the RNA

This data is particularly important in comparing genomic deviations between different eukaryotes and prokaryotes.
The 'GC' content (number of guanines and cytosines) is something evolutionary biologists look for when categorizing animal phyla and identifying speciation.

### Transcribing RNA data

ZGEN is able to transcribe RNA into DNA and Protein sequences.
Users have the option of analyzing those transcribed sequences with the functions in [ZGEN : DNA](README.md#zgen-:-dna) and [ZGEN : Protein](README.md#zgen-:-protein) respectively.

### Obtaining complementary strands

ZGEN also is able to process and present complementary DNA and RNA sequences, which is particularly important in validation and verification tests with
control groups involving a single RNA sequence and in identifying mutations between different strands of RNA.

### Finding motifs

ZGEN also finds motifs of certain nucleotide sequences of interest by the user.
These nucleotide sequences specified by the user could be a promoter region that stimulates tumor creation, thus
searching specifically for the positions of these nucleotide sequences may help locate possible regions of RNA that code for cancer.

## ZGEN : Protein

### Input file formats

ZGEN can take in Protein data from either a text file or from the user typing in the Protein sequence into the text box.
If both are present, the text file will take precedence over the typed sequence in the text box.

ZGEN is very sensitive to Protein-specific data in the form of amino acids.  Because ZGEN is specifically interested in analyzing amino acids, it is imperative
that your file or your text box includes only amino acids.  Valid characters include the following:

C,
        D,
        S,
        Q,
        K,
        I,
        P,
        T,
        F,
        N,
        G,
        H,
        L,
        R,
        W,
        A,
        V,
        E,
        Y,
        M,
        and their corresponading lower-cased forms.

This is because each of these characters represent and denote one of the twenty amino acids:

'C': 'Cysteine', 'D': 'Aspartate', 'S': 'Serine', 'Q': 'Glutamine', 'K': 'Lysine',
'I': 'Isoleucine', 'P': 'Proline', 'T': 'Threonine', 'F': 'Phenylalanine', 'N': 'Asparagine',
'G': 'Glycine', 'H': 'Histidine', 'L': 'Leucine', 'R': 'Arginine', 'W': 'Tryptophan',
'A': 'Alanine', 'V': 'Valine', 'E': 'Glutamate', 'Y': 'Tyrosine', 'M': 'Methionine'

ZGEN does, however, handle and ignore whitespaces that comes in the form of spaces and line breaks, so it is fine for you to accidentally insert
a whitespace in your text file or text box.  Additionally, ZGEN accepts the special underline character ```_``` that denotes the end of an amino acid sequence, as
your protein data from the file or text box can include multiple seperate amino acid sequences for proteins.
The underline character helps distinguish between seperate amino acid sequences.

Finally, for a protein sequence that does not have an underline character at the end, ZGEN will be able to handle that and add an underline sequence to signify that
the amino acid sequence ends for the protein.

Please check out the file ```ZGEN_protein_1.txt``` under the ```inputfiles``` folder.

This shows the most standard format of a protein text file where all amino acids are positioned next to each other with no whitespace in the text file.
Additionally, the presence of underlined characters signify this protein has 5 amino acid sequences.

Please check out the file ```ZGEN_protein_2.txt``` under the ```inputfiles``` folder.

This shows a format of a protein text file where line breaks exist but no underline character exists at the end of the sequence.
ZGEN still reads in all amino acid sequence normally and writes in the underline character after the user has clicked submit.

Please check out the file ```ZGEN_protein_3.txt``` under the ```inputfiles``` folder.

This shows a format of a protein text file where spaces, line breaks, and all shorts of messy white space exist.
ZGEN still displays all amino acids normally.

Any other file not following the specifications of this protein text format will not be analyzed, and a page displaying the error message 'invalid text file' or 'invalid characters in text area' will appear.
See and test ```ZGEN_invalid_file.text``` for an example.

### Analyzing Protein data

ZGEN provides several options for users in analyzing protein data.
The following data is presented when a user checks the box (checkbox is checked when it changes color from gray to blue):

Amino Acid sequences -- Displays the total number of amino acid sequences in protein

Amino Acid counts -- Displays the number of amino acids in the protein sequence inputted

Amino Acid percentages -- Displays the percentages of amino acids in the protein sequence in relation to the total number of amino acids in the protein

### Obtaining variants of protein data formats

ZGEN is able to obtain variants of protein data for display.

Seperate sequences into different text boxes -- This allows users to differentiate between different amino acid sequences in the protein

Triple-Lettered display -- Allows users to display amino acids from single letters to its accepted triple-lettered form (e.g. M is converted to MET).
It also adds an N and C terminus to show the direction and order in which the amino acid sequences are read.

Full display -- Allows users to display amino acids from single letters to the full name of the amino acid (e.g. M is converted to Methionine).
'STOP' is added to the end of each amino acid sequence to signify the end of the amino acid sequence.  This format is used for displaying amino acid sequences in formal lab reports.

### Obtaining amino acid characteristics

ZGEN also is able to provide critical data relating to the chemical properties of amino acids in these protein sequences.
These chemical properties are important in understanding the biological interactions of proteins with their environment.

Characteristics include:

Polar groups -- creates hydrogen bonds, favors water

Nonpolar groups -- creates van der waal's interactions, disfavors water

Aromatic groups -- large, ring-shaped amino acids that take up space

Negatively-charged groups (at pH 7) -- creates ionic bonds with positively-charged groups

Positively-charged groups (at pH 7) -- creates ionic bonds with negatively-charged groups

Nonstandard structural R groups (Glycine and Proline) -- lacking or containing aberrant R group that disrupts the peptide bond formation between amino acids

Disulfide bridges (Cysteine) -- creates covalent bonds with other amino acids that contain sulfur

### Finding motifs

ZGEN also finds motifs of certain amino acid sequences of interest for the user.

These amino acid sequences specified by the user could be a nonpolar signal sequence that characterizes a protein found in hydrophobic surfaces of the mitochondria.  Thus
searching specifically for those nonpolar amino acid sequences can help identify the protein as a vital component of metabolic processes.

Meanwhile, certain amino acids bind well with certain chemical molecules, so searching for those amino acid sequences can help identify potent drug interactions that can optimize
the efficiency of the protein as a whole.

## ZGEN : FASTA

ZGEN finally parses fasta files, the standard input file containing genomic data used in bioinformatics.

The first line in a FASTA file starts either with a ```>``` (greater-than) symbol and is the identifier for the sequence.
Following the first line is the actual sequence itself containing standard one-letter characters representing nucleotides or amino acids.

See examples of FASTA files by going to ```inputfiles``` and clicking on ```ZGEN_dna.fasta``` for a fasta file containing DNA data, clicking on ```ZGEN_rna.fasta``` for a fasta file containing RNA data, and
clicking on ```ZGEN_protein.fasta``` for a fasta file containing protein data.

After fasta files are parsed, users can copy a specific sequence of interest from the fasta file by clicking the copy button below each text box.
An alert box pops up, confirming that the sequence has been copied and the user can go analyze that specific sequence with functions specified prior in the README
file under the sections: [ZGEN : DNA](#zgen-:-dna), [ZGEN : RNA](#zgen-:-rna), and [ZGEN : Protein](#zgen-:-protein)

## Quitting ZGEN

Press CTRL+C in terminal

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Jinja](http://jinja.pocoo.org/) - Python handler in HTML files
* [Bootstrap](https://getbootstrap.com/) - Stylized CSS/HTML files
* [W3](https://www.w3schools.com/) - Icons for Webpage
* [CS50 IDE](https://cs50.io/) - Coding environment

## Contributing

Open to collaboration for making this a bigger project -- email me at justinzhu@college.harvard.edu

## Usage

Code is free to use for all!

## Authors

* *Justin Zhu* - *Student* - [justinzhu10](https://github.com/justinzhu10)

## Acknowledgments

* Much thanks to the CS50 staff for teaching me how to code and how to code well
* Credit to Professor David Malan for his instruction and lectures over the course of the semester
* Special thank you to Doug Smith, my teaching fellow, for all his tutelage, grading, and guidance in my CS growth this semester
* Special thank you to Derek Wang, who was kind enough to let me sit in on some his more comfortable sections, challenging me to think deeper about certain CS topics
* Additional thanks to Professor Rich Losick and Professor Dan Kahne for instruction and lectures in biology and chemistry in their LS1A class, partly inspiring me to use CS in addressing problems in the fields of biology and chemistry
* Finally, thank you to my parents, who have been there to support me every step of the way, and quite frankly, provide the "genes" that allow me to learn computer science
