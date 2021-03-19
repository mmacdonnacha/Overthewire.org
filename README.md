# Overthewire.org - Bandit

[OverTheWire - Bandit](https://overthewire.org/wargames/bandit/)

Table of Contents  
[Bandit Level 00 -> Level 01](#bandit-level-0-->-level-1)  
[Bandit Level 01 -> Level 02](#bandit-level-1-->-level-2)  
[Bandit Level 02 -> Level 03](#bandit-level-2-->-level-3)  
[Bandit Level 03 -> Level 04](#bandit-level-3-->-level-4)  
[Bandit Level 04 -> Level 05](#bandit-level-4-->-level-5)  
[Bandit Level 05 -> Level 06](#bandit-level-5-->-level-6)  
[Bandit Level 06 -> Level 07](#bandit-level-6-->-level-7)  
[Bandit Level 07 -> Level 08](#bandit-level-7-->-level-8)  
[Bandit Level 08 -> Level 09](#bandit-level-8-->-level-9)  
[Bandit Level 09 -> Level 10](#bandit-level-9-->-level-10)  
[Bandit Level 10 -> Level 11](#bandit-level-10-->-level-11)  



---

## Bandit Level 0 -> Level 1  
### Level Goal  
The password for the next level is stored in a file called **readme** located in the home directory.  
Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.  

**Walkthrough**  
Login to the server  

```
ssh bandit0@bandit.labs.overthewire.org -p 2220

Use the password: bandit0  
```

The Level Goal states the password for the next level in the file **readme**
Reading the contents of readme to get the password.

```shell
bandit0@bandit:~$ cat readme 
```


---


## Bandit Level 1 -> Level 2
### Level Goal  
The password for the next level is stored in a file called **-** located in the home directory

**Walkthrough**   
Login to the server  

```
ssh bandit1@bandit.labs.overthewire.org -p 2220

Use the password obtained from the previous level  
```

Running *ls* command we can see a single file with the name *-*.  
Running '*cat -*' does not print the contents of the file *-*.  
We need to give the path to the file for the cat command to print the contents.
```shell 
bandit1@bandit:~$ ls 
-
bandit1@bandit:~$ cat ./-  
```


---


## Bandit Level 2 -> Level 3  
### Level Goal 
The password for the next level is stored in a file called **spaces in this filename** located in the home directory

**Walkthrough**  
Login to the server  

```
ssh bandit2@bandit.labs.overthewire.org -p 2220

Use the password obtained from the previous level  
```

This time there is a file with spaces in the name.  
Running *'cat spaces in the filename'* will cause errors as it will think each word is its own file.  
Printing the contents of the file can be done 2 ways.  
One using *\\* before each space to indicate to the terminal that the filename continues and the other is surrounding the file name with quotes *'* or *"*. 
```shell
bandit2@bandit:~$ ls 
spaces in this filename 

bandit2@bandit:~$ cat spaces in this filename
cat: spaces: No such file or directory 
cat: in: No such file or directory 
cat: this: No such file or directory
cat: filename: No such file or directory

bandit2@bandit:~$ cat 'spaces in this filename'
bandit2@bandit:~$ cat spaces\ in\ this\ filename
```


---


## Bandit Level 3 -> Level 4  
### Level Goal  
The password for the next level is stored in a hidden file in the **inhere** directory.

**Walkthrough**  
Login to the server  

```
ssh bandit3@bandit.labs.overthewire.org -p 2220

Use the password obtained from the previous level  
```

Change directory into *inhere*, running *ls* command will show no files.  
Running *ls -al* will let us see all files including hidden files.  
We can then see a file named *.hidden*.  
The you can print to screen using *cat* command.

```shell
bandit3@bandit:~/inhere$ ls  
bandit3@bandit:~/inhere$ ls -al  
total 12  
drwxr-xr-x 2 root    root    4096 May  7  2020 . 
drwxr-xr-x 3 root    root    4096 May  7  2020 ..  
-rw-r----- 1 bandit4 bandit3   33 May  7  2020 .hidden  

bandit3@bandit:~/inhere$ cat ./.hidden
```


---


## Bandit Level 4 -> Level 5 
### Level Goal   
The password for the next level is stored in the only human-readable file in the **inhere** directory.

**Walkthrough**  
Login to the server  

```
ssh bandit4@bandit.labs.overthewire.org -p 2220

Use the password obtained from the previous level  
```

We run *ls inhere* to see what files are in the *inhere* directory.  

```shell
bandit4@bandit:~$ ls inhere/
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
```

There are 10 files which have names that are not descriptive.  
Here we use the *file* command to get information on each file in the *inhere* directory.  

```
bandit4@bandit:~$ file inhere/*  
inhere/-file00: data 
inhere/-file01: data  
inhere/-file02: data
inhere/-file03: data
inhere/-file04: data 
inhere/-file05: data 
inhere/-file06: data
inhere/-file07: ASCII text
inhere/-file08: data
inhere/-file09: data
```

We can see one file contains ASCII text which is human readable.  
Use *cat* command to print the password to the screen.

```shell
bandit4@bandit:~$ cat ./inhere/-file07
```


---


## Bandit Level 5 -> Level 6  
### Level Goal   
The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:

* human-readable  
* 1033 bytes in size  
* not executable  

**Walkthrough**  
Login to the server  

```
ssh bandit5@bandit.labs.overthewire.org -p 2220

Use the password obtained from the previous level  
```

Running *ls* on the inhere directory will give us 20 more directories.  
Each of those directories contains multiple files.  

```
bandit5@bandit:~$ ls inhere/
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17

bandit5@bandit:~$ ls inhere/maybehere00
-file1  -file2  -file3  spaces file1  spaces file2  spaces file3
```

We could run *cat* on each file but that would take a long time to complete.  
Instead we use the *find* command to find all file (*-type f*) of size 1033 bytes (*-size 1033c*) not executable (*-not -executable*) to get a list all files with those properties.  
There is only 1 file with all 3 properties.  
As before *cat* the file to print its content to screen.

```shell
bandit5@bandit:~$ find ./inhere/ -type f -size 1033c -not -executable
./inhere/maybehere07/.file2

bandit5@bandit:~$ cat ./inhere/maybehere07/.file2
```


---


## Bandit Level 6 -> Level 7  
### Level Goal   
The password for the next level is stored **somewhere on the server** and has all of the following properties:

* owned by user bandit7
* owned by group bandit6
* 33 bytes in size

**Walkthrough**  
Login to the server  

```
ssh bandit6@bandit.labs.overthewire.org -p 2220

Use the password obtained from the previous level  
```

Use **find** again to search the whole server **/**  
for files **-type f**  
that are owned by bandit7 **-user bandit7**  
and are part of the group bandit6 **-group bandit6**  
with a size of 33 bytes **-size 33c**.  

The **2>/dev/null** part of the command will not print errors such as permission denied to the screen.

```shell
bandit6@bandit:~$ find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
```


---


## Bandit Level 7 -> Level 8
### Level Goal   
The password for the next level is stored in the file **data.txt** next to the word **millionth**.

**Walkthrough**  
Login to the server  

```
ssh bandit7@bandit.labs.overthewire.org -p 2220

Use the password obtained from the previous level  
```

The *grep* command can be used to search files for specific words or string of text.  
Use *grep* to find the line containing word 'millionth' in the file 'data.txt' and print the lines to the screen.

```shell
bandit7@bandit:~$ grep millionth data.txt
```

---

## Bandit Level 8 -> Level 9
### Level Goal
The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once

**Walkthrough**  
Login to the server  

```
ssh bandit8@bandit.labs.overthewire.org -p 2220

Use the password obtained from the previous level  
```

The file contains lots of repeating lines of text so we first *sort* the contents of the file and then use *uniq* to remove repeating lines and the *-u* option will give us only unique lines of text in the file.

```shell
bandit8@bandit:~$ sort data.txt | uniq -u
```


---



## Bandit Level 9 -> Level 10
### Level Goal 
The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

**Walktrough**  
Login to the server  

```
ssh bandit9@bandit.labs.overthewire.org -p 2220

Use the password obtained from the previous level  
```

Use *strings* to get all the human readable text in the file and then *grep* on that text to find the line containing several '=' characters.

```shell
bandit9@bandit:~$ strings data.txt | grep ====
```


---


## Bandit Level 10 -> Level 11
### Level Goal
The password for the next level is stored in the file **data.txt**, which contains base64 encoded data.

**Walkthrough**  
Login to the server  

```
ssh bandit10@bandit.labs.overthewire.org -p 2220

Use the password obtained from the previous level  
```

Use *cat* to print the information in data.txt and then decode it using *base64 -d*

```shell
bandit10@bandit:~$ cat data.txt | base64 -d
```

---

## Bandit 11
**Level Goal**   
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

Rotated by 13 positions means a -> n, b -> o ... y -> l, z -> m  
We *cat* the contents of the file and pipe it to *tr* (translate) command to change all letters by 13 positions.

---

## Bandit 12
**Level Goal**   

```
bandit12@bandit:/tmp/micheal$ file data.txt
data.txt: ASCII text
bandit12@bandit:/tmp/micheal$ cat data.txt
00000000: 1f8b 0808 0650 b45e 0203 6461 7461 322e  .....P.^..data2.
00000010: 6269 6e00 013d 02c2 fd42 5a68 3931 4159  bin..=...BZh91AY
00000020: 2653 598e 4f1c c800 001e 7fff fbf9 7fda  &SY.O...........
00000030: 9e7f 4f76 9fcf fe7d 3fff f67d abde 5e9f  ..Ov...}?..}..^.
00000040: f3fe 9fbf f6f1 feee bfdf a3ff b001 3b1b  ..............;.
00000050: 5481 a1a0 1ea0 1a34 d0d0 001a 68d3 4683  T......4....h.F.
00000060: 4680 0680 0034 1918 4c4d 190c 4000 0001  F....4..LM..@...

bandit12@bandit:/tmp/micheal$ xxd -r data.txt data.out
bandit12@bandit:/tmp/micheal$ file *
data.out: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
data.txt: ASCII text
bandit12@bandit:/tmp/micheal$ gunzip data.out
gzip: data.out: unknown suffix -- ignored
bandit12@bandit:/tmp/micheal$ gunzip -S ".out" data.out
bandit12@bandit:/tmp/micheal$ ls
data  data.txt
bandit12@bandit:/tmp/micheal$ file *
data:     bzip2 compressed data, block size = 900k
data.txt: ASCII text
bandit12@bandit:/tmp/micheal$ bzip2 -d data
bzip2: Can't guess original name for data -- using data.out
bandit12@bandit:/tmp/micheal$ file *
data.out: gzip compressed data, was "data4.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
data.txt: ASCII text
bandit12@bandit:/tmp/micheal$ gunzip -S ".out" data.out
bandit12@bandit:/tmp/micheal$ ls
data  data.txt

bandit12@bandit:/tmp/micheal$ ls
data  data.txt
bandit12@bandit:/tmp/micheal$ file data
data: POSIX tar archive (GNU)
bandit12@bandit:/tmp/micheal$ tar xvf data
data5.bin
bandit12@bandit:/tmp/micheal$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/micheal$ tar xvf data5.bin
data6.bin
bandit12@bandit:/tmp/micheal$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/micheal$ bzip2 -d data6.bin
bzip2: Can't guess original name for data6.bin -- using data6.bin.out
bandit12@bandit:/tmp/micheal$ file data6.bin.out
data6.bin.out: POSIX tar archive (GNU)
bandit12@bandit:/tmp/micheal$ tar xvf data.bin.out
tar: data.bin.out: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
bandit12@bandit:/tmp/micheal$ tar xvf data6.bin.out
data8.bin
bandit12@bandit:/tmp/micheal$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
bandit12@bandit:/tmp/micheal$ gunzip -S ".bin" data8.bin
bandit12@bandit:/tmp/micheal$ ls
data  data5.bin  data6.bin.out  data8  data.txt
bandit12@bandit:/tmp/micheal$ file data
data: POSIX tar archive (GNU)
bandit12@bandit:/tmp/micheal$ file data8
data8: ASCII text
bandit12@bandit:/tmp/micheal$ cat data8

xxd -r data.txt data.out
gunzip -S ".out" data.out
bzip2 -d data
gunzip -S ".out" data.out
tar xvf data
tar xvf data5.bin
bzip2 -d data6.bin
tar xvf data6.bin.out
gunzip -S ".bin" data8.bin
cat data8

```
---

## Bandit 13
**Level Goal**   

ssh -i sshprivate bandit14@localhost

---

## Bandit 14

echo "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e" | nc localhost 30000

---

## Bandit 15

bandit15@bandit:~$ openssl s_client -connect localhost:30001
"enter password for current level"

---

## Bandit 16
nmap -sV -oA /tmp/mike/ -p 31000-32000 localhost
grep open nmap.nmap

bandit16@bandit:~$ openssl s_client -connect localhost:31790
"create ssh key"
chmod 700 key
ssh -i key bandit17@localhost

---

## Bandit 17
diff password.new password.old

---

## Bandit 18
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"

---

## Bandit 19
./bandit20-do cat /etc/bandit_pass/bandit20

---

## Bandit 20

bandit20@bandit:/tmp/blah$ grep open nmap.nmap
22/tcp    open  ssh                 OpenSSH 7.4p1 (protocol 2.0)
30000/tcp open  ndmps?


nmap -sV -sC -oA nmap localhost
- to find open ports
- port 30000 is looking for a password

'nc localhost 30000' gets a response
strings on 'suconnect' shows that it is checking /home/bandit21/.prevpass 
I assume it compares the contents of .prevpass with the input we provide but the programm does not complete


---
## Bandit 21
**Level Goal**   
There is a setuid binary in the homedirectory that does the following:  
it makes a connection to localhost on the port you specify as a commandline argument.  
It then reads a line of text from the connection and compares it to the password in the previous level (bandit20).  
If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

'''setup python server to send password with connected  
receive new password from suconnect  
print to screen'''