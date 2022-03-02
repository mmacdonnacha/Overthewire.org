# Leviathan Level 7

## Level Goal  

There is no information for this level, intentionally.


## Walkthrough 
Login to the server using the password obtained from the previous level [Leviathan level 6](../leviathan6/README.md). 

username: `leviathan7` 

```ssh
ssh leviathan7@leviathan.labs.overthewire.org -p 2223
```

This is not an actual challenge so there is nothing to do except read a file.

Checking the home directory there is a file `CONGRATUALATION` and reading the file will give a congratulation message.

```console
leviathan7@leviathan:~$ ls
CONGRATULATIONS

leviathan7@leviathan:~$ cat CONGRATULATIONS 
Well Done, you seem to have used a *nix system before, now try something more serious.
```