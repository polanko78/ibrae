import time
from operator import itemgetter
from pprint import pprint

# (date1,(ip1,(status, size, request),
#            (status, size, request)),
#        ip2,(status, size, request),
#        ip3,(status, size, request),
#        ...)
#  date2,(ip1,(status, size, request),
#        ip2,(status, size, request),
#        ip3,(status, size, request),
#        ...)
#  date3,(ip1(status, size, request),
#        ip2(status, size, request),
#        ip3(status, size, request),
#        ...)
#  )
#  big list = (date,(ip1,((staus, size, request),(status,size,request),(status,size,request)),
#                   ip2,((staus, size, request),(status,size,request),(status,size,request)),
#                   ip3,((staus, size, request),(status,size,request))
#              ))
# big_dic = {23feb:(10.254.50.18:((staus, size, request),(status,size,request))
#                  (10.254.50.18: ((staus, size, request), (status, size, request)              )
#                     )
#             }
# big_dic = {date:(ip1:((data),(data)),
#                  ip2:((data),(data))),
#             date1:(ip1:((data),(data)),
#                  ip2:((data),(data)))
#            }


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


big_list = []
date_dic = {}
ip_dic = {}
small_list = []
ip_line = []
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
                print(date_dic[date_to_list])
                ip_dic[ip].append(small_list)
                ip_dic[ip].append(ip_line)
                if date_to_list not in date_dic.keys():
                    date_dic = {date_to_list: []}
                    date_dic[date_to_list].append(ip_dic)
                else:
                    date_dic[date_to_list].append(ip_dic)
            else:
                ip_dic = {ip : []}
                ip_dic[ip].append(small_list)
                if date_to_list not in date_dic.keys():
                    date_dic = {date_to_list : []}
                    date_dic[date_to_list].append(ip_dic)
                else:
                    date_dic[date_to_list].append(ip_dic)



#            big_list.append(date_dic)
            small_list = []
            ip_line =[]

        else:
            x = False

pprint(date_dic)
#pprint()


