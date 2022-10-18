def keep_odds_from_odds(list_list):
    i = 1
    prev_i = 0
    while prev_i < len(list_list):
        if list_list != [] and list_list != [[]]:
            if i == prev_i:
                del list_list[i]
                i += 1
            else:
                i_i = 1
                prev_i_i = 0
                while i_i < len(list_list[prev_i]):
                    if i_i == prev_i_i:
                        del list_list[prev_i][i_i]
                        i_i += 1
                    else:
                        prev_i_i += 1
                prev_i = i
            print(list_list)



a = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [0, 7, 8], [1, 3, 5, 6, 9]]
keep_odds_from_odds(a)
