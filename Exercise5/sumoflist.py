def getsum(lists):
	if len(lists)==0:
		return 0
	else:
		return lists[0] + getsum(lists[1:])
print(getsum([1,2,3,4,5,6,7,8,9]))


