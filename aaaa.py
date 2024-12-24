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
