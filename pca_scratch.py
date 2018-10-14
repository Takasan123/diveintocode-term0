
# coding: utf-8

# # pythonで主成分分析スクラッチ

# In[ ]:

import numpy as np


# ### ①行列（データ）の準備

# In[37]:

# 行列（データ）の準備
arr = np.array([[1,2],[3,4],[5,6]])

print(arr)
print(type(arr))


# ### ②各カラムの平均の計算

# In[38]:

col_mean = np.mean(arr.T, axis=1)
# 各カラムの平均の計算
col_mean


# ### ③各カラムの要素から平均を引く

# In[41]:

center = arr - col_mean
# 各カラムの要素から平均を引く
center


# ### ④centerの共分散を求める

# In[46]:

cv = np.cov(center.T)
# centerの共分散を求める
cv


# ### ⑤固有分解すると、固有値と固有ベクトルが出る

# In[60]:

from numpy import linalg as LA
# linalg関数をLAとしてimport

w ,v = LA.eig(cv)
# 固有分解すると、固有値と固有ベクトルが出る
print(w)
# 固有値を出力


# In[62]:

print(v)
# 固有ベクトルを出力


# ### ⑥データに固有ベクトルを掛けて射影し、元のデータ（３×２）を３×１行列に変換した（カラムを削減した）

# In[71]:

projection_data = np.dot(v.T,center.T).T
print(projection_data)
# データに固有ベクトルを掛けて射影し、元のデータ（３×２）を３×１行列に変換した（カラムを削減した）


# ### 注意点（なぜ上の⑥で転置しまくっているのか）

# In[70]:

np.dot(v,center.T).T
# 前のvを転置しなかった場合（実験）
# 一列目がゼロになった


# In[ ]:



