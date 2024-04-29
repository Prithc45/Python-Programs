name="Prith"
print(name)
name1='Chouhan'
print(name1)
#Srting lines with conversation Exaple:
ex='''hey how are you?
I'm "good", what about you?
I'm also "good" thank you.'''
print(ex)
#Indexing
name2='Addon'
print(name2[0],end="")
print(name2[4],end="")
print(name2[2],end="\n")
#by forloop
ex1='Nothing'
for charecters in ex1:
    print(charecters,end="")
#String slashing
name3="Prith"
print("\n"+name3[0:5])#0 include but not 5 it's <5 nit <=5;;
print(name3[:3])
#nagative slashing
name4="chouhan"
print(name4[-4:-2])
'''logic:
length(name4)-4:length(name4)-2
7-4:7-2
3:5
therefor, name4[3:5] will be printed'''
#length functin (len())
print(len(name4))