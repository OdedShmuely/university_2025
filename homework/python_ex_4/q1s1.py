from q1s2 import duplicate_list

"""
the function will check a possibility to get from the current state
received as lightbulb_array to the desired target_array
"""
def lightbulb_solver_rec(lightbulb_array,target_array, idx):
    if lightbulb_array == target_array:
        return True
    if idx == len(lightbulb_array):
        return False
    no_switch = lightbulb_solver_rec(lightbulb_array,target_array,idx+1)
    lightbulb_array_copy = []
    duplicate_list(lightbulb_array,lightbulb_array_copy, len(lightbulb_array)-1)
    array_len = len(lightbulb_array)
    if idx == 0:
        lightbulb_array_copy[0] = not lightbulb_array_copy[0]
        lightbulb_array_copy[1] = not lightbulb_array_copy[1]
    elif idx == array_len-1:
        lightbulb_array_copy[array_len-1] = not lightbulb_array_copy[array_len-1]
        lightbulb_array_copy[array_len-2] = not lightbulb_array_copy[array_len-2]
    else:
        lightbulb_array_copy[idx-1] = not lightbulb_array_copy[idx-1]
        lightbulb_array_copy[idx] = not lightbulb_array_copy[idx]
        lightbulb_array_copy[idx+1] = not lightbulb_array_copy[idx+1]
    switch = lightbulb_solver_rec(lightbulb_array_copy,target_array,idx+1)
    return switch or no_switch

'''
this function is a wrapped function that will get the array and target array and returns
whether you can get to the target array or not using the solver recursion function
'''
def lightbulb_solver(lightbulb_array,target_array):
    return lightbulb_solver_rec(lightbulb_array,target_array,0)
