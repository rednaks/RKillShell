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
    self.stream = self.sock.recv(1024)
  
  def send(self, msg):
    self.sock.send(msg)

  def prompt(self):
    self.cmd = raw_input('ghost >> ')

  def processCMD(self):
    msg = re.sub(' ', ':', self.cmd)
    return msg

  def parseStream(self):
    print self.stream

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


