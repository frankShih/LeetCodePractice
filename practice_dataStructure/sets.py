
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
print(Days)
 
Days.add("Sun")
print(Days)

Days.discard("Sun") #better than remove(), no exception
print(Days)

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
print(DaysA | DaysB) #union
print(DaysA & DaysB) #intersect
print(DaysA - DaysB) #diff
print(DaysA >= DaysB) #subset/superset

