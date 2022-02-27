# Bandit Level 27 → Level 28

## Level Goal

There is a git repository at `ssh://bandit27-git@localhost/home/bandit27-git/repo`.  
The password for the user `bandit27-git` is the same as for the user `bandit27`.

Clone the repository and find the password for the next level.

---

## Walkthrough

Login to the server using the password obtained from the previous level [Bandit level 26 -> 27](../bandit26-27/README.md). 

username: `bandit27` 

```ssh
ssh bandit27@bandit.labs.overthewire.org -p 2220
```


For this challenge we need to clone a git repository and search the repo for the password.  
First thing is to create a working directory to clone the repository into and then clone the repo.

```console
bandit27@bandit:~$ mkdir /tmp/bandit27
bandit27@bandit:~$ cd /tmp/bandit27

bandit27@bandit:/tmp/bandit27$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
Cloning into 'repo'...

bandit27-git@localhost's password:
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.

bandit27@bandit:/tmp/bandit27$
```

Now that the repo has been cloned we can change into the repo directory and start inspecting.  
Using `git log` we can check the history of the repo.

```console
bandit27@bandit:/tmp/bandit27$ ls
repo

bandit27@bandit:/tmp/bandit27$ cd repo/

bandit27@bandit:/tmp/bandit27/repo$ git log
commit 4d1369bc8d0c563b6e8e33aadeefb02311806526
Author: Ben Dover <noone@overthewire.org>
Date:   Thu May 7 20:14:47 2020 +0200

    initial commit of README

bandit27@bandit:/tmp/bandit27/repo$ 
```

`git log` only shows one commit so this means the repository was never changed after it was created. Reading the single file in the repo will give the password.


```console
bandit27@bandit:/tmp/bandit27/repo$ ls
README

bandit27@bandit:/tmp/bandit27/repo$ cat README 
The password to the next level is: 0ef186##########################
```