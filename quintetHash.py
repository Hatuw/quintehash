# -*- coding: utf-8 -*-
import time
import hashlib
import zlib
import binascii


def mycrc20(szString):
    m_pdwCrc20Table = [0 for x in range(0, 256)]
    # CRC20生成多项式x^20 + x^12 + x^8 + 1即: 01101 CRC32: 04C11DB7L
    dwPolynomial = 0x01101
    dwCrc = 0
    for i in range(0,255):
        dwCrc = i
        for j in [8, 7, 6, 5, 4, 3, 2, 1]:
            if dwCrc & 1:
                dwCrc = (dwCrc >> 1) ^ dwPolynomial
            else:
                dwCrc >>= 1
        m_pdwCrc20Table[i] = dwCrc
    dwCrc20 = 0xFFFFFFFF
    for i in szString:
        b = ord(i)
        dwCrc20 = ((dwCrc20) >> 8) ^ m_pdwCrc20Table[(b) ^ ((dwCrc20) & 0x000000FF)]
    dwCrc20 = dwCrc20 ^ 0xFFFFFFFF
    return dwCrc20


if __name__ == '__main__':
    # import the dataset
    SAVEFILE = False
    file = open('data.txt', 'r')
    flowdata = file.readlines()
    flow = 0
    for flow in range(len(flowdata)):
        flowdata[flow] = flowdata[flow].strip().upper()
    file.close()

    # md5
    print('[+]processing md5:')
    remd5 = []
    bgtime = time.time()
    for i in flowdata:
        remd5.append(hashlib.md5(i.encode('utf-8')).hexdigest())
    endtime = time.time()
    runtime = endtime - bgtime
    print('runtime of md5: %f' % runtime)
    if SAVEFILE:
        # write the result
        resultmd5 = open('result_md5.txt', 'w+')
        for i in remd5:
            resultmd5.write(i + '\n')
        resultmd5.close()
    del(remd5)

    # sha1
    print('[+]processing sha1:')
    resha1 = []
    bgtime = time.time()
    for i in flowdata:
        resha1.append(hashlib.sha1(i.encode('utf-8')).hexdigest())
    endtime = time.time()
    runtime = endtime - bgtime
    print('runtime of sha1: %f' % runtime)
    if SAVEFILE:
        # write the result
        resultsha1 = open('result_sha1.txt', 'w+')
        for i in resha1:
            resultsha1.write(i + '\n')
        resultsha1.close()
    del(resha1)

    # crc32
    print('[+]processing crc32:')
    recrc32 = []
    bgtime = time.time()
    for i in flowdata:
        recrc32.append(zlib.crc32(i.encode('utf-8')))
    endtime = time.time()
    runtime = endtime - bgtime
    print('runtime of crc32: %f' % runtime)
    if SAVEFILE:
        # write the result
        resultcrc32 = open('result_crc32.txt', 'w+')
        for i in recrc32:
            resultcrc32.write('%s\n' % i)
        resultcrc32.close()
    del(recrc32)

    # crc20
    print('[+]processing crc20:')
    recrc20 = []
    bgtime = time.time()
    for i in flowdata:
        recrc20.append(mycrc20(i))
    endtime = time.time()
    runtime = endtime - bgtime
    print('runtime of crc20: %f' % runtime)
    if SAVEFILE:
        # write the result
        resultcrc20 = open('result_crc20.txt', 'w+')
        for i in recrc20:
            resultcrc20.write('%s\n' % i)
        resultcrc20.close()
    del(recrc20)


