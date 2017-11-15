""" Function for count words consists of polish characters,
numbers and their special combinations.

"""


def count_polish_words(path):
    """ Need path to txt file
    
    """

    text = ''
    with open(path, encoding='utf-8-sig') as text_file:
        for line in text_file:
            text += line

    pl_chr = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H',
              'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P',
              'R', 'S', 'Ś', 'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż',
              'a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h',
              'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p',
              'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']
    # allowed for string
    allowed = ['', ' ', ',', '.', ':', ';', '"', "'", '!', '?', '(', ')', '\n']
    # allowed for numbers
    allowed_n = ['+', '-']

    pl_chr_dic = {key: None for key in pl_chr}
    allowed_dic = {key: None for key in allowed}
    allowed_n_dic = {key: None for key in allowed_n}

    words = 0
    numbers = 0
    prog = True
    penu = ''
    last = ''
    for n, i in enumerate(text):
        if i in allowed_dic:
            if prog == 'w':
                words += 1
            elif prog == 'n':
                if not text[n+1].isdecimal():
                    numbers += 1
            prog = True
        elif prog:
            if i in pl_chr_dic:
                if any((last in allowed_dic,
                        last in pl_chr_dic,
                        last == '-' and penu in pl_chr_dic,
                        last == '-' and penu in allowed_dic,)):
                    prog = 'w'
                else:
                    prog = False
            elif i.isdecimal():
                if any((last in allowed_dic and not penu.isdecimal(),
                        last.isdecimal(),
                        last in allowed_n_dic)):
                    prog = 'n'
                else:
                    prog = False
            else:
                if i not in allowed_n_dic:
                    prog = False
        penu = last
        last = i

    return numbers, words
