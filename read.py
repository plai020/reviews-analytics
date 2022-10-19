#留言分析程式
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #每讀取一筆，count就加1
		if count % 1000 == 0: #每一千筆print一次
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

#計算留言平均長度
#字串可以求長度，把每一個字串的長度加總存到sum_len
sum_len = 0
for d in data:
	sum_len += len(d)

#計算平均長度
average = sum_len / len(data)
print('留言的平均長度為', average)

#篩選留言長度小於100的清單
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言的長度小於100')
