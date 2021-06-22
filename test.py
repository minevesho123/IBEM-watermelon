import pandas as pd

rows_list = []
for row in input_rows:

    dict1 = {}
    # get input row in dictionary format
    # key = col_name
    dict1.update(blah..)

    rows_list.append(dict1)

df = pd.DataFrame(rows_list)

print(df)


def markdetection(name):
    with open('data.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strtime('%H:%M"%S')
            f.writelines(f)
