import unicodedata

def ketasuawase(text, num):
    count = 0
    word = ""
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
        if num >= count:
            word = word + c
        else:
            break
        
    return word


def main():
    word = ketasuawase("teすと", 3)
    print(word)

    
if __name__ == ("__main__"):
    main()
