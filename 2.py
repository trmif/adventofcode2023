with open("inputs/2.txt", "r") as input:
    lines = input.readlines()


def solve1(lines):
    answer = 0

    for line in lines:

        separated_colon = line.split(sep=':')
        id = separated_colon[0].split(sep=' ')[1]
        balls_outputs = separated_colon[1].split(sep=';')
        flag = 0

        for part in balls_outputs:
            part_array = part.split(',')

            r = 0
            g = 0
            b = 0

            for color in part_array:

                if color.find('blue') != -1:
                    b += int(color[1:color.find('blue') - 1])
                if color.find('red') != -1:
                    r += int(color[1:color.find('red') - 1])
                if color.find('green') != -1:
                    g += int(color[1:color.find('green') - 1])

            if r <= 12 and g <= 13 and b <= 14:
                flag += 1

        if flag == len(balls_outputs):
            answer += int(id)

    return answer


def solve2(lines):
    answer = 0

    for line in lines:

        separated_colon = line.split(sep=':')
        id = separated_colon[0].split(sep=' ')[1]
        balls_outputs = separated_colon[1].split(sep=';')

        r_start = 0
        g_start = 0
        b_start = 0

        for part in balls_outputs:
            part_array = part.split(',')
            for color in part_array:

                if color.find('blue') != -1:
                    b = int(color[1:color.find('blue') - 1])
                    if b>=b_start:
                        b_start = b
                if color.find('red') != -1:
                    r = int(color[1:color.find('red') - 1])
                    if r>=r_start:
                        r_start = r
                if color.find('green') != -1:
                    g = int(color[1:color.find('green') - 1])
                    if g>=g_start:
                        g_start = g

        power = r_start*g_start*b_start

        answer+=power

    return answer

print(solve1(lines))
print(solve2(lines))
