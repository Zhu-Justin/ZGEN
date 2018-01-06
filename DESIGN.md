# Origins of this project's design and usage

Bioinformatics can be thought of as the application of computer science in the analysis of biological phenomenon.  The computational techniques of bioinformatics have allowed researchers to identify mutations used in cancer studies, clarify interactions between nucleic acids and protein sequences, and create novelties in gene-editing technologies.  Bioinformatics – as one paper (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3343106/) called it – has been “enthroned as the pillar of new biology”.

ZGEN is a CS50 project that was inspired by the developments and difficulties faced in the bioinformatics field.

Instead of manually scanning though large genomic datasets, researchers can use ZGEN to analyze biological data better and faster than before.

ZGEN utilizes the versatile powers of python and the user-friendly interface of a website to obtain the most essential data concerning DNA, RNA, and proteins in an automated process that minimizes computational calculations and manual searching demanded of the user.

ZGEN ultimately is a collection of tools that can identify significant data concerning DNA, RNA, and proteins, which aid in the interpretation and extrapolation of key biomolecular interactions.

# Helper functions

I wanted to create separate helper python functions that were specific only to the data in question – the dna.py file only deals with DNA data, rna.py file only deals with RNA data, and protein.py file deals only with Protein data.

When dealing with more complex relationships between these different types of genomic data, such as transcribing DNA sequences into Protein sequences and the like, the categorization of these functions did not become as clear-cut in that functions were not strictly limited to a particular genomic data type (DNA, RNA, or protein).

Therefore, I proceeded to create a separate bioinformatics.py file that contained the functions that were applicable to all three types of genomic data.

The application.py file then takes in all of the functions in these different python files and ties it all neatly together on a website.

# Design of dna.py

Let’s begin with the DNA python file.  The DNA class contains a series of helper functions that are able to count the nucleotides (adenosine, guanosine, cytosine, and thymine).

The code is pretty simple in that it returns the corresponding nucleotide counts of a given sequence.  The DNA parser function takes in a string of text (obtained either from a file input or a text box) and modifies the text through several steps.

It first splits the text in ridding the text of whitespace in addition to capitalizing characters (thereby allowing the user to put in lower-cased nucleotide characters like ‘a’, ‘c’, ‘g’, and ‘t’), and then proceeds to go through the array of text without whitespace, checking if all the characters are a legal nucleotide by calling the ```isDNAnucleotide``` function – adding the nucleotides if they are valid DNA nucleotides, but returning an empty string if not.

This empty string signifies that the text file is not a legitimate DNA file as it does not adhere to the specifications of being a DNA file, and thus when the empty string is returned to application.py, no meaningful data will be shown.

Meanwhile a complement function complements the nucleotides by pairing A with T, and C with G, while the reverse complement function complements the nucleotides by going in reverse order while conducting the same pairing of A with T and C with G.

# Design of rna.py

The rna.py file contains the same design principles as the dna.py python file with the exception that thymine is replaced with uracil.

I could technically just borrow the same functions from DNA.py, but I think by specifying these unique function names differentiating between RNA and DNA, I can successfully prevent myself from getting mixed up between DNA data and RNA data, which will reduce inaccuracies in the long term in addition to making the distinction between uracil and thymine pretty clear.

# Design of protein.py

The protein script design takes on a different approach in design than DNA and RNA.

Because DNA and RNA only takes on 4 different possible nucleotide values whereas protein takes on 20 different possible amino acid values, it would make sense to create an object class for the protein that is able to keep track of all of these different amino acid values rather than creating 20 different functions for each amino acid.

On top of that, the protein data is inherently different than DNA and RNA – whereas RNA and DNA data existed only as one long uninterrupted sequence of nucleotides, protein data could have multiple protein sequences because the nature of protein synthesis typically involves a single DNA/RNA strand that contains many nucleotides that correspond with a stop and start codon in coding for many multiple amino acid sequences that are interrupted, disconnected sequences in the protein.

Therefore, to handle all this data unique to the protein, I created three classes that contained three distinct information about the protein.

The ```AminoAcid``` class used the dictionary ```PROTEIN_CHARACTERISTIC``` to look up all the characteristics of the singular amino acids, while the ```Protein``` class stored all of the counts and total amino acids in the protein file, and finally the ```Sequence``` class stored the entire string of seperate amino acid sequences and its corresponding order relative to its position in the overall protein.

The function ```translate_protein``` translates each protein sequence into an array of individual amino acid object, the function ```new_Protein``` returns a protein object that can update its amino acid counts with a built-in ```add_counts``` function that takes in a protein sequence and adds in the corresponding count of amino acids.

The ```seperate_protein_sequence``` function separates the protein of disconnected amino acid sequences by splitting the entire protein by the stop codon indicator of ```_```, returning all of the seperated, disjoint protein sequences in an array.

To parse through a given text containing protein information, the ```parse_protein``` function utilizes the same design elements as the functions that parse through DNA and RNA, with the difference being it is only interested in 20 specific alphabetical characters that are not B, J, U, X, Z, as those alphabetical letters do not correspond to valid amino acids.
The if statement effectively precludes those letters from entering the protein sequence by returning an empty string that will not show any data when implemented in the application.py file.

Additionally, if no stop codon is present after the very last amino acid in the text file or text box, the ```parse_protein function``` will add ```_``` so that the parsed protein sequence is compatible with other functions in the application.

To convert single-lettered amino acids in the protein sequence into triple-lettered amino acids or fully-named amino acids, the functions ```Single_to_Triple_Protein``` and ```Single_to_Full_Protein``` implements the conversion respectively.  It uses a while loop that detects the stop codon indicator of ```_```, and finds the corresponding format of amino acids specified in the dictionaries.

# Design of bioinformatics.py

The bioinformatics.py file contains several functions that are able to convert between the genomic formats of DNA, RNA, and protein.  For example, the ```RNA_to_DNA``` function converts uracil to thymine when converting from RNA to DNA, while ```DNA_to_RNA``` does the reverse.

For the functions that convert DNA and RNA to protein, a while loop is used that first looks for a start codon, and then proceeds to make the conversion of three nucleotides to one amino acid based off of the dictionary specification.  If a stop codon is encountered, the conversion stops, ```_``` is added, and transcription will begin once another start codon is read again.  This process repeats itself until there are no more nucleotides in the DNA or RNA sequences to be read.

A ```Motifs``` class is created for the purpose of storing the positions of specific motifs in DNA, RNA, and Protein sequences and the occurrence frequency of those motifs in those DNA, RNA, and Protein sequences.  The ```find_motifs``` function helps search for the position and occurrences of motifs in the sequences, returning an array of ```Motif``` objects.

A ```FastaData``` class is created for storing the fasta_identifiers and fasta_sequences that have been parsed from the ```FASTAparser``` function.  The Fastaparser uses the ```split``` function two times, the first time to separate the different sequences based off of the ```>``` delimiter, as each sequence in the fasta file will have a ```>``` denoting the beginning of a new sequence and then an identifier name following right after the ```>```.  Then, the second split is based off of line breaks, as the first line contains the sequence identifier but everything that follows contains the actual data of the sequence itself.  Therefore, the first split differentiates between different sequences, while the second split differentiates between the sequence identifier and sequence data of each sequence in the fasta file.

The bioinformatics.py file also has a short and sweet ```calculate_percentages``` that cleanly executes the calculation of percentages based off of the counts of nucleotides or amino acids over the aggregated total as a floating type rather than integer.

# Design of application.py

The application.py file uses Flask’s decorator functions to navigate between pages.

It takes in values from html files when the user posts (i.e. when you clicks the submit button) and displays back the values from all those functions previously mentioned with the Flask’s ```render_template``` function if the user clicked on the checkboxes corresponding to those specifications.

Empty-valued fields returned to the template will be interpreted by Jinja in the HTML files to be false, such that those particular empty fields will not display the data corresponding to those empty fields when viewed on the website.

To display specific errors that can help the user better understand what to do and what not to do, ```abort``` is called to display the error page when the user misuses ZGEN.

# Final comments on CSS and HTML

Finally, the CSS template shows the color schemes and other design components employed in the website layout for ZGEN, and java scripts are located in the html templates to make the side bar interactive, and allows users to copy certain sequences from the fasta file by clicking a button present on the website.

The Jinja code used in the HTML pages displays all the genomics data specified by the user’s checked boxes concerning the DNA, RNA, and protein sequences with if statements.

### Thank you so much for all the support, guidance, and growth to making this all possible
# This was ZGEN -- My CS50 Final Project