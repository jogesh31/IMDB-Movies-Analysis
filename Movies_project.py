#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[11]:


df=pd.read_csv("C:/Users/hp/Downloads/movies.csv")
df.head(5)


# In[13]:


df.columns


# In[16]:


df.isnull().sum()


# In[27]:


#Drop unnecessary columns
df.drop(columns=['id','imdb_id','homepage','tagline','overview','budget_adj'],inplace=True)


# In[28]:


df.isnull().sum()


# In[29]:


#remove any rows in the DataFrame df where at least one of the values in the genres or director columns is NaN (missing). 
df.dropna(how='any',subset=['genres','director'],inplace=True)


# In[30]:


df.isnull().sum()


# In[34]:


#fill null with 0
df['production_companies']=df['production_companies'].fillna(0)
df['keywords']=df['keywords'].fillna(0)


# In[35]:


df.head(5)


# In[38]:


#round after decimal value to 2 decimal values
df['popularity']=df['popularity'].round(2)
df.head(5)


# In[42]:


#inserted the profit column at third place
df.insert(3,'profit',df.revenue-df.budget)


# In[138]:


df.head(5)


# In[48]:


#inserted the rate_of_interest column at 4th place
df.insert(4,'ROI',df.profit/df.budget)


# In[49]:


df.head(5)


# In[50]:


df['ROI']=df['ROI'].round(2)


# In[73]:


df.head(3)


# In[67]:


df1=df[['popularity','budget','revenue','profit','ROI','vote_count','vote_average','release_year']]
df1


# In[68]:


df.isnull().sum()


# In[61]:


#inf means infinity values are there
df.ROI.value_counts()


# In[65]:


#the total number of non-finite values (infinite or NaN) in the ROI column
non_finite_values=~np.isfinite(df['ROI'])


# In[64]:


non_finite_values.sum()


# In[66]:


df['ROI']=df['ROI'].replace([np.inf,-np.inf],np.nan)


# In[75]:


df2=df.groupby('release_year')['ROI'].mean()
df2.plot(kind='line')


# In[80]:


#Popularity over the years
df3=df.groupby('release_year')['popularity'].sum()
df3.plot(kind='line')
plt.xlabel('Year',fontsize=12)
plt.ylabel('Popularity',fontsize=12)


# In[82]:


#Vote average over the years
df3=df.groupby('release_year')['vote_average'].mean()
df3.plot(kind='line',color='red')
plt.xlabel('Year',fontsize=12)
plt.ylabel('Rating',fontsize=12)


# In[83]:


df.head(3)


# In[85]:


df.genres.value_counts()


# In[86]:


#to split the genres (turns the string into a list of substrings), 
#'Action|Adventure|Sci-Fi', it will be transformed into the list ['Action', 'Adventure', 'Sci-Fi']

split=['genres']
for i in split:
    df[i]=df[i].apply(lambda x:x.split('|'))
df.head(3)


# In[184]:


#Using df.explode('genres') is a great way to handle a DataFrame where the genres column contains lists of genres. 
#Exploding this column will transform each genre in the lists into its own row
df=df.explode('genres')
df


# In[94]:


df7=df.groupby('genres')['popularity'].sum().sort_values(ascending=False)
df7


# In[99]:


#Total movies according to genres 
df7.plot.barh(x='genres',y='popularity') #barh is for horizontal visual


# In[103]:


df.dtypes


# In[104]:


#change release_date column datatype to datetime
df['release_date']=pd.to_datetime(df['release_date'])


# In[105]:


df.dtypes


# In[106]:


df.head(3)


# In[108]:


df['months']=df['release_date'].dt.month


# In[122]:


#Top 5 highest grossing movies
df6=df.groupby(['original_title','release_year'])['profit'].max().sort_values(ascending=False).head(5)


# In[183]:


df6.plot(kind='pie',autopct='%1.1f%%')
plt.title('Top 5 highest grossing movies',color='red')
plt.show()


# In[153]:


df=pd.read_csv("C:/Users/hp/Downloads/movies.csv")
df.head(3)


# In[163]:


#Top 5 production companies
df8=df.production_companies.value_counts().head(5)
df8


# In[167]:


df8 = df.production_companies.value_counts().head(5)
df8.plot(kind='pie', autopct='%1.2f%%')
plt.ylabel('')  # This removes the y-label

plt.show()


# In[14]:


#Top 5 movies with high budget
df[['original_title','budget']].sort_values(by='budget',ascending=False).head(5)


# In[4]:


#Top 5 voted movies
top_5_movies = df[['original_title', 'vote_count']].sort_values(by='vote_count', ascending=False).head(5)

# Reset the index and drop the old index
top_5_movies = top_5_movies.reset_index(drop=True)
top_5_movies


# In[8]:


#a list of colors for each bar
colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'plum']

# Plotting
plt.figure(figsize=(10,6))
plt.bar(top_5_movies['original_title'], top_5_movies['vote_count'], color=colors)
plt.xlabel('Movie Title')
plt.ylabel('Vote Count')
plt.title('Top 5 Movies with the Highest Vote Count')
plt.xticks(rotation=45, ha='right')
plt.show()

