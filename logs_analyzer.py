import pandas as pd
import zipfile
import json
import re

# Python 3.6
# Pandas 0.20.2
# script use 'logs.zip' file
# located in the same directory as script file

data_obj = zipfile.ZipFile('logs.zip', mode='r') 
data_obj_names = data_obj.namelist()

logs_files_names = []
for i in data_obj_names:
    name = re.search(r'^.*/logs/[0-9].*$', i)
    if name:
        logs_files_names.append(i)
    else:
        pass
    
logs_valid = []
for j in logs_files_names:
    for i in data_obj.open(j).__iter__():
        try:
            temp = json.loads(i)
            temp = pd.io.json.json_normalize(temp).to_json(orient='records')
            logs_valid.append(temp[1:-1])
        except (ValueError, SyntaxError):
            pass

logs_valid_str = '[%s]' % ','.join(logs_valid)
logs = pd.read_json(logs_valid_str)

logs['timestamp'] = logs['timestamp'].apply(lambda x: pd.Timestamp(x))
logs['timestamp_qh'] = logs['timestamp'].apply(
    lambda x: pd.datetime(x.year, x.month, x.day, x.hour, 15*(x.minute // 15)))

logs_length = logs.shape[0]

# instead of „ismobile”, which was not present in received data in 
# prasedable json lines, I used nameValuePairs["system"][„newuser”] values:
newuser_count = logs['nameValuePairs.system.newuser'].value_counts()
newuser_true_rel = 100 * newuser_count.true / logs_length
newuser_false_rel = 100 * newuser_count.false / logs_length

tag_to_name = pd.read_csv(data_obj.open(
    'dane/tag_to_name'), index_col=0, header=None, sep=':').T.to_dict(orient='records')
tagid_count = logs['nameValuePairs.tagid'].value_counts().rename(tag_to_name[0]).to_dict()

log_count_qh = logs.groupby('timestamp_qh')[['eventId']].count()
log_count_qh_max = (
    log_count_qh.loc[log_count_qh['eventId'] == log_count_qh['eventId'].max()].index[0])

print(
    'Liczba poprawnych wpisów: {}\n'
    '\n'
    'Jaki procent wpisów posiada wartość nameValuePairs["system"][„newuser”]'
    ' równą „true”, a jaki „false”:\n'
    ' New user (true): {}%\n'
    ' Not new user (false): {}%\n'
    '\n'
    'Liczba wpisów dla każdej unikalnej wartości nameValuePairs[„tagid”]:'
    .format(
        logs_length,
        round(newuser_true_rel, 1),
        round(newuser_false_rel, 1)))
for i, j in tagid_count.items():
    print(' {}: {}'.format(i, j))
print(
    '\n'
    'Kwadrans, podczas którego zapisane jest najwięcej wpisów:\n'
    ' {}-{}'.format(
        str(log_count_qh_max)[:-3],
        str((log_count_qh_max + pd.Timedelta(15, unit='m')))[-8:-3]))
