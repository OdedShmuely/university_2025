# ************************ HOMEWORK 1 QUESTION 4 **************************
def question_4(input_list):
    new_Table = input_list
    for index in new_Table: #turn the int values to boolian, True = bomb, False = safe zone
        for j in range(len(index)):
            if index[j]%2==0:
                index[j] = True
            else:
                index[j] = False
    help_Divide = []
    for i in range(len(new_Table)):
        for j in range(len(new_Table[i])):
            if new_Table[i][j]==False:
                counter = 0
                if (i != 0 and i != (len(new_Table) - 1)) and (j != 0 and j != len(new_Table[i]) - 1):
                    movement = j  # helps moving the check to other cells
                    for t in range (3):
                        if new_Table[i-1][movement-1]==True:
                            counter +=1
                        movement+=1
                    movement = j
                    for t in range (2):
                        if new_Table[i][movement-1]==True:
                            counter+=1
                        movement+=2
                    movement = j
                    for t in range (3):
                        if new_Table[i+1][movement-1]==True:
                            counter+=1
                        movement+=1
                    help_Divide.append(counter)
                elif (i == 0 ) and j==0: #check private cases for the corners left top
                    movement=j
                    if new_Table[i][movement+1]==True:
                        counter+=1
                    for t in range(2):
                        if new_Table[i+1][movement]==True:
                            counter+=1
                        movement+=1
                    help_Divide.append(counter)
                elif i==0 and j == new_Table[i][len(new_Table[i])-1]: #Check private case top right
                    movement = j
                    if new_Table[i][movement -1] == True:
                        counter += 1
                    for t in range(2):
                        if new_Table[i + 1][movement-1] == True:
                            counter += 1
                        movement += 1
                    help_Divide.append(counter)
                elif i==len(new_Table)-1 and j == new_Table[i][len(new_Table[i])-1]:  # Check private case bottom right
                    movement = j
                    if new_Table[i][movement-1]== True:
                        counter += 1
                    for t in range(2):
                        if new_Table[i-1][movement-1] == True:
                            counter += 1
                        movement += 1
                    help_Divide.append(counter)
                elif i == len(new_Table)-1 and j == 0:  # Check private case bottom left
                    movement = j
                    if new_Table[i][movement+1]==True:
                        counter+=1
                    for t in range (2):
                        if new_Table[i-1][movement]==True:
                            counter+=1
                        movement+=1
                    help_Divide.append(counter)

                elif i==0 and 0<j<len(new_Table[i]): #check top line
                    movement= j-1
                    for t in range (2):
                        if new_Table[i][movement]==True:
                            counter += 1
                        movement+=2
                    movement= j-1
                    for t in range(3):
                        if new_Table[i+1][movement]==True:
                            counter+=1
                        movement+=1
                    help_Divide.append(counter)
                elif i == len(new_Table)-1 and 0<j<len(new_Table[i]): #chek bottom line
                    movement = j-1
                    for t in range (3):
                        if new_Table[i-1][movement]==True:
                            counter+=1
                        movement+=1
                    movement= j-1
                    for t in range(2):
                        if new_Table[i][movement]==True:
                            counter+=1
                        movement+=2
                    help_Divide.append(counter)
                elif 0<i<len(new_Table) and j==0: #check left side
                    movement = i-1 #this time I use 'i' to help move the check
                    for t in range (2):
                        if new_Table[movement][j]==True:
                            counter+=1
                        movement+=2
                    movement = i-1
                    for t in range (3):
                        if new_Table[movement][j+1]:
                            counter +=1
                        movement+=1
                    help_Divide.append(counter)
                elif 0<i<len(new_Table) and j==len(new_Table[i])-1: #check right side
                    movement = i - 1  # this time I use 'i' to help move the check
                    for t in range(2):
                        if new_Table[movement][j] == True:
                            counter += 1
                        movement += 2
                    movement = i - 1
                    for t in range(3):
                        if new_Table[movement][j - 1]==True:
                            counter += 1
                        movement += 1
                    help_Divide.append(counter)
    before_Divide = 0
    for index in help_Divide:
        before_Divide+=index
    print(help_Divide)
    print((before_Divide/len(help_Divide)))
    print (new_Table)






question_4([[0,1,2],[3,4,5],[6,7,8]])
'''
if (i == 0 or i == (len(new_Table) - 1)) and (j == 0 or j == len(new_Table[i] - 1)):  # check the outside squares
    if i == 0 or i == (len(new_Table) - 1):
        if i == 0:
            for i in range(3):
'''