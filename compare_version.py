def compare_version(ver_1, ver_2):
    ver_list_1 = ver_1.split('.')
    ver_list_2 = ver_2.split('.')
    if int(ver_list_1[0]) > int(ver_list_2[0]):
        return 1
    elif int(ver_list_1[0]) < int(ver_list_2[0]):
        return -1
    else:
        if int(ver_list_1[1]) > int(ver_list_2[1]):
            return 1
        elif int(ver_list_1[1]) < int(ver_list_2[1]):
            return -1
        else:
            return 0    
    

compare_version("0.1", "0.2")