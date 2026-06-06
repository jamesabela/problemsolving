import random  
Choose_Name = ["James","John","Mark","Rick"]  
for i in range(1,5):  
   chosen = random.choice(Choose_Name)  
   print(chosen)  
   Choose_Name.remove(chosen)
