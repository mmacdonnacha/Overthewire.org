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

## Bandit 1  
**Description** 
The password for the next level is stored in a file called - located in the home directory

running *ls* command we can see a single file with the name *-*  
runnging cat - does not work, so this time we give cat the relative path to the file
```shell
bandit1@bandit:~$ cat ./- 
```

## Bandit 2  
**Description** 
The password for the next level is stored in a file called spaces in this filename located in the home directory

This time there is a file with spaces in the name
running cat spaces in the filename will cause errors as it will think each word is its own file
print the contents of the file can be done 2 ways
```shell
bandit2@bandit:~$ cat spaces\ in\ this\ filename

bandit2@bandit:~$ cat "spaces in this filename"
```

## Bandit 3  
**Description** 
The password for the next level is stored in a hidden file in the inhere directory.

The new challenge here is hidden folders  
When we login to bandit3 we can see a folder *inhere*  
After changing directory into *inhere* it appears to be empty.  
running ls -al will let us see all files including hidden files.
now we see a file called *.hidden*

```shell
bandit3@bandit:~/inhere$ ls  
bandit3@bandit:~/inhere$ ls -al  
total 12  
drwxr-xr-x 2 root    root    4096 May  7  2020 . 
drwxr-xr-x 3 root    root    4096 May  7  2020 ..  
-rw-r----- 1 bandit4 bandit3   33 May  7  2020 .hidden  

bandit3@bandit:~/inhere$ cat ./.hidden
```

## Bandit 4  
**Description**  
The password for the next level is stored in the only human-readable file in the inhere directory.
```
bandit4@bandit:~$ file ./inhere/* | grep ASCII
```


## Bandit 5  
**Description**  
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

* human-readable  
* 1033 bytes in size  
* not executable  

```
bandit5@bandit:~$ find ./inhere/ -readable -size 1033c -not -executable
```

## Bandit 6  
**Description**  
The password for the next level is stored somewhere on the server and has all of the following properties:

* owned by user bandit7
* owned by group bandit6
* 33 bytes in size

```
bandit6@bandit:~$ find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

## Bandit 7
**Description**  
The password for the next level is stored in the file data.txt next to the word *millionth*

```
grep millionth data.txt
```

## Bandit 8
**Description**  
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

```
sort data.txt | uniq -u
```

## Bandit 9
**Description**  
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.
```
strings data.txt | grep ===
```
## Bandit 10
**Description**  
The password for the next level is stored in the file data.txt, which contains base64 encoded data.

```
cat data.txt | base64 -d
```

## Bandit 11
**Description**  
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

```
cat data.txt | tr [:upper:] [:lower:] | tr 'a-z' 'n-za-m'
```

