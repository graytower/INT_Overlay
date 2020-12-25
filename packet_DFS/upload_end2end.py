# !/usr/bin/python
import sys
import MySQLdb
from scapy.all import *

''' transfer int information to table int_info in database INT_INFO. '''


class Uploadend2end:

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
        print('mysql connect succes')
        ip_pair = self.paths[0]

        index_start = []
        index_end = []
        for i in range(len(self.meta)):
            if self.meta[i] == 'start':
                index_start.append(i)
        for i in range(len(self.meta)):
            if self.meta[i] == 'end':
                index_end.append(i)
        print(len(index_start))
        print(len(index_end))

        delay = []
        for i in range(len(index_start)):
            tmp = 0
            for j in range(index_start[i], index_end[i]):
                if self.meta[j] == '[':
                    tmp += self.meta[j + 5] - self.meta[j + 4] + int(self.meta[j + 6])
            delay.append(tmp)

        for n in range(len(delay)):
            try:
                cue.execute("insert into delay_end2end (ip_pair, end2end_delay) values (%s, %s)", [ip_pair, delay[n]])
            except Exception as e:
                print('Insert error:', e)
                db.rollback()
            else:
                db.commit()

        db.close()


if __name__ == "__main__":
    pass
