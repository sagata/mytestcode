data_list = []
data_list.append({'softname':'1','version':'1.2.2.2'})
data_list.append({'softname':'7','version':'1.2.2.2'})
data_list.append({'softname':'5','version':'1.2.2.2'})
data_list.append({'softname':'2','version':'1.2.2.2'})
data_list.append({'softname':'3','version':'1.2.2.2'})
data_list.append({'softname':'9','version':'1.2.2.2'})

data_list.sort(key=lambda obj:obj.get('softname'), reverse=False)
for each in data_list:
	print each['softname']










L = [('b',6),('a',1),('c',3),('d',4)]
L.sort(lambda x,y:cmp(x[1],y[1])) 
print L
test = [1,2,3,4,5]
test = [str(i) for i in test]
print ','.join(test)


test = {'test':'233'}

if 'test1' in test and test['test'] == '233':
	print 'yes'