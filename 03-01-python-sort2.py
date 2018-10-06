
# coding: utf-8

# ## python

# In[18]:

## テキストファイルに貼り付ける　　'test_tokyo.csv'


import csv ## csvファイルを開く
with open('../test_tokyo.csv', 'r') as f:    ## テキストファイルを開く
       reader = csv.reader(f)   ## csvファイルからReaderオブジェクトを生成
       for row in reader:    ## forループで一行ずつのデータを取り出す
           print(row)    ## 1行づつ取得できる

