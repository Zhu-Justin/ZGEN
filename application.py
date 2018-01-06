from flask import Flask, abort, redirect, render_template, request
import csv
import urllib.request
from werkzeug.exceptions import default_exceptions, HTTPException

from bioinformatics import calculate_percentages, DNA_to_RNA, RNA_to_DNA, DNA_to_Protein, RNA_to_Protein, find_motifs, FASTAparser
from dna import isDNANucleotide, DNAparser, adenosine_count, guanosine_count, cytosine_count, thymine_count, complement_DNA, reverse_complement_DNA
from rna import isRNANucleotide, RNAparser, uracil_count, complement_RNA, reverse_complement_RNA
from protein import protein_parser, translate_protein, new_Protein, Single_to_Triple_Protein, Single_to_Full_Protein, seperate_protein_sequence

# Configure application
app = Flask(__name__)
app.config['DEBUG'] = True


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def dashboard():
    """Show Home for user"""
    # Redirects users to tutorials if button is clicked
    if request.method == "POST":
        return redirect("/welcome")
    # Otherwise returns home page
    else:
        return render_template("home.html")


@app.route("/welcome")
def welcome():
    """Shows tutorials for new users"""
    return render_template("tutorials.html")


@app.route("/DNA", methods=["GET", "POST"])
def DNA():
    """Show DNA data for user"""
    # Initialize variables
    DNAsequence = ""
    ac = ""
    gc = ""
    cc = ""
    tc = ""
    total = ""
    ap = ""
    gp = ""
    cp = ""
    tp = ""
    RNAsequence = ""
    proteinsequence = ""
    complementaryDNA = ""
    complementaryRNA = ""
    rcomplementaryDNA = ""
    rcomplementaryRNA = ""
    motifsequence = ""
    motifs = []

    # Check to see if person reached through "POST"
    if request.method == "POST":
        if not request.files.get("DNAfile"):
            # Obtain DNA text if no DNA file found
            if not request.form.get("DNAtext"):
                abort(400, "No DNA text file found")
            else:
                DNAsequence = DNAparser(request.form.get("DNAtext"))

        # Otherwise, use information from DNA file
        if request.files.get("DNAfile"):
            try:
                text = request.files["DNAfile"].read().decode("utf-8")
                DNAsequence = DNAparser(text)
            except Exception:
                abort(400, "invalid file")

        # Check to see if DNAsequence is not empty
        if len(DNAsequence) > 0:

            # Check to see if user wants counts of nucleotides
            if request.form.get("counts") == "1":
                ac = adenosine_count(DNAsequence)
                gc = guanosine_count(DNAsequence)
                cc = cytosine_count(DNAsequence)
                tc = thymine_count(DNAsequence)
                total = len(DNAsequence)

            # Check to see if user wants percentages of nucleotides
            if request.form.get("percentages") == "1":
                total = len(DNAsequence)
                ap = calculate_percentages(adenosine_count(DNAsequence), total)
                gp = calculate_percentages(guanosine_count(DNAsequence), total)
                cp = calculate_percentages(cytosine_count(DNAsequence), total)
                tp = calculate_percentages(thymine_count(DNAsequence), total)

            # Check to see if RNA is to be transcribed from DNA
            if request.form.get("transcribeRNA") == "1":
                RNAsequence = DNA_to_RNA(DNAsequence)

            # Check to see if protein is to be transcribed from DNA
            if request.form.get("transcribeprotein") == "1":
                proteinsequence = DNA_to_Protein(DNAsequence)

            # Check to see if complementary DNA strand needed
            if request.form.get("cDNA") == "1":
                complementaryDNA = complement_DNA(DNAsequence)

            # Check to see if complementary RNA strand needed
            if request.form.get("cRNA") == "1":
                complementaryRNA = complement_RNA(DNA_to_RNA(DNAsequence))

            # Check to see if reverse complementary DNA strand needed
            if request.form.get("rDNA") == "1":
                rcomplementaryDNA = reverse_complement_DNA(DNAsequence)

            # Check to see if reverse complementary RNA strand needed
            if request.form.get("rRNA") == "1":
                rcomplementaryRNA = reverse_complement_RNA(DNA_to_RNA(DNAsequence))

            # Check to see if motifs in DNA strand needed
            if request.form.get("motifs"):
                motifsequence = request.form.get("motifs").upper()
                motifs = find_motifs(motifsequence, DNAsequence)

            # Return with specified information added to variables
            return render_template("DNA.html",
                                   DNAsequence=DNAsequence,
                                   ac=ac, gc=gc, cc=cc, tc=tc, total=total,
                                   ap=ap, gp=gp, cp=cp, tp=tp,
                                   RNAsequence=RNAsequence,
                                   proteinsequence=proteinsequence,
                                   complementaryDNA=complementaryDNA,
                                   complementaryRNA=complementaryRNA,
                                   rcomplementaryDNA=rcomplementaryDNA,
                                   rcomplementaryRNA=rcomplementaryRNA,
                                   motifsequence=motifsequence,
                                   motifs=motifs
                                   )

        # Otherwise, an empty DNA sequence means that invalid characters were present in the textfile
        abort(400, "Illegal nucleotide characters in DNA sequence -- Click on 'ZGEN' for more information on proper DNA sequence text values")

    else:
        # Otherwise the person reached through page through "GET"
        return render_template("DNA.html")


@app.route("/RNA", methods=["GET", "POST"])
def RNA():
    """Show RNA data for user"""
    # Initialize variables
    RNAsequence = ""
    ac = ""
    gc = ""
    cc = ""
    uc = ""
    total = ""
    ap = ""
    gp = ""
    cp = ""
    up = ""
    DNAsequence = ""
    proteinsequence = ""
    complementaryDNA = ""
    complementaryRNA = ""
    rcomplementaryDNA = ""
    rcomplementaryRNA = ""
    motifsequence = ""
    motifs = []

    # Check to see if person reached through "POST"
    if request.method == "POST":
        # Obtain RNA text if no RNA file found
        if not request.files.get("RNAfile"):
            if not request.form.get("RNAtext"):
                abort(400, "No RNA text file found")
            else:
                RNAsequence = RNAparser(request.form.get("RNAtext"))

        # Otherwise, use information from RNA file
        if request.files.get("RNAfile"):
            try:
                text = request.files["RNAfile"].read().decode("utf-8")
                RNAsequence = RNAparser(text)
            except Exception:
                abort(400, "invalid file")

        # Check to see if RNA sequence is not empty
        if len(RNAsequence) > 0:

            # Check to see if user wants counts of nucleotides
            if request.form.get("counts") == "1":
                ac = adenosine_count(RNAsequence)
                gc = guanosine_count(RNAsequence)
                cc = cytosine_count(RNAsequence)
                uc = uracil_count(RNAsequence)
                total = len(RNAsequence)

            # Check to see if user wants percentages of nucleotides
            if request.form.get("percentages") == "1":
                total = len(RNAsequence)
                ap = calculate_percentages(adenosine_count(RNAsequence), total)
                gp = calculate_percentages(guanosine_count(RNAsequence), total)
                cp = calculate_percentages(cytosine_count(RNAsequence), total)
                up = calculate_percentages(uracil_count(RNAsequence), total)

            # Check to see if DNA is to be transcribed from RNA
            if request.form.get("transcribeDNA") == "1":
                DNAsequence = RNA_to_DNA(RNAsequence)

            # Check to see if protein is to be transcribed from RNA
            if request.form.get("transcribeprotein") == "1":
                proteinsequence = RNA_to_Protein(RNAsequence)

            # Check to see if complementary RNA strand needed
            if request.form.get("cRNA") == "1":
                complementaryRNA = complement_RNA(RNAsequence)

            # Check to see if complementary DNA strand needed
            if request.form.get("cDNA") == "1":
                complementaryDNA = complement_DNA(RNA_to_DNA(RNAsequence))

            # Check to see if reverse complementary RNA strand needed
            if request.form.get("rRNA") == "1":
                rcomplementaryRNA = reverse_complement_RNA(RNAsequence)

            # Check to see if reverse complementary DNA strand needed
            if request.form.get("rDNA") == "1":
                rcomplementaryDNA = reverse_complement_DNA(RNA_to_DNA(RNAsequence))

            # Check to see if motifs in RNA strand needed
            if request.form.get("motifs"):
                motifsequence = request.form.get("motifs").upper()
                motifs = find_motifs(motifsequence, RNAsequence)

            # Return with specified information added to variables
            return render_template("RNA.html",
                                   DNAsequence=DNAsequence,
                                   ac=ac, gc=gc, cc=cc, uc=uc, total=total,
                                   ap=ap, gp=gp, cp=cp, up=up,
                                   RNAsequence=RNAsequence,
                                   proteinsequence=proteinsequence,
                                   complementaryDNA=complementaryDNA,
                                   complementaryRNA=complementaryRNA,
                                   rcomplementaryDNA=rcomplementaryDNA,
                                   rcomplementaryRNA=rcomplementaryRNA,
                                   motifsequence=motifsequence,
                                   motifs=motifs
                                   )

        # Otherwise, an empty RNA sequence means that invalid characters were present in the textfile
        abort(400, "Illegal nucleotide characters in RNA sequence -- Click on 'ZGEN' for more information on proper RNA sequence text values")

    else:
        # Otherwise the person reached through page through "GET"
        return render_template("RNA.html")


@app.route("/Protein", methods=["GET", "POST"])
def proteinpage():
    """Show Protein data for user"""
    # Initialize variables
    proteinsequence = ""
    splitsequence = []
    aminoacids = []
    protein = []
    counts = ""
    sequencecounts = ""
    percentages = ""
    tripleprotein = ""
    fullprotein = ""
    nonpolar = ""
    polar = ""
    aromatic = ""
    positive = ""
    negative = ""
    nonstandard = ""
    disulfide = ""
    motifsequence = ""
    motifs = []

    # Check to see if person reached through "POST"
    if request.method == "POST":
        # Obtain protein text if no protein file found
        if not request.files.get("proteinfile"):
            if not request.form.get("proteintext"):
                abort(400, "No Protein text file found")
            else:
                proteinsequence = protein_parser(request.form.get("proteintext"))

        # Otherwise, use information from protein file
        if request.files.get("proteinfile"):
            try:
                text = request.files["proteinfile"].read().decode("utf-8")
                proteinsequence = protein_parser(text)

            except Exception:
                abort(400, "invalid file")

        # Check to see if proteinsequence is not empty
        if len(proteinsequence) > 0:

            # Create protein and amino acid objects and data
            aminoacids = translate_protein(proteinsequence)
            protein = new_Protein()
            protein.add_counts(proteinsequence)

            # Check to see if user wants counts of amino acids
            if request.form.get("counts") == "1":
                counts = "1"

            # Check to see if user wants percentages of amino acids
            if request.form.get("percentages") == "1":
                percentages = "1"

            # Check to see if user wants number of sequences of amino acids
            if request.form.get("sequencecounts") == "1":
                sequencecounts = "1"

            # Check to see if user wants sequences seperated
            if request.form.get("splitsequence") == "1":
                splitsequence = seperate_protein_sequence(proteinsequence)

            # Check to see if user wants triple-lettered sequence of amino acids
            if request.form.get("triple") == "1":
                tripleprotein = Single_to_Triple_Protein(proteinsequence)

            # Check to see if user wants fully-named sequence of amino acids
            if request.form.get("full") == "1":
                fullprotein = Single_to_Full_Protein(proteinsequence)

            # Obtain specified characteristics of protein from user
            if request.form.get("polar") == "1":
                polar = "1"
            if request.form.get("nonpolar") == "1":
                nonpolar = "1"
            if request.form.get("aromatic") == "1":
                aromatic = "1"
            if request.form.get("positive") == "1":
                positive = "1"
            if request.form.get("negative") == "1":
                negative = "1"
            if request.form.get("nonstandard") == "1":
                nonstandard = "1"
            if request.form.get("disulfide") == "1":
                disulfide = "1"

            # Check to see if motifs in protein strand needed
            if request.form.get("motifs"):
                motifsequence = request.form.get("motifs").upper()
                motifs = find_motifs(motifsequence, proteinsequence)

            # Return with specified information added to variables
            return render_template("Protein.html",
                                   proteinsequence=proteinsequence,
                                   splitsequence=splitsequence,
                                   aminoacids=aminoacids,
                                   protein=protein,
                                   counts=counts, percentages=percentages, sequencecounts=sequencecounts,
                                   tripleprotein=tripleprotein, fullprotein=fullprotein,
                                   nonpolar=nonpolar,
                                   polar=polar,
                                   aromatic=aromatic,
                                   positive=positive,
                                   negative=negative,
                                   nonstandard=nonstandard,
                                   disulfide=disulfide,
                                   motifsequence=motifsequence,
                                   motifs=motifs
                                   )

        # Otherwise, an empty protein sequence means that invalid characters were present in the textfile
        abort(400, "Illegal amino acid characters in protein sequence -- Click on 'ZGEN' for more information on proper protein text values")

    else:
        # Otherwise the person reached through page through "GET"
        return render_template("Protein.html")


@app.route("/FASTA", methods=["GET", "POST"])
def FASTA():
    """Show FASTA data for user"""
    # Initialize variables
    fasta = []
    data = ""

    # Check to see if person reached through "POST"
    if request.method == "POST":
        if not request.files.get("fastafile"):
            abort(400, "No FASTA file found")

        # Create FASTA file
        if request.files.get("fastafile"):
            try:
                text = request.files["fastafile"].read().decode("utf-8")
                fasta = FASTAparser(text)
                data = "1"
            except Exception:
                abort(400, "invalid file")

        # Return with fasta file parsed
        return render_template("FASTA.html",
                               fasta=fasta,
                               data=data
                               )

    else:
        # Otherwise the person reached through page through "GET"
        return render_template("FASTA.html")


# Handles abort cases of error
@app.errorhandler(HTTPException)
def errorhandler(error):
    """Handle errors"""
    return render_template("error.html", error=error)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
