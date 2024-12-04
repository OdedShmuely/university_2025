import math


# Example Sequence Corpus
seq_corpus = {
    1: 'GCTTA_tGC:GXATC  CGTAGACffx:TYAGgytACGTMA',
    2: 'AGG. Ddfe::wscv',
    3: 'cl_yuCATGATGCGTACCAGGCTqwAGCATGCGTbbAGCTAxzvGCATGAC'
}

#Helper function
def codon_translator(codon):
    RNA_to_protien = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y',
                      'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P',
                      'CCG': 'P', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I',
                      'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K',
                      'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A',
                      'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
                      'GGG': 'G'}
    decoding = RNA_to_protien.get(codon, "stop")
    return decoding


####### Part A #########
def remove_punctuation(seq):
    pass


def remove_spaces(seq):
    pass


def remove_invalid_letters(seq):
    pass


def capitalize_letters(words_list):
    pass


def proofreading(seq):
    pass


def transcript(func_seq):
    pass


def translate(rna_seq):
    pass


def preprocessing(seq):
    pass


###### Part B #######
def get_sequences_data(sequence_corpus):
    pass


def create_inverted_index(sequence_corpus):
    pass


def add_to_data(inverted_index, sequences_data, seq_id, seq):
    pass


def remove_from_data(inverted_index, sequences_data, seq_id):
    pass


def preprocess_query(query):
    pass


###### Part C #######
def calculate_aaf_isf(amino_acid, seq_id, inverted_index, sequences_data):
    pass


def get_scores_of_relevance_sequences(query, inverted_index, sequences_data):
    pass


###### Part D #######
def menu(sequence_corpus):
    pass
        # choice = input('Choose an option from the menu:\n\t(1) Insert a query.\n\t(2) Add sequence to sequence_corpus.\n\t(3) Calculate AAF-ISF Score for an amino acid in a sequence.\n\t(4) Delete a sequence from the sequence_corpus.\n\t(5) Exit.\nYour choice: ')
        # query_choice = input('Choose the type of results you would like to retrieve:\n\t(A) All relevant sequences.\n\t(B) The most relevant sequence.\n\t(C) Back to the main menu.\nYour choice: ')


