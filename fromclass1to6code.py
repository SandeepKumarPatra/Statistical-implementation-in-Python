import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# df=pd.read_csv('diet_recommendation_dataset_1000 - diet_recommendation_dataset_1000.csv')
# print(df.columns)

# # print(df['Height_cm'].unique)

# heightmean=df['Height_cm'].mean()
# heightsd=df['Height_cm'].std()

# #outlier detection(imperical rule )
# def outlierdet(x):
#     if x<heightmean-heightsd*3 or x>heightmean+heightsd*3:
#         return 'outlier'

#     else:
#         return "normal"
    
# df['outlierflag']=df['Height_cm'].apply(outlierdet)

# print(df['outlierflag'].unique())


# # check gausian
# # histogram
# # # q-q plot

# # sns.histplot(df['Height_cm'],kde=True)
# # plt.show()

# import scipy.stats as stat
# # stat.probplot(df['Height_cm'],dist="norm",plot=plt)
# # plt.show()

# # for age

# # print(df['Age'].unique())

# # check gausian

# # sns.histplot(df['Height_cm'],kde=True)
# # plt.show()

# # stat.probplot(df['Age'],dist='norm',plot=plt)
# # plt.show()

# # print(df[ 'Sugar_Level'].unique())

# def sugarlevel_cat(x):
#     if x<80:
#         return 'Low'
#     elif x>=80 and x<=140:
#         return 'Normal'
#     else:
#         return 'High'
    
# df['Sugar_Catagory']=df['Sugar_Level'].apply(sugarlevel_cat)


# # print(df['Cholesterol'].unique())

# def colestrol_cat(x):
#     if x<200:
#         return 'Good'
#     elif x<=240:
#         return 'Boderliner'
#     else:
#         return "High"
    
# df['Colestrol_Catagory']=df['Cholesterol'].apply(colestrol_cat)

# print(df)

# def helthrisk(x): #x represent that 1 row down explained
#     if x['Sugar_Catagory']=="High" and x['Colestrol_Catagory']=="High":
#          return "High Risk"
    
#     elif x['Sugar_Catagory']=='High' or x['Colestrol_Catagory']=='High':
#         return 'Medium Risk'
    
#     else :
#         return "low risk"
# df['Risk_level']=df.apply(helthrisk,axis=1)#look after 1 row at a a itme 

# print(df)

# # probability of high sugar  P(E) = favorable / total

# probability_high=len(df[df['Sugar_Catagory']=='High'])/len(df)
# print(probability_high)



# import random

# def coin_experiment():
#     coins = ["H", "T"]
#     result = [random.choice(coins), random.choice(coins)]
#     return result.count("H")

# # This looks at the result list and counts how many times the string "H" appears. It will return one of three numbers:
# # 2: Both coins were Heads (HH).
# # 1: One coin was Heads, the other was Tails (HT or TH).
# # 0: Both coins were Tails (TT).

# # simulate
# data = [coin_experiment() for _ in range(1000)]

# # data = [1, 0, 2, 1, 2, 1, 0, 0, 1, 2, ...] (repeated 1,000 times).
# # Every 0 represents a trial where both coins were Tails.
# # Every 1 represents a trial where one was Heads and one was Tails.
# # Every 2 represents a trial where both were Heads.

# #EMPERICAL RULE

# import scipy.stats as stat

# from scipy.stats import skew,kurtosis

# print("skewness= ",skew(df['Age']))
# print("kurtosis= ",kurtosis(df['Age']))

# print(df['Age'].unique())

# def agecat(x):
#     if x<=20:
#         return "adult"
#     elif x<40:
#         return "medium age"
#     else:
#         return "senior"
# df['Age_catagory']=df['Age'].apply(agecat)
# print(df)

# # how many persent people in all 3 range using emperical rule 68,95,99.7

# mean=df['Weight_kg'].mean()
# std=df['Weight_kg'].std()

# # 1st range
# lower1=mean-std
# upper1=mean+std
# #2nd range
# lower2=mean-std*2
# upper2=mean+std*2
# # 3rd range
# lower3=mean-std*3
# upper3=mean+std*3

# print(lower1,upper1)
# people_in_range1=len(df[(df['Weight_kg']>=lower1) & (df['Weight_kg']<=upper1)])
# percentage_range1=(people_in_range1)/len(df)*100
# print(f"Persentage in 1st range {percentage_range1}%")


# print(lower2,upper2)
# people_in_range2=len(df[(df['Weight_kg']>=lower2) & (df['Weight_kg']<=upper2)])
# percentage_range2=people_in_range2/len(df)*100
# print(f"persentage of people in range2= {percentage_range2}%")



# print(lower3,upper3)
# people_in_range3=len(df[(df['Weight_kg']>=lower3)&(df['Weight_kg']<=upper3)])
# percentage_range3=people_in_range3/len(df)*100
# print(f"persentage in 3rd range {percentage_range3}%")




# # 3. Chebyshev Inequality (Non-Gaussian)

# # You should apply Chebyshev's Inequality specifically when your data does
# # not follow a Normal (Gaussian) distribution. range 2>=75 ,range 3=>88.8=89


# mean=df['Weight_kg'].mean()
# std=df['Weight_kg'].std()

# k=2
# lower=mean-std*k
# upper=mean+std*k

# theoryprob=1-1/(k**2)
# actualprob=len(df[(df['Weight_kg']>=lower) & (df['Weight_kg']<=upper)])/len(df)*100

# print("range",lower,"to",upper)
# print("minimum probability by theory (chebyshev)",theoryprob*100)
# print("actual data in range ",actualprob)

# # Chebyshev is the "Passing Grade": To be a valid mathematical dataset,
# # you must score at least 75% in the 2-SD range. Your data scored 100%. 
# # You passed the test!

# # Gaussian is a "Specific Score": To be called "Gaussian," you must score
# # almost exactly 95%. If you score 100%, you are not a "Typical Gaussian "
# # "Student." You are something else (like a Uniform or Bounded distribution).



# #scateer plot (bivariate)

# sns.scatterplot(data=df,x='Age',y='BMI')
# plt.show()

# #  boxplot (outlier)

# sns.boxplot(x=df['Weight_kg'])
# plt.show()

# # barplot (catagorical)

# sns.countplot(x=df['Activity_Level'])
# plt.show()

# # FacetGrid (Advanced Visualization) color scater plot

# sns.set_style("whitegrid")
# sns.FacetGrid(df,hue='Gender',height=5)\
#     .map(plt.scatter,'Height_cm','Weight_kg')\
#     .add_legend()

# plt.show()

# # .map: This tells the grid to "draw" a specific type of plot on every section.
# # plt.scatter: The type of plot (Dots).
# # "sepal.length", "sepal.width": The X and Y axes.
# # .add_legend():
# # This adds a box on the side that explains what each color means (e.g., Blue = Low Carb, Orange = Diabetic).


# #Central Limit Theorem

## The CLT states that if you take sufficiently large random samples from 
# # any population (regardless of the population's original distribution), 
# # the distribution of the sample means will approach a normal distribution
# #  as the sample size increases.

# data=np.random.uniform(0,100,1000)
# sample_mean=[]
# for i in range(1000):
#     sample=np.random.choice(data,size=30)
#     sample_mean.append(sample.mean())
# sns.histplot(sample_mean,kde=True)
# plt.show()

# # qq plot to conform its gausian distribution
# import scipy.stats as stat
# stat.probplot(sample_mean,dist='norm',plot=plt)
# plt.show()

# # skewness and kurtosis
# from scipy.stats import kurtosis,skew
# print(skew(sample_mean))
# print(kurtosis(sample_mean))


# # chebeshev inequality
# sample_mean=np.array(sample_mean)
# mean=sample_mean.mean()
# std=sample_mean.std()
# k=2
# lower=mean-std*k
# upper=mean+std*k
# theorypro=1-1/k**2
# realprob=np.sum((sample_mean>=lower) & (sample_mean<=upper))/len(sample_mean)*100

# print(realprob)
# print(theorypro*100)
# # why array
# # A Python list does not have methods like .mean() or .std()
# # Python will throw an AttributeError. By converting it to a NumPy array, 
# # you gain access to these optimized statistical functions.
# # why sum 
# # The Math: In Python/NumPy, True is treated as 1 and False is treated as 0.
# # The Sum: When you run np.sum() on that array of Booleans, it adds up 
# # all the 1s.
# # 1 + 0 + 1 + 1 = 3


# CDF ( Cumulative Distribution Function)

# The Cumulative Distribution Function (CDF) is a fundamental concept in 
# probability that answers the question: "What is the probability that a 
# random variable $X$ will take a value less than or equal to x?"
# CDF tells you the accumulated probability up to that point.

#manual code or ecdf emperical cdf
import numpy as np

data = np.array([160,158,155,160,163,162,168,166,170,172,148,189])
sorted_data = np.sort(data)

n = len(data)

cdf = []

# Think of enumerate as a helper that lets you see two things at once: 
# the index (the position) and the value of an item in a list.
for i, x in enumerate(sorted_data):
    prob = (i+1)/n
    cdf.append(prob)
    print(x, prob)

plt.plot(sorted_data, cdf, marker='o')
plt.xlabel("X")
plt.ylabel("CDF")
plt.show()

# ex- For the first point (148): $i=0$, so $(0+1)/12 = 0.083. This means 8.3%
# of your data is <= 148.For the middle point (162): 
# You've seen 6 points. 6/12 = 0.50. This means 50\% of your data is <= 162
# .For the last point (189): 12/12 = 1.0. 100\% of your data is <= 189


# by norm (Theoretical" CDF)
# It assumes your data follows a perfect mathematical curve.

from scipy.stats import norm
pdf = norm.pdf(sorted_data)
cdf = norm.cdf(sorted_data)

plt.plot(x, pdf, label='PDF (Density)')
plt.plot(x, cdf, label='CDF (Cumulative)', cumulative=True)
plt.legend()
plt.show()


# Gaussian CDF using math.erf

# This code calculates the Cumulative Distribution Function (CDF) of a
#  Normal (Gaussian) distribution using a built-in mathematical function 
# called the Error Function (erf).
import math

# (x - mean) / std: This tells us how many "steps" (standard deviations) we are from the center.
#  / math.sqrt(2): This scales that distance so the erf function can understand it.
# math.erf(...): This calculates the raw area (from -1 to 1).
# 0.5 * (1 + ...): This shifts the result so it starts at 0 and ends at 1 (a standard 0% to 100% probability).

def gaussian_cdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

print(gaussian_cdf(160, 150, 10))


# Uniform Distribution (Code)

import numpy as np
import seaborn as sns

data = np.random.uniform(0, 1, 1000)

sns.histplot(data, kde=True)
plt.show()


# check uniform or mot  
import scipy.stats as stats

stats.probplot(data, dist="uniform", plot=plt)
plt.show()