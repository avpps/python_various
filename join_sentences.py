ends = ['.', '!', '?', ':']

with open('/path/to/dest/file', 'w') as new_file:
    with open('/path/to/orig/file.txt', 'r') as file:

        previous_blank = True
        sentence = ''
        for line in file:
            line = line.replace('\n', '')

            if line == '':
                if sentence:
                    new_file.write('{}\n'.format(sentence))
                    sentence = ''
                previous_blank = True
                if not previous_blank:
                    new_file.write('')
            elif line.startswith('Часть') or line.startswith('Глава'):
                if sentence:
                    new_file.write('{}\n'.format(sentence))
                    sentence = ''
                previous_blank = False
                new_file.write('\n\n{}\n\n'.format(line))
            elif previous_blank and line[-1] not in ends:
                if sentence:
                    new_file.write('{}\n'.format(sentence))
                    sentence = ''
                previous_blank = False
                new_file.write('\n{}\n'.format(line))
            elif line[-1] not in ends:
                previous_blank = False
                sentence += ' '
                sentence += line
            elif line[-1] in ends:
                previous_blank = False
                sentence += ' '
                sentence += line
                if sentence:
                    new_file.write('{}\n'.format(sentence))
                    sentence = ''
            else:
                previous_blank = False
                sentence += ' '
                sentence += line
