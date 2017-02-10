import itertools
def join(L,k):
    C=set()
    for i in L:
        for j in L:
            X=set(i)|set(j)
            new=itertools.combinations(X,k)
            for r in new:
                rr=tuple(sorted(r))
                C.add(rr)
    return C
def apriori() :
    
    file = open("data/test.dat","r")
    fw = open("output.txt","w")
    data = file.readlines();
    freq = {};
    bucket = set();
    for strings in data :
        for c in strings.split():
            if(int(c) in bucket):
                freq[int(c)] += 1
            else :
                bucket.add(int(c))
                freq[int(c)]=1
    print(freq)
    min_support = 2 #raw_input("enter minimum support : ");
    min_conf = 0.5 #raw_input("enter minimum confidence : ");
    k=1
    L=set()
    for i in bucket:
        if(freq[i] >= min_support) :
            S = tuple([i])
            freq[S]=freq[i]
            L.add(S)
    for r in L:
        fw.write(str(r)+"\n")
    FL = []
    while(1) :
        k+=1 
        if(len(L)==0): break 
        C = join(L,k)
        C1=set()
        for r in C:
            rr=set(r)
            count = 0
            for strings in data:
                num=set()
                for c in strings.split():
                    num.add(int(c))
                if(rr.issubset(num)):
                    count+=1
            freq[r]=count
            if(count >= min_support):
               C1.add(r)
        C2=set()
        for r in C1:
            new=itertools.combinations(r,k-1)
            flag=1
            for x in new:
                y=tuple(sorted(x))
                if(y not in L):
                    flag=0;
                    break;
            if(flag==1):
                C2.add(r)
        L=C2
        for r in L:
            FL.append(r)
            fw.write(str(r)+"\n")
    ans=[]
    for r in FL:
        t=len(r)
        for i in range(1,t):
            new=itertools.combinations(r,i)
            for subset in new:
                temp = freq[r]/freq[subset]
                if(temp >= min_conf):
                    ans.append(tuple([set(subset),set(r)-set(subset),temp]))

    fw.write("\n\nAssociation Rules :\n\n")
    for r in ans:
        fw.write(str(r[0])+"    ---->   "+str(r[1])+"    confidence : "+str(r[2])+"\n")
    return

apriori()
