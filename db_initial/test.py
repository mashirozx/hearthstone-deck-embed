from json_to_mysql import *

host='localhost'
user='root'
passwd='password'
db_name='hearthstone'
table_name='cards_data_27845'
json_file='../cards.json'

jsonToMySQL(host, user, passwd, db_name, table_name, json_file)

key = input('Press any key to quit')
quit()
