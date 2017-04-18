# -*- coding: utf-8 -*-
import random

if __name__ == '__main__':
    datafile = open('./data.txt', 'w+')
    i = 0
    for i in range(10000000):
        srcip = '%d.%d.%d.%d' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        srcport = random.randint(0, 65535)
        dstip = '%d.%d.%d.%d' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        dstport = random.randint(0, 65535)
        # pto = 'Tcp'.upper()
        pto = random.choice(['TCP', 'UDP'])
        # print(pto)
        srcstr = '%s_%s_%s_%s_%s' % (srcip, srcport, dstip, dstport, pto)
        datafile.write(srcstr + '\n')
    datafile.close()