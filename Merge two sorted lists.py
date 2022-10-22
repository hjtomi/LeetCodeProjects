def merge(list1, list2):
    new_list = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            new_list.append(list1[0])
            del(list1[0])
        elif list1[0] > list2[0]:
            new_list.append(list2[0])
            del (list2[0])
        elif list1[0] == list2[0]:
            new_list.append(list1[0])
            new_list.append(list2[0])
            del(list1[0])
            del (list2[0])

    if len(list1) > 0:
        for num in list1:
            new_list.append(num)
    elif len(list2) > 0:
        for num in list2:
            new_list.append(num)

    return new_list

print(merge([1,3,5,7,9], [1,4,6,9]))
