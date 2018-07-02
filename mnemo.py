# coding: utf8
what_do_you_want = str(input("What kind of training do you want?\n"))

if(what_do_you_want == 'words'):
	import random
	file_nouns = open("nouns.md", "r")
	file_result = open("./results/words.md", "w")
	arr = []
	rand_indexes = []
	cx = 0

	for line in file_nouns:
		arr.append(line)

	how_many = int(input("Enter how many random words you want: "))

	while(cx < how_many):
		rand_index = random.randint(0, len(arr) - 1)
		if(not(rand_index in rand_indexes)):
			rand_indexes.append(rand_index)
			file_result.write(arr[rand_index])
			cx += 1
		else:
			continue

elif(what_do_you_want == 'numbers'):
	import random
	file_numbers = open("./results/numbers.md", "w")
	file_LN = open("./results/LN.md", "w")
	rand_values = []
	cx = 0

	num_min = int(input("MIN: "))
	num_max = int(input("MAX: "))
	num_count = int(input("How many: "))

	LN_codes = ["нм", "гж", "дт", "кх", "чщ", "пб", "шл", "сз", "вф", "рц"]

	while(cx < num_count):
		rand_value = random.randint(num_min, num_max)
		if(not(rand_value in rand_values)) or (num_max - num_min + 1 < num_count):
			rand_values.append(rand_value)
			file_numbers.write(str(rand_value) + "\n")

			rand_value_str = str(rand_value)
			for letter in rand_value_str:
				file_LN.write(LN_codes[int(letter)])
			file_LN.write("\n")
			cx += 1
		else:
			continue

elif(what_do_you_want == 'images'):
	import random
	file_nums_images = open("nums_img_codes.md", "r")
	answers = open("./results/answers.md", "w")
	nums_images_arr = []
	correct_answers = 0

	for line in file_nums_images:
		nums_images_arr.append({line[:line.find(' ')] : line[line.rfind(' '):len(line)]})

	nums_or_images = input("Что будем узначать, числа или образы?\n")
	attempts = int(input("Сколько попыток?\n"))
	if(nums_or_images == 'nums'):
		for attempt in range(attempts):
			rand_value = random.randint(0, len(nums_images_arr) - 1)
			rand_value_str = str(rand_value)
			if(len(rand_value_str) < 2):
				rand_value_str = '0' + rand_value_str

			answer = str(input("Введите название образа для " + rand_value_str + ": "))

			if(nums_images_arr[rand_value][rand_value_str][1:-2] == answer):
				is_correct = "CORRECT"
				correct_answers += 1
			else:
				is_correct = "WRONG"

			answers.write(rand_value_str + ":" + nums_images_arr[rand_value][rand_value_str][:-2] + " => " + answer + " | " + is_correct + "\n")

		answers.write("_______________________________________________________________________\n")
		answers.write("Total amount: " + str(correct_answers) + " OUT OF " + str(attempts) + "\n")
		answers.write(str(int(correct_answers) / (int(attempts) / 100.0)) + "%")

	elif(nums_or_images == 'imgs'):
		for attempt in range(attempts):
			rand_value = random.randint(0, len(nums_images_arr) - 1)
			rand_value_str = str(rand_value)
			if(len(rand_value_str) < 2):
				rand_value_str = '0' + rand_value_str

			answer = str(input("Введите число соответствующее образу " + nums_images_arr[rand_value][rand_value_str][:-2] + ": "))
			if(len(answer) < 2):
				answer = '0' + answer

			if(int(rand_value) == int(answer)):
				is_correct = "CORRECT"
				correct_answers += 1
			else:
				is_correct = "WRONG"

			answers.write(rand_value_str + ":" + nums_images_arr[rand_value][rand_value_str][:-2] + " => " + answer + " | " + is_correct + "\n")

		answers.write("_______________________________________________________________________\n")
		answers.write("Total amount: " + str(correct_answers) + " OUT OF " + str(attempts) + "\n")
		answers.write(str(int(correct_answers) / (int(attempts) / 100.0)) + "%")