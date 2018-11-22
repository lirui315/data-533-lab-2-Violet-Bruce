
# coding: utf-8

# In[23]:


class Birthinfo:
    def __init__(self,year,month,date):
        self.year=year
        self.month=month
        self.date=date
    def display(self):
        return 'Year is %s'%self.year,'Month is %s'%self.month,'Date is %s'%self.date


# In[38]:





# In[36]:


class Year(Birthinfo):
    def __init__(self,year,month,date):
        Birthinfo.__init__(self,year,month,date)
    def chinese_zodiac(self):
        if self.year%12==4:
            return 'Year is %s'%self.year,'Chinese Zodiac is Rat'
        elif self.year%12==5:
            return 'Year is %s'%self.year,'Chinese Zodiac is Ox'
        elif self.year%12==6:
            return 'Year is %s'%self.year,'Chinese Zodiac is Tiger'
        elif self.year%12==7:
            return 'Year is %s'%self.year,'Chinese Zodiac is Rabbit'
        elif self.year%12==8:
            return 'Year is %s'%self.year,'Chinese Zodiac is Dragon'
        elif self.year%12==9:
            return 'Year is %s'%self.year,'Chinese Zodiac is Snake'
        elif self.year%12==10:
            return 'Year is %s'%self.year,'Chinese Zodiac is Horse'
        elif self.year%12==11:
            return 'Year is %s'%self.year,'Chinese Zodiac is Goat'
        elif self.year%12==0:
            return 'Year is %s'%self.year,'Chinese Zodiac is Monkey'
        elif self.year%12==1:
            return 'Year is %s'%self.year,'Chinese Zodiac is Rooster'
        elif self.year%12==2:
            return 'Year is %s'%self.year,'Chinese Zodiac is Dog'
        elif self.year%12==3:
            return 'Year is %s'%self.year,'Chinese Zodiac is Pig'


# In[37]:




