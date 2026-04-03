# # Bernoli sistribution only 2 outcome 
# import numpy as np

# p=0.7
# np.random.seed(42)
# deta=np.random.binomial(n=1,p=p,size=10)
# print(deta)
# # here n is how many trail in a single binomial experiment
# # example tossing a coin 1 time 

# # mean And Variance

# data=[5,6,4,8,3,0,5,9]
# print(np.mean(data))
# print(np.var(data))
# # Variance is the average of these squared distances.

# # Standard Deviation
# # Standard deviation measures how spread out the values are from the mean (average).
# print(np.std(data))

# # BINOMIAL DISTRIBUTION (Multiple Trials)
# from scipy.stats import binom
# n=4
# p=0.5
# prob=binom.pmf(3,n,p)
# print(prob)

# # UNIFORM DISTRIBUTION

# import numpy as np
# import pandas as pd
# import seaborn as sns 
# import matplotlib.pyplot as plt

# data=np.random.uniform(low=0,high=1,size=1000)
# sns.histplot(data,kde=True)
# plt.show()

# # check using qq plot
# import scipy.stats as stat

# stat.probplot(data,dist='uniform',plot=plt)
# plt.show()
# # conclusinon it is a uniform distribution

# ----------

# # Gausian normal distribution

# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# data=np.random.normal(loc=50,scale=10,size=1000)#here location for mean,scale=std
# sns.histplot(data,kde=True)
# plt.show()

# from scipy.stats import skew,kurtosis
# print(kurtosis(data))
# print(skew(data))

# # LOG-NORMAL DISTRIBUTION

# # A lognormal distribution is a distribution where the logarithm of the 
# # variable follows a normal distribution.
# # let x is lognormal then log(x)-----Normal distribution
# date=np.random.lognormal(mean=2,sigma=0.5,size=1000)#always right skewed graph
# sns.histplot(date,kde=True)
# plt.show()

# # check lognormal
# log_data=np.log(date)
# sns.histplot(log_data,kde=True)
# plt.show()

# #BOXCOX TRANSFORMATION

# # convert non gausian to gaussian
# # We use Box-Cox transformation to convert non-normal data into normally
# # distributed data, because many statistical models and ML algorithms assume
# # the data is normal.

# # box-Cox requires all values to be strictly positive (> 0). 
# # If your data has zeros or negatives, use the Yeo-Johnson transformation
# # instead, which handles those cases.

# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# from scipy.stats import boxcox
# data=np.random.lognormal(mean=2,sigma=1,size=1000)
# transformed_data,lam=boxcox(data)
# print("lambda",lam)
# sns.histplot(transformed_data,kde=True)
# plt.show()

# # λ        Formula = the SOLUTION           Evaluation = what it says about data
# # −1      y = 1/x                        your data had strong right skew
# # −0.5    y = 1/√x                    your data had moderate right skew
# # 0       y = log(x)                 your data was lognormal
# # 0.5     y = √x                    your data had mild right skew
# # 1       y = x                       your data was already normal


# covariance and corelation

# Covariance tells you the direction of the relationship between two 
# variables — positive means they move together, negative means they move 
# opposite. But its value depends on the units/scale of your data, so you 
# can't easily compare covariances across different datasets.

# Correlation is just covariance divided by both standard deviations 
# — this normalizes it into a fixed range of −1 to +1, making it easy to 
# interpret regardless of units.
# correlation = covariance / (std of X × std of Y)


# import pandas as pd
# import numpy as np

# df=pd.DataFrame({
#     "height":[150,160,170,180],
#     "weight":[50,60,70,80]
# })

# print(df.cov())
# print(df.corr())

# # Chebyshev’s Inequality

# deta=np.random.exponential(scale=2,size=1000)
# k=2
# mean=np.mean(deta)
# std=np.std(deta)

# low=mean-k*std
# high=mean+k*std

# count=np.sum((deta>=low) & (deta<=high))
# prob=count/len(deta)

# print("probability ",prob)
# print("chebeshev bound is ",1-1/(k**2))

# import scipy.stats as start
# print(start.skew(deta))
# print(start.kurtosis(deta))

# # not gausian

# # CLT   (central limit theorem)

# # we take multiple sample of sample size more than 30 and find sample mean of 
# # each sample and took that and plot histogram and find the grraph is normal

# import seaborn as sns
# import matplotlib.pyplot as plt

# data=np.random.exponential(scale=2,size=1000)
# sample_mean=[]

# for i in range(1000):
#     sample=np.random.choice(data,size=30)
#     sample_mean.append(np.mean(sample))
# sns.histplot(sample_mean,kde=True)     
# plt.show()


# # PARETO DISTRIBUTION

# # A Pareto distribution is a probability distribution where:
# # A small number of things contribute to most of the effect
# # like 20 persent costomer 80 persent revenue 
# # to handadle pareto data convert it into log or boxcox transformation

# datee=np.random.pareto(a=2,size=1000)
# sns.histplot(datee,kde=True)
# plt.show()

# # 10.3.26

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats

# # Parameters
# xm    = 1.0   # scale (minimum value)
# alpha = 2.5   # shape

# # Generate Pareto samples
# np.random.seed(42)
# X = (np.random.pareto(alpha, size=500) + 1) * xm

# # --- QQ Plot to check if data follows Pareto ---
# fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# # Apply log transform (Box-Cox with lambda=0) → should become Gaussian
# log_X = np.log(X)
# stats.probplot(log_X, dist="norm", plot=axes[0])
# axes[0].set_title("QQ Plot: log(X) vs Normal\n(Pareto → Gaussian after log)")

# # Raw Pareto density
# x_vals = np.linspace(xm, 10, 300)
# pdf_vals = stats.pareto.pdf(x_vals, alpha, scale=xm)
# axes[1].plot(x_vals, pdf_vals, color='steelblue')
# axes[1].set_title(f"Pareto PDF  (Xm={xm}, α={alpha})")
# axes[1].set_xlabel("x"); axes[1].set_ylabel("Density")

# plt.tight_layout()
# plt.savefig("pareto.png", dpi=120)
# plt.show()

# # Verify 80-20 rule
# sorted_X   = np.sort(X)[::-1]
# top20_pct  = sorted_X[:int(0.2 * len(X))].sum() / sorted_X.sum()
# print(f"Top 20% accounts for {top20_pct*100:.1f}% of total  (expect ≈80%)")


# #11.03.2026------------------------------------------


# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(42)
# n = 100

# # Height (cm) and Weight (kg) — positively related
# height_cm = np.random.normal(168, 8, n)
# weight_kg  = 0.6 * height_cm + np.random.normal(0, 5, n)

# # ── Manual covariance formula from notes ──────────────────────────
# def manual_cov(x, y):
#     return np.mean((x - x.mean()) * (y - y.mean()))

# cov_val = manual_cov(height_cm, weight_kg)
# print(f"Cov(height, weight) = {cov_val:.4f}")
# print(f"Cov(X,X) = Var(X)  = {manual_cov(height_cm, height_cm):.4f}")
# print(f"np.var(height)      = {np.var(height_cm):.4f}  ← same thing")
# print(f"Cov(X,Y) == Cov(Y,X)? {np.isclose(manual_cov(height_cm, weight_kg), manual_cov(weight_kg, height_cm))}")

# # ── np.cov always returns a 2x2 matrix ────────────────────────────
# cov_matrix = np.cov(height_cm, weight_kg)   # uses n-1 (ddof=1) by default
# print("\nCovariance Matrix (np.cov):")
# print(f"  Cov(X,X)={cov_matrix[0,0]:.3f}  Cov(X,Y)={cov_matrix[0,1]:.3f}")
# print(f"  Cov(Y,X)={cov_matrix[1,0]:.3f}  Cov(Y,Y)={cov_matrix[1,1]:.3f}")

# # ── DRAWBACK: units change → covariance changes ───────────────────
# height_ft = height_cm / 30.48          # convert to feet
# cov_ft    = manual_cov(height_ft, weight_kg)
# print(f"\nCov (height in cm, weight in kg) = {cov_val:.4f}")
# print(f"Cov (height in ft, weight in kg) = {cov_ft:.4f}")
# print("Same relationship, DIFFERENT covariance → not comparable!")

# # ── Four quadrant interpretation ──────────────────────────────────
# mx, my = height_cm.mean(), weight_kg.mean()
# q1 = ((height_cm > mx) & (weight_kg > my)).sum()   # +ve * +ve → +ve
# q2 = ((height_cm < mx) & (weight_kg < my)).sum()   # -ve * -ve → +ve
# q3 = ((height_cm > mx) & (weight_kg < my)).sum()   # +ve * -ve → -ve
# q4 = ((height_cm < mx) & (weight_kg > my)).sum()   # -ve * +ve → -ve
# print(f"\nQ1 (+,+): {q1}  Q2 (-,-): {q2}  → push cov POSITIVE")
# print(f"Q3 (+,-): {q3}  Q4 (-,+): {q4}  → push cov NEGATIVE")
# print(f"Net → Cov = {cov_val:.4f}  (positive relationship)")

# # ── Plot ──────────────────────────────────────────────────────────
# plt.figure(figsize=(6,4))
# colors = ['steelblue' if ((x > mx and y > my) or (x < mx and y < my)) else 'coral'
#           for x, y in zip(height_cm, weight_kg)]

# plt.scatter(height_cm, weight_kg, c=colors, alpha=0.6, s=30)
# plt.axvline(mx, color='k', ls='--', lw=0.8)
# plt.axhline(my, color='k', ls='--', lw=0.8)
# plt.xlabel("Height (cm)")
# plt.ylabel("Weight (kg)")
# plt.title(f"Covariance = {cov_val:.2f}  | Blue = +ve quadrants  Red = -ve quadrants")
# plt.tight_layout()
# plt.savefig("covariance.png", dpi=120)
# plt.show()


# # 12.03.2026-------------------------------------------------------

# import numpy as np
# from scipy.stats import spearmanr

# np.random.seed(42)
# n = 100
# height = np.random.normal(168, 8, n)
# weight = 0.6 * height + np.random.normal(0, 5, n)

# # ── 1. Covariance ─────────────────────────────────────────────────
# cov_matrix = np.cov(height, weight)       # syntax from notes
# print("np.cov(X, Y) →")
# print(cov_matrix.round(4))
# print(f"\nCov(X,Y) = {cov_matrix[0,1]:.4f}")
# print("Drawback: value depends on units, can't say 'how much' positive/negative")

# # ── 2. Pearson (PCC) ──────────────────────────────────────────────
# pcc_matrix = np.corrcoef(height, weight)  # syntax from notes
# pcc = pcc_matrix[0, 1]
# print(f"\nnp.corrcoef(X, Y) →")
# print(pcc_matrix.round(4))
# print(f"\nPCC = {pcc:.4f}  (always between -1 and +1)")
# print("Works best for LINEAR relationships")

# # ── 3. Spearman ───────────────────────────────────────────────────
# rho, p_val = spearmanr(height, weight)    # syntax from notes
# print(f"\nspearmanr(a, b) → rho={rho:.4f}, p={p_val:.4e}")
# print("Works best for NON-LINEAR (monotone) relationships")

# # ── Summary table ─────────────────────────────────────────────────
# print("\n" + "="*55)
# print(f"{'Measure':<12} {'Value':>10}  {'Range':<15} {'Best for'}")
# print("-"*55)
# print(f"{'Covariance':<12} {cov_matrix[0,1]:>10.4f}  {'(-inf, +inf)':<15} direction only")
# print(f"{'PCC':<12} {pcc:>10.4f}  {'[-1, +1]':<15} linear")
# print(f"{'Spearman':<12} {rho:>10.4f}  {'[-1, +1]':<15} non-linear monotone")
# print("="*55)


# # 13.03.2026------------------------------------------------------


# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(42)

# # Simulate population (we normally NEVER see this fully)
# population_mean = 170
# population_sd   = 8
# population       = np.random.normal(population_mean, population_sd, 100_000)

# print(f"True population mean (µ) = {population.mean():.4f}  ← we never know this in real life")

# # ── Point estimation: take a sample, compute x_bar ───────────────
# sample_sizes = [5, 10, 30, 100, 500, 1000, 5000]

# print(f"\n{'Sample Size (n)':<18} {'x_bar':>10} {'Error |µ - x_bar|':>20}")
# print("-" * 52)
# for n in sample_sizes:
#     sample = np.random.choice(population, size=n, replace=False)
#     x_bar  = np.mean(sample)         # formula from notes: 1/n * Σxi
#     error  = abs(population_mean - x_bar)
#     print(f"{n:<18} {x_bar:>10.4f} {error:>20.4f}")

# print("\nAs n increases → x_bar gets closer to µ (Law of Large Numbers)")
# print("But: point estimation gives ONE number, no sense of uncertainty!")

# # ── Visualise convergence ─────────────────────────────────────────
# ns     = np.arange(5, 2001, 10)
# x_bars = [np.mean(np.random.choice(population, size=n)) for n in ns]

# plt.figure(figsize=(8, 4))
# plt.plot(ns, x_bars, color='steelblue', lw=1, alpha=0.8, label='x_bar')
# plt.axhline(population_mean, color='red', ls='--', lw=1.5, label=f'True µ={population_mean}')
# plt.fill_between(ns, population_mean-2, population_mean+2, alpha=0.1, color='red')
# plt.xlabel("Sample size (n)")
# plt.ylabel("Sample mean x_bar")
# plt.title("Point estimation: x_bar converges to µ as n → ∞")
# plt.legend(); plt.tight_layout()
# plt.savefig("point_est.png", dpi=120); plt.show()



  