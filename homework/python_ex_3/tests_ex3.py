import HW3
from python_ex_3.HW3 import preprocess_query

#
# lst_of_seq = ["Ha_TT:AG,HF.inish", "JT,,,__:::HH...Finish"]
# for test in lst_of_seq:
#     seq_without_p = HW3.remove_punctuation(test)
#     print(seq_without_p)
# #
# lst_of_seq2 = ["Ha_TT:AG,HF.inish", "JT,,,__:::HH...Finish", "hello Cats<TillCCCccc", "A gcrTG-G"]
# for test in lst_of_seq2:
#     seq_without_inv_char = HW3.remove_invalid_letters(test)
#     print(seq_without_inv_char)
# #
# lst_of_seq3 = ["   hyyrgncj", "jfd djnd jdbmn c sdb sd j f", "       t"]
# for test in lst_of_seq3:
#     seq_without_spaces = HW3.remove_spaces(test)
#     # print(seq_without_spaces)
# #
# for test in lst_of_seq3:
#     seq_upper = HW3.capitalize_letters(test)
#     print(seq_upper)
# #
# lst_of_seq = ['ATGAAATGTACGTG', 'ATGCCGACGTGAT', 'GGATG', 'GGATGAAATAG', 'GACT', 'A']
# ordered_seq = []
# for i in range(len(lst_of_seq)):
#     ordered_seq.append(HW3.proofreading(lst_of_seq[i]))
# print(ordered_seq)
# #
# for i in range(len(ordered_seq)):
#     ordered_seq[i] = HW3.transcript(ordered_seq[i])
# print(ordered_seq)
# #
# for i in range (len(ordered_seq)):
#     ordered_seq[i] = HW3.translate(ordered_seq[i])
# print(ordered_seq)
# #
# seq1 = 'Aga---tGACggcrfAlmn: GCATA'
# seq1 = HW3.preprocessing(seq1)
# print (seq1)
# dict_for_test = {1:'ATGAAATGTACGTG', 2:'ATGCCGACGTGAT', 3:'GGATG',4:'GGATGAAATAG',5:'GACT'}
'''
inverted index question
'''
dict_for_test = {1:'GCTTA_tGC:GXATC CGTAGACffx:TYAGgytACGTMA',2:'AGG. Ddfe::wscv',3:'cl_yuCATGATGCGTACCAGGCTqwAGCATGCGTbbAGCTAxzvGCATGAC'}
inverted_index = HW3.create_inverted_index(dict_for_test)
print(inverted_index)
'''
sequences_data question
'''
sequences_data = HW3.get_sequences_data(dict_for_test)
print(sequences_data)


'''
add_to_date function
'''
# inverted_index,sequences_data = HW3.add_to_data(inverted_index,sequences_data,4,".yyyuTACGATGGTAGCTAGCTAGCGlllTACGATCGTA")
# print(f"new_inverted_index: {inverted_index}")
# print(f"new_sequences_data: {sequences_data}")

# inverted_index, sequences_data = HW3.remove_from_data(inverted_index, sequences_data, 3)
# print(f"new_inverted_index: {inverted_index}")
# print(f"new_sequences_data: {sequences_data}")

aaf_isf_M = HW3.calculate_aaf_isf('M', 1, inverted_index, sequences_data)
print(f'AAF-ISF of seq 1 and the amino acid "M" is: {aaf_isf_M}')
aaf_isf_M_2 = HW3.calculate_aaf_isf('M', 3, inverted_index,sequences_data)
print(f'AAF-ISF of seq 3 and the amino acid "M" is: {aaf_isf_M_2}')
tf_idf_L = HW3.calculate_aaf_isf('L', 1, inverted_index, sequences_data)
print(f'AAF-ISF of seq 1 and the amino acid "L" is: {tf_idf_L}')

print(HW3.preprocess_query("M,L,P"))
print(HW3.get_scores_of_relevance_sequences(('R', 'M', 'S'),inverted_index, sequences_data))
