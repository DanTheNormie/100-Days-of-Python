with open("file_1.txt") as file1:
    file_1_list = file1.readlines()
with open("file_2.txt") as file2:
    file_2_list = file2.readlines()

common_num_list = [int(num) for num in file_1_list if num in file_2_list]

print(common_num_list)


