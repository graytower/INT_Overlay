# !/usr/bin/python
import MySQLdb
from scapy.all import *

''' transfer int information to table int_info in database INT_INFO. '''


class UploadV1:

    def __init__(self, meta, paths):
        self.meta = meta
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
        my_key = self.paths

        for i in range(len(self.meta)):
            if self.meta[i] == '[':
                tmp = self.meta[i + 5] - self.meta[i + 4]
                self.meta[i + 4] = str(tmp)
                self.meta[i + 5] = ''

        index_start = []
        index_end = []
        for i in range(len(self.meta)):
            if self.meta[i] == 'start':
                index_start.append(i)
        for i in range(len(self.meta)):
            if self.meta[i] == 'end':
                index_end.append(i)

        print(index_start)
        print(index_end)

        new_meta = []
        for i in range(len(index_start)):
            new_meta.append(' '.join(self.meta[index_start[i] + 1:index_end[i]]))

        for n in range(len(new_meta)):
            try:
                cue.execute("insert into int_vxlan_heavy (host_ip, int_meta) values (%s, %s)", [my_key, new_meta[n]])
            except Exception as e:
                print('Insert error:', e)
                db.rollback()
            else:
                db.commit()

        db.close()


if __name__ == "__main__":
    pass
