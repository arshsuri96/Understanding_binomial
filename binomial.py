#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Coin flip experiment to understand binomial


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


np.random.radom() returns float value between the range(0, 1)


# In[31]:


n, p , trial = 10, 0.5, 1000
heads = []
def bio(n, p, trial):
    for i in range(trial):
        toss = [np.random.random() for i in range(n)]
        heads.append(len([i for i in toss if i>=0.5]))
    return heads

heads = bio(n, p, trial)

fig, ax = plt.subplots(figsize=(16,7))
ax = sns.distplot(heads, bins=11, label='simulation results')
ax.set_xlabel("Number of Heads",fontsize=16)
ax.set_ylabel("Frequency",fontsize=16)

from scipy.stats import binom
x = range(0,11)
ax.plot(x, binom.pmf(x, n, p), 'ro', label='actual binomial distribution')
ax.vlines(x, 0, binom.pmf(x, n, p), colors='r', lw=5, alpha=0.5)
plt.legend()
plt.show()


# In[29]:


##Stimulating a single sequence of experiment where n=10

#This would confirm the range where our binomial distribution lies 


# In[28]:


np.random.binomial(n,p)
runs = 1000
prob_6 = sum([1 for i in np.random.binomial(n,p, size = runs)if i ==6])/runs

print('The probability of 6 heads is: ' + str(prob_6))


# In[ ]:




