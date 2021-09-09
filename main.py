"""
Что я хочу:
1. Взять данные с OPC DA
2. Собрать их в кучу
3. Сохранить их в БД
Время - Машина - скорость - привод - момент - статус машины  """

import OpenOPC

MACHINE = ('FLEXA5',)

tags = ('Random.Int2', 'Random.Real4', 'Random.String')

def connect_to_OPC():
    try:
        opc = OpenOPC.client()
        opc.connect(opc.servers()[0])
        return opc
    except Exception as a:
        print('Connection error :', a)
    
def get_server_info(opc):
    return opc.info()


def read_opc_data(opc,tags):
     return opc.read(tags)
    

def prepare_data(data):
    result = []
    for item in data:
        item = MACHINE + item
        result.append(item)
    print(result)

    
opc_connection = connect_to_OPC()

for i in range(20):
    data = read_opc_data(opc_connection,tags)
    prepare_data(data)

opc_connection.close()

