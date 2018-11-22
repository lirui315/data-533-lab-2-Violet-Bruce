# Data-533-lab-2-Violet-Bruce
533 lab2 repository for (Rui Li) Violet and (Xiangyu Pei) Bruce

This package is called padaku and it has 2 subpackages as below:


### Sub-package 1. *`birth`*


#### A. The sub-package *`birth`* has a module named *`birthdate`* which has class(*`birthinfo`*) and its sub-class(*`Year`*) as inheritance

TO DO: 
1. take birthday then returns the person's year
2. chinese_zodiac return the person's Chinese zodiac

**note: The Chinese zodiac is a classification scheme that assigns an animal and it represents for each year in a repeating 12 year cycle. Animals including in the cycle are rat, ox, tiger, rabbit, dragon, snake, horse, goat, monkey, rooster, dog and pig.**

`Probably you can try it for yourself.`

Example: 

>from padaku.birth import birthdate as b
>
>p1=b.Year(1996,3,15)
>
>print(p1.chinese_zodiac())
>
>('Year is 1996', 'Chinese Zodiac is Rat')

#### B. The sub-package *`birth`* also has a *`constellation`* module which has a constellation function

TO DO:
1. take person's birth month and date then return the person's constellation

Example:

>from padaku.birth import constellation as c
>
>print(c.constellation(3,15))
>
>Your constellation is Pisces


### Sub-package 2. perinfo

#### A. The sub-package *`perinfo`* has an age module which has an *`age`* function

TO DO:
1. take a person's birthday as "YYYY-MM-DD" then returns the person's age

Example:

>from padaku.perinfo import age as a
>
>a.age("1996-3-15")
>
>'The age of the person is 22'

#### B. The sub-package *`perinfo`* has a *`name`* module which has a *`lastname`* function and a *`firstname`* function. 

TO DO:
The lastname function returns the person's lastname with only the first character as captalized; the firstname function returns the person's firstname with only the first character as captalized

Example: 

>from padaku.perinfo import name
>
>name.lastname("BRUCE PEI")
>
>('Lastname:', 'Pei')

>name.firstname("BRUCE PEI")
>
>('Firstname:', 'Bruce')

