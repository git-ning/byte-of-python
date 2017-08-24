#!/usr/bin/python

import os, platform, logging

if platform.platform().startswith('Windows'):
    # 写入日志文件的路径要注意，是否有写权限
    logging_file = os.path.join('D:\\workspace\\PycharmProjects\\byte-of-python', 'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')