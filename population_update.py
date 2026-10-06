import pymysql
from pymysql.cursors import DictCursor, Cursor

# Соединяемся с базой данных
dbh = pymysql.connect(
        host='ithub-ai.ru',
        user='teacher',
        password='a-007-007-007',
        db='ithub',
        charset='utf8mb4',
        cursorclass=DictCursor
    )

try:
  with dbh.cursor() as cur:
    cur.execute('SELECT * FROM vd_population')
    rows = cur.fetchall()

    countries = ''
    population = ''
    for row in rows:
        countries += ',"'+row['country']+'"'
        population += ','+str(row['population'])

    countries = 'countrties_list = ['+countries[1:]+'];'
    population = 'population = ['+population[1:]+'];'

    file = open('static\population_data.js', 'w', encoding='utf-8')
    file.write(countries+"\n"+population)
    file.close()

except Exception as error:
  print("Что-то пошло не так", error)
