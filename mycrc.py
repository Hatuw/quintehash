# -*- coding: utf-8 -*-


def mycrc32(szString):
    m_pdwCrc32Table = [0 for x in range(0, 256)]
    dwPolynomial = 0xEDB88320
    dwCrc = 0
    for i in range(0,255):
        dwCrc = i
        for j in [8, 7, 6, 5, 4, 3, 2, 1]:
            if dwCrc & 1:
                dwCrc = (dwCrc >> 1) ^ dwPolynomial
            else:
                dwCrc >>= 1
        m_pdwCrc32Table[i] = dwCrc
    dwCrc32 = 0xFFFFFFFF
    for i in szString:
        b = ord(i)
        dwCrc32 = ((dwCrc32) >> 8) ^ m_pdwCrc32Table[(b) ^ ((dwCrc32) & 0x000000FF)]
    dwCrc32 = dwCrc32 ^ 0xFFFFFFFF
    return dwCrc32

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
