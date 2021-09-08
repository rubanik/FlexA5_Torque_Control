import sqlite3

conn = sqlite3.connect('./FlexA5_Torque_Control/mydb.db')
cursor = conn.cursor()

try:
    # Создание таблицы
    cursor.execute("""CREATE TABLE data
                    (time text, machine text, speed text,
                    drive text, torque text,state text)
                """)
except:
    print("Already Exist")


# cursor.execute("""INSERT INTO data
#                   VALUES ('Glow', 'Andy Hunter', '7/24/2012',
#                   'Xplore Records', 'MP3')"""
#                )
 
# Сохраняем изменения
conn.commit()
 
# Вставляем множество данных в таблицу используя безопасный метод "?"
data = [('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.435','130'),
          ('10/10/2021', 'FlexA', '470', 'Wheel3Folder', '1.445','130'),
          ('10/10/2021', 'FlexA', '470', 'CutDrum', '0.23','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.835','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.435','130'),
          ('10/10/2021', 'FlexA', '470', 'Wheel3Folder', '1.445','130'),
          ('10/10/2021', 'FlexA', '470', 'CutDrum', '0.23','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.835','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.435','130'),
          ('10/10/2021', 'FlexA', '470', 'Wheel3Folder', '1.445','130'),
          ('10/10/2021', 'FlexA', '470', 'CutDrum', '0.23','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.835','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.435','130'),
          ('10/10/2021', 'FlexA', '470', 'Wheel3Folder', '1.445','130'),
          ('10/10/2021', 'FlexA', '470', 'CutDrum', '0.23','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.835','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.435','130'),
          ('10/10/2021', 'FlexA', '470', 'Wheel3Folder', '1.445','130'),
          ('10/10/2021', 'FlexA', '470', 'CutDrum', '0.23','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.835','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.435','130'),
          ('10/10/2021', 'FlexA', '470', 'Wheel3Folder', '1.445','130'),
          ('10/10/2021', 'FlexA', '470', 'CutDrum', '0.23','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.835','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.435','130'),
          ('10/10/2021', 'FlexA', '470', 'Wheel3Folder', '1.445','130'),
          ('10/10/2021', 'FlexA', '470', 'CutDrum', '0.23','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.835','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.435','130'),
          ('10/10/2021', 'FlexA', '470', 'Wheel3Folder', '1.445','130'),
          ('10/10/2021', 'FlexA', '470', 'CutDrum', '0.23','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.835','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.435','130'),
          ('10/10/2021', 'FlexA', '470', 'Wheel3Folder', '1.445','130'),
          ('10/10/2021', 'FlexA', '470', 'CutDrum', '0.23','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.835','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.435','130'),
          ('10/10/2021', 'FlexA', '470', 'Wheel3Folder', '1.445','130'),
          ('10/10/2021', 'FlexA', '470', 'CutDrum', '0.23','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.835','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.435','130'),
          ('10/10/2021', 'FlexA', '470', 'Wheel3Folder', '1.445','130'),
          ('10/10/2021', 'FlexA', '470', 'CutDrum', '0.23','130'),
          ('10/10/2021', 'FlexA', '470', 'TinFoilDrive', '1.835','130')]
 
for i in range(0,1000):
    cursor.executemany("INSERT INTO data VALUES (?,?,?,?,?,?)", data)

conn.commit()

print('done')
# print("Here's a listing of all the records in the table:")
# for row in cursor.execute("SELECT rowid, * FROM data ORDER BY machine"):
#     print(row)

