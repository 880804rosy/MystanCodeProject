"""
File: class_reviews.py
Name: Rosy Huang
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    This program gives the results of max, min, avg score of SC001 and SC101 classes.
    """
    a_max = 0
    a_min = 0
    a = 0
    a_total = 0
    b_max = 0
    b_min = 0
    b = 0
    b_total = 0

    while True:
        original_x = input("Which class? ")
        x = original_x.upper()
        if original_x == "-1":
            break
        if x == "SC101":
            score = int(input("Score: "))
            a_total += score
            a += 1
            a_avg = a_total / a
            if a_max == 0:
                a_max = score
                a_min = score
            if score > a_max:
                a_max = score
            if score < a_min:
                a_min = score
        if x == "SC001":
            score = int(input("Score: "))
            b_total += score
            b += 1
            b_avg = b_total / b
            if b_max == 0:
                b_max = score
                b_min = score
            if score > b_max:
                b_max = score
            if score < b_min:
                b_min = score
    if b_max == 0 and a_max == 0:
        print("No class scores were entered")
    else:
        print("=============SC001==============")
        if b_max != 0:
            print("Max (001): " + str(b_max))
            print("Min (001): " + str(b_min))
            print("Avg (001): " + str(b_avg))
        else:
            print("No score for SC001")
        print("=============SC101==============")
        if a_max != 0:
            print("Max (101): " + str(a_max))
            print("Min (101): " + str(a_min))
            print("Avg (101): " + str(a_avg))
        else:
            print("No score for SC101")




# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
