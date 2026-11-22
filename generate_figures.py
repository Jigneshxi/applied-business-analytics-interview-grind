"""
generate_figures.py
Generates 6 publication-quality statistical figures in figures/ for M1_ABA:
  1. 01_domain_distribution_pie.png
  2. 02_bayes_theorem_posterior_curve.png
  3. 03_central_limit_theorem_convergence.png
  4. 04_type_i_type_ii_error_tradeoff.png
  5. 05_correlation_vs_causation_confounder.png
  6. 06_ab_testing_conversion_distributions.png
"""

import os
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

from statistical_engine import StatisticalEngine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")
plt.rcParams.update({"font.size": 11, "font.family": "sans-serif"})


def main():
    print("Generating statistical analysis figures...")

    # Figure 1: Domain Distribution Pie Chart
    domains = [
        "Probability Theory & Distributions",
        "Statistical Inference & CIs",
        "Hypothesis & A/B Testing",
        "Linear Algebra & Vectors",
        "Descriptive Stats & Quality",
        "Calculus & ML Optimization"
    ]
    counts = [20, 18, 18, 12, 7, 5]
    colors = ["#2b5c8f", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02"]

    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, texts, autotexts = ax.pie(
        counts, labels=domains, autopct="%1.1f%%", startangle=140,
        colors=colors, wedgeprops=dict(width=0.6, edgecolor="white", linewidth=2)
    )
    for at in autotexts:
        at.set_color("white")
        at.set_fontweight("bold")
    ax.set_title("Master Question Bank: 80 Questions Domain Distribution", fontsize=13, fontweight="bold", pad=12)
    plt.tight_layout()
    f1 = os.path.join(FIGURES_DIR, "01_domain_distribution_pie.png")
    plt.savefig(f1, dpi=300)
    plt.close()
    print(f"Generated: {f1}")

    # Figure 2: Bayes Theorem Posterior vs Prior (Base Rate Fallacy)
    priors = np.logspace(-4, -1, 100)
    posteriors_sens99 = [StatisticalEngine.calculate_bayes_theorem(p, 0.99, 0.01)["posterior_probability"] for p in priors]
    posteriors_sens95 = [StatisticalEngine.calculate_bayes_theorem(p, 0.95, 0.05)["posterior_probability"] for p in priors]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(priors * 100, [p * 100 for p in posteriors_sens99], label="99% Sensitivity / 1% FPR (High Accuracy)", color="#2b5c8f", linewidth=2.5)
    ax.plot(priors * 100, [p * 100 for p in posteriors_sens95], label="95% Sensitivity / 5% FPR (Standard Test)", color="#d95f02", linewidth=2.5, linestyle="--")
    ax.axvline(0.1, color="crimson", linestyle=":", label="Rare Disease Prevalence (0.1%)")
    ax.scatter([0.1], [9.02], color="red", s=80, zorder=5)
    ax.text(0.15, 12, "Base Rate Paradox:\nAt 0.1% prior, 99% test\nyields only ~9% posterior!", fontsize=10, fontweight="bold", color="crimson")
    ax.set_xscale("log")
    ax.set_title("Bayes' Theorem: Posterior Probability vs. Prior Base Rate", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Prior Prevalence (%) [Log Scale]", fontsize=11)
    ax.set_ylabel("Posterior Probability P(Disease|Positive) (%)", fontsize=11)
    ax.legend(frameon=True)
    plt.tight_layout()
    f2 = os.path.join(FIGURES_DIR, "02_bayes_theorem_posterior_curve.png")
    plt.savefig(f2, dpi=300)
    plt.close()
    print(f"Generated: {f2}")

    # Figure 3: Central Limit Theorem Convergence
    np.random.seed(42)
    pop = np.random.exponential(scale=2.0, size=20000)
    sample_means_n5 = [np.mean(np.random.choice(pop, 5)) for _ in range(2500)]
    sample_means_n35 = [np.mean(np.random.choice(pop, 35)) for _ in range(2500)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    sns.histplot(pop, bins=35, color="#e7298a", kde=True, ax=ax1, edgecolor="black")
    ax1.set_title("Skewed Population (Exponential Distribution, λ=0.5)", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Value")
    ax1.set_xlim(0, 14)

    sns.histplot(sample_means_n35, bins=30, color="#2b5c8f", kde=True, ax=ax2, edgecolor="black", label="Sample Size n=35 (Normal)")
    sns.histplot(sample_means_n5, bins=30, color="#ff7f0e", kde=True, ax=ax2, edgecolor="black", alpha=0.4, label="Sample Size n=5 (Skewed)")
    ax2.axvline(2.0, color="crimson", linestyle="--", linewidth=2, label="Population Mean (μ = 2.0)")
    ax2.set_title("Central Limit Theorem: Sampling Distribution of Means", fontsize=12, fontweight="bold")
    ax2.set_xlabel("Sample Mean Value")
    ax2.legend()
    plt.tight_layout()
    f3 = os.path.join(FIGURES_DIR, "03_central_limit_theorem_convergence.png")
    plt.savefig(f3, dpi=300)
    plt.close()
    print(f"Generated: {f3}")

    # Figure 4: Type I and Type II Error Tradeoff (Q40)
    x = np.linspace(-4, 8, 1000)
    h0 = stats.norm.pdf(x, loc=0, scale=1)
    ha = stats.norm.pdf(x, loc=3, scale=1)
    crit_val = 1.645

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x, h0, label="Null Hypothesis H0 (No Effect)", color="#1f77b4", linewidth=2.2)
    ax.plot(x, ha, label="Alternative Hypothesis Ha (True Effect)", color="#2ca02c", linewidth=2.2)
    ax.axvline(crit_val, color="black", linestyle="--", linewidth=1.5, label=f"Critical Threshold (Z={crit_val})")

    # Fill Type I (alpha)
    ax.fill_between(x[x >= crit_val], h0[x >= crit_val], color="crimson", alpha=0.6, label="Type I Error (α = False Positive)")
    # Fill Type II (beta)
    ax.fill_between(x[x < crit_val], ha[x < crit_val], color="orange", alpha=0.4, label="Type II Error (β = False Negative)")
    # Fill Power
    ax.fill_between(x[x >= crit_val], ha[x >= crit_val], color="lightgreen", alpha=0.3, label="Statistical Power (1 - β)")

    ax.set_title("Hypothesis Testing Decision Space: Type I (α) vs. Type II (β) Errors", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Test Statistic Value (Z-Score)", fontsize=11)
    ax.set_ylabel("Probability Density", fontsize=11)
    ax.legend(loc="upper left")
    plt.tight_layout()
    f4 = os.path.join(FIGURES_DIR, "04_type_i_type_ii_error_tradeoff.png")
    plt.savefig(f4, dpi=300)
    plt.close()
    print(f"Generated: {f4}")

    # Figure 5: Correlation vs Causation Confounder (Q41 & Q62)
    np.random.seed(42)
    temperature = np.random.uniform(15, 38, 200)
    ice_cream_sales = 50 + 12 * temperature + np.random.normal(0, 25, 200)
    shark_attacks = 1 + 0.45 * temperature + np.random.normal(0, 1.5, 200)
    corr = np.corrcoef(ice_cream_sales, shark_attacks)[0, 1]

    fig, ax = plt.subplots(figsize=(8, 5))
    scatter = ax.scatter(ice_cream_sales, shark_attacks, c=temperature, cmap="coolwarm", s=50, edgecolor="black", alpha=0.85)
    cbar = plt.colorbar(scatter)
    cbar.set_label("Confounder: Summer Temperature (°C)", fontsize=10)
    sns.regplot(x=ice_cream_sales, y=shark_attacks, scatter=False, ax=ax, color="darkred")
    ax.set_title(f"Spurious Correlation vs. Causation (r = {corr:.3f})", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Daily Ice Cream Sales ($)", fontsize=11)
    ax.set_ylabel("Observed Coastal Shark Attacks", fontsize=11)
    plt.tight_layout()
    f5 = os.path.join(FIGURES_DIR, "05_correlation_vs_causation_confounder.png")
    plt.savefig(f5, dpi=300)
    plt.close()
    print(f"Generated: {f5}")

    # Figure 6: Marketing A/B Testing Distribution (Q78)
    n_a, n_b = 2000, 2000
    p_a, p_b = 0.06, 0.0825  # 6% vs 8.25% (37.5% lift)
    se_a = math.sqrt(p_a * (1 - p_a) / n_a)
    se_b = math.sqrt(p_b * (1 - p_b) / n_b)

    x_axis = np.linspace(0.04, 0.105, 500)
    y_a = stats.norm.pdf(x_axis, p_a, se_a)
    y_b = stats.norm.pdf(x_axis, p_b, se_b)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x_axis * 100, y_a, label="Control (Variant A, p=6.0%)", color="#1f77b4", linewidth=2.5)
    ax.plot(x_axis * 100, y_b, label="Variant B (Landing Page Redesign, p=8.25%)", color="#2ca02c", linewidth=2.5)
    ax.fill_between(x_axis * 100, y_a, color="#1f77b4", alpha=0.15)
    ax.fill_between(x_axis * 100, y_b, color="#2ca02c", alpha=0.25)
    ax.axvline(p_a * 100, color="#1f77b4", linestyle="--")
    ax.axvline(p_b * 100, color="#2ca02c", linestyle="--")
    ax.set_title("Marketing A/B Testing: Two-Proportion Hypothesis Lift (p < 0.01)", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Conversion Rate (%)", fontsize=11)
    ax.set_ylabel("Probability Density", fontsize=11)
    ax.legend(frameon=True)
    plt.tight_layout()
    f6 = os.path.join(FIGURES_DIR, "06_ab_testing_conversion_distributions.png")
    plt.savefig(f6, dpi=300)
    plt.close()
    print(f"Generated: {f6}")

    print("All 6 figures successfully generated!")


if __name__ == "__main__":
    main()
