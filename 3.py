# with open("inputs/3.txt", "r") as input:
#     lines = input.readlines()
#
# lines[len(lines)-1]+='.'
#
# length = 0
# lines_array = []
# for line in lines:
#     line = line[:-1:]
#     length = len(line)
#     lines_array.append(line)
#
# lines_str = ''.join(lines_array)
#
# symbol_points_str = '0'* len(lines_str)
#
# for i in range(len(lines_str)):
#     if not lines_str[i].isdigit() and lines_str[i]!='.':
#         for j in range(3):
#             try:
#
#                 if lines_str[i+length+j-1].isdigit():
#                     symbol_points_str = symbol_points_str[:i+length+j-1:]+'1'+symbol_points_str[i+length+j::]
#
#                 if lines_str[i-length+j-1].isdigit():
#                     symbol_points_str = symbol_points_str[:i - length + j - 1:] + '1' + symbol_points_str[i - length + j::]
#
#                 if lines_str[i+j-1].isdigit():
#                     symbol_points_str = symbol_points_str[:i+j-1:] + '1' + symbol_points_str[i+j::]
#
#             except:
#                 continue
#
# symbol_array = list(symbol_points_str)
# lines_array = list(lines_str)
#
#
# for i in range(len(lines_array)):
#     k = 0
#     n = 0
#     try:
#         if symbol_array[i+k] == '1':
#             while lines_array[i+k+1].isdigit():
#                 symbol_array[i+k+1] = '1'
#                 k += 1
#
#     except:
#         continue
#
#     try:
#         if symbol_array[i-k] == '1':
#             while lines_array[i-k-1].isdigit():
#                 symbol_array[i-k-1] = '1'
#                 k += 1
#
#     except:
#         continue
#
# final_array = []
#
# for i in range(len(symbol_array)):
#     if (symbol_array[i] == '0' and lines_array[i].isdigit()) or (not lines_array[i].isdigit() and lines_array[i] != '.'):
#         final_array.append('.')
#     else:
#         final_array.append(lines_array[i])
#
# final_str = ''.join(final_array)
# megafinal_str = final_str.split(sep='.')
#
# answer = 0
#
# for k in megafinal_str:
#     if k != '':
#         answer += int(k)
#
# print(answer)



with open("inputs/3.txt", "r") as input:
    lines = input.readlines()

answer = 0

lines_1 = []
for line in lines:
    new_line = []
    for el in line:
        if el != '*' and el.isdigit() == False:
            el = '.'
            new_line.append(el)
        else: 
            el = el
            new_line.append(el)
    lines_1.append(new_line)

lines_2 = []
lines_2.append(['.'] * (len(lines_1[0])+2))
for line in lines_1:
    new_line = ['.'] * (len(line)+1)
    number = ''
    for el_index in range(len(line)):
        if line[el_index].isdigit():
            number += line[el_index]
            if line[el_index + 1].isdigit() == False:
                for i in range(0, len(number)):
                    new_line[el_index - i +1] = number
                number = ''
        else:
            new_line[el_index + 1] = line[el_index]
    lines_2.append(new_line)
lines_2.append(['.'] * (len(lines_1[0])+2))


for line_index in range(1, len(lines_2)):
    for el_index in range(1, len(lines_2[line_index])):
        a = 0
        b = 0
        if lines_2[line_index][el_index] == "*":
            for i in range(0, 3):
                for j in range(0, 3):
                    if lines_2[line_index+i-1][el_index+j-1].isdigit():
                            a = int(lines_2[line_index+i-1][el_index+j-1])
                            if a != b:
                                answer += a*b
                                b = a
print(answer)