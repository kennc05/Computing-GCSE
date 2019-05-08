def triangle(size):
    spaces=""
    stars=""
    line=""

    for i in range(0,size):
        for j in range(0,(size-1-i)+11-(size-1-i)-i): 
            line=line+" "

        for k in range(0,2*i+1):
            line=line+"*"

        print(line)
        line=""

triangle(2)
triangle(3)
triangle(4)
