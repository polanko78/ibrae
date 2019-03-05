import time
from operator import itemgetter

# топ 10 исходящих IP
# топ 10 сайтов
# топ 10 01 - ip - данные
# топ 10 01 - ip - сайт - данные
# топ 10 по Connect IP - количество подключений




def sort(dict):
    #    ip = input('IP? :')
    count = 0
    dom_list = []
    d_l = []
    spisok = []
    domen_l = []
    top10ip = []
    top10dom = []
    dom_check_list = ['.ru/', '.com/', '.org/', '.net/']

    for ip in dict.keys():
        count = len(dict[ip])
        spisok.append([ip, count])
    top10ip = sorted(spisok, key = itemgetter(1), reverse = True)
    print(top10ip[:10])

    for ip in dict.keys():
        for x in dict[ip]:
            for y in dom_check_list:
                if y in x['url']:
                    t = x['url'].split(sep = '/')
                    dom_list.append(t[2])
    for y in dom_list:
        t = y.split(sep = '.')
        d_l.append(t[-2] + '.' + t[-1])
    domen_l = sorted(d_l, key = lambda x: d_l.count(x), reverse = True)
    for domen in domen_l:
        if domen not in top10dom:
            top10dom.append(domen)
    print(top10dom)





    #    filename = 'top.log'
    #    with open(filename, 'w', encoding='UTF-8') as nf:
    #        nf.write('TOP10 IP \n')
#        if ip in dict.keys():
#            for x in dict[ip]:
#                nf.write('Дата: {}  Время в работе: {}  Объем данных: {}  URL : {}'.format(time.ctime(float(x['date'])), x['time'], x['size'], x['url'] + '\n'))
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
#print(dict.keys())
sort(dict)