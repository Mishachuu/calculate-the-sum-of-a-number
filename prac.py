
def function(mass):
    if (len(mass)==1): return None
    min_ind=0
    for i in range(len(mass)-1):
        if mass[min_ind]>mass[i]: min_ind=i
    mass[min_ind]+=1
    mass[-1]-=1
    part_sum=sum(mass[min_ind+1::])
    return mass[0:min_ind+1]+[1 for i in range(part_sum)]
    
def counting(n):
    counts=0
    mass=[1]*n
    while mass is not None:
        counts+=1
        mass=function(mass)
    print(counts)
        
def main():
    n=int(input())
    counting(n)
        
if __name__ == "__main__":
    main()       
    