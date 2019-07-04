original_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

url_code = "map"
for c in url_code:
    if chr(97) <= c <= chr(122):
        c = chr(((ord(c) + 2 - ord("a")) % 26) + 97)
        print(c, end="")
    else:
        print(c, end="")
