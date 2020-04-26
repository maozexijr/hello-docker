"""
hello docker
"""
import configparser
import os
import time
import traceback


def config():
    cwd = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(cwd, 'config.ini')
    print('%s' % path)

    # 读配置文件
    conf = configparser.ConfigParser()
    conf.read(path, encoding='utf-8')
    return int(conf.get("PROPERTIES", "interval"))


def hello():
    # 简单输出
    at_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print('[%s] hello docker ~' % at_time)


if __name__ == '__main__':
    try:
        # 循环间隔，秒
        interval = config()

        while True:
            hello()
            time.sleep(interval)
    except:
        traceback.print_exc()
