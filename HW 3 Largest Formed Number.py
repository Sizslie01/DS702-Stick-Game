def number_group (list_of_number):
    new_list = []
    list_len = []
    while len(list_of_number) > 0:
        new_list.append([s for s in list_of_number if s.startswith(max(list_of_number)[0])])
        list_len.append(len([s for s in list_of_number if s.startswith(max(list_of_number)[0])]))
        list_of_number = [s for s in list_of_number if not s.startswith(max(list_of_number)[0])]
    return new_list, list_len

def number_sort (group_of_number, list_len):
    sorting = []
    for i in group_of_number:
        
        for m in range(len(i)):
            max_num = '0'
            group_lenght = len(i)
            if group_lenght > 1:
                for j in range(group_lenght):

                    for k in range(min(len(max_num),len(i[j]))):
                        if int(i[j][k]) != int(max_num[k]):

                            max_num = max_num if max_num[k] > i[j][k] else i[j]
                            
                        else:
                            if len(max_num) == min(len(max_num),len(i[j])):
                                
                                if max_num[-1] != i[j][0]: 
                                    max_num = max_num if max_num[-1] > i[j][0] else i[j]
                                else:
                                    max_num = max_num if max_num[0] > i[j][-1] else i[j]
                            else:
                                if i[j][-1] != max_num[0]:
                                    max_num = i[j] if i[j][-1] > max_num[0] else max_num
                                else:
                                    max_num = i[j] if i[j][0] > max_num[-1] else max_num  

                
                sorting.append(max_num)
            else:
                max_num = i[0]
                sorting.append(max_num)
            #print(max_num)
            i = [s for s in i if s!= max_num]
            #print(i)
    return sorting
            
def combine(list_num):
    string = ''
    for i in list_num:
        string += i
    return string

n = int(input('How many n of number that you want to input ? : '))
number_list = []
for i in range(n):
    number_list.append(input('Input number {} in number list : '.format(i+1)))
group , size = number_group(number_list)
print(combine(number_sort(group,size)))