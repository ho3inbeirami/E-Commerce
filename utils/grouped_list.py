
def group_list(custom_list: list, size:int):
    grouped_list = []
    for i in range(0,len(custom_list),size):
        grouped_list.append(custom_list[i:i+4])
    return grouped_list