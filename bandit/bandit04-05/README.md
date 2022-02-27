# Bandit Level 4 -> Level 5

## Level Goal   
The password for the next level is stored in the only human-readable file in the `inhere` directory.

---

## Walkthrough

Login to the server using the password obtained from the previous level [Bandit level 3 -> 4](../bandit03-04/README.md). 

username: `bandit4` 

```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
```

We run `ls inhere` to see what files are in the `inhere` directory.  

```bash
bandit4@bandit:~$ ls inhere/
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
```

There are 10 files which have names that are not descriptive.  
We can use `cat` on each file to find the human readable file but can use another command to see what information is in each file without reading the contents.  
The `file` command can be used to find out what data is stored in a file.  

Now we use the `file` command to get information on each file in the `inhere` directory.  

```bash
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
Use `cat` command to print the contents of the file which is the password for the next level.

```bash
bandit4@bandit:~$ cat ./inhere/-file07
koReBO##########################
```