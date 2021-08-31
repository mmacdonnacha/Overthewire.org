# Bandit Level 13

## Level Goal

The password for the next level is stored in `/etc/bandit_pass/bandit14 and can only be read by user bandit14`. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. `Note: localhost` is a hostname that refers to the machine you are working on

---

## Walkthrough 
Login to the server using the password obtained from the previous level [Bandit level 12 -> 13](../bandit12-13/README.md). 

username: `bandit13` 

```
ssh bandit13@bandit.labs.overthewire.org -p 2220
```

This time the password is located in a file that we (bandit13) do not have read access to.  
We have been given an an SSH key to login to next level.  
The key is a file `sshkey.private` in the home directory.  

```
bandit13@bandit:~$ ls
sshkey.private

bandit13@bandit:~$ file sshkey.private 
sshkey.private: PEM RSA private key
```

Reading the contents of the sshkey shows alot of base64 encoding.

```
bandit13@bandit:~$ cat sshkey.private 
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxkkOE83W2cOT7IWhFc9aPaaQmQDdgzuXCv+ppZHa++buSkN+
gg0tcr7Fw8NLGa5+Uzec2rEg0WmeevB13AIoYp0MZyETq46t+jk9puNwZwIt9XgB
ZufGtZEwWbFWw/vVLNwOXBe4UWStGRWzgPpEeSv5Tb1VjLZIBdGphTIK22Amz6Zb
ThMsiMnyJafEwJ/T8PQO3myS91vUHEuoOMAzoUID4kN0MEZ3+XahyK0HJVq68KsV
ObefXG1vvA3GAJ29kxJaqvRfgYnqZryWN7w3CHjNU4c/2Jkp+n8L0SnxaNA+WYA7
jiPyTF0is8uzMlYQ4l1Lzh/8/MpvhCQF8r22dwIDAQABAoIBAQC6dWBjhyEOzjeA
J3j/RWmap9M5zfJ/wb2bfidNpwbB8rsJ4sZIDZQ7XuIh4LfygoAQSS+bBw3RXvzE
pvJt3SmU8hIDuLsCjL1VnBY5pY7Bju8g8aR/3FyjyNAqx/TLfzlLYfOu7i9Jet67
xAh0tONG/u8FB5I3LAI2Vp6OviwvdWeC4nOxCthldpuPKNLA8rmMMVRTKQ+7T2VS
nXmwYckKUcUgzoVSpiNZaS0zUDypdpy2+tRH3MQa5kqN1YKjvF8RC47woOYCktsD
o3FFpGNFec9Taa3Msy+DfQQhHKZFKIL3bJDONtmrVvtYK40/yeU4aZ/HA2DQzwhe
ol1AfiEhAoGBAOnVjosBkm7sblK+n4IEwPxs8sOmhPnTDUy5WGrpSCrXOmsVIBUf
laL3ZGLx3xCIwtCnEucB9DvN2HZkupc/h6hTKUYLqXuyLD8njTrbRhLgbC9QrKrS
M1F2fSTxVqPtZDlDMwjNR04xHA/fKh8bXXyTMqOHNJTHHNhbh3McdURjAoGBANkU
1hqfnw7+aXncJ9bjysr1ZWbqOE5Nd8AFgfwaKuGTTVX2NsUQnCMWdOp+wFak40JH
PKWkJNdBG+ex0H9JNQsTK3X5PBMAS8AfX0GrKeuwKWA6erytVTqjOfLYcdp5+z9s
8DtVCxDuVsM+i4X8UqIGOlvGbtKEVokHPFXP1q/dAoGAcHg5YX7WEehCgCYTzpO+
xysX8ScM2qS6xuZ3MqUWAxUWkh7NGZvhe0sGy9iOdANzwKw7mUUFViaCMR/t54W1
GC83sOs3D7n5Mj8x3NdO8xFit7dT9a245TvaoYQ7KgmqpSg/ScKCw4c3eiLava+J
3btnJeSIU+8ZXq9XjPRpKwUCgYA7z6LiOQKxNeXH3qHXcnHok855maUj5fJNpPbY
iDkyZ8ySF8GlcFsky8Yw6fWCqfG3zDrohJ5l9JmEsBh7SadkwsZhvecQcS9t4vby
9/8X4jS0P8ibfcKS4nBP+dT81kkkg5Z5MohXBORA7VWx+ACohcDEkprsQ+w32xeD
qT1EvQKBgQDKm8ws2ByvSUVs9GjTilCajFqLJ0eVYzRPaY6f++Gv/UVfAPV4c+S0
kAWpXbv5tbkkzbS0eaLPTKgLzavXtQoTtKwrjpolHKIHUz6Wu+n4abfAIRFubOdN
/+aLoRQ0yBDRbdXMsZN/jvY44eM+xRLdRVyMmdPtP8belRi2E2aEzA==
-----END RSA PRIVATE KEY-----

bandit13@bandit:~$
```

We have been using ssh with a password to access these levels but now we need to see how to use ssh with a private key.  
Time to look at the [man page](https://linux.die.net/man/1/ssh)

Looking through the man page we can see an entry that mentions private key.    
The `-i` option for ssh will allow us to specify an identity (private ssh key) to use instead of a password.

Here is the section of the `man ssh` page concerning `-i` option.

```
-i identity_file
    Selects a file from which the identity (private key) for public key authentication is read.  
    The default is ~/.ssh/identity for protocol version 1, 
    and ~/.ssh/id_dsa, ~/.ssh/id_ecdsa, ~/.ssh/id_ed25519 and ~/.ssh/id_rsa for protocol version 2.  
    Identity files may also be specified on a per-host basis in the configuration file.
    It is possible to have multiple -i options (and multiple identities specified in
    configuration files).  
    If no certificates have been explicitly specified by the CertificateFile directive, 
    ssh will also try to load certificate information from the filename obtained by appending
    -cert.pub to identity filenames.
```

So now we can use the `-i` option to login to the next level (bandit14).  
Since the level we are logged into (bandit13) and the next level (bandit14) are located on  
the same server we use `@localhost` instead of `@bandit.labs.overthewire.org` as the address.  

```bash
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
```

Now that we are logged into bandit14 we can get the password for bandit14 from `/etc/bandit_pass/bandit14`.  
Getting this password will make it easier to access bandit14 later.

```
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJ##########################
```