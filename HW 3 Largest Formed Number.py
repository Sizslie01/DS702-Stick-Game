number_list = ['3935','3939','39','38','7','78','8','784','3']
# number_list = ['50','9','8','1']
# for i in range(4):
#     number_list.append(input('Input number {} in number list : '.format(i+1)))
while len(number_list) >0:
    element_delete = [s for s in number_list if s.startswith(max(number_list)[0])]
    # for i in element_delete:
    #     max_num = i
    #     for j in i:
    #
    # max_num = element_delete[0]
    # num_compare = 0
    # k = 0

    number_list = [s for s in number_list if not s.startswith(max(number_list)[0])]

    print(element_delete,number_list)


