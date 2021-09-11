#!/usr/bin/env python3

import socket, time, sys, struct

ip = ""
port = 
timeout = 5

prefix = b""
fuzz = b"A" * 100
payload = prefix + fuzz

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      print("Fuzzing with {} bytes".format(len(payload) - len(prefix)))
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      s.send(payload)
      s.recv(1024)
  except:
    print("Fuzzing crashed at {} bytes".format(len(payload) - len(prefix)))
    sys.exit(0)
  payload += b"A" * 100
  time.sleep(1)
