# Natas Level 7 -> Level 8

## Description

<pre>
Username: <b>natas8</b>  

URL:      <b>http://natas8.natas.labs.overthewire.org</b>
</pre>
---

## Solution

Visit the url `http://natas8.natas.labs.overthewire.org` in the browser and we get a prompt for login.

Use the username `natas8` and the password obtained from the previous challenge.

Once logged in we can see an input box for entering a secret.

![](img/natas08_index.png)

When entering the wrong secret we get an error message.

![](img/natsa08_wrong.png)


We can inspect the source code using the *view sourcecode* link.

```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas8", "pass": "<censored>" };</script></head>
<body>
<h1>natas8</h1>
<div id="content">

<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>

<form method=post>
Input secret: <input name=secret><br>
<input type=submit name=submit>
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

In the source code we can see php code that needs further inspection.

```php
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```

From reading the php script we can see that the `secret` we enter is passed to the `encodeSecret()` function and the output is compared tot eh `encodedSecret` variable.

Since we have been given the `encodedSecret` and the function used to encode it we can reverse the process and find the `plaintext` secret.

To find the `plaintext` we have to 
* convert the hexadecimal `encodedSecret` to ascii string
* reverse the order of the ascii string
* and decode the resulting base64 string to get the `plaintext`.


```python
from base64 import b64decode
from binascii import unhexlify


encoded_secret = '3d3d516343746d4d6d6c315669563362'

# Convert from hexadecimal to ascii
unhexed_secret = unhexlify(encoded_secret)

# Reverse string
reverse_secret = unhexed_secret[::-1]

# Decode the Base64 string
decoded_base64 = b64decode(reverse_secret).decode()

print(decoded_base64)
```

Entering the `plaintext` into the text box will give the password for `natas9`.

![](img/natas08_password.png)

