from collections import Counter

a = input("Enter string: \n")
b = a.lower().replace(' ','')

counter = Counter(b)
c = counter.most_common(len(b))
most_repeated = []

for i in c:
    if c[0][1] == i[1]:
        most_repeated.append(i[0])

if len(most_repeated) > 1:
    print('The most common characters are ', end="")
    for i in most_repeated:
        print(i[0], end=" ")
    print('with ' + str(c[0][1]) + ' repetitions.')
else:
    print('The most common character is '+ str(most_repeated[0]) + ' with ' + str(c[0][1]) + ' repetitions.')
