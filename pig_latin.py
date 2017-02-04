def pigLatin (word):


    ww = word
    list1 = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
    if ww[0] not in list1:
        ww = ww[1:] + ww[0] + 'ay'
    else:
        ww = ww + 'yay'
    return ww
    
print(pigLatin('input string here')    
