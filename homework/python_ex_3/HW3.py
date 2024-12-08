import math
from operator import index

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
    seq_without_pun = seq
    to_remove = [",","_",".",":"]
    for p_to_remove in (to_remove):
        seq_without_pun = seq_without_pun.replace(p_to_remove , " ")
        continue
    return seq_without_pun



def remove_spaces(seq):
    seq_without_space = seq
    seq_without_space = seq_without_space.replace(" " , "")
    return seq_without_space



def remove_invalid_letters(seq):
    char_allowed_in_seq = ['a','t','c','g','A','T','C','G']
    seq_without_inv_char = ''
    for char in seq:
        if char in char_allowed_in_seq:
            seq_without_inv_char += char
        else:
            seq_without_inv_char += ' '
    return seq_without_inv_char


def capitalize_letters(words_list):
    return words_list.upper()

def proofreading(seq):
    if len(seq) < 3: return []
    func_dna = []
    seq_to_reduce = seq
    for i in range(len(seq)):
        if seq_to_reduce[0] == 'A' and seq_to_reduce[1] == 'T' and seq_to_reduce[2] == 'G':
            func_dna.append(seq_to_reduce[:3])
            seq_to_reduce = seq_to_reduce[3:]
            break
        else:
            seq_to_reduce = seq_to_reduce [1:]
            continue
    finished = False
    stop_seq = ['TAA', 'TAG', 'TGA']
    seq_length = seq_to_reduce #length after shortening the beginning
    for i in range (len(seq_to_reduce) // 3):
        first_3_digits = seq_to_reduce[:3]
        func_dna.append(first_3_digits)
        for finisher in stop_seq:
            if finisher == first_3_digits:
                finished = True
                break
        if finished: break
        seq_to_reduce = seq_to_reduce[3:]
    if len(seq_length) % 3 != 0 and finished == False or len(func_dna) == 1: func_dna.append('ATT')
    return func_dna

def transcript(func_seq): ###delete one option###

    for i in range (len(func_seq)):
        func_seq[i] = func_seq[i].replace('T','U')
        continue
    return func_seq
    # for i in range (len(func_seq)):
    #     for sub_seq in func_seq:
    #         for j in range(len(sub_seq)):
    #             sub_seq[j] = sub_seq[j].replace('T','U')
    # return func_seq

def translate(rna_seq):
    for i in range (len(rna_seq)-1):
        rna_seq[i] = codon_translator(rna_seq[i])
        continue
    rna_seq = rna_seq[:-1]
    return rna_seq


def preprocessing(seq):
    seq = (remove_invalid_letters(seq))
    seq = (remove_spaces(seq))
    seq = capitalize_letters(seq)
    seq = proofreading(seq)
    seq = transcript(seq)
    seq = translate(seq)
    return seq


###### Part B #######
def get_sequences_data(sequence_corpus):
    sequences_data_to_r = sequence_corpus.copy()
    for i in range (1, len(sequences_data_to_r) + 1):
        sequences_data_to_r[i] = len(preprocessing(sequences_data_to_r[i]))
        continue
    return sequences_data_to_r


'''
help me function the create inverted index or add a new processed seq to the letters dict
'''
def fun_create_inverted_index(letter,letters_dict,i):
    if letter not in letters_dict:
        letters_dict[letter] = {i: 1}
    elif i not in letters_dict[letter]:
        letters_dict[letter][i] = 1
    else:
        letters_dict[letter][i] += 1
    return letters_dict


def create_inverted_index(sequence_corpus):
    letters_dict = {}
    sequence_corpus_copy = sequence_corpus.copy()
    for i in range (1, len(sequence_corpus) + 1):
        sequence_corpus_copy[i] = preprocessing(sequence_corpus_copy[i])
        for j in range (len(sequence_corpus_copy[i])):
            letter = sequence_corpus_copy[i][j]
            fun_create_inverted_index(letter,letters_dict, i)
    return letters_dict


def add_to_data(inverted_index, sequences_data, seq_id, seq):
    new_inverted_index = inverted_index.copy()
    new_sequences_data = sequences_data.copy()
    new_seq = seq[::]
    new_seq = preprocessing(new_seq)
    for i in range(len(new_seq)):
        new_inverted_index = fun_create_inverted_index(new_seq[i],new_inverted_index,seq_id)
    new_sequences_data[seq_id] = len(new_seq)
    return new_inverted_index,new_sequences_data


def remove_from_data(inverted_index, sequences_data, seq_id):
    lst_remove_keys = []
    for letter in inverted_index:
        if seq_id in inverted_index[letter]:
            inverted_index[letter].pop(seq_id)
        if len(inverted_index[letter])==0: lst_remove_keys.append(letter)
    for letter in lst_remove_keys:
        inverted_index.pop(letter)
    sequences_data.pop(seq_id)
    return inverted_index, sequences_data


###### Part C #######
def calculate_aaf_isf(amino_acid, seq_id, inverted_index, sequences_data):
    if seq_id not in inverted_index[amino_acid]: return float(0)
    aaf_val = math.log(len(sequences_data)/len(inverted_index[amino_acid]),2)
    isf_val = inverted_index[amino_acid][seq_id]/sequences_data[seq_id]
    aaf_isf_val = round(aaf_val*isf_val,3)
    return aaf_isf_val



def preprocess_query(query):
    lst_of_amino = []
    for letter in query:
        if letter == ',': continue
        lst_of_amino.append(letter)
    tuple_to_return = tuple(lst_of_amino)
    return tuple_to_return

def get_scores_of_relevance_sequences(query, inverted_index, sequences_data):
    dict_to_return = {}
    for letter in query:
        if letter in inverted_index:
            for key in inverted_index[letter]:
                if key not in dict_to_return:
                    dict_to_return[key] = round(calculate_aaf_isf(letter,key,inverted_index,sequences_data),3)
                else:
                    dict_to_return[key] += round(calculate_aaf_isf(letter,key,inverted_index,sequences_data),3)
    for key in dict_to_return:
        dict_to_return[key] = round(dict_to_return[key],3)
    return dict_to_return


###### Part D #######
def menu(sequence_corpus):
    pass
        # choice = input('Choose an option from the menu:\n\t(1) Insert a query.\n\t(2) Add sequence to sequence_corpus.\n\t(3) Calculate AAF-ISF Score for an amino acid in a sequence.\n\t(4) Delete a sequence from the sequence_corpus.\n\t(5) Exit.\nYour choice: ')
        # query_choice = input('Choose the type of results you would like to retrieve:\n\t(A) All relevant sequences.\n\t(B) The most relevant sequence.\n\t(C) Back to the main menu.\nYour choice: ')


