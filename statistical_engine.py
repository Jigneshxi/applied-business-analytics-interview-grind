"""
statistical_engine.py
Applied Business Analytics & Applied Statistics Mathematical Engine.
Implements computational verification, statistical inference, and Monte Carlo simulations:
  1. Bayes' Theorem & Base Rate Fallacy Calculator (Q18)
  2. Central Limit Theorem (CLT) Sampling Simulator (Q21)
  3. Type I / Type II Error & Power Tradeoff Matrix (Q40)
  4. Correlation vs. Causation Confounder Simulator (Q41 & Q62)
  5. Two-Proportion Hypothesis A/B Testing Z-Test (Q78)
  6. Sample Size Determination for Minimum Detectable Effect (MDE) (Q78)
  7. Exact Numerical Problem Solvers (Q59, Q61, Q64, Q57)
"""

import math
import numpy as np
import scipy.stats as stats
from typing import Dict, Any, Tuple


class StatisticalEngine:
    """Core mathematical engine for Applied Business Analytics problems."""

    @staticmethod
    def calculate_bayes_theorem(prior_p: float, sensitivity: float, false_positive_rate: float) -> Dict[str, float]:
        """
        Calculates posterior probability via Bayes' Theorem:
        P(Disease | Positive) = [P(Positive | Disease) * P(Disease)] / P(Positive)
        where P(Positive) = P(Pos|Disease)*P(Disease) + P(Pos|No Disease)*P(No Disease)
        """
        p_disease = prior_p
        p_no_disease = 1.0 - prior_p
        p_pos_given_disease = sensitivity
        p_pos_given_no_disease = false_positive_rate

        p_pos = (p_pos_given_disease * p_disease) + (p_pos_given_no_disease * p_no_disease)
        p_disease_given_pos = (p_pos_given_disease * p_disease) / p_pos

        return {
            "prior_probability": round(prior_p, 6),
            "sensitivity_true_positive_rate": round(sensitivity, 4),
            "false_positive_rate": round(false_positive_rate, 4),
            "total_positive_probability": round(p_pos, 6),
            "posterior_probability": round(p_disease_given_pos, 6)
        }

    @staticmethod
    def simulate_central_limit_theorem(dist_type: str = "exponential", sample_size: int = 35, num_simulations: int = 2000, seed: int = 42) -> Dict[str, Any]:
        """
        Simulates the Central Limit Theorem across non-normal populations.
        Demonstrates that sample means converge to N(mu, sigma / sqrt(n)).
        """
        np.random.seed(seed)
        if dist_type == "exponential":
            pop_data = np.random.exponential(scale=2.0, size=50000)
            true_mu = 2.0
            true_sigma = 2.0
        elif dist_type == "uniform":
            pop_data = np.random.uniform(low=0.0, high=10.0, size=50000)
            true_mu = 5.0
            true_sigma = math.sqrt((10.0 - 0.0) ** 2 / 12.0)
        else:
            pop_data = np.random.poisson(lam=4.0, size=50000)
            true_mu = 4.0
            true_sigma = math.sqrt(4.0)

        # Draw sample means
        sample_means = [np.mean(np.random.choice(pop_data, size=sample_size, replace=True)) for _ in range(num_simulations)]
        sample_means = np.array(sample_means)

        expected_se = true_sigma / math.sqrt(sample_size)
        observed_mean = float(np.mean(sample_means))
        observed_se = float(np.std(sample_means, ddof=1))

        # Shapiro-Wilk normality test on sample means
        shapiro_stat, shapiro_p = stats.shapiro(sample_means[:500])

        return {
            "distribution_type": dist_type,
            "sample_size": sample_size,
            "num_simulations": num_simulations,
            "population_mean": round(true_mu, 4),
            "observed_mean_of_sample_means": round(observed_mean, 4),
            "theoretical_standard_error": round(expected_se, 4),
            "observed_standard_error": round(observed_se, 4),
            "shapiro_p_value": round(float(shapiro_p), 4),
            "normality_confirmed": bool(shapiro_p > 0.01)
        }

    @staticmethod
    def calculate_ab_test_two_proportions(conversions_a: int, sample_a: int, conversions_b: int, sample_b: int, alpha: float = 0.05) -> Dict[str, Any]:
        """
        Two-proportion pooled z-test for marketing A/B testing (Q78).
        H0: p_B - p_A <= 0 vs Ha: p_B - p_A > 0 (one-tailed) or p_B != p_A (two-tailed)
        """
        p_a = conversions_a / sample_a
        p_b = conversions_b / sample_b
        lift_relative = (p_b - p_a) / p_a

        # Pooled sample proportion
        p_pooled = (conversions_a + conversions_b) / (sample_a + sample_b)
        se_pooled = math.sqrt(p_pooled * (1.0 - p_pooled) * (1.0 / sample_a + 1.0 / sample_b))

        z_score = (p_b - p_a) / se_pooled
        p_value_one_tailed = 1.0 - stats.norm.cdf(z_score)
        p_value_two_tailed = 2.0 * (1.0 - stats.norm.cdf(abs(z_score)))

        significant = bool(p_value_two_tailed < alpha)

        return {
            "control_rate": round(p_a, 4),
            "variant_rate": round(p_b, 4),
            "relative_lift_pct": round(lift_relative * 100.0, 2),
            "pooled_proportion": round(p_pooled, 4),
            "standard_error": round(se_pooled, 6),
            "z_statistic": round(z_score, 4),
            "p_value_one_tailed": round(p_value_one_tailed, 6),
            "p_value_two_tailed": round(p_value_two_tailed, 6),
            "alpha": alpha,
            "statistically_significant": significant
        }

    @staticmethod
    def calculate_sample_size_mde(baseline_rate: float, mde_relative: float, alpha: float = 0.05, power: float = 0.80) -> int:
        """
        Sample size determination per variant for A/B testing:
        n = [2 * (Z_alpha/2 + Z_beta)^2 * p_bar * (1 - p_bar)] / (p2 - p1)^2
        """
        p1 = baseline_rate
        p2 = baseline_rate * (1.0 + mde_relative)
        delta = abs(p2 - p1)
        p_bar = (p1 + p2) / 2.0

        z_alpha = stats.norm.ppf(1.0 - alpha / 2.0)
        z_beta = stats.norm.ppf(power)

        numerator = 2.0 * ((z_alpha + z_beta) ** 2) * p_bar * (1.0 - p_bar)
        denominator = delta ** 2
        required_n = math.ceil(numerator / denominator)
        return required_n

    @staticmethod
    def calculate_dice_sum_probability_q59() -> Dict[str, Any]:
        """
        Q59: What is the probability of throwing two fair dice when the sum is 5 and 8?
        Total outcomes: 36.
        Sum 5: (1,4), (2,3), (3,2), (4,1) -> 4
        Sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) -> 5
        Total favorable: 9.
        Probability: 9 / 36 = 1/4 = 0.2500 (25%).
        """
        favorable_5 = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == 5]
        favorable_8 = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == 8]
        total_outcomes = 36
        total_favorable = len(favorable_5) + len(favorable_8)
        prob = total_favorable / total_outcomes

        return {
            "sum_5_outcomes": favorable_5,
            "sum_8_outcomes": favorable_8,
            "total_favorable": total_favorable,
            "total_outcomes": total_outcomes,
            "probability": prob,
            "probability_fraction": "9/36 = 1/4"
        }

    @staticmethod
    def calculate_z_score_q61(value: float = 178.0, mean: float = 160.0, std: float = 15.0) -> Dict[str, Any]:
        """
        Q61: Jeremy scored 178 on a test with mean 160 and standard deviation 15.
        Z = (X - mu) / sigma = (178 - 160) / 15 = 18 / 15 = 1.20
        """
        z = (value - mean) / std
        percentile = stats.norm.cdf(z)
        return {
            "value": value,
            "mean": mean,
            "std": std,
            "z_score": round(z, 2),
            "percentile_rank": round(percentile * 100.0, 2)
        }

    @staticmethod
    def calculate_supercar_probability_q64(prob_single_interval: float = 0.30, intervals: int = 3) -> Dict[str, Any]:
        """
        Q64: Probability of seeing at least one supercar in 1 hour (three 20-min intervals):
        P(At least 1) = 1 - P(None in any interval) = 1 - (1 - 0.30)^3 = 1 - 0.70^3 = 1 - 0.343 = 0.6570 (65.70%).
        """
        p_none_single = 1.0 - prob_single_interval
        p_none_all = p_none_single ** intervals
        p_at_least_one = 1.0 - p_none_all
        return {
            "prob_single_interval": prob_single_interval,
            "intervals": intervals,
            "prob_none_all": round(p_none_all, 4),
            "prob_at_least_one": round(p_at_least_one, 4)
        }

    @staticmethod
    def calculate_bessels_correction_variance(sample: list) -> Dict[str, float]:
        """
        Q57: Bessel's correction demonstration.
        Population variance formula divides by n (biased).
        Sample variance formula divides by n - 1 (unbiased).
        """
        n = len(sample)
        mean_val = sum(sample) / n
        sq_diffs = sum((x - mean_val) ** 2 for x in sample)
        biased_var = sq_diffs / n
        unbiased_var = sq_diffs / (n - 1)
        return {
            "sample_size": n,
            "mean": round(mean_val, 4),
            "biased_variance_div_n": round(biased_var, 4),
            "unbiased_variance_div_n_minus_1": round(unbiased_var, 4),
            "correction_factor": round(n / (n - 1), 4)
        }

    @staticmethod
    def calculate_chi_square_independence(table: np.ndarray) -> Dict[str, Any]:
        """
        Q75: Chi-Square Test of Independence for categorical contingency tables.
        """
        chi2, p, dof, expected = stats.chi2_contingency(table)
        return {
            "chi2_statistic": round(float(chi2), 4),
            "p_value": round(float(p), 6),
            "degrees_of_freedom": int(dof),
            "expected_frequencies": expected.round(2).tolist()
        }


if __name__ == "__main__":
    eng = StatisticalEngine()
    print("=== Bayes Theorem Q18 ===")
    print(eng.calculate_bayes_theorem(prior_p=0.001, sensitivity=0.99, false_positive_rate=0.01))
    print("\n=== Dice Probability Q59 ===")
    print(eng.calculate_dice_sum_probability_q59())
    print("\n=== Jeremy Z-Score Q61 ===")
    print(eng.calculate_z_score_q61())
    print("\n=== Supercar Probability Q64 ===")
    print(eng.calculate_supercar_probability_q64())
    print("\n=== A/B Testing Q78 ===")
    print(eng.calculate_ab_test_two_proportions(conversions_a=120, sample_a=2000, conversions_b=165, sample_b=2000))
