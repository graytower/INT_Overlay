#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import MySQLdb


def main():

    db = MySQLdb.connect("localhost", "root", "233233", "INT_INFO", charset='utf8')
    cursor = db.cursor()
    t1 = time.time()

    # once
    meta = []
    sql = "SELECT * FROM int_vxlan_heavy WHERE host_ip = 1"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        meta.append(row[1])
    db.close()
    t3 = time.time()
    print(t3 - t1)
    print(meta)

    # # twice
    # deq_timedelta = []
    # process_delay = []
    # ingress_port = []
    # egress_port = []
    # switch_list = 0
    # sql = "SELECT * FROM dfs_path WHERE path_id = '1-3'"
    # cursor.execute(sql)
    # results = cursor.fetchall()
    # for row in results:
    #     switch_list = str(row[2])
    #
    # new_list = switch_list.strip().split('|')
    # print(new_list)
    #
    # t2 = time.time()
    #
    # for i in range(len(new_list)):
    #     switch_id = new_list[i]
    #     if i == len(new_list) - 1:
    #         switch_id_follow = 0
    #     else:
    #         switch_id_follow = new_list[i + 1]
    #     sql_2 = "SELECT * FROM dfs_int WHERE switch_id = %s AND next_switch_id = %s" % (switch_id, switch_id_follow)
    #     cursor.execute(sql_2)
    #     results_2 = cursor.fetchall()
    #     for row in results_2:
    #         ingress_port.append(row[3])
    #         egress_port.append(row[4])
    #         deq_timedelta.append(row[7])
    #         process_delay.append(row[8])
    # t3 = time.time()
    # db.close()
    # print(t2 - t1)  # first lookup
    # print(t3 - t2)  # second lookup
    # print(ingress_port)
    # print(egress_port)
    # print(deq_timedelta)
    # print(process_delay)
    # print(type(process_delay[0]))


if __name__ == '__main__':
    main()
