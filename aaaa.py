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
##################################################
f=open('scores.txt', 'r')
games=[] 
for line in f:
    L=line.split()
    games.append([L[1],int(L[2]),L[3],int(L[4])]) 
# print(games)
d={}    
for team1,score1,team2,score2 in games:
    if team1 not in d:
        d[team1]={'win':0, 'loss':0,'my_score':0,'against_score':0}
    if team2 not in d:
        d[team2]={'win':0, 'loss':0,'my_score':0,'against_score':0}
    d[team1]['my_score']+=score1
    d[team1]['against_score']+=score2
    d[team2]['my_score']+=score2
    d[team2]['against_score']+=score1
    if score2>score1:
        d[team2]['win']+=1
        d[team1]['loss']+=1
    else:
        d[team1]['win']+=1
        d[team2]['loss']+=1
count=1        
for i,j in d.items():
    if (j['win']>j['loss']) and (j['my_score']<j['against_score']):
        print(count,i)
        count+=1                    
for i,j in d.items():
    if  (sum(j)/len(j))>=70:
        print(i,sum(j)/len(j))
###################################################################

