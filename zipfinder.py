from zipfile import ZipFile, ZipInfo
from re import search


def find_napis(path='C://repositories//files//channel.zip'):
    with ZipFile(path) as zip_file:        
        result = ''
        next_file = '90052.txt'
        while next_file != '.txt':
            with zip_file.open(next_file) as act_file:
                act_comm = zip_file.getinfo(next_file).comment.decode('UTF-8')
                if act_comm.isalpha():
                    if act_comm not in result:
                        result += act_comm
                act_cont = act_file.read().decode('UTF-8')
                next_n = search(r'[0-9]*$', act_cont)[0]
                next_file = '{}.txt'.format(next_n)
                
    return result


if __name__ == '__main__':
    find_napis()