# import telnetlib
# import time
#
#
# session = telnetlib.Telnet('192.168.2.112')
# session.read_until(b'Username:')
# session.write(b'gena\n')
# session.read_until(b'Password:')
# session.write(b'595632383447\n')
# session.read_until(b'>')
# session.write(b'ena\n')
# session.write(b'sho epon inactive-onu\n')
# # session.write(b'sho epon act\n')
# # session.read_until(b'sho epon act')
# time.sleep(1)
# output = session.read_very_eager().decode('utf-8')
#
# with open('bdcom1210.txt', 'w') as bdcom1210:
#     bdcom1210.write(str(output))

with open(r"bdcom1210.txt", "r") as file:
    for line in file:
        if 'wire-down' in line:
            print(line.split())
