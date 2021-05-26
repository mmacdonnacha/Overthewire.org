# Bandit Level 1 -> Level 2

## Level Goal  

The password for the next level is stored in a file called `-` located in the home directory

## Walkthrough   
Login to the server using the password obtained from the previous level [Bandit level 0 -> 1](../bandit00-01/README.md).  

username: `bandit1`

```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
```

Running `ls` command we can see a single file with the name `-`.  

```bash 
bandit1@bandit:~$ ls 
-
```

Running `cat -` does not print the contents of the file `-` as the cat command thinks you are setting an option like `-n` for line numbers.  
We need to give the path to the file for the cat command to print the contents.

```bash
bandit1@bandit:~$ cat ./-  
CV1Dtq##########################
```