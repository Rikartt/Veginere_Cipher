def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    # return string   
    return str1  
Message2 = []
Message = input(str("Input Message: "))
Key = input(str("Input Key: ")).lower()
Nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
Alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Message = Message.lower()
Message = [x for x in Message]
Key = [x for x in Key]
print(Message)
print(Key)
input()
lalala = len(Key)
lalala2 = lalala
lalala3 = 0
for x in Message:
    if x not in ["1","2","3","4","5","6","7","8","9","0"," ", ",", ".", "-", "\'", "\"", "?", "!"]:
        lala = Alph.index(x)
        haha = Alph.index(Key[lalala3])
        hala = haha + lala
        if hala > 26 or hala == 26:
            hala = hala - 26
            laha = Alph[hala]
        elif hala < 26:
            laha = Alph[hala]
        lalala3 = lalala3 + 1
    else:
        laha = x
    x = laha
    lalala2 = lalala2 - 1
    if lalala2 == 0:
        lalala2 = lalala
    if lalala3 == lalala:
        lalala3 = 0
    Message2.append(x)
Message = listToString(Message2)
print(Message)
input()