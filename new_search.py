import time
from operator import itemgetter
from pprint import pprint

def make_url(url):
    dom_check_list = ['.ru/', '.com/', '.org/', '.net/']
    d = []
    for y in dom_check_list:
        if y in url:
            t = url.split(sep = '/')
            d.append(t[2])
    for y in d:
        t = y.split(sep = '.')
        dom_name = (t[-2] + '.' + t[-1])
        return dom_name

def sort(date_dic, ip_dic):
    ip_list = []
    domens = []
    top10size_date = []
    date_size_ip = []
    for a in date_dic.keys():
        for x in ip_dic.keys():
            counter = 0
            b_size = 0
            for y in ip_dic[x]:
                counter += 1
                b_size += int(y[2])
                if y[3] != '':
                    if y[3] not in domens:
                        domens.append(y[3])
            ip_l = [x, counter, b_size]
            ip_list.append(ip_l)
        dsi = [a, ip_list]
        date_size_ip.append(dsi)
    for x in date_size_ip:
        ml = sorted(x[1], key=itemgetter(2), reverse=True)
        list_to_add = [x[0], ml]
        top10size_date.append(list_to_add)
    top10dom = sorted(domens, key=lambda x: domens.count(x), reverse=True)
    top10ip = sorted(ip_list, key=itemgetter(1), reverse=True)
    # pprint(top10dom[0:10])
    # pprint(top10ip[0:10])
    # print(top10size_date[0][0], top10size_date[0][1][0:10])
    filename = 'top.log'
    with open(filename, 'w', encoding='UTF-8') as nf:
        nf.write('TOP10 domains \n')
        for x in top10dom[0:10]:
            st = x + '\n'
            nf.write(st)
        nf.write('\n')
        nf.write('TOP10 IP \n')
        for x in top10ip[0:10]:
            st = x[0] + '\n'
            nf.write(st)
        nf.write('\n')
        nf.write('TOP10 data size for date \n')
        for x in top10size_date:
            st = x[0] + '\n'
            nf.write(st)
            for y in x[1][0:10]:
                st = str(y[0])+ '  ' + str(y[2]) + '  bites \n'
                nf.write(st)


def sort2(ip_dic):
    big = []
    for x in ip_dic.keys():
        count = 0
        for y in ip_dic[x]:
            if y[0] == 'CONNECT':
                count += 1
        small = [x, count]
        big.append(small)
    sorted_list = sorted(big, key=itemgetter(1), reverse=True)
    filename = 'top2.log'
    with open(filename, 'w', encoding='UTF-8') as nf:
        nf.write('TOP10 IP with CONNECT \n')
        for x in sorted_list[0:10]:
            st = str(x[0]) + '   ' + str(x[1]) + '\n'
            nf.write(st)


date_dic = {}
ip_dic = {}
small_list = []
x = True
with open('test.log') as f:
    while x == True:
        list_tmp = f.readline()
        if list_tmp is not '':
            list = list_tmp.split(' ')
            list[:] = [x for x in list if x != '']
            ip = list[2]
            date = time.ctime(float(list[0]))
            d = date.split(' ')
            date_to_list = d[2] + ' ' + d[1]
            t = list[1]
            size = list[4]
            url = list[6]
            result = list[3]
            request = list[5]
            dom_name = make_url(url)
            if dom_name == None:
                dom_name = ''
            small_list = [request, result, size, dom_name, date]
            if ip in ip_dic.keys():
                ip_dic[ip].append(small_list)
            else:
                ip_dic[ip] = []
                ip_dic[ip].append(small_list)
            if date_to_list not in date_dic.keys():
                date_dic[date_to_list] = []
                date_dic[date_to_list].append(ip_dic)
            small_list = []
        else:
            x = False

command = None
x = True
while x == True:
    command = input('1 - просто сортировка, 2 - сортировка по connect :')
    if command == '1':
        sort(date_dic, ip_dic)
    elif command == '2':
        sort2(ip_dic)
    else:
        x = False
