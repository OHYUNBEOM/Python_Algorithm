grid=[]
for _ in range(5):
    grid.append(input()) #['ABCDE','abcde',01234,'FGHIJ','fghij']

for i in range(15):#최대15글자
    for j in range(5):#5줄
        if i<len(grid[j]):
            print(grid[j][i],end='')