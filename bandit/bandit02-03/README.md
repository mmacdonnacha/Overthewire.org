# Bandit Level 2 -> Level 3

## Level Goal 
The password for the next level is stored in a file called `spaces in this filename` located in the home directory

## Walkthrough  
Login to the server using the password obtained from the previous level [Bandit level 1 -> 2](../bandit01-02/README.md). 

username: `bandit2`

```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
```

This time there is a file with spaces in the name.  
```bash
bandit2@bandit:~$ ls 
spaces in this filename 
```

Running `cat spaces in the filename` will cause errors as it will think each word in `spaces in the filename` is its own separate file.  

```bash
bandit2@bandit:~$ cat spaces in this filename
cat: spaces: No such file or directory 
cat: in: No such file or directory 
cat: this: No such file or directory
cat: filename: No such file or directory
```

Printing the contents of the file can be done 2 ways.  
One using `\` before each space to indicate to the terminal that the filename continues and the other is surrounding the file name with quotes `'` or `"`. 

```bash
bandit2@bandit:~$ cat 'spaces in this filename'
UmHadQ##########################
bandit2@bandit:~$ cat spaces\ in\ this\ filename
UmHadQ##########################
```