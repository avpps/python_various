''' Demand txt file with digits-matrix separated with ','
    Eg:
    
    1,2,3
    4,5,6
    7,8,9

'''

path = 'C://repositories//files//matrix_1.txt'


def find_way_dr(path):
    '''looking for cheapest way going only down and right'''
    matrix = []
    with open(path) as m_file:
        for line in m_file:
            tmp_l = line.replace('\n', '').split(',')
            matrix.append(list(map(lambda x: int(x), tmp_l)))

    print(matrix)

    start = [0, 0]
    end = [len(matrix)-1, len(matrix[0])-1]

    act_line = 0
    act_col = 0
    pre_line = None
    pre_col = None
    act_way = []
    act_score = 0

    ch_way = []
    ch_way_score = 0

    def go(pre_line, pre_col, act_line, act_col):
        pre_pos = [pre_line, pre_col]
        act_pos = [act_line, act_col]
        
        print([act_line, act_col])
        if act_pos != pre_pos:
            try:
                next_line = act_line
                next_col = act_col + 1
                matrix[next_line][next_col]
            except IndexError:
                try:
                    next_line = act_line + 1
                    next_col = act_col
                    matrix[next_line][next_col]
                except IndexError:
                    return 'hmm...'
                
            next_pos = [next_line, next_col]
            act_way.append(act_pos)
            act_score += matrix[act_line][act_col]
                
            if act_pos == end and act_score > ch_way_score:
                ch_way = act_way
                ch_way_score = act_score
                return
            else:
                go(act_line, act_col, next_line, next_col)

        
    go(pre_line, pre_col, act_line, act_col)
    return ch_way


def find_way_drul(path):
    '''looking for cheapest way going in down, right, up and left'''

    return 'ongoing'


if __name__ == '__main__':
    print(find_way_dr(path))
    print(find_way_drul(path))
