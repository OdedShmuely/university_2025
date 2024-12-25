'''
this function duplicates a list using recursion
'''
def duplicate_list(list_1, list_2, idx):
    if idx < 0: return
    if idx == 0:
        list_2.append(list_1[0])
        return
    duplicate_list(list_1,list_2,idx-1)
    list_2.append(list_1[idx])
    return

'''
this function returns the switches that were pressed and an empty list for no answer, and a boolian true/false
if there is a solution
'''
def lightbulb_solver_steps_rec(lightbulb_array, target_array, idx, idx_lst, finished):
    if lightbulb_array == target_array: return idx_lst, True
    if finished: return idx_lst, finished
    if len(lightbulb_array) == idx:
        return idx_lst, False
    lightbulb_array_changed = []
    duplicate_list(lightbulb_array, lightbulb_array_changed, len(lightbulb_array)-1) #make a copy of the list
    array_len = len(lightbulb_array_changed)
    if idx == 0:
        lightbulb_array_changed[0] = not lightbulb_array_changed[0]
        lightbulb_array_changed[1] = not lightbulb_array_changed[1]
    elif idx == array_len-1:
        lightbulb_array_changed[array_len - 1] = not lightbulb_array_changed[array_len - 1]
        lightbulb_array_changed[array_len - 2] = not lightbulb_array_changed[array_len - 2]
    else:
        lightbulb_array_changed[idx - 1] = not lightbulb_array_changed[idx - 1]
        lightbulb_array_changed[idx] = not lightbulb_array_changed[idx]
        lightbulb_array_changed[idx + 1] = not lightbulb_array_changed[idx + 1]
    idx_lst.append(idx)
    idx_lst, finished = lightbulb_solver_steps_rec(lightbulb_array_changed, target_array, idx + 1, idx_lst, finished)
    if lightbulb_array_changed == target_array: return idx_lst, finished
    if len(idx_lst) and not finished: idx_lst.pop(len(idx_lst)-1)
    idx_lst, finished = lightbulb_solver_steps_rec(lightbulb_array, target_array, idx + 1, idx_lst, finished)
    return idx_lst, finished

'''
the function returns a list of the switches that were pressed and -1 in case there is no solution
'''
def lightbulb_solver_with_steps(lightbulb_array,target_array):
    list_to_return, finished = lightbulb_solver_steps_rec(lightbulb_array,target_array,0, [], False)
    if finished: return list_to_return
    else: return [-1]
print(lightbulb_solver_with_steps([True,False,True], [True, True, True]))
# print(lightbulb_solver_with_steps([True,False, False, False, False, False], [False, True, False, True , True, True]))

'''
    if lightbulb_array_head == target_array:
        return idx_lst_head
    if idx == len(lightbulb_array_head):
        return  idx_lst_head
    lightbulb_array_copy = lightbulb_array_head[::]
    idx_lst_copy = idx_lst_head.copy()
    idx_lst_copy = lightbulb_solver_steps_rec(lightbulb_array_head, target_array, idx + 1, idx_lst_copy)
    array_len = len(lightbulb_array_copy)
    if idx == 0:
        lightbulb_array_copy[0] = not lightbulb_array_copy[0]
        lightbulb_array_copy[1] = not lightbulb_array_copy[1]
    elif idx == array_len - 1:
        lightbulb_array_copy[array_len - 1] = not lightbulb_array_copy[array_len - 1]
        lightbulb_array_copy[array_len - 2] = not lightbulb_array_copy[array_len - 2]
    else:
        lightbulb_array_copy[idx - 1] = not lightbulb_array_copy[idx - 1]
        lightbulb_array_copy[idx] = not lightbulb_array_copy[idx]
        lightbulb_array_copy[idx + 1] = not lightbulb_array_copy[idx + 1]
    idx_lst_copy.append(idx)
    idx_lst_copy = lightbulb_solver_steps_rec(lightbulb_array_copy, target_array, idx + 1, idx_lst_head)
    if lightbulb_array_copy != target_array and idx_lst_copy:
        idx_lst_copy.pop()
        return idx_lst_copy
    return idx_lst_copy
    
    
    
    
    
    if lightbulb_array == target_array:
        return True
    if idx == len(lightbulb_array):
        return False

    array_len = len(lightbulb_array)
    if idx == 0:
        lightbulb_array[0] = not lightbulb_array[0]
        lightbulb_array[1] = not lightbulb_array[1]
    elif idx == array_len-1:
        lightbulb_array[array_len-1] = not lightbulb_array[array_len-1]
        lightbulb_array[array_len-2] = not lightbulb_array[array_len-2]
    else:
        lightbulb_array[idx - 1] = not lightbulb_array[idx - 1]
        lightbulb_array[idx] = not lightbulb_array[idx]
        lightbulb_array[idx + 1] = not lightbulb_array[idx + 1]
    turn_on = lightbulb_solver_steps_rec(lightbulb_array,target_array,idx+1, idx_list,1)
    lightbulb_solver_steps_rec(lightbulb_array,target_array,idx+1, idx_list,0)
    if switched == 1 and turn_on: idx_list.append(idx)
    return idx_list
    '''