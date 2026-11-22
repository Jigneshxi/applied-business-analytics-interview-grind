"""
test_statistical_engine.py
Automated Unit Test Suite for Applied Business Analytics (M1_ABA).
10 comprehensive unit tests covering:
  1. Bayes' Theorem & Base Rate Fallacy (Q18)
  2. Central Limit Theorem (CLT) Convergence (Q21)
  3. Two Dice Sum Probability Calculation (Q59)
  4. Jeremy Z-Score & Percentile Rank (Q61)
  5. Supercar Observation Probability (Q64)
  6. Bessel's Correction Sample Variance (Q57)
  7. Two-Proportion A/B Testing Z-Score & Lift (Q78)
  8. Minimum Detectable Effect Sample Size Formula (Q78)
  9. Chi-Square Test of Independence (Q75)
  10. Submission Documents & Figure Assets Integrity
"""

import os
import sys
import math
import pytest
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from statistical_engine import StatisticalEngine

FIGURES_DIR = os.path.join(BASE_DIR, "figures")


def test_01_bayes_theorem_calculation():
    res = StatisticalEngine.calculate_bayes_theorem(prior_p=0.001, sensitivity=0.99, false_positive_rate=0.01)
    assert math.isclose(res["posterior_probability"], 0.090164, rel_tol=1e-4)
    assert res["posterior_probability"] < 0.15  # Base rate fallacy holds


def test_02_central_limit_theorem_convergence():
    res = StatisticalEngine.simulate_central_limit_theorem(dist_type="exponential", sample_size=35, num_simulations=1500)
    assert math.isclose(res["observed_mean_of_sample_means"], res["population_mean"], rel_tol=0.05)
    assert math.isclose(res["observed_standard_error"], res["theoretical_standard_error"], rel_tol=0.10)


def test_03_dice_sum_probability_q59():
    res = StatisticalEngine.calculate_dice_sum_probability_q59()
    assert len(res["sum_5_outcomes"]) == 4
    assert len(res["sum_8_outcomes"]) == 5
    assert res["total_favorable"] == 9
    assert res["total_outcomes"] == 36
    assert math.isclose(res["probability"], 0.25, abs_tol=1e-6)


def test_04_z_score_calculation_q61():
    res = StatisticalEngine.calculate_z_score_q61(value=178.0, mean=160.0, std=15.0)
    assert res["z_score"] == 1.20
    assert math.isclose(res["percentile_rank"], 88.49, abs_tol=0.5)


def test_05_supercar_probability_q64():
    res = StatisticalEngine.calculate_supercar_probability_q64(prob_single_interval=0.30, intervals=3)
    assert math.isclose(res["prob_none_all"], 0.3430, abs_tol=1e-4)
    assert math.isclose(res["prob_at_least_one"], 0.6570, abs_tol=1e-4)


def test_06_bessels_correction_sample_variance():
    sample = [10.0, 12.0, 14.0, 16.0, 18.0]
    res = StatisticalEngine.calculate_bessels_correction_variance(sample)
    assert res["sample_size"] == 5
    assert res["mean"] == 14.0
    assert res["biased_variance_div_n"] == 8.0
    assert res["unbiased_variance_div_n_minus_1"] == 10.0
    assert res["correction_factor"] == 1.25


def test_07_ab_testing_two_proportions_z_test():
    res = StatisticalEngine.calculate_ab_test_two_proportions(conversions_a=120, sample_a=2000, conversions_b=165, sample_b=2000)
    assert res["control_rate"] == 0.0600
    assert res["variant_rate"] == 0.0825
    assert res["relative_lift_pct"] == 37.5
    assert res["z_statistic"] > 2.5
    assert res["p_value_two_tailed"] < 0.01
    assert res["statistically_significant"] is True


def test_08_sample_size_determination_mde():
    n_req = StatisticalEngine.calculate_sample_size_mde(baseline_rate=0.05, mde_relative=0.20, alpha=0.05, power=0.80)
    assert n_req > 3000
    assert n_req < 35000


def test_09_chi_square_independence_test():
    table = np.array([[50, 30], [20, 60]])
    res = StatisticalEngine.calculate_chi_square_independence(table)
    assert res["degrees_of_freedom"] == 1
    assert res["chi2_statistic"] > 10.0
    assert res["p_value"] < 0.001


def test_10_submission_files_and_figures_integrity():
    f80 = os.path.join(BASE_DIR, "ALL_80_QUESTIONS_ANSWERED.md")
    f50 = os.path.join(BASE_DIR, "FINAL_SUBMISSION_50_QUESTIONS.md")
    readme = os.path.join(BASE_DIR, "README.md")

    assert os.path.exists(f80), "ALL_80_QUESTIONS_ANSWERED.md missing"
    assert os.path.exists(f50), "FINAL_SUBMISSION_50_QUESTIONS.md missing"
    assert os.path.exists(readme), "README.md missing"

    expected_figs = [
        "01_domain_distribution_pie.png",
        "02_bayes_theorem_posterior_curve.png",
        "03_central_limit_theorem_convergence.png",
        "04_type_i_type_ii_error_tradeoff.png",
        "05_correlation_vs_causation_confounder.png",
        "06_ab_testing_conversion_distributions.png"
    ]
    for fig in expected_figs:
        p = os.path.join(FIGURES_DIR, fig)
        assert os.path.exists(p), f"Figure {fig} missing"
