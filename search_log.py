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


def sort(big_list):
    m = d = ''
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
    # for x in big_list:
    #     if m != x[0][1]:
    #         if d != x[0][2]:
    #             m = x[0][1]
    #             d = x[0][2]
    #     if '200' in x[4]:
    #         sort_list_size = [m + ' ' + d, x[5], x[2]]






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
            date = time.ctime(float(list[0]))
            d = date.split(' ')
            t = list[1]
            size = list[4]
            url = list[6]
            result = list[3]
            request = list[5]
            dom_name = make_url(url)
            if dom_name == None:
                dom_name = ''
            session_line = [d, list[1], list[4], dom_name, list[3], list[5], list[2]]
            big_list.append(session_line)
        else:
            x = False

#pprint(big_list)
sort(big_list)
print(session_line)
#for d in big_list:
ipx = day = m = d = ''
x_list = []
for x in big_list:
    if m != x[0][1]:
        if d != x[0][2]:
            m = x[0][1]
            d = x[0][2]
    if '200' in x[4]:
        sort_list_size = [m + ' ' + d, x[6], x[2]]
        x_list.append(sort_list_size)
for x in x_list:
    if day !=x[0]:
        day = x[0]
        if x[0] == day:

    # if ipx != x[1]
    #     ipx = x[1]
    # count_size += int(x[2])



pprint(x_list)
