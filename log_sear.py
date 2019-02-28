import time

def sort(dict):
    ip = input('IP? :')
    filename = ip +'.log'
    with open(filename, 'w', encoding='UTF-8') as nf:
        nf.write(ip + '\n')
        if ip in dict.keys():
            for x in dict[ip]:
                nf.write('Дата: {}  Время в работе: {}  Объем данных: {}  URL : {}'.format(time.ctime(float(x['date'])), x['time'], x['size'], x['url'] + '\n'))
#                print('Дата: {}  Время в работе: {}  Объем данных: {}  URL : {}'.format(time.ctime(float(x['date'])), x['time'], x['size'], x['url']))

dict = {}
x = True
with open('test.log') as f:
    while x == True:
        ip_line = []
        list_tmp = f.readline()
        if list_tmp is not '':
            list = list_tmp.split(' ')
            list[:] = [x for x in list if x != '']
            ip = list[2]
            session_line = {'date': list[0], 'time': list[1], 'size': list[4], 'url': list[6]}
            if ip in dict.keys():
                dict[ip].append(session_line)
            else:
                ip_line.append(session_line)
                dict[ip] = ip_line
        else:
            x = False
print(dict.keys())
sort(dict)