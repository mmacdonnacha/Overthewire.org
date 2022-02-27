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
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls  

```

Running `ls -a` will let us see all files including hidden files.  
`-a` for all files (do not ignore entries starting with .)  
We can then see a file named `.hidden`.  
The you can print to screen using `cat` command.

```bash
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ cat ./.hidden
pIwrPr##########################
```