import time
from operator import itemgetter
from pprint import pprint

def make_url(url):
    dom_check_list = ['.ru/', '.com/', '.org/', '.net/']
    d = []
    for y in dom_check_list:
        if y in url:
            t = url.split(sep='/')
            d.append(t[2])
    for y in d:
        t = y.split(sep = '.')
        dom_name = (t[-2] + '.' + t[-1])
        return dom_name

def sort(big_list):
    top10dom = []
    top10ip = []
    domens = []
    ip_list = []
    for d in big_list:
        if d[3] != '':
            if d[3] not in domens:
                domens.append(d[3])
        if d[6] not in ip_list:
            ip_list.append(d[6])
    top10dom = sorted(domens, key = lambda x: domens.count(x), reverse = True)
    top10ip = sorted(ip_list, key = lambda x: ip_list.count(x), reverse = True)
    pprint(top10dom[0:10])
    pprint(top10ip[0:10])




big_list = []
x = True
with open('test.log') as f:
    while x == True:
        ip_line = []
        list_tmp = f.readline()
        if list_tmp is not '':
            list = list_tmp.split(' ')
            list[:] = [x for x in list if x != '']
            ip = list[2]
            date = list[0]
            t = list[1]
            size = list[4]
            url = list[6]
            result = list[3]
            request = list[5]
            dom_name = make_url(url)
            if dom_name == None:
                dom_name = ''
            session_line = [list[0], list[1], list[4], dom_name, list[3], list[5], list[2]]
            big_list.append(session_line)
        else:
            x = False

#pprint(big_list)
sort(big_list)
print(session_line)
#for d in big_list:

d = time.ctime(float(session_line[0]))
print(d)
print(type(d))