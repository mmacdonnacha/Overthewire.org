<?php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

// Hexadecimal to ASCII
$hex_2_bin = hex2bin($encodedSecret);

// Reverse String
$reverseString = strrev($hex_2_bin);

// Decode base64 string to plaintext
$b64Decode = base64_decode($reverseString);

print $b64Decode . "\n";

?>
