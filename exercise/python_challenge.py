original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
the_word = ""
url = "map"
for c in url:
    if c >= 'a' and c <= 'z':
        the_word = the_word + chr(((ord(c) + 2) - ord('a')) % 26 + ord('a'))
    else:
        the_word = the_word + c
print(the_word)