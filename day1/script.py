sum = 0

with open('./data.txt') as f:
    for line in f.readlines():
        numbers = [c for c in line if c.isnumeric()]
        # print(numbers[0] + numbers[-1])
        sum += (int)(numbers[0] + numbers[-1])

print(sum)