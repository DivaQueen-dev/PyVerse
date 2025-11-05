# matrix m*n elem22ents in zig zag row wise pattern 
# even rows ==> left-->right
# odd rows:right-->left
rows,columns = map(int,input().split())
matrix =[]
for i in range(rows):
    row = list(map(int,input().split()))
    if(len(row)!=columns):
        print("enter valid no of elements")
    matrix.append(row)
for i in range(rows):
    if(i%2==1):
        matrix[i] = matrix[i][::-1]
for row in matrix:
    print(*row)


