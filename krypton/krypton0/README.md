# Krypton Level 0 → Level 1

## Level Info

Welcome to Krypton! The first level is easy. The following string encodes the password using Base64:

```
S1JZUFRPTklTR1JFQVQ=
```

Use this password to log in to krypton.labs.overthewire.org with username krypton1 using SSH on port 2231.  
You can find the files for other levels in /krypton/


## Solution

The level info tells us how the text was encoded, it uses Base64 encoding.  
We can reverse the process using the `base64 -d` command.

```console
$ echo S1JZUFRPTklTR1JFQVQ= | base64 -d

KRYPTON*******
```