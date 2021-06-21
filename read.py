data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:  # % 用來求餘數，用1000除餘數等於0(print非常花時間)
			print(len(data))		
print(len(data))
print(data[0])
print('----------------------')
print(data[3])