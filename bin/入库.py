import pymysql
from pymysql.converters import escape_string
import re

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='10086.com',
    db='test',
    charset='utf8mb4',
    port=3306)

cur = conn.cursor()

with open(r"/Users/jacentsao/Documents/WechatHistory/🚀/洁珊.txt", encoding='utf-8') as f:
    lines = f.readlines()
    filter_lines = []
    reg = "^.+[\u4E00-\u9FFF]\s\(.+\):"

    for line in lines:
        # 去除转发的聊天记录 简单过滤
        if (line.startswith('洁珊') or line.startswith('🚀')) and re.match(reg, line):
            filter_lines.append(line.strip())


# Python program to convert time
# from 12 hour to 24 hour format

# Function to convert the date format
def convert24(str1):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[11:13] == "12":
        return str1[:11] + "00" + str1[13:-2]

    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[11:13] == "12":
        return str1[:-2]

    else:

        # add 12 to hours and remove PM
        return str1[:11] + str(int(str1[11:13]) + 12) + str1[13:19]


for line in filter_lines:
    s1 = line.find(" ")
    s2 = line.find("):")
    name = line[:s1]
    time = convert24(line[s1 + 2:s2])
    content = line[s2 + 2:]
    print(line)
    insert_sql = f"insert into log(user,datetime,content) values ('{name}','{time}' ,'{content}')"
    cur.execute(insert_sql)
conn.commit()
