# Bandit Level 3 -> Level 4

## Level Goal  
The password for the next level is stored in a hidden file in the `inhere` directory.

---

## Walkthrough  
Login to the server using the password obtained from the previous level [Bandit level 2 -> 3](../bandit02-03/README.md). 

username: `bandit3` 

```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
```

Change directory into `inhere`, running `ls` command will show no files.  

```bash
bandit3@bandit:~/inhere$ ls  

```

Running `ls -al` will let us see all files including hidden files.  
We can then see a file named `.hidden`.  
The you can print to screen using `cat` command.

```bash
bandit3@bandit:~/inhere$ ls -al  
total 12  
drwxr-xr-x 2 root    root    4096 May  7  2020 . 
drwxr-xr-x 3 root    root    4096 May  7  2020 ..  
-rw-r----- 1 bandit4 bandit3   33 May  7  2020 .hidden  

bandit3@bandit:~/inhere$ cat ./.hidden
```