import os
import sys
import argparse
import logging.config


from server.config import default_configure_dir, Configure
from server.logger import worklog


def parse_argv():
    parser = argparse.ArgumentParser()
    parser.add_argument('--conf', metavar='CONF_DIR', default=default_configure_dir, help='Specify configure file')
    return parser.parse_args(sys.argv[1:])


if __name__ == '__main__':
    args = parse_argv()
    config = Configure(args.conf)

    logging.config.fileConfig(config.LoggingConfPath)
    logging.basicConfig(level=logging.DEBUG)

    print("Application begin to run... pid: {}".format(os.getpid()))
    worklog.debug("Application begin to run... pid: ")

    