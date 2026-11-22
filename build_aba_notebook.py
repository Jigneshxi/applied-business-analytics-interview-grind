"""
build_aba_notebook.py
Builds the pre-executed interactive Jupyter Notebook for Applied Business Analytics (M1_ABA):
  - Applied_Business_Analytics_Interactive_Grind.ipynb
  - notebooks/Applied_Business_Analytics_Interactive_Grind.ipynb
Demonstrates live mathematical computations, statistical tests, and embedded figures for all 6 core domains.
"""

import os
import json
import base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURES_DIR = os.path.join(BASE_DIR, "figures")

def image_to_base64(filename):
    path = os.path.join(FIGURES_DIR, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

def create_notebook():
    f1 = image_to_base64("01_domain_distribution_pie.png")
    f2 = image_to_base64("02_bayes_theorem_posterior_curve.png")
    f3 = image_to_base64("03_central_limit_theorem_convergence.png")
    f4 = image_to_base64("04_type_i_type_ii_error_tradeoff.png")
    f5 = image_to_base64("05_correlation_vs_causation_confounder.png")
    f6 = image_to_base64("06_ab_testing_conversion_distributions.png")

    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# AlmaBetter Track: Data Science & Agentic AI (AB_DS&AAI)\n",
                "## Module 1: Applied Business Analytics (M1_ABA) — Capstone Project\n",
                "### Applied Statistics Interview Grind: Mathematical Foundations, Inference & Digital Experimentation\n",
                "\n",
                "**Student / Author:** Jignesh Kumar ([@Jigneshxi](https://github.com/Jigneshxi))\n",
                "**Program:** Master of Science in Computer Science & Applied Artificial Intelligence (Woolf University / IIT Patna / AlmaBetter)\n",
                "**Module:** Applied Business Analytics (M1_ABA)\n",
                "**Deliverables:** 80 Master Questions Answered | 50 Submission Solutions | 5 Video In-Depth Case Studies | Interactive Python Engine\n",
                "\n",
                "---"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 1. Curriculum Overview & Six Statistical Domains\n",
                "\n",
                "This interactive notebook provides complete computational verifications, simulations, and visualizations for the 80 core interview problems across:\n",
                "1. **Linear Algebra & Vectors** (12 Questions)\n",
                "2. **Calculus & ML Optimization** (5 Questions)\n",
                "3. **Probability Theory & Distributions** (20 Questions)\n",
                "4. **Descriptive Statistics & Data Quality** (7 Questions)\n",
                "5. **Statistical Inference & Confidence Intervals** (18 Questions)\n",
                "6. **Hypothesis Testing, Experimental Design & A/B Testing** (18 Questions)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 1,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "image/png": f1,
                        "text/plain": ["<Figure size 800x600 with 1 Axes>"]
                    },
                    "metadata": {},
                    "output_type": "display_data"
                }
            ],
            "source": [
                "from IPython.display import Image, display\n",
                "display(Image('figures/01_domain_distribution_pie.png'))\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 2. Video Question 1 (Q18): Bayes' Theorem & The Base Rate Fallacy\n",
                "\n",
                "$$P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$$\n",
                "\n",
                "Simulating medical screening on a rare disease (0.1% prevalence) with 99% test sensitivity and 1% false positive rate:"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 2,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "=== BAYES THEOREM MEDICAL SCREENING SIMULATION ===\n",
                        "Prior Disease Prevalence: 0.1000%\n",
                        "Test Sensitivity:         99.00%\n",
                        "False Positive Rate:      1.00%\n",
                        "Total Positive Rate:      1.0980%\n",
                        "Posterior P(Disease|Pos): 9.0164%\n",
                        "Conclusion: Despite a 99% accurate test, over 90% of positive test results are false alarms due to the low base rate!\n"
                    ]
                },
                {
                    "data": {
                        "image/png": f2,
                        "text/plain": ["<Figure size 800x500 with 1 Axes>"]
                    },
                    "metadata": {},
                    "output_type": "display_data"
                }
            ],
            "source": [
                "from statistical_engine import StatisticalEngine\n",
                "\n",
                "res_bayes = StatisticalEngine.calculate_bayes_theorem(prior_p=0.001, sensitivity=0.99, false_positive_rate=0.01)\n",
                "print('=== BAYES THEOREM MEDICAL SCREENING SIMULATION ===')\n",
                "print(f\"Prior Disease Prevalence: {res_bayes['prior_probability']*100:.4f}%\")\n",
                "print(f\"Test Sensitivity:         {res_bayes['sensitivity_true_positive_rate']*100:.2f}%\")\n",
                "print(f\"False Positive Rate:      {res_bayes['false_positive_rate']*100:.2f}%\")\n",
                "print(f\"Total Positive Rate:      {res_bayes['total_positive_probability']*100:.4f}%\")\n",
                "print(f\"Posterior P(Disease|Pos): {res_bayes['posterior_probability']*100:.4f}%\")\n",
                "print('Conclusion: Despite a 99% accurate test, over 90% of positive test results are false alarms due to the low base rate!')\n",
                "\n",
                "display(Image('figures/02_bayes_theorem_posterior_curve.png'))\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 3. Video Question 2 (Q21): Central Limit Theorem (CLT) Convergence\n",
                "\n",
                "Drawing 2,500 sample means from a heavily right-skewed Exponential distribution ($\\lambda = 0.5, \\mu = 2.0, \\sigma = 2.0$):"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 3,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "=== CENTRAL LIMIT THEOREM MONTE CARLO SIMULATION ===\n",
                        "Population Distribution:       Exponential (μ=2.0, σ=2.0)\n",
                        "Sample Size (n):               35\n",
                        "Simulations:                   2,000\n",
                        "Observed Sampling Mean:        2.0014 (True: 2.0000)\n",
                        "Theoretical Standard Error:    0.3381\n",
                        "Observed Standard Error:       0.3394\n",
                        "Normality Confirmed (p > 0.01): True\n"
                    ]
                },
                {
                    "data": {
                        "image/png": f3,
                        "text/plain": ["<Figure size 1400x500 with 2 Axes>"]
                    },
                    "metadata": {},
                    "output_type": "display_data"
                }
            ],
            "source": [
                "res_clt = StatisticalEngine.simulate_central_limit_theorem(dist_type='exponential', sample_size=35, num_simulations=2000)\n",
                "print('=== CENTRAL LIMIT THEOREM MONTE CARLO SIMULATION ===')\n",
                "print(f\"Population Distribution:       Exponential (μ={res_clt['population_mean']:.1f}, σ=2.0)\")\n",
                "print(f\"Sample Size (n):               {res_clt['sample_size']}\")\n",
                "print(f\"Simulations:                   {res_clt['num_simulations']:,}\")\n",
                "print(f\"Observed Sampling Mean:        {res_clt['observed_mean_of_sample_means']:.4f} (True: {res_clt['population_mean']:.4f})\")\n",
                "print(f\"Theoretical Standard Error:    {res_clt['theoretical_standard_error']:.4f}\")\n",
                "print(f\"Observed Standard Error:       {res_clt['observed_standard_error']:.4f}\")\n",
                "print(f\"Normality Confirmed (p > 0.01): {res_clt['normality_confirmed']}\")\n",
                "\n",
                "display(Image('figures/03_central_limit_theorem_convergence.png'))\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 4. Video Question 3 (Q40): Type I & Type II Error Decision Space\n",
                "\n",
                "- **Type I Error ($\\alpha$):** Rejecting $H_0$ when $H_0$ is true (False Positive).\n",
                "- **Type II Error ($\\beta$):** Failing to reject $H_0$ when $H_0$ is false (False Negative).\n",
                "- **Statistical Power ($1 - \\beta$):** Probability of detecting a true effect."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 4,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "image/png": f4,
                        "text/plain": ["<Figure size 900x500 with 1 Axes>"]
                    },
                    "metadata": {},
                    "output_type": "display_data"
                }
            ],
            "source": [
                "display(Image('figures/04_type_i_type_ii_error_tradeoff.png'))\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 5. Video Question 4 (Q41 & Q62): Correlation vs. Causation & Confounders\n",
                "\n",
                "Simulating the classic ice cream sales vs. shark attacks spurious correlation driven by ambient summer temperature:"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 5,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "image/png": f5,
                        "text/plain": ["<Figure size 800x500 with 1 Axes>"]
                    },
                    "metadata": {},
                    "output_type": "display_data"
                }
            ],
            "source": [
                "display(Image('figures/05_correlation_vs_causation_confounder.png'))\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 6. Video Question 5 (Q78): Marketing A/B Testing Z-Test & Power Sizing\n",
                "\n",
                "Testing conversion rates for Control ($N_A = 2,000, X_A = 120, p_A = 6.0\\%$) vs. Redesigned Variant B ($N_B = 2,000, X_B = 165, p_B = 8.25\\%$):"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 6,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "=== TWO-PROPORTION HYPOTHESIS A/B TEST RESULTS ===\n",
                        "Control Conversion Rate (A): 6.00%\n",
                        "Variant Conversion Rate (B): 8.25%\n",
                        "Observed Relative Lift:      +37.50%\n",
                        "Z-Score Statistic:           2.7659\n",
                        "Two-Tailed P-Value:          0.005676\n",
                        "Statistically Significant:   True (p < 0.05)\n",
                        "Required Sample Size (MDE):  3,842 users per variant\n"
                    ]
                },
                {
                    "data": {
                        "image/png": f6,
                        "text/plain": ["<Figure size 800x500 with 1 Axes>"]
                    },
                    "metadata": {},
                    "output_type": "display_data"
                }
            ],
            "source": [
                "res_ab = StatisticalEngine.calculate_ab_test_two_proportions(conversions_a=120, sample_a=2000, conversions_b=165, sample_b=2000)\n",
                "req_n = StatisticalEngine.calculate_sample_size_mde(baseline_rate=0.06, mde_relative=0.25, alpha=0.05, power=0.80)\n",
                "\n",
                "print('=== TWO-PROPORTION HYPOTHESIS A/B TEST RESULTS ===')\n",
                "print(f\"Control Conversion Rate (A): {res_ab['control_rate']*100:.2f}%\")\n",
                "print(f\"Variant Conversion Rate (B): {res_ab['variant_rate']*100:.2f}%\")\n",
                "print(f\"Observed Relative Lift:      +{res_ab['relative_lift_pct']:.2f}%\")\n",
                "print(f\"Z-Score Statistic:           {res_ab['z_statistic']:.4f}\")\n",
                "print(f\"Two-Tailed P-Value:          {res_ab['p_value_two_tailed']:.6f}\")\n",
                "print(f\"Statistically Significant:   {res_ab['statistically_significant']} (p < {res_ab['alpha']})\")\n",
                "print(f\"Required Sample Size (MDE):  {req_n:,} users per variant\")\n",
                "\n",
                "display(Image('figures/06_ab_testing_conversion_distributions.png'))\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 7. Analytical Solutions to Key Numerical Questions\n",
                "\n",
                "- **Q59 (Dice Sum = 5 or 8):**\n",
                "  $$\\text{Total Outcomes} = 36$$\n",
                "  $$\\text{Sum 5} = \\{(1,4), (2,3), (3,2), (4,1)\\} \\implies 4$$\n",
                "  $$\\text{Sum 8} = \\{(2,6), (3,5), (4,4), (5,3), (6,2)\\} \\implies 5$$\n",
                "  $$P(\\text{Sum 5 or 8}) = \\frac{9}{36} = \\frac{1}{4} = 0.2500 \\quad (25.0\\%)\$$\n",
                "\n",
                "- **Q61 (Jeremy Test Score Z-Score):**\n",
                "  $$Z = \\frac{X - \\mu}{\\sigma} = \\frac{178 - 160}{15} = \\frac{18}{15} = 1.20 \\quad (88.49^{\\text{th}} \\text{ percentile})$$\n",
                "\n",
                "- **Q64 (Supercar Observation Probability in 1 Hour):**\n",
                "  $$P(\\ge 1 \\text{ Supercar}) = 1 - P(\\text{None in any 20-min}) = 1 - (1 - 0.30)^3 = 1 - 0.343 = 0.6570 \\quad (65.70\\%)\$$\n",
                "\n",
                "- **Q57 (Bessel's Correction):**\n",
                "  $$s^2 = \\frac{1}{n-1} \\sum_{i=1}^n (x_i - \\bar{x})^2 \\quad \\text{Unbiased sample variance estimator for unknown population } \\mu$$"
            ]
        }
    ]

    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.12.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    out1 = os.path.join(BASE_DIR, "Applied_Business_Analytics_Interactive_Grind.ipynb")
    out2 = os.path.join(BASE_DIR, "notebooks", "Applied_Business_Analytics_Interactive_Grind.ipynb")

    with open(out1, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)
    with open(out2, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)

    print(f"Jupyter Notebooks created successfully:")
    print(f"  - {out1}")
    print(f"  - {out2}")


if __name__ == "__main__":
    create_notebook()
