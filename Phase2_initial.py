import os
import pandas as pd


path = '~/Downloads/Balanced_IEC104_Train_Test_CSV_Files/Balanced_IEC104_Train_Test_CSV_Files/iec104_train_test_csvs'
tp = 'cic'
tm = 180
n_workers = 2


assert tp in ('cic', 'custom'), "Wrong dataset type"
assert tm in (15, 30, 60, 90, 120, 180), "Wrong time"
assert 2 <= n_workers <= 5, "At least 2 and at most 5 workers (docker containers) are required"


dataset = f'tests_{tp}_{tm}'


if 'cic' in dataset:
    n = dataset.split('_')[-1]
    train_csv = os.path.join(os.path.join(path, dataset), f'train_{tm}_cicflow.csv')
    test_csv = os.path.join(os.path.join(path, dataset), f'test_{tm}_cicflow.csv')
elif 'custom' in dataset:
    n = dataset.split('_')
    train_csv = os.path.join(os.path.join(path, dataset), f'train_{tm}_custom_script.csv')
    test_csv = os.path.join(os.path.join(path, dataset), f'test_{tm}_custom_script.csv')
else:
    raise Exception("Wrong dataset")


df_train = pd.read_csv(train_csv)
df_test = pd.read_csv(test_csv)


if tp == 'cic':
    df_train = df_train.drop(columns=['Flow ID', 'Src IP', 'Src Port', 'Dst IP', 'Dst Port', 'Protocol', 'Timestamp'])
    df_test = df_test.drop(columns=['Flow ID', 'Src IP', 'Src Port', 'Dst IP', 'Dst Port', 'Protocol', 'Timestamp'])


output_dir = './output' 
os.makedirs(output_dir, exist_ok=True)

train_output_csv = os.path.join(output_dir, 'train.csv')
test_output_csv = os.path.join(output_dir, 'test.csv')

df_train.to_csv(train_output_csv, index=False)
df_test.to_csv(test_output_csv, index=False)

print(f"Train CSV file created: {train_output_csv}")
print(f"Test CSV file created: {test_output_csv}")
