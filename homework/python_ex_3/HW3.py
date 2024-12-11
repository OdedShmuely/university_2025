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
'''
this function takes the seq (str) and replace the punctuation with spaces
'''
def remove_punctuation(seq):
    seq_without_pun = seq
    to_remove = [",","_",".",":"]
    for p_to_remove in (to_remove):
        seq_without_pun = seq_without_pun.replace(p_to_remove , " ")
        continue
    return seq_without_pun


'''
this function takes the seq (str) and remove the spaces
'''
def remove_spaces(seq):
    seq_without_space = seq
    seq_without_space = seq_without_space.replace(" " , "")
    return seq_without_space


'''
this function takes the seq (str) and keeps only the valid characters: a,c,t,g,A,C,T,G
'''
def remove_invalid_letters(seq):
    char_allowed_in_seq = ['a','t','c','g','A','T','C','G']
    seq_without_inv_char = ''
    for char in seq:
        if char in char_allowed_in_seq:
            seq_without_inv_char += char
        else:
            seq_without_inv_char += ' '
    return seq_without_inv_char

'''
this function takes the seq (str) and make all the string in CAPS
'''
def capitalize_letters(seq):
    return seq.upper()

'''
this function takes the seq (str) with only the valid characters in caps and returns a list
with the functional dna sequence
'''
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
    for i in range (len(seq_to_reduce) // 3):
        first_3_digits = seq_to_reduce[:3]
        func_dna.append(first_3_digits)
        for finisher in stop_seq:
            if finisher == first_3_digits:
                finished = True
                break
        if finished: break
        seq_to_reduce = seq_to_reduce[3:]
    if (finished == False and len(func_dna) > 0) or len(func_dna) == 1: func_dna.append('ATT')
    return func_dna

'''
this function receives a functional seq list and replace al the 'T' with a 'U' 
'''
def transcript(func_seq):
    for i in range (len(func_seq)):
        func_seq[i] = func_seq[i].replace('T','U')
        continue
    return func_seq

'''
the function takes the list of RNA seq and replace the representation of the value with capital
letters representing the amino acid
'''
def translate(rna_seq):
    for i in range (len(rna_seq)-1):
        rna_seq[i] = codon_translator(rna_seq[i])
        continue
    rna_seq = rna_seq[:-1]
    return rna_seq

'''
this function combine all the another functions and make a list of amino acids from an unorganized string'''
def preprocessing(seq):
    seq = (remove_invalid_letters(seq))
    seq = (remove_spaces(seq))
    seq = capitalize_letters(seq)
    seq = proofreading(seq)
    seq = transcript(seq)
    seq = translate(seq)
    return seq


###### Part B #######
'''
this function takes a dict with sequences and builds a dictionary that contains the number of amino acids in each sequence
'''
def get_sequences_data(sequence_corpus):
    build_sequences_data = sequence_corpus.copy()
    for i in range (1, len(build_sequences_data) + 1):
        build_sequences_data[i] = len(preprocessing(build_sequences_data[i]))
        continue
    return build_sequences_data


'''
the function helps me create inverted index or add a new processed seq to the letters dict
'''
def fun_create_inverted_index(letter,letters_dict,i):
    if letter not in letters_dict:
        letters_dict[letter] = {i: 1}
    elif i not in letters_dict[letter]:
        letters_dict[letter][i] = 1
    else:
        letters_dict[letter][i] += 1
    return letters_dict

'''
this function creates a dictionary that contains the letters as keys and the items as dictionaries
that contains the seq id as their key and the item as the number of times the amino acid with the letter in the
key appears in the seq - seq ID
'''
def create_inverted_index(sequence_corpus):
    letters_dict = {}
    sequence_corpus_copy = sequence_corpus.copy()
    for i in range (1, len(sequence_corpus_copy) + 1):
        sequence_corpus_copy[i] = preprocessing(sequence_corpus_copy[i])
        for j in range (len(sequence_corpus_copy[i])):
            letter = sequence_corpus_copy[i][j]
            fun_create_inverted_index(letter,letters_dict, i)
    return letters_dict

'''
this function add new sequence to the inverted index and sequences data dicts
'''
def add_to_data(inverted_index, sequences_data, seq_id, seq):
    new_inverted_index = inverted_index.copy()
    new_sequences_data = sequences_data.copy()
    new_seq = seq[::]
    new_seq = preprocessing(new_seq)
    for i in range(len(new_seq)):
        new_inverted_index = fun_create_inverted_index(new_seq[i],new_inverted_index,seq_id)
    new_sequences_data[seq_id] = len(new_seq)
    return new_inverted_index,new_sequences_data

'''
this function removes a sequence from the inverted index and the sequences data
'''
def remove_from_data(inverted_index, sequences_data, seq_id):
    lst_remove_keys = []
    for letter in inverted_index:
        if seq_id in inverted_index[letter]:
            inverted_index[letter].pop(seq_id)
        if len(inverted_index[letter])==0: lst_remove_keys.append(letter)
    for letter in lst_remove_keys:
        inverted_index.pop(letter)
    if seq_id in sequences_data: sequences_data.pop(seq_id)
    return inverted_index, sequences_data


###### Part C #######
'''
this function calculates the aaf-isf value of a seq and returns 0 if the sequence does not exist
'''
def calculate_aaf_isf(amino_acid, seq_id, inverted_index, sequences_data):
    if seq_id not in inverted_index[amino_acid]: return float(0)
    aaf_val = math.log(len(sequences_data)/len(inverted_index[amino_acid]),2)
    isf_val = inverted_index[amino_acid][seq_id]/sequences_data[seq_id]
    aaf_isf_val = round(aaf_val*isf_val,3)
    return aaf_isf_val

'''
the function takes the string query input and make it in the form of a tuple
'''
def preprocess_query(query):
    lst_of_amino = []
    for letter in query:
        if letter == ',': continue
        lst_of_amino.append(letter)
    tuple_to_return = tuple(lst_of_amino)
    return tuple_to_return

'''
the function gets a query and returns a dictionary with seq id as keys
and aaf_isf values of the query letters as items
'''
def get_scores_of_relevance_sequences(query, inverted_index, sequences_data):
    dict_to_return = {}
    for letter in query:
        if letter in inverted_index:
            for seq_id in inverted_index[letter]:
                if seq_id not in dict_to_return:
                    dict_to_return[seq_id] = round(calculate_aaf_isf(letter,seq_id,inverted_index,sequences_data),3)
                    continue
                else:
                    dict_to_return[seq_id] += round(calculate_aaf_isf(letter,seq_id,inverted_index,sequences_data),3)
                    continue
    for seq_id in dict_to_return:
        dict_to_return[seq_id] = round(dict_to_return[seq_id],3)
    return dict_to_return

'''
this function helps me find the max value of aaf asf within the dictionary and returns the sequence id and the value of aaf asf
'''
def highest_score_seq(query_value, inverted_index,sequences_data):
    max_value = 0
    max_index = None
    dict_to_search_max = get_scores_of_relevance_sequences(query_value,inverted_index,sequences_data)
    for key, value in dict_to_search_max.items():
        if value > max_value:
            max_value = value
            max_index = key
    return max_index,max_value

'''
this function check the validity of an input, according to the choice 2/3/4
'''
def check_validity_of_input (sequences_data,choice):
    while True:
        new_seq_id = int(input('Insert the sequence ID: '))
        if new_seq_id in sequences_data and choice == 2:
            print(f'The sequence ID {new_seq_id} is already in sequence_corpus.')
        elif new_seq_id not in sequences_data and (choice == 3 or choice == 4):
            print(f'The sequence ID {new_seq_id} is not in sequence_corpus.')
        else: return new_seq_id
'''
this function check the validity of an amino acid, that it exists in the inverted index dict.
'''
def valid_amino_acid (inverted_index):
    while True:
        amino_acid = input('Insert an amino acid: ')
        if amino_acid not in inverted_index:
            print(f'The amino acid {amino_acid} is not in sequence_corpus.')
        else: return amino_acid

###### Part D #######
'''
this function combines all of the functions above to manipulate the inverted index and sequences data
according to the input we get from the user
'''
def menu(sequence_corpus):
    inverted_index = create_inverted_index(sequence_corpus)
    sequences_data = get_sequences_data(sequence_corpus)
    continue_function = True
    while continue_function:
        choice = input('Choose an option from the menu:\n\t(1) Insert a query.\n\t(2) Add sequence to sequence_corpus.\n\t(3) Calculate AAF-ISF Score for an amino acid in a sequence.\n\t(4) Delete a sequence from the sequence_corpus.\n\t(5) Exit.\nYour choice: ')
        if choice in ('1','2','3','4','5'): choice = int(choice)
        else:
            print('Invalid choice. Please select a valid option.')
            continue
        if choice == 1:
            query_value = input('Write your query here: ')
            query_value = preprocess_query(query_value)
            continue_function_choice1 = True
            while continue_function_choice1:
                query_choice = input('Choose the type of results you would like to retrieve:\n\t(A) All relevant sequences.\n\t(B) The most relevant sequence.\n\t(C) Back to the main menu.\nYour choice: ')
                if query_choice == 'A':
                    relevant_score = get_scores_of_relevance_sequences(query_value,inverted_index,sequences_data)
                    if len(relevant_score) != 0:
                        for key in relevant_score:
                            print(f'{key} : {relevant_score[key]}')
                elif query_choice == 'B':
                    highest_score_seq_id, highest_score = highest_score_seq(query_value, inverted_index, sequences_data)
                    if highest_score_seq_id is not None:
                        print(f'The most relevant sequence is {highest_score_seq_id} with a score of {highest_score}')
                elif query_choice == 'C':
                    break
                else:
                    print('Invalid choice. Please select a valid option.')

        elif choice == 2: #add new sequence
            new_seq_id = check_validity_of_input(sequences_data,choice)
            new_seq = input('Insert the sequence itself: ')
            inverted_index, sequences_data = add_to_data(inverted_index, sequences_data, new_seq_id, new_seq)
            print(f'Sequence {new_seq_id} was successfully added!')
        elif choice == 3:
            seq_id_to_cal = check_validity_of_input(sequences_data,choice)
            amino_acid = valid_amino_acid(inverted_index)
            aaf_isf = calculate_aaf_isf(amino_acid,seq_id_to_cal,inverted_index, sequences_data)
            print(f'AAF-ISF of the amino acid {amino_acid} in sequence {seq_id_to_cal} is: {aaf_isf}')
        elif choice == 4:
            seq_id_to_del = check_validity_of_input(sequences_data, choice)
            inverted_index, sequences_data = remove_from_data(inverted_index,sequences_data,seq_id_to_del)
            print(f'Sequence {seq_id_to_del} was successfully deleted.')
        elif choice == 5: continue_function = False
menu(seq_corpus)