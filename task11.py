from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty, order='>'):
    pattern = FMT[ty]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'int64')
    d2, offs = parse(buf, offs, 'int8')
    d3, offs = parse(buf, offs, 'int32')
    d4, offs = parse(buf, offs, 'double')
    d5_size, offs = parse(buf, offs, 'uint32')
    d5_offset, offs = parse(buf, offs, 'uint16')
    d5 = []
    for _ in range(d5_size):
        val, d5_offset = parse(buf, d5_offset, 'double')
        d5.append(val)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5), offs


def parse_c(buf, offs):
    c1 = []
    for _ in range(3):
        val, offs = parse(buf, offs, 'uint8')
        c1.append(val)
    c2, offs = parse(buf, offs, 'int64')
    return dict(C1=c1, C2=c2), offs


def parse_b(buf, offs):
    b1 = []
    for _ in range(7):
        val, offs = parse(buf, offs, 'char')
        b1.append(val)
    b1 = b''.join(b1).decode('utf-8')
    b2, offs = parse(buf, offs, 'uint8')
    b3 = []
    for _ in range(3):
        # Can be an error
        val, offs = parse_c(buf, offs)
        b3.append(val)
    b4, offs = parse(buf, offs, 'double')

    return dict(B1=b1, B2=b2, B3=b3, B4=b4), offs


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, 'float')
    a2, offs = parse(buf, offs, 'int16')
    a3, offs = parse_b(buf, offs)
    d_offset, offs = parse(buf, offs, 'uint16')
    a4, _ = parse_d(buf, d_offset)
    a5, offs = parse(buf, offs, 'double')
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5), offs


def main(stream):
    return parse_a(stream, 4)[0]


print(main((b'\xb3PRO?s\x05\xd3\xbecnzqwlhy,\x9b\x8c\x9e\x16\xa8\x1d\xb0[\x02m'
            b'{\x1e\xed\xd4\xc0\n\xc8\x8d\x8e\xa1\x13\x82J/\x93\xba\xe7\xfe\x07\xceA ;\xbf'
            b'\xe8Pb4\x0e\xfe6\x00]\xbf\xeb\x12\xdc\xa1\xea\xd0\x16?\xbc\x9f'
            b'\xaa\xcf\xd0\xf7\xd0\xbf\xd2!\x0cB\x01\xca\xfc?\xdd\xd6x\xb5\x85\x02'
            b'pZ\xe9\x06{Z\x96D\xc6G\xa2M\xac\xac\xbf\xe3\x9b\xf8\xde\x90?\x9e\x00\x00'
            b'\x00\x03\x00E')))

print(main((b'\xb3PRO?J\xdd7\xbc\xb2wxysjfzf#\xbcR\xea\x84\xa6\x83\x1d\x89\xb47/W\x91'
            b"\xa3`\xd6\x88K\xdej'Py\xad\xc4\t\xc3\xb6\x9e\xa8'\xb4\xbf\xea\xe1;\xb6"
            b"\xe6,\x10\x00e?\xe8v\xefj\xd5'<\xbf\xe7\xaf3\x8c\xfb\xbe\x1a?\xe8qa\xcc1\xa3"
            b'\x00\xbf\xd8\xaf@\xdf\x0cT\\?\xe8e\x17T\x7fP\xc0\x0cK\xe3\x12\xf1\xaf\xe4'
            b'\xd0N\xa2\xe11\xd0\xbf\xcaH\xc3/\xc4\xef\xe8\x00\x00\x00\x04\x00E')
           ))
