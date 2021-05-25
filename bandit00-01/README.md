# Bandit Level 0 -> Level 1

## Level Goal  

The password for the next level is stored in a file called `readme` located in the home directory.  
Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.  

## Walkthrough 
Login to the server using the provided username and password.  
username: `bandit0`  
password: `bandit0`

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

Enter the password when prompted to login to the level.  

The Level Goal states the password for the next level in the file `readme`.  
Reading the contents of readme to get the password.

```bash
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme 
```