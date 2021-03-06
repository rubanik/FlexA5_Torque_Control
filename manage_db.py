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
    """ ?????????????????????????? ???????? ????????????"""
    db = get_connection()
    try:
        # ???????????????? ??????????????
        db.execute("""CREATE TABLE data
                    (time text, machine text, drive text,
                     torque text,current text, speed text,
                     state text)
                """)
    except:
        print("[!]Data Table Already Exist")
    finally:
        print('[INFO]DB is ready')
        return db
    

def get_connection():
    """?????????????? ???????????? ???????????????????? ?? ?????????? ????????????"""
    try:
        connection = sqlite3.connect('./FlexA5_Torque_Control/mydb.db')
        return connection
    except:
        print('Wrong Path or Not Exist')


def write_to_db(db,data):
    """ ???????????????????? ???????????? ?? DB. ???????? ??????????????:
    Date Time - ?????????????????? ?????????? 
    Machine -   ?????? ????????????
    Speed -     ?????????????? ???????????????? ????????????
    Drive -     ???????????????? ??????????????
    Torque -    ???????????? ??????????????????
    State -     ?????????????? ?????????????????? ????????????"""

    try:
        db.executemany("INSERT INTO data VALUES (?,?,?,?,?,?,?)", data)
        db.commit()
        print('[INFO]Data has been written')
    except:
        print('Write Error')


def read_db(db):
    """???????????? ???? ????. ?????? ??????????"""
    for row in db.execute("SELECT rowid, * FROM data ORDER BY machine"):
        print(row)


if __name__ =='__main__':
    # Start
    data_base = init_db()

    with data_base:
        write_to_db(data_base,data)

    #read_db(data_base)

    data_base.close()