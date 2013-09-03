#!/usr/bin/python
from ghostServer import *


if __name__ == '__main__':
  gs = GhostServer(('127.0.0.1', 9999))
  gs.serve_forever()
