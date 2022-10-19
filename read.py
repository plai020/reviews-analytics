#留言分析程式
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #每讀取一筆，count就加1
		if count % 1000 == 0: #每一千筆print一次
			print(len(data))
print(len(data))
print(data[0])
print('------------------')
print(data[1])