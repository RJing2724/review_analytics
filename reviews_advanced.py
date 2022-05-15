# reviews_advanced.py

data = []
count = 0 #设一项计数
with open('reviews.txt', 'r') as f:
	for line in f: # 每一笔review中的字串data为line
		data.append(line)
		# 以下是使终端运行1000项print一次
		count += 1 #count = count +1
	if count % 1000 == 0: 	# %用来求余数，例如7 % 3 = 1
								# 在此是指count可以被1000整除
		# 若没有这一段，则会每次都运行
		print(len(data))

# 以上写完之后data这个list里面就装着所有的留言

print(data[0])

word_count = {}
# 多个loop套在一起叫做nested for loop
for d in data:	# data清单中的每一笔留言
	words = d.split()	# 将每一笔留言都按照空格分割，并存入words清单
	for word in words:	# words中的每一个被分割后的清单，现在是一个个的单词
		if word in word_count:	# 如果word在字典中出现过
			word_count[word] += 1
			# word_count[word] 就是从字典中查找单词，来找对照的数字, 也就是{key:value}
			# 此处word_count[word]输出的是数字
		else:
			word_count[word] = 1
			# 如果word没出现在字典中，就写入字典并计数1次(注意这里要用字典的写入方式)
# 直接输出后会发现，由于整个list是由空格切割的，
# 所以单词后跟着标点符号会被当作一整个单词

for word in word_count: # 将每一笔单行列出
	if word_count[word] > 1000000:
		print(word, word_count[word])
			#(key,	value)

print(word_count['Allen'])	# 直接从字典中查找Allen这个词

while True:
	word = input('Please enter the word you would like to search:')
	if word in word_count:
		print(word, 'has occured in message for', word_count[word], 'times.' )
	else:	
		print('The word you entered does not exist in message.')

	if word == 'q':
		print('Thank you for using the program...')
		break









