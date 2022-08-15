"""
File: webcrawler.py
Name: Rosy Huang
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def produce_num(string):
    num = ""
    for i in range(len(string)):
        ch = string[i]
        if ch.isdigit():
            num += ch
    return num


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)        # response is an object
        html = response.text                # html is a text
        soup = BeautifulSoup(html)          # soup is an object created by BeautifulSoup

        # ----- Write your code below this line ----- #

        tag = soup.tbody
        data = tag.text   # string
        data_list = data.split()

        boy_name_num = 0
        girl_name_num = 0

        for i in range(1000):
            if i % 5 == 2:
                num = produce_num(data_list[i])
                boy_name_num += int(num)
            if i % 5 == 4:
                num = produce_num(data_list[i])
                girl_name_num += int(num)
        print("Male Number: ",boy_name_num)
        print("Female Number: ",girl_name_num)


if __name__ == '__main__':
    main()
