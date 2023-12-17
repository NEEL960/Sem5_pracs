import random
def selected(li):
    dec=list(map(lambda x: int(x,2),li))
    fit=list(map(lambda x: x*x,dec))
    s=sum(fit)
    prob=list(map(lambda x:round(x/s,3),fit))
    avg=s/n
    exe=list(map(lambda x:round(x/avg,3),fit))
    ac=list(map(lambda x: round(x),exe))

    return dec,fit,prob,exe,ac


def pp(li,ac,n):
    co=[]
    temp=[]
    index=[]
    for i in range(n):
        if ac[i]==1:
            co.append(li[i])
        elif ac[i]>=2:
            for j in range(ac[i]-1):
                temp.append(li[i])
            co.append(li[i])  
        elif ac[i]==0 and len(temp)!=0:
            co.append(temp[0])  
            temp.pop(0)     
        elif ac[i]==0 and len(temp)==0:
            index.append(i)  

    return co    

def cr(x):
    s=0
    for i in x:
        if i=='1':
            s=s+1
    return s        

def crossover(li,n):
    crossed=[]
    for i in range(0,n,2):
        temp1=li[i]
        j=i+1
        temp2=li[j]     
        crosspoint=cr(temp1)  
        print("The crosspoint for pair " + str(i) + " is " + str(crosspoint))
        temp3=temp1[crosspoint:]
        temp4=temp2[crosspoint:]
        temp1=temp1[0:crosspoint]+temp4
        temp2=temp2[0:crosspoint]+temp3
        crossed.append(temp1)
        crossed.append(temp2)

    return crossed    

def mutation(li,n):
    mut=[]
    for i in li:
        j=random.randint(0,n-1)
        print("For pair " + str(i) + ", the bit that will be changed is " + str(j))
        if i[j]=='1':
            i=i[0:j]+'0'+i[j+1:]
            mut.append(i)
        elif i[j]=='0':
            i=i[0:j]+'1'+i[j+1:]
            mut.append(i)   
    return mut    

n=int(input("Enter the number of samples"))
sam=[]
for i in range(n):
    sam.append(input("Enter gene: "))   #has to be string so int()can be used to conver to decimal

crossed=sam.copy()

m=int(input("Enter the number of generations:"))

for i in range(m):
    dec,fit,prob,exe,ac=selected(crossed)
    s=sum(ac)
    if s<n:
        maxi=max(ac)
        k=ac.index(maxi-1)
        ac[k]+=1

    if s>n:
        maxi=max(ac)   
        k=ac.index(maxi)
        ac[k]-=1
    print(f"\n------------------------------------Generation {i}------------------------------------------------")     
    print("Samples\t\tX value\t\tFitness\t\tProbability\tExpected\t\tActual\t\t")
    for j in range(n):
         print(f"{crossed[j]}\t\t{dec[j]}\t\t{fit[j]}\t\t{prob[j]}\t\t{exe[j]}\t{ac[j]}")
    co=pp(crossed,ac,n)
    print(f"\nSamples selected for crossover :{co}")    
    cross=crossover(co,n) 
    print(f"Samples after crossover :{cross}") 
    mut=mutation(cross,n)
    print(f"Samples after mutation :{mut}") 

print("\nGENERATION ", (m + 1), " - ", mut)

# ----------------------------------------------------------------------------------------------------------------------------

import random
gene = ['01101', '11000', '01000', '10011']
def selection(gene):
    x=[]
    for i in gene:
        x.append(int(i,2))
    fx=[]
    for i in x:
        fx.append(i*i)
    fx_sum = sum(fx)
    fx_avg = fx_sum // len(fx)
    expected_count=[]
    for i in fx:
        expected_count.append(round((i / fx_avg), 4))
    actual_count=[]
    for i in expected_count:
        actual_count.append(round(i))

    mate_pool = []
    for i, j in zip(actual_count, gene): 
        if i:
            for c in range(i):
                mate_pool.append(j)
    return x, fx, fx_sum, fx_avg, expected_count, actual_count, mate_pool
def generate_mate(size, mate_element_size):
    if size % 2 != 0:
        return -1
    available_positions = list(range(size)) #[0,1,2,3]
    random.shuffle(available_positions) # [2,3,0,1]
    mate = [-1] * size # [-1,-1,-1,-1]
    for i in range(size):
        if mate[i] == -1:  #i=0
            j = random.choice(available_positions) #j=1
            while mate[j] != -1 or j == i:              #crossover ke pehle check kar rhe mate virgin hai ki nhi
                j = random.choice(available_positions)
            mate[i] = j #mate will be [1,-1,-1,-1]
            mate[j] = i #mate will be [1,0,-1,-1]
            available_positions.remove(i) # nikaal do kyuki unka pair ban gaya and kisi aur ke saath nhi ban sakta vaapas
            available_positions.remove(j)
    #upar wala loop khatam hoga tab tak apne paas mate mein pairs mil jaaenge
    crossover = [-1] * size #[-1,-1,-1,-1]
    for i in mate:
        if crossover.count(-1) != 0:
            crossover[i] = crossover[mate[i]] = random.randint(1, mate_element_size - 1)
    return mate, crossover
def crossover(mate_pool):
    mate, crossover_points = generate_mate(len(mate_pool), len(mate_pool[0]))
    new_poplu = [-1] * len(mate_pool)
    for i in mate:
        new_poplu[i] = mate_pool[i][:crossover_points[i]] + mate_pool[mate[i]][crossover_points[i]:]
        #mate_pool=01101 crossover_point=4  0110+  left wale ka jo bhi mate hai uska baaki ka part concat kardo
    x=[]
    for i in new_poplu:
        x.append(int(i, 2))
    fx=[]
    for i in x:
        fx.append(int(i) * int(i))
    return mate_pool, new_poplu, mate, crossover_points, x, fx
def GA(gene, iter, n):
    if iter == 0:
        return
    x, fx, fx_sum, fx_avg, expected_count, actual_count, mate_pool = selection(gene)
    if sum(actual_count) != len(gene):
        print("Error: Don't know what to do in this situation")
        return
    print(f"\n------------------------------------------------- GENERATION {n} --------------------------------------------------")
    print("Initial Population\tX Value\t\tFitness Value( f(x) )\tProbability(Expected Count)\tActual Count")
    print(f"-----------------------------------------------------------------------------------------------------------------")
    for i in range(len(gene)):
        print(f"{gene[i]}\t\t\t{x[i]}\t\t{fx[i]}\t\t\t{expected_count[i]}\t\t\t\t{actual_count[i]}")
    mate_pool, new_poplu, mate, crossover_points, x, fx = crossover(mate_pool)
    print(f"\n----------------------------------------------- New Population {n} ------------------------------------------------")
    print("Mate Pool\tMate\t\tCrossover Points\tNew Population\t\tx value\t\tf(x)")
    print(f"-----------------------------------------------------------------------------------------------------------------")
    for i in range(len(gene)):
        print(f"{mate_pool[i]}\t\t{mate[i]}\t\t{crossover_points[i]}\t\t\t{new_poplu[i]}\t\t\t{x[i]}\t\t{fx[i]}")
    GA(new_poplu, iter - 1, n + 1)
GA(gene, 3, 0)