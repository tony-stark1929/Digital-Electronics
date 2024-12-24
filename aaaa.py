f=open('scores.txt')
l=[]
cont=0
for line in f:3
    detail=line.split()
    l.extend([int(detail[2]),int(detail[4])])
    cont+=1
print(f"Avg points is{sum(l)/cont}")
#  ########
my_team=input("enter the name of the team:")
loss=0
won=0
for line in f:
    l=line.split()
    if l[1] == my_team:
        if int(l[2])>int(l[4]):
            won += 1
        else :
            loss += 1
    if l[3] == my_team:
        if int(l[4])>int(l[2]):
            won += 1
        else:
            loss += 1
print(won,loss)

# ##################
d={}
for line in f:
    l=line.split()
    if (int(l[2]))-int(l[4])>=30:
        d[l[3]]=d.get(l[3],0)+1
    if (int(l[4])-int(l[2]))>=30:
        d[l[1]]=d.get(l[1],0)+1
# print(d)
k=list(d.items())
k.sort(key=lambda x:x[1],reverse=True)
print(k[0][0],k[0][1])
###############################################
d={}
cont=0
for line in f:
    l=line.split()
    d[l[1]]=d.get(l[1],[])+[int(l[2])]
    d[l[3]]=d.get(l[3],[])+[int(l[4])]
print(d)
for i,j in d.items():
    if  (sum(j)/len(j))>=70:
        print(i,sum(j)/len(j))
###################################################################

