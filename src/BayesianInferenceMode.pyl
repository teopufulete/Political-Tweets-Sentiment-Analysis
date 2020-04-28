import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import MatplotlibDeprecationWarning
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=MatplotlibDeprecationWarning)

candidates = ['Donald Trump', 'Elizabeth Warren', 'Bernie Sanders', 'Joe Biden', 'Tulsi Gabbard']
c = np.array([18315, 3794, 11369, 12205, 4259])

# hyperparameters (initially all equal)
alphas = np.array([1, 1, 1, 1, 1])

alpha_list = [np.array([0.1, 0.1, 0.1, 0.1, 0.1]), np.array([1, 1, 1, 1 ,1]),
                    np.array([5, 5, 5, 5, 5]), np.array([3, 1, 2, 2, 1]),
                    np.array([2, 1, 1, 1, 1])]



display_probs = dict(zip(candidates, (alphas + c) / (c.sum() + alphas.sum())))
print(display_probs)

values = []
for alpha_new in alpha_list:
    values.append((alpha_new + c) / (c.sum() + alpha_new.sum()))

value_df = pd.DataFrame(values, columns = candidates)
value_df['alphas'] = [str(x) for x in alpha_list]
print(value_df)

if __name__ == '__main__':      # needed or it won't run on windows
    import pymc3 as pm

    with pm.Model() as model:
        # Parameters of the Multinomial are from a Dirichlet
        parameters = pm.Dirichlet('parameters', a=alphas, shape=5)
        # Observed data is from a Multinomial distribution
        observed_data = pm.Multinomial(
            'observed_data', n=49942, p=parameters, shape=5, observed=c)

    with model:
        # Sample from the posterior
        trace = pm.sample(draws=10000, chains=4, tune=5000,
                          discard_tuned_samples=True)

    summary = pm.summary(trace)
    summary.index = candidates
    print(summary)

    ax = pm.plot_posterior(trace, varnames=['parameters'], kind='hist')

    plt.rcParams['font.size'] = 22
    for i, a in enumerate(candidates):
        ax[i].set_title(a);

    with model:
        # Find the maximum a posteriori estimate
        map_ = pm.find_MAP()

    display_probs = dict(zip(candidates, map_['parameters']))
    print(display_probs)

    with model:
        samples = pm.sample_ppc(trace, samples=1000)

    dict(zip(candidates, samples['observed_data'].mean(axis=0)))
