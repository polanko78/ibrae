from typing import Dict, Any

import time

# открываем файл
# считываем строки
# разбираем строки на список
# список переводим в словарь

class File_date:
    # date = None
    # time = None
    # ip = None
    # size = None
    # url = None
    dict = {}

    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        dict = {}
        session_line = []
        with open(self.file_path) as f:
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
                    session_line = {'date':date, 'time':time, 'size':size, 'url':url}
                    if ip in self.dict.keys():
                        tmp_list = self.dict[ip]
                        tmp_list.append(session_line)
                        self.dict[ip] = tmp_list
                    else:
                        ip_line.append(session_line)
                        self.dict[ip] = ip_line
                else:
                    return self


    def __exit__(self, exc_type, exc_val, exc_tp):
        pass


with File_date('test.log') as my_dict:
    print('Bam!')
    print(my_dict.dict.get('10.254.55.18'))