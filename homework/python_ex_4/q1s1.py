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
    array_len = len(lightbulb_array)
    if idx == 0:
        lightbulb_array[0] = not lightbulb_array[0]
        lightbulb_array[1] = not lightbulb_array[1]
    elif idx == array_len-1:
        lightbulb_array[array_len-1] = not lightbulb_array[array_len-1]
        lightbulb_array[array_len-2] = not lightbulb_array[array_len-2]
    else:
        lightbulb_array[idx-1] = not lightbulb_array[idx-1]
        lightbulb_array[idx] = not lightbulb_array[idx]
        lightbulb_array[idx+1] = not lightbulb_array[idx+1]
    switch = lightbulb_solver_rec(lightbulb_array,target_array,idx+1)
    return switch or no_switch

'''
this function is a wrapped function that will get the array and target array and returns
whether you can get to the target array or not using the solver recursion function
'''
def lightbulb_solver(lightbulb_array,target_array):
    return lightbulb_solver_rec(lightbulb_array,target_array,0)


print(lightbulb_solver( [True, False, False],[True, False, True]))



# final_answer, ig_idx, ig_pressed, temp_res = lightbulb_solver_rec(lightbulb_array,target_array,0, False, True)
# if temp_res == False: return False
# else: return True
'''
def lightbulb_solver_rec(lightbulb_array,target_array,idx, pressed,res_temp):
    if len(lightbulb_array) == 1:
        if lightbulb_array[idx] is not target_array[idx]: pressed = True
        return True, idx + 1, pressed, res_temp
    res, idx, pressed,res_temp = lightbulb_solver_rec(lightbulb_array[:-1],target_array[:-1],idx, pressed, res_temp)
    if not res: return False, idx+1, False, False
    if res_temp == False:
        if lightbulb_array[idx] is not target_array[idx]:
            res_temp = True
            pressed = True
            return True, idx, pressed, res_temp
        if lightbulb_array[idx] == target_array[idx]:
            return False, idx+1, False, False
    if lightbulb_array[idx] is not target_array[idx] and pressed == True:
        pressed = False
        return True, idx + 1, pressed, res_temp
    if lightbulb_array[idx] == target_array[idx] and pressed == False:
        return True, idx + 1, pressed, res_temp

    return res, idx + 1, False, False
'''