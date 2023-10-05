# %26으로 해서 순환 되도록 하는 것만 인지하면 됨
def caesar(word, num):
    result = ''
    for ch in word:
        if ch.isupper():
            ch = chr(65 +ord(ch) -65 + num) % 26
        elif ch.isupper():
            ch = chr(97 +ord(ch) -97 + num) % 26
    result += ch
    
    return result
            
        
    