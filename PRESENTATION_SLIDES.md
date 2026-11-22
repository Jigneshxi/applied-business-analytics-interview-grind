# Presentation Slides: Applied Business Analytics & Applied Statistics
## 50 Core Statistical Problems, Mathematical Formulations, & Video Case Studies

**Presenter:** Jignesh Kumar ([@Jigneshxi](https://github.com/Jigneshxi))  
**Track:** Data Science & Agentic AI — Module 1 (Applied Business Analytics)  
**Institution:** Woolf University & Vishleshan I-Hub, IIT Patna (AlmaBetter Track)  
**Date:** November 2026  

---

## Slide 1: Title & Author Details
- **Project Title:** Applied Statistics Interview Grind — 50 Core Business Analytics Solutions
- **Author:** Jignesh Kumar
- **Degree:** Master of Science in Computer Science & Applied Artificial Intelligence
- **Affiliation:** Woolf University / IIT Patna / AlmaBetter
- **Rewards:** +300 APs | Contributes 10% to Final Course Grade

---

## Slide 2: Curriculum Overview & Domain Map
- **Total Master Questions:** 80 Questions
- **Selected Submission Questions:** 50 Written Solutions
- **Selected Video Case Studies:** 5 In-Depth Presentations (~18 mins total)
- **Six Analytics Domains:**
  1. *Linear Algebra & Vector Calculus* (12 Questions)
  2. *Calculus & Machine Learning Optimization* (5 Questions)
  3. *Probability Theory & Theoretical Distributions* (20 Questions)
  4. *Descriptive Statistics & Data Quality* (7 Questions)
  5. *Statistical Inference & Confidence Intervals* (18 Questions)
  6. *Hypothesis Testing & Marketing A/B Testing* (18 Questions)

---

## Slide 3: Video Case Study 1 — Bayes' Theorem & Base Rate Fallacy (Q18)
- **Mathematical Formulation:**
  $$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$
- **The Core Intuition:** Updating initial prior belief $P(A)$ upon observing new evidence $B$ to yield posterior belief $P(A|B)$.
- **The Medical Screening Paradox:**
  - Disease Prevalence: $0.1\%$ ($P(D) = 0.001$)
  - Test Sensitivity: $99\%$ ($P(+|D) = 0.99$)
  - False Positive Rate: $1\%$ ($P(+|\neg D) = 0.01$)
  - **Posterior Probability:**
    $$P(D|+) = \frac{0.99 \times 0.001}{(0.99 \times 0.001) + (0.01 \times 0.999)} = \frac{0.00099}{0.01098} \approx 9.02\%$$
- **Business Takeaway:** Even a 99% accurate test yields over 90% false alarms when the base rate is rare.

---

## Slide 4: Video Case Study 2 — Central Limit Theorem (CLT) (Q21)
- **The Fundamental Theorem:**
  - For any population with mean $\mu$ and standard deviation $\sigma$ (regardless of whether the distribution is exponential, uniform, or skewed):
  - The distribution of the sample mean $\bar{X}$ approaches a Normal distribution as sample size $n \ge 30$:
    $$\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma}{\sqrt{n}}\right)$$
- **Monte Carlo Simulation Evidence:**
  - Drawing 2,000 samples of $n=35$ from a heavily skewed Exponential ($\lambda = 0.5, \mu = 2.0$):
  - Observed Sampling Mean = $2.0014 \approx 2.0000$
  - Observed $SE = 0.3394 \approx$ Theoretical $SE = 0.3381$
- **Business Impact:** Justifies constructing confidence intervals and running z-tests on customer spending, delivery times, and website traffic without assuming raw data follows a bell curve.

---

## Slide 5: Video Case Study 3 — Type I & Type II Errors (Q40)
- **The Decision Matrix:**

| Reality \ Decision | Fail to Reject $H_0$ | Reject $H_0$ |
| :--- | :--- | :--- |
| **$H_0$ is True** | Correct Decision ($1 - \alpha$) | **Type I Error ($\alpha$, False Positive)** |
| **$H_0$ is False** | **Type II Error ($\beta$, False Negative)** | Correct Decision (**Power: $1 - \beta$**) |

- **Business Asymmetry & Capital Costs:**
  - *Fraud Detection:* A Type II error (failing to catch a fraudulent transaction) costs direct capital loss.
  - *Spam Filter:* A Type I error (blocking a legitimate invoice as spam) causes severe client friction.
  - *Clinical Trials:* A Type I error releases an ineffective drug; a Type II error abandons a cure.

---

## Slide 6: Video Case Study 4 — Correlation vs. Causation & Confounders (Q41 & Q62)
- **The Golden Rule:** Correlation ($r \in [-1, 1]$) does **not** imply causation.
- **The Confounder Problem:**
  - Ice cream sales and coastal shark attacks show strong correlation ($r = 0.88$).
  - Does eating ice cream cause shark attacks? **No.**
  - Lurking Confounder: **Summer Temperature**. High heat drives both ice cream consumption and ocean swimming.
- **Deep Dive on Q62 (Sleep vs. Productivity):**
  - High sleep correlates with high employee output.
  - Forcing workers to sleep 10 hours will not automatically increase sales. Confounders like lower stress and work-life balance drive both.
  - **Resolution:** Only randomized controlled A/B experiments can verify true causal impact.

---

## Slide 7: Video Case Study 5 — Marketing A/B Testing Z-Test (Q78)
- **Experimental Setup:**
  - Control Variant A: $N_A = 2,000, X_A = 120 \implies p_A = 6.00\%$
  - Redesigned Variant B: $N_B = 2,000, X_B = 165 \implies p_B = 8.25\%$
  - Observed Relative Lift: $+37.50\%$
- **Statistical Hypothesis Test:**
  - $H_0: p_B - p_A \le 0 \quad \text{vs.} \quad H_a: p_B - p_A > 0$
  - Pooled Proportion $\hat{p} = \frac{120 + 165}{4000} = 0.07125$
  - Standard Error $SE = \sqrt{\hat{p}(1-\hat{p})(2/n)} = 0.008135$
  - Z-Statistic:
    $$Z = \frac{0.0825 - 0.0600}{0.008135} = 2.766 \implies p = 0.0028 < 0.01$$
  - **Decision:** Reject $H_0$; lift is statistically significant at $\alpha = 0.05$.

---

## Slide 8: Sample Size & Minimum Detectable Effect (MDE) Sizing
- **Pre-Experiment Power Analysis:**
  $$n = \frac{2 \cdot (Z_{\alpha/2} + Z_{\beta})^2 \cdot \bar{p}(1 - \bar{p})}{(p_B - p_A)^2}$$
- Given $\alpha = 0.05$ ($Z_{\alpha/2} = 1.96$), Power $= 80\%$ ($Z_{\beta} = 0.84$), baseline $6\%$, and relative MDE $25\%$:
  - Required sample size: **3,842 users per variant**.
- **Business Guardrail:** Avoid "p-hacking" and peeking before reaching the target sample size.

---

## Slide 9: Linear Algebra & Vector Calculus Highlights
- **Q1 & Q2:** Vectors represent directional feature embeddings; scalars represent magnitudes (e.g. learning rate $\eta$, conversion rate).
- **Q5:** L2 Euclidean Norm: $\|v\|_2 = \sqrt{\sum v_i^2}$, foundation of Ridge Regression penalty.
- **Q8 & Q9:** Basis vectors span coordinate spaces; linear transformations map features without warping origin.
- **Q10:** Eigenvectors: $A v = \lambda v$, foundation of Principal Component Analysis (PCA) dimensionality reduction.

---

## Slide 10: Numerical Problem Highlights
- **Q59 (Two Dice Sum = 5 or 8):**
  - Sum 5 outcomes: $(1,4), (2,3), (3,2), (4,1) \implies 4$
  - Sum 8 outcomes: $(2,6), (3,5), (4,4), (5,3), (6,2) \implies 5$
  - $P(\text{Sum 5 or 8}) = \frac{9}{36} = 0.2500$ (25.0%).
- **Q61 (Jeremy Test Score Z-Score):**
  - $Z = \frac{178 - 160}{15} = 1.20 \implies 88.49^{\text{th}}$ percentile rank.
- **Q64 (Supercar Observation Probability):**
  - $P(\ge 1 \text{ Supercar}) = 1 - (1 - 0.30)^3 = 1 - 0.343 = 0.6570$ (65.70%).

---

## Slide 11: Descriptive Statistics & Data Quality Highlights
- **Q25 (Outlier Detection):**
  - Tukey's IQR Method: Outliers lie outside $[Q_1 - 1.5 \times IQR, Q_3 + 1.5 \times IQR]$.
  - Z-Score threshold: $|Z| > 3.0$.
- **Q57 (Bessel's Correction):**
  - Sample variance divides by $n - 1$ instead of $n$ to correct for downward bias when estimating unknown population mean $\mu$.
- **Q65 (Empirical Rule 68-95-99.7):**
  - $68.27\%$ within $\pm 1\sigma$, $95.45\%$ within $\pm 2\sigma$, $99.73\%$ within $\pm 3\sigma$.

---

## Slide 12: Statistical Inference & Confidence Intervals
- **Q42 & Q43 (Confidence Intervals):**
  - $95\%$ Confidence Level means: If we repeat sampling 100 times, 95 of the constructed intervals will capture true population parameter $\mu$.
  - It does **not** mean there is a 95% probability that $\mu$ lies in a single fixed interval (frequentist interpretation).
- **Q74 (Sampling Error Reduction):**
  - Margin of error $ME = Z \cdot \frac{\sigma}{\sqrt{n}}$. Quadrupling sample size $n$ cuts error in half.

---

## Slide 13: Software & Testing Verification Suite
- **Modular Python Engine:** `statistical_engine.py` implements all 10 algorithms with NumPy and SciPy.
- **Automated Pytest Suite:** `tests/test_statistical_engine.py` validates all 10 mathematical assertions:
  ```
  tests/test_statistical_engine.py::test_01_bayes_theorem_calculation PASSED
  tests/test_statistical_engine.py::test_02_central_limit_theorem_convergence PASSED
  tests/test_statistical_engine.py::test_03_dice_sum_probability_q59 PASSED
  tests/test_statistical_engine.py::test_04_z_score_calculation_q61 PASSED
  tests/test_statistical_engine.py::test_05_supercar_probability_q64 PASSED
  tests/test_statistical_engine.py::test_06_bessels_correction_sample_variance PASSED
  tests/test_statistical_engine.py::test_07_ab_testing_two_proportions_z_test PASSED
  tests/test_statistical_engine.py::test_08_sample_size_determination_mde PASSED
  tests/test_statistical_engine.py::test_09_chi_square_independence_test PASSED
  tests/test_statistical_engine.py::test_10_submission_files_and_figures_integrity PASSED
  10 passed in 2.98s
  ```

---

## Slide 14: Final Submission Checklist & Artifacts
- [x] **80 Question Master Bank:** `ALL_80_QUESTIONS_ANSWERED.md`
- [x] **50 Question Final Submission:** `FINAL_SUBMISSION_50_QUESTIONS.md`
- [x] **Pre-Executed Jupyter Notebook:** `Applied_Business_Analytics_Interactive_Grind.ipynb`
- [x] **Live Python Simulation Engine:** `statistical_engine.py`
- [x] **6 High-Resolution Visualizations:** `figures/01` to `06`
- [x] **Automated Acceptance Test Suite:** `tests/test_statistical_engine.py` (10/10 passed)
- [x] **Video Presentation Script & Timeline:** `VIDEO_PRESENTATION_SCRIPT.md`

---

## Slide 15: Conclusion & Q&A
- **Key Takeaway:** Statistical rigor and probabilistic thinking are the indispensable backbone of reliable data science and autonomous AI systems.
- **GitHub Repository:** [https://github.com/Jigneshxi/applied-business-analytics-interview-grind](https://github.com/Jigneshxi/applied-business-analytics-interview-grind)
- **Thank You!** Open for questions and discussion.
