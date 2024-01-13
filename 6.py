race = open("inputs/6.txt").read().split("\n")
time = [x for x in race[0].split(" ") if(x.isdigit())]
dsnc = [x for x in race[1].split(" ") if(x.isdigit())]    
    
def foo(time, dsnc):
    count = 0
    h_time = time//2
    new_dsnc = (time - h_time) * h_time

    while new_dsnc>=dsnc and h_time>0:
        h_time -= 1
        new_dsnc = (time - h_time) * h_time
        count+=1
    return count*2-1

answer1 = 1
for i in range(len(time)):
    answer1 *= foo(int(time[i]), int(dsnc[i]))

time_total = ''
dsnc_total = ''

for i in range(len(time)):
    time_total += time[i]
    dsnc_total += dsnc[i]
    

    
print(answer1)
print(foo(int(time_total), int(dsnc_total)))