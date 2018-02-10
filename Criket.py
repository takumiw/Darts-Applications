'''
ー仕様ー
入力方法
Single：数字 例. 20, bull
Double：数字の後にd 例. 20d, bulld
Triple：数字の後にt 例. 20t

ー改善点ー
d, tの実装
ポイント加算
18以上の時の対応
'''
def Criket():
	stats = 0
	throw = 0
	criket_number = [0, 0, 0, 0, 0, 0] #[16, 17, 18, 19, 20, 'bull']
	criket_data = []
	point = 0
	while throw <= 19:
		if sum(criket_number) == 18: # ゲーム終了
			print_result(criket_number, throw, input_line)
			print("finish!!: ")
			#print(stats)
			record_data(criket_data, stats)
			break
		#elif sum(criket_number) == 15: # スタッツ算出
		#	stats = 15 / throw
		input_line = input().split() # e.g. 20 19 18
		criket_data.append(input_line)
		for i in input_line:
			for j in range(16, 21):
				if not i == 'bull':
					if i == str(j):
						criket_number[j-16] += 1
			if i == 'bull':
				criket_number[5] += 1
		throw += 1
		print_result(criket_number, throw, input_line)
		
	else:
		print("finish: not clear")
		record_data(criket_data, stats)
	
def print_result(criket_number, throw, input_line):
	for i in range(16, 21):
		if criket_number[i - 16] == 0:
			print(str(i) + ': ')
		elif criket_number[i - 16] == 1:
			print(str(i) + ': ／')
		elif criket_number[i - 16] == 2:
			print(str(i) + ': ×')
		else:
			print(str(i) + ': ○')
		
	if criket_number[5] == 0:
		print('bull: ')
	elif criket_number[5] == 1:
		print('bull: ／')
	elif criket_number[5] == 2:
		print('bull: ×')
	else:
		print('bull: ○')
	print(str(throw) + '\'s throw')
	print()
	#print(criket_number)
	#print(input_line)

def record_data(criket_data, stats):
	from datetime import datetime
	time = datetime.now()
	year, month, day, hour, minute = time.year, time.month, time.day, time.hour, time.minute
	time = str(year) + str(month) + str(day) + str(hour) + str(minute)
	output_file_name = 'C:\\Users\\ics\\Documents\\darts_data\\criket_result_' + time + '.txt'
	output_file = open(output_file_name, 'w')
	output_file.write(time + '\n')
#	output_file.write(str(stats))
	for data in criket_data:
		output_file.write(str(data) + '\n')
	output_file.close()