import struct

format = '5s'
print struct.calcsize(format)
s = struct.pack(format,'12345')
print '%s'%s
s = struct.unpack(format,s)
print '%s'%s
