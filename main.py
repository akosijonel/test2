import pexpect
child = pexpect.spawn("telnet 54.250.224.118 32773")
child.sendline("\r\n")
child.expect(">")
child.sendline("enable\r\n")
child.expect("#")
child.sendline("config terminal\r\n")
child.expect("#")
child.sendline("hostname Router1\r\n")
child.expect("#")
child.sendline("end\r\n")
child.expect("#")


