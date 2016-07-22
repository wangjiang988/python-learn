#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
# Author: ChenLiang

# 进程池
from multiprocessing import Pool
import time


def f1(args):
    time.sleep(1)
    print(args)
# win if __name__ == '__main__':
pool = Pool(5)

for i in range(30):
    # pool.apply(func=f1, args=(i, ))
    pool.apply_async(func=f1, args=(i, ))

# pool.close()  # 所有任务执行完毕才往下走
time.sleep(1)
pool.terminate()  # 立即结束
pool.join()  # 主线程执行完成, 子线程不再执行