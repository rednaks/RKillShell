import socket
import utils

commands = {'list':utils.listAllPIDs, 'kill':utils.kill}

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
    res = None
    cmd = self.stream.split(':')
    if(cmd[0] in commands):
      if(len(cmd) < 2):
        res = commands[cmd[0]]()
      else:
        res = commands[cmd[0]](int(cmd[1]))

    return res

  def serve_forever(self):
    self.conn, self.addr = self.sock.accept()
    while True:
      self.receive()
      if(not self.stream):
       break
      haveSomeThingToSay = self.processing()
      if(haveSomeThingToSay is not None):
        self.send(haveSomeThingToSay)

    # once outside of the loop we close the actual connection and start wating for a new one
    self.conn.close()
    self.serve_forever()

  def close(self):
    self.sock.close()
