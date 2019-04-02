"""
1、导入模块logging

"""
# %(filename)s-%(lineno)d-%(levelname)s-%(filename)s
# demo10.py-10-ERROR-demo10.py
# demo10.py-11-INFO-demo10.py
# demo10.py-12-WARNING-demo10.py


import logging

logging.Formatter
logging.basicConfig(level=logging.DEBUG, filename='sys.log',
                    format="%(filename)s-%(lineno)d-%(levelname)s-%(filename)s")

logging.error("没有实例化")
logging.info("实例化")
logging.warning("警告信息")
