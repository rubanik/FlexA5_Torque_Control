import sqlite3

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

def init_db() -> sqlite3.Connection:
    """ Инициализация базы данных"""
    db = get_connection()
    try:
        # Создание таблицы
        db.execute("""CREATE TABLE data
                    (time text, machine text, speed text,
                    drive text, torque text,state text)
                """)
    except:
        print("[!]Data Table Already Exist")
    finally:
        print('[INFO]DB is ready')
        return db
    

def get_connection():
    """Создаём объект соединения с базой данных"""
    try:
        connection = sqlite3.connect('./FlexA5_Torque_Control/mydb.db')
        return connection
    except:
        print('Wrong Path or Not Exist')


def write_to_db(db,data):
    """ Записываем данные в DB. Поля таблицы:
    Date Time - Временной штамп 
    Machine -   Тип Машины
    Speed -     Текущая скорость машины
    Drive -     Название привода
    Torque -    Момент двигателя
    State -     Текущее состояние машины"""

    try:
        db.executemany("INSERT INTO data VALUES (?,?,?,?,?,?)", data)
        db.commit()
        print('[INFO]Data has been written')
    except:
        print('Write Error')


def read_db(db):
    """Читаем из БД. для теста"""
    for row in db.execute("SELECT rowid, * FROM data ORDER BY machine"):
        print(row)


if __name__ =='__main__':
    # Start
    data_base = init_db()

    with data_base:
        write_to_db(data_base,data)

    #read_db(data_base)

    data_base.close()