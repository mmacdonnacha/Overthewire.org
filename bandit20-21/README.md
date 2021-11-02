# Bandit Level 20 -> Level 21

## Level Goal 
There is a setuid binary in the homedirectory that does the following:  
it makes a connection to localhost on the port you specify as a commandline argument.  
It then reads a line of text from the connection and compares it to the password in the previous level (bandit20).  
If the password is correct, it will transmit the password for the next level (bandit21).

**NOTE:** Try connecting to your own network daemon to see if it works as you think

---

## Walkthrough  

Login to the server using the password obtained from the previous level [Bandit level 19 -> 20](../bandit19-20/README.md). 

username: `bandit20` 

```
ssh bandit20@bandit.labs.overthewire.org -p 2220
```

Like the previous level we will be using a setuid binary file. We can run it to find out how to use it correctly.

```
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ ./suconnect 
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.        

bandit20@bandit:~$
```

So `suconnect` will accept a port number as an argument and try to receive the password from the other side, if the password is correct `suconnect` will send the new password to the other side.

One problem is that there is nothing for `suconnect` to connect to. The challenge is for us to create a network daemon that will send the correct passowrd to `suconnect` and then receive the new password back.

We can create this daemon using python. First we define a `host` '127.0.0.1' and a `port` of our own choosing. We then bind them together and open connection. Then we send the current password and print out the new password to the screen.  
Here is the python code I used.

```python
#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' # localhost
PORT = 4444 # Change to what ever port you want

# Password for bandit20
PASSWORD = 'GbKksE##########################' 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        conn.sendall(bytes(PASSWORD, "utf-8"))
        data = conn.recv(1024)
        print(data.decode('utf-8'))
```

Lets create a directory in `/tmp` to write our python script and run it using python3. While our python script is running it will not print anything to screen until `suconnect` has run. Now either use tmux, screen or login to bandit20 from a different terminal so that we have 2 sessions on bandit20.

In Session 1 our python script is running and in session 2 we will run `suconnect` using the same port that is in the python script. Assuming the correct password was provided the python script will receive the new password.

```
Session 1

bandit20@bandit:~$ mkdir /tmp/mike
bandit20@bandit:~$ cd /tmp/mike

bandit20@bandit:/tmp/mike$ vim server.py
bandit20@bandit:/tmp/mike$ ls
server.py

bandit20@bandit:/tmp/mike$ python3 server.py
gE269g##########################

bandit20@bandit:/tmp/mike$
```

```
Session 2

bandit20@bandit:~$ ./suconnect 4444
Read: GbKksE########################## 
Password matches, sending next password

bandit20@bandit:~$
```