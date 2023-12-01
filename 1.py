with open("1.txt", "r") as input:
    lines = input.readlines()


def solve(array):
    lines = array
    digit_array = []
    for line in lines:
        digits_in_line = ''
        for literal in line:
            if literal.isdigit():
                digits_in_line += literal
        digit_array.append(digits_in_line)

    answer = 0

    for i in digit_array:
        start = i[:1:]
        end = i[-1::]
        try:
            full_digit = start+end
        except:
            continue
        answer += int(full_digit)

    return answer


def translate_array(lines):
    digits_literals = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    translated_array=[]

    for line in lines:
        left_dict = {}
        right_dict = {}
        for digital_literal in digits_literals:
            index_left = line.find(digital_literal)
            index_right = line.rfind(digital_literal)
            if index_left != -1:
                left_dict[index_left] = digital_literal
            if index_right != -1:
                right_dict[index_right] = digital_literal
        if sorted(left_dict.items(), key=lambda item: item[0]):
            sorted_index_left_dict = sorted(left_dict.items(), key=lambda item: item[0])
        else:
            translated_array.append(line)
            continue
        if sorted(right_dict.items(), key=lambda item: item[0]):
            sorted_index_right_dict = sorted(right_dict.items(), key=lambda item: item[0])
        else:
            translated_array.append(line)
            continue
        if sorted_index_left_dict[0][1]:
            sorted_index_start = sorted_index_left_dict[0][1]
        else:
            continue
        line = line.replace(sorted_index_start, digits_literals[sorted_index_start])
        if sorted_index_right_dict[-1][1]:
            sorted_index_end = sorted_index_right_dict[-1][1]
        else:
            continue
        line = line.replace(sorted_index_end, digits_literals[sorted_index_end])
        translated_array.append(line)


    return translated_array

translated_lines = translate_array(lines)

print(solve(lines)) # решение первой
print(solve(translated_lines)) # решение второй