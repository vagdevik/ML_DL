inp_file = open('../../Deep-Learning-/Text_Classification/category_headlines.csv','r')
f=open("data.txt",'w')
flag=0
data = []

for line in inp_file:
	break
for line in inp_file:
	split = line.split(',')
	string = "__label__"+split[0]+" "+split[1]
	data.append(string)
	f.write(string)
f.close()
inp_file.close()	 

train_size = int(len(data)*.8)

train_data = data[:train_size]
test_data = data[train_size:]

f=open("train_data.txt",'w')
for line in train_data:
	f.write(line)
f.close()

f=open("test_data.txt",'w')
for line in test_data:
	f.write(line)
f.close()
