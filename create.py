# coding: utf-8
# -*- coding:utf-8 -*-
import uuid


def act():
    file_name = "シリアルコード.txt"
    rets = []
    with open(file_name, mode='w') as f:
        write_count = 0
        for cnt in range(10000):
            ret = str(uuid.uuid4())
            ret = ret.replace("-", "")
            ret = ret.replace("i", "")
            ret = ret.replace("l", "")
            ret = ret.replace("o", "")
            ret = "{}\n".format(ret[:8])
            ret = ret.upper()

            if ret not in rets:
                write_count = write_count + 1
                rets.append(ret)
                f.write(ret)

            if write_count == 1000:
                break

    print(write_count)


if __name__ == '__main__':
    act()
