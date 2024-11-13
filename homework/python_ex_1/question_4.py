def question_4 (input_list):
    new_Table = input_list
    for index in new_Table:  # turn the int values to boolian, True = bomb, False = safe zone
        for j in range(len(index)):
            if index[j] % 2 == 0:
                index[j] = True
            else:
                index[j] = False
    position_pairs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]] #help me sort the surrounding of each single cell in the "table"
    sum_of_bombs = []
    for y in range(len(new_Table)):
        for x in range (len(new_Table[y])): #for each cell in the "table"
            if new_Table[y][x]==False: #only work if the cell is safe
                count_bombs_local =0
                for position in position_pairs: #a loop to check each cell's suroundings
                    dx = position[1]
                    dy = position[0]
                    if x + dx < 0 or x + dx >= len(new_Table[y]):
                        continue
                    if y + dy < 0 or y + dy >= len(new_Table):
                        continue
                    if new_Table[y+dy][x+dx]:
                        count_bombs_local += 1
                sum_of_bombs.append(count_bombs_local) #adding to a list the sum of each cell's close cells marked as bombs
    to_divide = 0
    for index in sum_of_bombs:
        to_divide += index
    average_of_bombs = to_divide/len(sum_of_bombs)
    print(average_of_bombs)
