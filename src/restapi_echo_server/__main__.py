import argparse
import logging
import time
from . import server


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03dZ %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    logging.Formatter.converter = time.gmtime

    arg_parser = argparse.ArgumentParser(prog='restapi_echo_server')
    arg_parser.add_argument(
        '--host', 
        type=str,
        default='localhost',
        help='hostname or ipaddress to listen on',
    )
    arg_parser.add_argument(
        '--port',
        type=int, 
        default=8080,
        help='port to listen on',
    )

    args = arg_parser.parse_args()
    server.start(host=args.host, port=args.port)
