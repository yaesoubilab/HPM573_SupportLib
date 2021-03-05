import numpy as np

import SimPy.Plots.ProbDist as Plot
import SimPy.RandomVariateGenerators as RVGs
from tests.ProbDistributions.RVGtests import get_samples


def test_fitting_beta():

    print("\nTesting Beta with a=2, b=3, loc=1, scale=2:")
    dist = RVGs.Beta(a=2, b=3, loc=1, scale=2)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    # method of moment
    dict_mm_results = RVGs.Beta.fit_mm(
        mean=np.mean(data), st_dev=np.std(data), minimum=1, maximum=3)
    # maximum likelihood
    dict_ml_results = RVGs.Beta.fit_ml(data=data, minimum=1, maximum=3)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_beta_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_beta_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_beta_binomial():

    print("\nTesting Beta-Binomial with n=100, a=2, b=3, loc=1, scale=2:")
    dist = RVGs.BetaBinomial(n=20, a=2, b=3, loc=1)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    # method of moment
    dict_mm_results = RVGs.BetaBinomial.fit_mm(
        mean=np.mean(data), st_dev=np.std(data), n=20, fixed_location=1)
    # maximum likelihood
    dict_ml_results = RVGs.BetaBinomial.fit_ml(data=data, fixed_location=1)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_beta_binomial_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_beta_binomial_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_binomial():

    print("\nTesting Binomial with n=100, p=0.3, loc=1:")
    dist = RVGs.Binomial(n=100, p=0.3, loc=1)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    # method of moment
    dict_mm_results = RVGs.Binomial.fit_mm(
        mean=np.mean(data), st_dev=np.std(data), fixed_location=1)
    # maximum likelihood
    dict_ml_results = RVGs.Binomial.fit_ml(
        data=data, fixed_location=1)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_binomial_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_binomial_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_empirical():

    print("\nTesting empirical with p=[0.1, 0.2, 0.7]")
    dist = RVGs.Empirical(probabilities=[0.1, 0.2, 0.7])

    data = np.array(get_samples(dist, np.random))
    # method of moments
    dict_mm_results = RVGs.Empirical.fit_mm(
        data=data, bin_size=1)

    print("  Fit:")
    print("    MM:", dict_mm_results)


def test_fitting_exponential():

    print("\nTesting Exponential with scale=0.5, loc=2")
    dist = RVGs.Exponential(scale=0.5, loc=2)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    # method of moment
    dict_mm_results = RVGs.Exponential.fit_mm(
        mean=np.average(data), fixed_location=2)
    # maximum likelihood
    dict_ml_results = RVGs.Exponential.fit_ml(
        data=data, fixed_location=2)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_exponential_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_exponential_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_gamma():

    print('\nTesting Gamma with a=10, scale=1, loc=2:')
    dist = RVGs.Gamma(a=10, scale=1, loc=2)
    print('  mean, st dev: ', dist.get_mean_st_dev())
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_mm_results = RVGs.Gamma.fit_mm(
        mean=np.average(data), st_dev=np.std(data), fixed_location=2)
    dict_ml_results = RVGs.Gamma.fit_ml(
        data=data, fixed_location=2)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_gamma_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_gamma_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_gamma_poisson():

    print("\nTesting Gamma Poisson with a=2, gamma_scale=4, loc=2")
    dist = RVGs.GammaPoisson(a=2, gamma_scale=4, loc=2)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_mm_results = RVGs.GammaPoisson.fit_mm(
        mean=np.average(data), st_dev=np.std(data), fixed_location=2)
    dict_ml_results = RVGs.GammaPoisson.fit_ml(
        data=data, fixed_location=2)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_gamma_poisson_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_gamma_poisson_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_geometric():
    print("\nTesting Geometric with p=0.3, loc=1")
    dist = RVGs.Geometric(p=0.3, loc=1)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_mm_results = RVGs.Geometric.fit_mm(
        mean=np.average(data), fixed_location=1)
    dict_ml_results = RVGs.Geometric.fit_ml(
        data=data, fixed_location=1)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_geometric_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_geometric_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_johnson_sb():
    print("\nTesting Johnson Sb with a=10, b=5, loc=10, scale=100")
    dist = RVGs.JohnsonSb(a=10, b=5, loc=10, scale=100)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_ml_results = RVGs.JohnsonSb.fit_ml(
        data=data, fixed_location=10)

    print("  Fit:")
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_johnson_sb_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_johnson_su():

    print("\nTesting Johnson Su with a=2, b=3, loc=1, scale=4")
    dist = RVGs.JohnsonSu(a=2, b=3, loc=1, scale=4)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_ml_results = RVGs.JohnsonSu.fit_ml(
        data=data, fixed_location=1)

    print("  Fit:")
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_johnson_su_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_lognormal():

    print("\nTesting LogNormal with mu=0.2, sigma=0.1, loc=1")
    dist = RVGs.LogNormal(mu=0.2, sigma=0.1, loc=1)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_mm_results = RVGs.LogNormal.fit_mm(
        mean=np.average(data), st_dev=np.std(data), fixed_location=1)
    dict_ml_results = RVGs.LogNormal.fit_ml(
        data=data, fixed_location=1)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_lognormal_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_lognormal_fit(data=data, fit_results=dict_mm_results, title='Maximum Likelihood')


def test_fitting_normal():

    print("\nTesting Normal with loc=10, scale=2")
    dist = RVGs.Normal(loc=10, scale=2)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_mm_results = RVGs.Normal.fit_mm(
        mean=np.average(data), st_dev=np.std(data))
    dict_ml_results = RVGs.Normal.fit_ml(
        data=data)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_normal_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_normal_fit(data=data, fit_results=dict_mm_results, title='Maximum Likelihood')


def test_fitting_negbinomial():
    print("\nTesting NegBinomial with n=10, p=0.2, loc=1")
    dist = RVGs.NegativeBinomial(n=10, p=0.2, loc=1)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_mm_results = RVGs.NegativeBinomial.fit_mm(
        mean=np.average(data), st_dev=np.std(data), fixed_location=1)
    dict_ml_results = RVGs.NegativeBinomial.fit_ml(
        data=data, fixed_location=1)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_negbinomial_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    # Plot.plot_negbinomial_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_poisson():

    print("\nTesting Poisson with mean=100 and loc = 10")
    dist = RVGs.Poisson(mu=100, loc=10)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_mm_results = RVGs.Poisson.fit_mm(mean=np.average(data), fixed_location=10)
    dict_ml_results = RVGs.Poisson.fit_ml(data=data, fixed_location=10)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_poisson_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_poisson_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_triangular():

    print("\nTesting triangular with c=0.2, loc=6, scale=7")
    dist = RVGs.Triangular(c=0.2, loc=6, scale=7)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_ml_results = RVGs.Triangular.fit_ml(data=data, fixed_location=6)

    print("  Fit:")
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_triangular_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_uniform():

    print("\nTesting triangular with scale=10, loc=2")
    dist = RVGs.Uniform(scale=10, loc=2)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_mm_results = RVGs.Uniform.fit_mm(mean=np.average(data), st_dev=np.std(data))
    dict_ml_results = RVGs.Uniform.fit_ml(data=data)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_uniform_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_uniform_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_uniform_discrete():

    print("\nTesting uniform discrete with l=10, u=18")
    dist = RVGs.UniformDiscrete(l=10, u=18)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_mm_results = RVGs.UniformDiscrete.fit_mm(mean=np.average(data), st_dev=np.std(data))
    dict_ml_results = RVGs.UniformDiscrete.fit_ml(data=data)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_uniform_discrete_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_uniform_discrete_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')


def test_fitting_weibull():

    print("\nTesting Weibull with a=5, scale=2, loc=1")
    dist = RVGs.Weibull(a=5, scale=2, loc=1)
    print('  percentile interval: ', dist.get_percentile_interval(alpha=0.05))

    data = np.array(get_samples(dist, np.random))
    dict_mm_results = RVGs.Weibull.fit_mm(
        mean=np.average(data), st_dev=np.std(data), fixed_location=1)
    dict_ml_results = RVGs.Weibull.fit_ml(
        data=data, fixed_location=1)

    print("  Fit:")
    print("    MM:", dict_mm_results)
    print("    ML:", dict_ml_results)

    # plot the fitted distributions
    Plot.plot_weibull_fit(data=data, fit_results=dict_mm_results, title='Method of Moment')
    Plot.plot_weibull_fit(data=data, fit_results=dict_ml_results, title='Maximum Likelihood')

