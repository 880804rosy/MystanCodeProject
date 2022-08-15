"""
File: coin_flip_runs.py
Name: Rosy Huang
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	This program simulates coin flip(s) with the number of runs input by users.
	"""
	print("Let's flip a coin!")
	num_run = int(input("Number of runs: "))
	num = 0
	ans = ""
	s = random_word()
	ans += s
	while True:
		s = random_word()
		ans += s
		# Exclude the situation of more than 2 'H' or 'T' are linked together
		if ans[len(ans)-2] == ans[len(ans)-1]:
			if len(ans) >= 3 and ans[len(ans)-3] == ans[len(ans)-2]:
				pass
			else:
				num += 1
		if num == num_run:
			break
	print(ans)

# pick 1 or 2
def random_word():
	num = r.choice(range(2))
	if num == 0:
		return "H"
	elif num == 1:
		return "T"


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
