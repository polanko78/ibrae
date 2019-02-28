
dict = {}
with open(test.log) as f:
    while True:
        ip_line = []
        list_tmp = f.readline()
        if list_tmp is not '':
            list = list_tmp.split(' ')
            list[:] = [x for x in list if x != '']
            date = list[0]
            time = list[1]
            ip = list[2]
            size = list[4]
            url = list[6]
            session_line = {'date': date, 'time': time, 'size': size, 'url': url}
            if ip in dict.keys():
                dict[ip].append(session_line)
                print(dict[ip])
            else:
                ip_line.append(session_line)
                dict[ip] = ip_line
        else:
            return self