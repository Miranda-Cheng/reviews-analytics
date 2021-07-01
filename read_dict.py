data = []
count = 0
with open('reviews.txt', 'r', encoding = 'utf-8') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))		
print('檔案讀取完了!總共有', len(data), '筆資料')

# 文字計數

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度是', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '筆留言長度小於100')
print(new[3])

good = []
for d in data:
	if 'good' in d:
		good.append(d)  # 以上四行快寫法, good = [d for d in data if 'good' in d]
print(good[5])
# good = [d for d in data if 'good' in d]
# 第一個d代表原封不動地把它裝進去good清單(代表good.append(d)的d)
# 也可以裝1 或是布林值
bad = ['bad' in d for d in data]
print(bad)

#練習字典

word_count = {}
for d in data:
	words = d.split()   # split()預設就是空白鍵，切割時如果遇到很多的空白鍵，會自動忽略，不會切成空字串
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

for word in word_count:
	if word_count[word] > 1000000:
		print(word, word_count[word])

print(len(word_count))
print(word_count['Miranda'])

while True:
	word = input('請問你想查什麼字:')
	if word == 'q':
		break
	if word in word_count:
		print(word, '出現過的次數為:', word_count[word])
	else:
		print('這個字沒有出現過哦')
print('感謝使用本查詢功能')