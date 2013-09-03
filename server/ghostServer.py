import socket
from utils import *


class GhostServer():
  def __init__(self, addr):
    self.stream = ''
    self.conn = None
    self.addr = None
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind(addr)
    self.sock.listen(1)
  
  def receive(self):
    self.stream = self.conn.recv(128)

  def send(self, msg):
    self.conn.send(msg)

  def processing(self):
    #TODO do some processing: parsing the message, executings commands, 
    print 'Processing ', self.stream
    return None

  def serve_forever(self):
    print 'Serving ...'
    self.conn, self.addr = self.sock.accept()
    print 'Connected from ', self.addr
    while True:
      self.receive()
      if(not self.stream):
       break
      haveSomeThingToSay = self.processing()
      if(haveSomeThingToSay is not None):
        slef.send(haveSomeThingToSay)

    print 'Loop broken'
    # once outside of the loop we close the actual connection and start wating for a new one
    self.conn.close()
    self.serve_forever()

  def close(self):
    self.sock.close()
