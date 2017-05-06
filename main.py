import pexpect
child = pexpect.spawn("telnet 54.250.224.118 32773")
child.sendline("\r\n")
child.expect(">")
child.sendline("enable")
child.expect("#")
child.sendline("config terminal")
child.expect("#")
child.sendline("hostname Router1")
child.expect("#")
child.sendline("end")
child.expect("#")


