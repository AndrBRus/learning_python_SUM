# -*- coding: utf-8 -*-

conditions_numb_list = []    # empty list for numbers that match the conditions

# selection of numbers by conditions in the range [2476, 7857]:
# 1) number multiple of 2, but not multiple of 8
# 2) the second digit from the end of the number doesn't exceed 7
for iter in range(2476, 7858):    # go through the range by iter
    if ((iter % 2 == 0) and (iter % 8 != 0)) and (int(iter % 100 / 10) <= 7):    # check conditions
        conditions_numb_list.append(iter)    # add element for list

# print length of list
print('Number of elements that match the conditions: {};'.format(len(conditions_numb_list)))
# print arithmetic mean of max and min elements (only the whole part) 
print('Arithmetic mean of max and min elements: {}'.format(int((max(conditions_numb_list) + min(conditions_numb_list)) / 2)))