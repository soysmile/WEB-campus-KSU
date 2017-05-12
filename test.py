import hashlib
from decimal import *


def digest(number):
    number = bytearray('{}'.format(number), encoding='utf-8')
    h = hashlib.md5(number)
    return h.hexdigest()


def main():
    file = open('file.txt', 'w')
    range = Decimal('0.00001')
    min = Decimal('0.00000')
    max = Decimal('0.99999')
    while min != max:
        file.write('{0}:{1}\n'.format(min, digest('{0:.5f}'.format(min))))
        min += range
    file.close()


if __name__ == "__main__":
    main()
