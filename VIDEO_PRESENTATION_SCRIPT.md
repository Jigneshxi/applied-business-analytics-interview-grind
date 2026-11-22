# Official Video Presentation Script & Viva Defense Guide
## Applied Business Analytics (M1_ABA) — Applied Statistics Interview Grind

**Presenter:** Jignesh Kumar ([@Jigneshxi](https://github.com/Jigneshxi))  
**Track:** Data Science & Agentic AI — Module 1  
**Institution:** Woolf University & Vishleshan I-Hub, IIT Patna (AlmaBetter Track)  
**Total Target Video Duration:** 15 – 20 Minutes (Camera ON, English narration)  
**Selected Video Questions:** Q18 (Bayes' Theorem), Q21 (Central Limit Theorem), Q40 (Type I/II Errors), Q41/Q62 (Correlation vs Causation), Q78 (A/B Testing Hypothesis & Sizing)  

---

## ⏱️ Video Presentation Timing Breakdown

| Section | Topic | Allocated Duration | Running Time |
| :---: | :--- | :---: | :---: |
| **Intro** | Self Introduction, Curriculum Context & Agenda | 1.0 min | 00:00 – 01:00 |
| **Part 1** | **Q18: Bayes' Theorem & Base Rate Fallacy** | 3.5 min | 01:00 – 04:30 |
| **Part 2** | **Q21: Central Limit Theorem (CLT) & Sampling Distributions** | 3.5 min | 04:30 – 08:00 |
| **Part 3** | **Q40: Type I & Type II Errors, Statistical Power & Asymmetric Costs** | 3.5 min | 08:00 – 11:30 |
| **Part 4** | **Q41 & Q62: Correlation vs. Causation, Confounders & Sleep Study** | 3.5 min | 11:30 – 15:00 |
| **Part 5** | **Q78: Hypothesis Testing in Marketing A/B Testing & MDE Sample Sizing** | 3.5 min | 15:00 – 18:30 |
| **Outro** | Conclusion, Project Artifacts & Final Wrap-up | 1.0 min | 18:30 – 19:30 |

---

## 🎬 Word-for-Word Video Recording Script

### Introduction (00:00 – 01:00)
> *"Hello everyone, respected mentors, and evaluators. I am Jignesh Kumar, candidate for the Master of Science in Computer Science and Applied Artificial Intelligence at Woolf University in collaboration with Vishleshan I-Hub, IIT Patna and AlmaBetter.*
>
> *Today, I am presenting my final capstone defense for **Module 1: Applied Business Analytics** in the **Data Science & Agentic AI** track, titled the **'Applied Statistics Interview Grind.'**
>
> *In modern enterprise data science and machine learning engineering, statistical inference and experimental design are the indispensable bedrock of reliable business decision-making. In this project, I have completed comprehensive mathematical and business solutions for all 80 core interview problems, prepared the final 50 written submission answers, and engineered an executable Python simulation engine with automated pytest verification.
>
> *In this 18-minute presentation, I will deliver an in-depth oral defense of five core statistical case studies: Bayes' Theorem, the Central Limit Theorem, Type I and Type II errors, Correlation versus Causation, and Marketing A/B Testing."*

---

### Part 1: Question 18 — Bayes' Theorem & The Base Rate Fallacy (01:00 – 04:30)
> *"Let us begin with Question 18: What is Bayes' Theorem, and how is it utilized in business analytics?*
>
> *Mathematically, Bayes' Theorem provides a rigorous formulation for updating our prior probability belief $P(A)$ after observing new empirical evidence $B$, yielding the posterior probability $P(A|B)$:*
>
> $$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$
>
> *Where the total probability of evidence $B$ is expanded using the law of total probability:*
> $$P(B) = P(B|A)P(A) + P(B|\neg A)P(\neg A)$$
>
> *While the formula is simple, its business application reveals one of the most counter-intuitive phenomena in data science: **The Base Rate Fallacy**. Let us examine a classic medical or fraud screening scenario:*
>
> *Suppose a rare financial fraud or disease affects 1 in 1,000 transactions—a prior probability of 0.1% ($P(D) = 0.001$). A vendor provides a machine learning detector with 99% sensitivity ($P(+|D) = 0.99$) and only a 1% false positive rate ($P(+|\neg D) = 0.01$). When a transaction is flagged as positive, what is the actual probability that it is truly fraudulent?*
>
> *Most human executives intuitively guess 99%. However, applying Bayes' Theorem reveals:*
> $$P(D|+) = \frac{0.99 \times 0.001}{(0.99 \times 0.001) + (0.01 \times 0.999)} = \frac{0.00099}{0.00099 + 0.00999} = \frac{0.00099}{0.01098} \approx 9.02\%$$
>
> *Notice what this means: Over 90% of flagged positive alerts are actually false alarms! Because the underlying event is rare, the false positives generated from the 99.9% non-fraudulent population overwhelm the true positives. In financial analytics, understanding Bayes' Theorem prevents institutions from blocking legitimate high-value customers while properly sizing fraud review operations."*

---

### Part 2: Question 21 — Central Limit Theorem (CLT) & Sampling (04:30 – 08:00)
> *"Next, let us turn to Question 21: What is the Central Limit Theorem, and why is it the cornerstone of statistical inference?*
>
> *The Central Limit Theorem states that: Given any population with an arbitrary probability distribution—whether it is heavily skewed, uniform, bimodal, or discrete—with finite mean $\mu$ and finite variance $\sigma^2$, the sampling distribution of the sample mean $\bar{X}$ approaches a Gaussian Normal distribution as the sample size $n$ becomes sufficiently large (typically $n \ge 30$).*
>
> *Furthermore, this sampling distribution has two fundamental mathematical parameters:*
> 1. *The mean of the sample means equals the true population mean: $\mu_{\bar{X}} = \mu$.*
> 2. *The standard error of the sample means shrinks inversely proportional to the square root of $n$: $SE = \frac{\sigma}{\sqrt{n}}$.*
>
> *In our Python simulation engine in `statistical_engine.py`, we demonstrated this empirically by generating 50,000 values from a heavily right-skewed Exponential distribution with rate $\lambda = 0.5$ and mean $\mu = 2.0$. The raw data is severely asymmetrical. However, when we draw 2,000 independent samples of size $n = 35$, the distribution of sample means transforms into a pristine bell curve centered at exactly 2.0014, with an observed standard error of 0.3394 matching the theoretical value of 0.3381.*
>
> *Why is this vital for enterprise business analytics? Because in the real world, customer transaction amounts, website session durations, and server latencies are never normally distributed—they are heavily skewed Pareto or log-normal distributions. The CLT gives business analysts mathematical license to construct confidence intervals and run hypothesis z-tests on sample means without needing to assume the raw customer data follows a bell curve."*

---

### Part 3: Question 40 — Type I & Type II Errors & Decision Power (08:00 – 11:30)
> *"Now let us examine Question 40: What are Type I and Type II errors in hypothesis testing, and how do we balance them in business decision-making?*
>
> *In statistical hypothesis testing, we formulate a Null Hypothesis $H_0$ representing the baseline status quo, and an Alternative Hypothesis $H_a$ representing a real effect or change. Every decision produces a 2-by-2 confusion matrix:*
>
> *1. **Type I Error ($\alpha$, False Positive):** Rejecting the Null Hypothesis when it is actually true. For example, convicting an innocent defendant, or claiming a new website layout increased sales when the lift was merely random noise. We control this via the significance level $\alpha$, conventionally set at 0.05.*
>
> *2. **Type II Error ($\beta$, False Negative):** Failing to reject the Null Hypothesis when it is actually false. For example, failing to detect an effective drug treatment, or failing to identify a fraudulent cyber attack. The complement of $\beta$, ($1 - \beta$), represents **Statistical Power**—the probability of correctly detecting an effect when one truly exists.*
>
> *In business, Type I and Type II errors have profoundly asymmetric financial costs:*
> - *In **Credit Card Fraud Detection**, $H_0$ states the transaction is legitimate. A Type I error falsely declines a valid customer purchase, causing user annoyance. But a Type II error permits a $10,000 fraudulent wire transfer to clear, causing direct, unrecoverable capital loss. Therefore, risk teams tune their thresholds to minimize $\beta$ (Type II error), deliberately accepting a higher false positive rate $\alpha$.*
> - *Conversely, in **Email Spam Filtering**, a Type I error routes an urgent client contract into the junk folder, causing severe business harm. Here, engineers tune thresholds to minimize $\alpha$ (Type I error).*
>
> *Balancing these errors requires rigorous cost-benefit modeling rather than blindly adopting arbitrary p-value cutoffs."*

---

### Part 4: Questions 41 & 62 — Correlation vs. Causation & Confounders (11:30 – 15:00)
> *"Let us address Questions 41 and 62: What is the fundamental difference between correlation and causation, and how do confounders mislead business conclusions?*
>
> *Mathematically, **correlation** measures the degree of linear association between two variables $X$ and $Y$, quantified by Pearson's correlation coefficient $r \in [-1, 1]$:*
> $$r = \frac{\sum (X - \bar{X})(Y - \bar{Y})}{\sqrt{\sum (X - \bar{X})^2 \sum (Y - \bar{Y})^2}}$$
>
> *Correlation indicates that when variable $X$ is high, variable $Y$ tends to be high. However, **causation** requires empirical proof of an active causal mechanism: that an intentional intervention on variable $X$ directly forces variable $Y$ to change, holding all other variables constant.*
>
> *The classic trap in business analytics is the presence of a **Lurking Confounder**—a third unobserved variable $Z$ that simultaneously drives both $X$ and $Y$. In our Python engine, we simulated the classic example of Daily Ice Cream Sales ($X$) versus Coastal Shark Attacks ($Y$). In the raw data, $X$ and $Y$ exhibit a strong positive correlation of $r = 0.88$. Does eating ice cream cause sharks to attack swimmers? Of course not. Both are driven by the common confounder: **Summer Temperature** ($Z$). High heat causes more people to buy ice cream and more people to swim in the ocean.*
>
> *Applying this to Question 62 regarding the observed high correlation between hours of employee sleep and productive work output: An executive might mistakenly infer that mandating 10 hours of sleep will automatically boost sales. In reality, employees with high sleep may also experience lower stress, better physical wellness, and manageable workloads. Only randomized controlled trials (A/B testing) can eliminate confounders and establish causal validity."*

---

### Part 5: Question 78 — Marketing A/B Testing & Sample Sizing (15:00 – 18:30)
> *"Finally, let us explore Question 78: How is hypothesis testing utilized in digital marketing A/B testing, and how do we determine sample size?*
>
> *In digital product management, A/B testing is the gold standard for causal inference. Consider an experiment evaluating a checkout flow redesign:*
> - *Control Group A ($N_A = 2,000$ users): 120 purchases $\implies$ baseline conversion rate $p_A = 6.00\%$.*
> - *Variant Group B ($N_B = 2,000$ users): 165 purchases $\implies$ new conversion rate $p_B = 8.25\%$.*
> - *Observed Relative Lift: $\frac{8.25 - 6.00}{6.00} = +37.50\%$.*
>
> *To determine whether this lift is statistically significant or merely random sampling fluctuation, we formulate a two-proportion pooled z-test:*
> $$H_0: p_B - p_A \le 0 \quad \text{vs.} \quad H_a: p_B - p_A > 0$$
>
> *We compute the pooled proportion $\hat{p} = \frac{120 + 165}{4000} = 0.07125$ and the standard error $SE = \sqrt{\hat{p}(1-\hat{p})(1/N_A + 1/N_B)} = 0.008135$.*
> *The resulting z-score is:*
> $$Z = \frac{0.0825 - 0.0600}{0.008135} = 2.766$$
> *With a one-tailed p-value of $p = 0.0028 < 0.01$, we reject the null hypothesis and confirm that Variant B produces a genuine, statistically significant lift.*
>
> *Crucially, before running any A/B experiment, an analyst must compute the required sample size based on the Minimum Detectable Effect (MDE), significance level $\alpha = 0.05$, and statistical power $1 - \beta = 0.80$:*
> $$n = \frac{2 \cdot (Z_{\alpha/2} + Z_{\beta})^2 \cdot \bar{p}(1 - \bar{p})}{(p_B - p_A)^2}$$
> *In our engine, detecting a 25% relative lift on a 6% baseline requires exactly **3,842 users per variant**. Running tests with insufficient sample size leads to underpowered experiments, while 'peeking' early inflates Type I error rates."*

---

### Outro (18:30 – 19:30)
> *"In conclusion, this project provides a rigorous, end-to-end mastery of applied business statistics. All 80 master questions and 50 final submission solutions are documented in our repository, backed by a fully tested Python engine (`statistical_engine.py`), pre-executed Jupyter notebooks, and publication-quality figures.*
>
> *Thank you very much for your time, and I look forward to your evaluation."*

---

## 🎓 Viva Defense: Key Oral Interview Questions & Model Answers

### Q1: What is Bessel's Correction, and why is it necessary?
> **Answer:** *"When calculating sample variance from $n$ observations, dividing by $n$ produces a biased underestimate of the true population variance $\sigma^2$ because sample deviations are measured around the sample mean $\bar{X}$ rather than the true population mean $\mu$. Bessel's correction divides by $n - 1$ instead of $n$, mathematically restoring unbiasedness: $E[s^2] = \sigma^2$."*

### Q2: What is the p-value, and what is its most common misconception?
> **Answer:** *"The p-value is the probability of observing a test statistic as extreme as, or more extreme than, the observed result, assuming the Null Hypothesis $H_0$ is completely true. The most common misconception is believing that the p-value represents the probability that the null hypothesis is true, or the probability that the alternative hypothesis is false. It is strictly a statement about the data under $H_0$."*

### Q3: How do you choose between a Z-test and a T-test?
> **Answer:** *"A Z-test is appropriate when the population standard deviation $\sigma$ is known, or when the sample size is very large ($n \ge 30$) under the Central Limit Theorem. A Student's T-test is mandatory when the population standard deviation $\sigma$ is unknown and must be estimated using the sample standard deviation $s$, particularly for small sample sizes ($n < 30$), as the t-distribution incorporates heavier tails to account for estimation uncertainty."*
