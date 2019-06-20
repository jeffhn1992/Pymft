from statistics import mean

list_test = [2, 34, 12, 213, 43, 546, 7, 12, 1, 8]
ave = sum(list_test)/ len(list_test)
print(ave)
mean_list = mean(list_test)
print(mean_list)

reverse_list = list_test[::-2]

first_list = list_test[:5]
second_list = list_test[5::-1]
third_list = first_list + second_list
print(first_list, second_list)
print(third_list)