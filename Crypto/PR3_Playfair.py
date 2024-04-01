import string
def genKeyMat(key):
    atoz = string.ascii_lowercase.replace('j', '.')
    key_matrix = ['' for i in range(5)]
    i = 0
    j = 0
    for c in key:
        if c in atoz:
            key_matrix[i] += c
            atoz = atoz.replace(c, '.')

            j += 1
            if j > 4:
                i += 1
                j = 0
    for c in atoz:
        if c != '.':
            key_matrix[i] += c

            j += 1
            if j>4:
                i += 1
                j = 0
    return key_matrix



def encrypt(plainText):
    plaintextpairs = []
    ciphetextpairs = []
    # Rule 1: if both latter are same or only one left add "X" after first letter
    i = 0
    while i < len(plainText):
        a = plainText[i]
        b = ""
        if (i+1) == len(plainText):
            b = 'x'
        else:
            b = plainText[i+1]
        if a != b:
            plaintextpairs.append(a + b)
            i += 2
        else :
            plaintextpairs.append(a + 'x')
            i += 1
    # Rule 2: if letters are  in same row, replace with letters to their immediate right letter
    for pair in plaintextpairs:
        applied_rule = False
        for row in key_matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])
                ciphetextpair = row[(j0 + 1) % 5] + row[(j1 + 1) % 5]
                ciphetextpairs.append(ciphetextpair)
                applied_rule = True
        if applied_rule:
            continue
    # Rule 3 :If letter are in same column, replace them with immediate below letter
        for j in range(5):
            col = "".join([key_matrix[i][j] for i in range(5)])
            if pair[0] in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])
                ciphetextpair = col[(i0 + 1) % 5] + col[(i1 + 1) % 5]
                ciphetextpairs.append(ciphetextpair)
                applied_rule = True
        if applied_rule:
            continue
    # Rule 4: not in same column or row,replace them with the letters on same row respectively but at
    # the other pair of corners of the rectangle define by the original pairs
        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0
        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])
            if pair[1] in row:
                i1 = i
                j1 = row.find(pair[1])
        ciphetextpair = key_matrix[i0][j1] + key_matrix[i1][j0]
        ciphetextpairs.append(ciphetextpair)
    return "".join(ciphetextpairs)

def decrypt(ciphetext):
    encryptedtextpairs =[]
    ciphetextpairs = []
    # Rule 1: if both latter are same or only one left add "X" after first letter
    i = 0
    while i<len(ciphetext):
        a = ciphetext[i]
        b = ciphetext[i+1]
        ciphetextpairs.append(a + b)
        i+=2
    # print(ciphetextpairs)

    for pair in ciphetextpairs:
        applied_rule = False
        for row in key_matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])
                encryptedtextpair = row[(j0 + 4) % 5] + row[(j1 + 4) % 5]
                encryptedtextpairs.append(encryptedtextpair)
                applied_rule = True
        if applied_rule:
            continue
            # Rule 3 :If letter are in same column, replace them with immediate below letter
        for j in range(5):
            col = "".join([key_matrix[i][j] for i in range(5)])
            if pair[0] in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])
                encryptedtextpair = col[(i0 + 4) % 5] + col[(i1 + 4) % 5]
                encryptedtextpairs.append(encryptedtextpair)
                applied_rule = True
        if applied_rule:
            continue
        # Rule 4: not in same column or row,replace them with the letters on same row respectively but at
        # the other pair of corners of the rectangle define by the original pairs
        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0
        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])
            if pair[1] in row:
                i1 = i
                j1 = row.find(pair[1])
        encryptedtextpair = key_matrix[i0][j1] + key_matrix[i1][j0]
        encryptedtextpairs.append(encryptedtextpair)
    return "".join(encryptedtextpairs)


key = 'playfair example'
key_matrix = genKeyMat(key)
plainText = "hidethegoldinthetreestump"
ciphetext = encrypt(plainText)
print("Plain text: ",plainText)
print("Key: ",key)
print("Cipher text: ",ciphetext)
print("Decrypted text: ",decrypt(ciphetext))