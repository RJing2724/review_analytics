# python3 reviews.py

data = []
count = 0 #设一项计数
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		#以下是使终端运行1000项print一次
		count += 1 #count = count +1
		if count % 1000 == 0: 	# %用来求余数，例如7 % 3 = 1
								# 在此是指count可以被1000整除
		#若没有这一段，则会每次都运行
			print(len(data))
print('The document has', len(data), 'data in total.')

print('-------------')

#现在请算出平均长度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('The average length is', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new), 'data that has length < 100.')




#print(data[0].strip()) # print清单的第0个位置
#print('-------------')
#print(data[1])