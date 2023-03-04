import telnetlib
import time


session = telnetlib.Telnet('192.168.0.190')
session.read_until(b'login:')
session.write(b'gena\n')
session.read_until(b'Password:')
session.write(b'595632383447\n')
session.read_until(b'>')
session.write(b'enable\n')
session.read_until(b'Password:')
session.write(b'fastcom236\n')
session.read_until(b'#')
session.write(b'terminal length 0\n')
session.write(b'sho mac-address-table\n')
time.sleep(1)
result = session.read_very_eager().decode('utf-8')
# print(result)

with open('qtech.txt', 'w') as qtech:
    qtech.write(str(result))
# # if 'wire-down' in result:
# #     print(f'Interface: {result[0]}, status: {result[6]}, time: {result[7]}')
# # print(result)
#
# with open('bdcom.txt', 'r') as bdcom:
#     for x in bdcom:
#         print(x)


# print(''.join(result))
# print(session.read_very_eager().decode('utf-8'))
