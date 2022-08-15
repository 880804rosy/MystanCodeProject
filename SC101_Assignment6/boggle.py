"""
File: boggle.py
Name: Rosy Huang
----------------------------------------
TODO: Play Boggle!
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():			# I cannot fix the "roomy" bug!
	"""
	TODO: Play Boggle!
	"""
	start = time.time()

	checklist = []
	while True:
		s = input("1 row of letters: ")
		row1 = s.split()
		for i in range(4):
			if len(row1[i]) != 1:
				print("Illegal input")
				break
			checklist.append((0, i, row1[i].lower()))
		s = input("2 row of letters: ")
		row2 = s.split()
		for i in range(4):
			if len(row2[i]) != 1:
				print("Illegal input")
				break
			checklist.append((1, i, row2[i].lower()))
		s = input("3 row of letters: ")
		row3 = s.split()
		for i in range(4):
			if len(row3[i]) != 1:
				print("Illegal input")
				break
			checklist.append((2, i, row3[i].lower()))
		s = input("4 row of letters: ")
		row4 = s.split()
		for i in range(4):
			if len(row4[i]) != 1:
				print("Illegal input")
				break
			checklist.append((3, i, row4[i].lower()))

		dict_list = read_dictionary()
		word_list = []
		for y in range(4):
			for x in range(4):
				used_word = [(x, y)]
				ans = checklist[4*y+x][2]
				boggle(dict_list, checklist, used_word, ans, x, y, word_list)
		print(f'There are {len(word_list)} words in total.')
		break
	#
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(dict_list, checklist, used_word, ans, x, y, word_list):
	if ans in dict_list and len(ans) >= 4 and ans not in word_list:
		print("Found",ans)
		word_list.append(ans)
	else:
		# set limit for border situation
		if x == 0:
			neighbor_x0 = x
		else:
			neighbor_x0 = x - 1
		if x == 3:
			neighbor_xx = x
		else:
			neighbor_xx = x + 1
		if y == 0:
			neighbor_y0 = y
		else:
			neighbor_y0 = y - 1
		if y == 3:
			neighbor_yy = y
		else:
			neighbor_yy = y + 1
		for i in range(neighbor_x0, neighbor_xx + 1):
			for j in range(neighbor_y0, neighbor_yy + 1):
				# Choose
				if i == x and j == y:	    # to avoid first alphabet
					pass
				elif (i, j) in used_word:
					pass
				else:
					# Choose
					ans += checklist[4*j+i][2]
					used_word.append((i, j))
					# Explore
					if has_prefix(ans, dict_list) is True:
						boggle(dict_list, checklist, used_word, ans, i, j, word_list)
					# Unchoose
					ans = ans[:len(ans)-1]
					used_word.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open("dictionary.txt", "r") as f:
		dict_list = []
		for line in f:
			dict_list.append(line.strip())
	return dict_list


def has_prefix(sub_s, dict_list):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dict_list: (list) A list that stores words in dictionary.txt
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_list:
		if len(word) == 4 and word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
