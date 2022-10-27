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

print(data[0])

# 建立字典；把出現的字以及次數記錄下來；讓使用者輸入字，查找出現次數
wc = {} # word_count
for d in data: # 從大清單裡面，把一筆一筆留言提取出來
	words = d.split(' ') # 針對每一筆留言，用空格隔開，拆出很多小字串
	for word in words:
		if word not in wc: # 如果沒有出現在字典過，就設定1
			wc[word] = 1
		else:
			wc[word] += 1 # 如果已經出現在字典，就加次數

# 把字典的內容變成一行一行的，只跑出出現次數大於1000000以上的
for word in wc:
	if wc[word] >1000000:
		print(word, wc[word])
print('共出現', len(wc), '個字')

while True:
	look = input('請輸入要查詢的字：')
	if look == 'q':
		break
	if look in wc:
		print('你查詢的字', look, '共出現', wc[look], '次')
	else:
		print('你查詢的字', look, '沒有出現過喔！')
print('感謝使用本查詢功能')