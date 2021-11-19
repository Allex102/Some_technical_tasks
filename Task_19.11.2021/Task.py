def func(N:int,C:int):
    result=[]
    count=0
    for x in range(1,N+1):
        result.append(x)
        length_result=len(result)
        if length_result%C==0:
            print(result[x-C:x],sep='\n')
            count+=1
    if len(result)%C!=0:
        print(result[C*count%len(result):])
