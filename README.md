# Overthewire.org - Bandit

[OverTheWire - Bandit](https://overthewire.org/wargames/bandit/)

Table of Contents  
[Bandit 00](#bandit-0)  
[Bandit 01](#bandit-1)  
[Bandit 02](#bandit-2)  
[Bandit 03](#bandit-3)  
[Bandit 04](#bandit-4)  
[Bandit 05](#bandit-5)  
[Bandit 06](#bandit-6)  
[Bandit 07](#bandit-7)  
[Bandit 08](#bandit-8)  
[Bandit 09](#bandit-9)  
[Bandit 10](#bandit-10)  
[Bandit 11](#bandit-11)  

---

## Bandit 0  
**Description**  
The password for the next level is stored in a file called readme located in the home directory. 

Printing file contents to screen will give the password.
```shell
bandit0@bandit:~$ cat readme 
```

---

## Bandit 1  
**Description** 
The password for the next level is stored in a file called - located in the home directory

Running *ls* command we can see a single file with the name *-*  
running '*cat -*' does not work.  
We need to give the path to the file for the cat command to print the contents.
```shell 
bandit1@bandit:~$ cat ./- 
```

---

## Bandit 2  
**Description** 
The password for the next level is stored in a file called *'spaces in this filename'* located in the home directory

This time there is a file with spaces in the name.  
Running *'cat spaces in the filename'* will cause errors as it will think each word is its own file.  
Print the contents of the file can be done 2 ways. One using *\\* before each space and the other is surrounding the file name with quotes. 
```shell
bandit2@bandit:~$ cat spaces\ in\ this\ filename

bandit2@bandit:~$ cat "spaces in this filename"
```
---

## Bandit 3  
**Description** 
The password for the next level is stored in a hidden file in the inhere directory.

Change directory into *inhere*, running *ls* command will show no files.  
Running *ls -al* will let us see all files including hidden files.  
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

## Bandit 4  
**Description**  
The password for the next level is stored in the only human-readable file in the inhere directory.

Here we use the *file* command to get information on each file in the *inhere* directory.  
We can then pipe the output of the file command into *grep* to find the only file with ASCII text (human readable).  
Use *cat* command to print the contents of the file to the screen.

```shell
bandit4@bandit:~$ file ./inhere/* | grep ASCII
```

---

## Bandit 5  
**Description**  
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

* human-readable  
* 1033 bytes in size  
* not executable  

We can use the *find* command to find all file (*-type f*) of size 1033 bytes (*-size 1033c*) not executable (*-not -executable*) to get a list all files with those properties.  
Then run *file* to determine what type of content they contain and *grep* for only files containing human readable text.  
As before *cat* the file to print its content to screen.

```shell
bandit5@bandit:~$ find ./inhere/ -type f -size 1033c -not -executable -exec file {} + | grep ASCII
```

---

## Bandit 6  
**Description**  
The password for the next level is stored somewhere on the server and has all of the following properties:

* owned by user bandit7
* owned by group bandit6
* 33 bytes in size

Use *find* again to search the whole server (*/*) for files (*-type f*) that are owned by bandit7 (*-user bandit7*) and are part of the group bandit6 (*-group bandit6*) with a size of 33 bytes (*-size 33c*).  
The *2>/dev/null* part of the command will not print errors such as permission denied to the screen.

```shell
bandit6@bandit:~$ find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

---

## Bandit 7
**Description**  
The password for the next level is stored in the file data.txt next to the word *millionth*

Use *grep* to find the line containing word 'millionth' in the file 'data.txt' and print the lines to the screen.

```shell
bandit7@bandit:~$ grep millionth data.txt
```

---

## Bandit 8
**Description**  
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

The file contains lots of repeating lines of text so we first *sort* the contents of the file and then use *uniq* to remove repeating lines and the *-u* will give us the only unique line of text in the file.

```shell
bandit8@bandit:~$ sort data.txt | uniq -u
```

---

## Bandit 9
**Description**  
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

Use *strings* to see the human readable text in the file and then *grep* to find the line containing several '=' characters.

```shell
bandit9@bandit:~$ strings data.txt | grep ====
```

---

## Bandit 10
**Description**  
The password for the next level is stored in the file data.txt, which contains base64 encoded data.

Use *cat* to print the information in data.txt and then decode it using *base64 -d*

```shell
bandit10@bandit:~$ cat data.txt | base64 -d
```

---

## Bandit 11
**Description**  
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

Rotated by 13 positions means a -> n, b -> o ... y -> l, z -> m  
We *cat* the contents of the file and pipe it to *tr* (translate) command to change all letters by 13 positions.

```shell
bandit11@bandit:~$ cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'
```

---