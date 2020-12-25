# !/usr/bin/python
import MySQLdb
from scapy.all import *

''' transfer int information to table int_info in database INT_INFO. '''


class Upload_num:

    def __init__(self, int_dict, paths):
        self.int_dict = int_dict
        self.paths = paths
        self.insert_info()

    def insert_info(self):
        db = MySQLdb.connect(host='localhost',
                             user='root',
                             passwd='233233',
                             db='INT_INFO',
                             charset='utf8')
        cue = db.cursor()
        print("mysql connect succes")

        #  insert paths
        path_id = self.paths[0]
        paths_tmp = self.paths[::-1]
        index_start = []
        index_end = []
        for i in range(len(paths_tmp)):
            if paths_tmp[i] == "start":
                index_start.append(i)
        for i in range(len(paths_tmp)):
            if paths_tmp[i] == "end":
                index_end.append(i)
        print(len(index_start))
        print(len(index_end))
        num = len(index_start)

        try:
            cue.execute("insert into packet_num (ip_pair, numbers) values(%s, %s)", [path_id, num])
        except Exception as e:
            print('Insert error:', e)
            db.rollback()
        else:
            db.commit()

        db.close()


if __name__ == "__main__":
    pass
