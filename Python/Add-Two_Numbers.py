def add_two_numbers(l1,l2):
    flag = False
    result = []
    while len(l1) < len(l2):
        l1.insert(0,0)
    while len(l2) < len(l1):
        l2.insert(0,0)

    for i in range(1,len(l1)+1):
        if flag == False:
            curr_num = l1[-i] + l2[-i]
            if curr_num >= 10:
                if i == len(l1):
                    list_num = []
                    curr_num = str(curr_num)
                    for num in curr_num:
                        list_num.append(int(num))
                    flag = True
                    result.insert(0, list_num[-1])
                    result.insert(0,1)

                else:
                    list_num = []
                    curr_num = str(curr_num)
                    for num in curr_num:
                        list_num.append(int(num))
                    flag = True
                    result.insert(0,list_num[-1])

            else:
                result.insert(0, curr_num)
        else:
            curr_num = l1[-i] + l2[-i]+1
            if curr_num >= 10:
                if i == len(l1):
                    list_num = []
                    curr_num = str(curr_num)
                    for num in curr_num:
                        list_num.append(int(num))
                    flag = True
                    result.insert(0, list_num[-1])
                    result.insert(0, 1)

                else:
                    list_num = []
                    curr_num = str(curr_num)
                    for num in curr_num:
                        list_num.append(int(num))
                    flag = True
                    result.insert(0, list_num[-1])

            else:
                result.insert(0, curr_num)
    return result
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print(add_two_numbers(l1,l2)[::-1])
