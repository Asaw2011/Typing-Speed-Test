from time import time
import random


words=["sense","planes","position","circle","vase","nation","fruit","advertisment","cat","harbor","cakes","use","brother","bike","example","playground","lettuce","smile","summer","dress","vest","nest","protest","deer","rail","suit","look","hour","planets","strech","governor","sail","hope","hair","python","coding"]

sentance = ""

for i in range(10):
    rand = random.choice(words)
    sentance+= rand+" "


print("->", sentance)
start=time()
typing=input("-> ")
stop=time()
time_taken=round(stop-start)
characters=len(typing)
cps=characters/time_taken
print("Your cps is",cps)
minutes=time_taken/60
cpm=characters/minutes
print("Your cpm is ", cpm)
wpm=cpm/4.7
wpm_approximate=round(wpm)
print("Your approximate wpm is", wpm_approximate)
correct=0
for i in range(min(len(),len(typing))):
    

    if sentance[i]==typing[i]:
        correct+=1
        acc=(correct/len(sentance))*100
print("Your accuracy is",acc,"%")

