# Overthewire.org - Bandit

**Bandit 0**  
Password for bandit1 is located in a readme file  
Printing file contents to screen will give the password.
```shell
bandit0@bandit:~$ cat readme 
```

**Bandit 1**  
running *ls* command we can see a single file with the name *-*  
runnging cat - does not work, so this time we give cat the relative path to the file
```shell
bandit1@bandit:~$ cat ./- 
```

**Bandit 2**  
This time there is a file with spaces in the name
running cat spaces in the filename will cause errors as it will think each word is its own file
print the contents of the file can be done 2 ways
```shell
bandit2@bandit:~$ cat spaces\ in\ this\ filename

bandit2@bandit:~$ cat "spaces in this filename"
```

**Bandit 3**  
The new challenge here is hidden folders  
When we login to bandit3 we can see a folder *inhere*  
After changing directory into *inhere* it appears to be empty.  
running ls -al will let us see all files including hidden files.
now we see a file called *.hidden*
```shell
bandit3@bandit:~/inhere$ cat .hidden 
bandit3@bandit:~/inhere$ cat .hidden 
bandit3@bandit:~$ cd inhere/  
bandit3@bandit:~/inhere$ ls  
bandit3@bandit:~/inhere$ ls -al  
total 12  
drwxr-xr-x 2 root    root    4096 May  7  2020 . 
drwxr-xr-x 3 root    root    4096 May  7  2020 ..  
-rw-r----- 1 bandit4 bandit3   33 May  7  2020 .hidden  

bandit3@bandit:~/inhere$ cat ./.hidden
```