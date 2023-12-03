with open('d:\\work\\Advent_Of_Code_2023\\1_input.txt') as f:
    lines = f.read().splitlines()
#print(lines)
total = 0
for line in lines:

    first = None
    last = None
    f = 0
    l = -1
    while first is None:
        if line[f].isdigit():
            
            first = int(line[f])
        f += 1
    while last is None:
        if line[l].isdigit():
            
            last = int(line[l])
        l -= 1
    total+= first*10 + last
  
print(total)
#55172-answer part 1


#--------------------PART 2--------------------
total = 0
seq = ['one','two','three','four','five','six','seven','eight','nine']
seq_values = [1,2,3,4,5,6,7,8,9]
run =3
for line in lines:
    ans = []
    #print(line)
    n=0
    for i in range(len(line)):
        
        #print(ans)
        #print('n:',n)
        if line[n].isdigit():
            ans.append(int(line[n]))
        if line[n:n+3] in seq:
            #print('three:',line[n:n+3])
            idx = seq.index(line[n:n+3])
            ans.append(seq_values[idx])
        if line[n:n+4] in seq:
            #print(line[n:n+4])
            idx = seq.index(line[n:n+4])
            ans.append(seq_values[idx])
        if line[n:n+5] in seq:
            #print(line[n:n+5])
            idx = seq.index(line[n:n+5])
            ans.append(seq_values[idx])
        
        n+=1
    total += ans[0] * 10 + ans[-1]
print(total)