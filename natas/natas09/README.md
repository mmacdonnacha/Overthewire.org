# Natas Level 8 -> Level 9

## Description

<pre>
Username: <b>natas9</b>  

URL:      <b>http://natas9.natas.labs.overthewire.org</b>
</pre>
---

## Solution

Visit the url `http://natas9.natas.labs.overthewire.org` in the browser and we get a prompt for login.

Use the username `natas9` and the password obtained from the previous challenge.

Once logged in we can see a text box and a search button

![](img/natas09_index.png)

When entering text into the box and clicking search button the app appears to search a file for the text we entered.

![](img/natas09_search.png)


Checking the *View sourcecode* link will show php code used for the search button.

```php
<?
    $key = "";

    if(array_key_exists("needle", $_REQUEST)) {
        $key = $_REQUEST["needle"];
    }

    if($key != "") {
        passthru("grep -i $key dictionary.txt");
    }
?>
```


The php code takes our input and uses `passthru` to execute a command.  
The command is using grep to search a file for the text we entered.  

Because the php script is not sanitizing our input before passing it to grep we can use `command injection` to insert our own command and have it be executed.

First we end the grep command by using a `;` and then we can type our own command.
Then we can retrieve the password file.

```bash
;cat /etc/natas_webpass/natas9 #
```

Entering the command into the search box and clicking on search will give the password.

![](img/natas09_password.png)