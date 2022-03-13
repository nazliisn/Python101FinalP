print("Task 1")
resultList = []
def foo(l):
    for i in l: 
        if type(i)==list:
            foo(i)
        else:
            resultList.append(i)

foo([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(resultList)

print("-----------------------------------")
print("Task 2")
def reverse(l):
    l.reverse()
    secList=[]
        
    for i in range(len(l)):
        l[i].reverse()
    
    print(l)

reverse([[1, 2], [3, 4], [5, 6, 7]])
