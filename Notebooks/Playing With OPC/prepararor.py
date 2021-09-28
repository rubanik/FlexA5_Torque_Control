import datetime

# TODO: The Drive List should be imported from file
drive_tuple = ('Cut Drum','Pusher Left', 'Pusher Right', 'Pusher Central', 'Pusher Wheel 1')

def get_timestamp():
    return datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')


def get_machine_name():
    return 'FlexA5'


def prepare_list_of_data(data):
    result = []
    # Проходимся по полученным данным и вытаскиваем нужные элементы в виде tuple. (data[i],) = data[1:2]
    for index in range(1,len(data)-2,2):
        result.append(data[index-1][1:2] + data[index][1:2] + data[-2:][0][1:2]+ data[-2:][1][1:2])

    # Additional data - храним там время и название машины
    additional_data = get_timestamp(),get_machine_name()
    for i in zip(drive_tuple,result):
        res = (additional_data + i[0:1] + i[1])
        print(res)


def prepare_from_generator(generator):
<<<<<<< HEAD
    """ Тут нужно доработать!!"""
=======
    """ Тут нужно доработать!"""
>>>>>>> 0d871234229aa2d621a94f95ddf6fed23e4c119c
    count = 0
    pair = []
    out = []
    for part in generator:
    # Вся херня разбивается на пары момент - ток, по положению в Data. если находим 
    # Нечетную позицию - просто добавляем в лист Пары, если нашли чётную позицию то добавзяем в Пары, копируем из пар в итоговый список
        if count%2 != 0:
            pair.append(part)
            out.append(tuple(pair.copy()))
            pair.clear() 
        else:
            pair.append(part)
        count+=1
    print(out)

    out_2 = []
    date_mach = get_timestamp(),get_machine_name()

    for ind,part in enumerate(out,0):
        if ind < len(out)-1:
            part = date_mach +(drive_tuple[ind],) + part + out[-1]
            out_2.append(part)