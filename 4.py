# with open("inputs/4.txt", "r") as input:
#     lines = input.readlines()

# lines_our = []
# lines_correct = []
# for line in lines:
#     line = line.strip()
#     new_line = line.split(sep = ':')
#     new_line = new_line[1].split(sep = '|')
#     new_line_our = new_line[0].split(sep = ' ')
#     new_line_correct = new_line[1].split(sep = ' ')
#     new_line_our = [x for x in new_line_our if x]
#     new_line_correct = [x for x in new_line_correct if x]
#     lines_our.append(new_line_our)
#     lines_correct.append(new_line_correct)

# answer = 0

# for line_index in range(len(lines_our)):
#     k = 0
#     for our_index in range(len(lines_our[line_index])):
#         for correct_index in range(len(lines_correct[line_index])):
#             if lines_our[line_index][our_index] == lines_correct[line_index][correct_index]:
#                     k += 1
#     print(k)
#     k = 0

with open("inputs/4.txt", "r") as input:
    lines = input.readlines()


lines_our = []
lines_correct = []
for line in lines:
    line = line.strip()
    new_line = line.split(sep = ':')
    new_line = new_line[1].split(sep = '|')
    new_line_our = new_line[0].split(sep = ' ')
    new_line_correct = new_line[1].split(sep = ' ')
    new_line_our = [x for x in new_line_our if x]
    new_line_correct = [x for x in new_line_correct if x]
    lines_our.append(new_line_our)
    lines_correct.append(new_line_correct)

answer = 0
matches = []

for line_index in range(len(lines_our)):
    k = 0
    for our_index in range(len(lines_our[line_index])):
        for correct_index in range(len(lines_correct[line_index])):
            if lines_our[line_index][our_index] == lines_correct[line_index][correct_index]:
                    k += 1
    matches.append(k)

print(matches)

answer_list = [1]* len(lines_our)

for i in range(len(lines_our)):
    adv_indexes = matches[i]
    for j in range(1, adv_indexes+1):
        answer_list[i+j] = answer_list[i+j]+answer_list[i]

print(sum(answer_list))








# answer = 0

# def number_counter(n):
#     global answer
#     if n == 1:
#         return 1
#     else:
#         for i in range(n):
#             if matches[i] >= 0 and matches[i]>=n:
#                 answer += matches[i] - n + 1
#                 print(n, i, matches[i])
#                 print(matches[i] - n + 1)
                
            
#     return number_counter(n-1)

# for n in range(1,len(lines_our)):
#     number_counter(n)
# print(answer + len(lines_our))

