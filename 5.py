# seeds, *blocks = open("inputs/5.txt").read().split('\n\n')

# seeds = list(map(int, seeds.split(':')[1].split()))

# for block in blocks:
#     ranges = []
#     for line in block.splitlines()[1::]:
#         ranges.append(list(map(int, line.split())))
    
#     new = []

#     for seed in seeds:
#         for a, b, c in ranges:
#             if b <= seed <= b+c:
#                 new.append(seed-b+a)
#                 break
#         else:
#             new.append(seed)
        
#     seeds = new

# print("Part 1:", min(seeds))

seeds, *blocks = open("inputs/5.txt").read().split('\n\n')

seeds = list(map(int, seeds.split(':')[1].split()))

seeds_new = []
for i in range(0, len(seeds)-1, 2):
    seeds_seq = []
    seeds_seq.append(seeds[i])
    seeds_seq.append(seeds[i+1]+seeds[i])
    seeds_new.append(seeds_seq)

print(seeds_new)

for block in blocks:
    ranges = []
    for line in block.splitlines()[1::]:
        ranges.append(list(map(int, line.split())))
    
    new = []

    for seed in seeds_new:
        for a, b, c in ranges:
            if b <= seed <= b+c:
                new.append(seed-b+a)
                break   
        else:
            new.append(seed)
        
    seeds_new = new

print(min(seeds_new))