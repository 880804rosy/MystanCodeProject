"""
File: largest_digit.py
Name: Rosy Huang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: Imput number n.
	:return: The biggest digit in integer.
	"""
	if n < 0:
		n *= -1
	param = n
	return find_largest_digit_helper(n, param, 0, 0)


def find_largest_digit_helper(n, param, digit, max_num):
	if n < 10**digit:
		if digit == 1:		# consider one-digit n's case
			return n
		return max_num
	else:
		num = param % 10  				# get first-digit number
		param = (param - num)//10
		if num > max_num:
			max_num = num
		return find_largest_digit_helper(n, param, digit+1, max_num)


if __name__ == '__main__':
	main()
