#!/usr/bin/python

import socket
import re

class GhostClient():
  def __init__(self, addr):
    self.stream = ''
    self.cmd = ''
    self.addr = addr
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def connect(self):
    self.sock.connect(self.addr)

  def close(self):
    self.sock.close()

  def recieve(self):
    self.stream = self.sock.recv(4096)
  
  def send(self, msg):
    self.sock.send(msg)

  def prompt(self):
    self.cmd = raw_input('ghost >> ')

  def processCMD(self):
    msg = re.sub(' ', ':', self.cmd)
    return msg

  def parseStream(self):
    splitted = self.stream.split(',')
    if(len(splitted) == 1):
      print self.stream
    else:
      #So it's a list of pids !
      print "PID      Name"
      for p in splitted:
        ps = p.split('|')
        print "%s      %s" %(ps[0], ps[1])

  def command_forever(self):
    self.connect()
    while True:
      self.prompt()
      if(self.cmd):
        msgToSend = self.processCMD()
        if(msgToSend):
          self.send(msgToSend)
          self.recieve()
          if(not self.stream): break
          self.parseStream()

    self.close()


if __name__ == '__main__':
  gc = GhostClient(('127.0.0.1', 9999))
  gc.command_forever()


