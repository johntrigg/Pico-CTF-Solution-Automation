import os
import re#regular expression to find the flag
import pwn #from pwn import remote as brandon

def whatsANetCat():
    pwn.context.log_level = "error"

    url = "jupiter.challenges.picoctf.org"

    port = 25103

    r = pwn.remote(url, port)

    output = r.recvall().decode()

    print(output)

    flag = re.findall(r"picoCTF{.*?}", output)[0]#take the output, find the first occurance of the regex, and put it into var flag

    print(flag)#print the flag found via regex

whatsANetCat()