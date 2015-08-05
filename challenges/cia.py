# https://www.cia.gov/kids-page/games/break-the-code/code-1.html

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ."
KEY =     "ZYXWVUTSRQPONMLKJIHGFEDCBA+@#$%^&*=~ ."

msg = "GSV XVMGIZO RMGVOORTVMXV ZTVMXB DZH XIVZGVW RM +=$& DSVM KIVHRWVMG GIFNZM HRTMVW GSV MZGRLMZO HVXFIRGB ZXG."

plaintext = ""
for letter in msg:
    plaintext += SYMBOLS[KEY.find(letter)]

print plaintext
