'''l=[8,1,3,0,5,3]
print(sorted(l))
print(l)
print(l.sort())
print(l)'''

'''l=['abc','df','sdfg','sdg','z']
l.sort(key=len)
print(l)'''

l=[[2,3,4],[5,6],[0,9],[1,0,3],[4,5]]
l.sort(key=lambda a:a[0]+a[1],reverse=True)
print(l)