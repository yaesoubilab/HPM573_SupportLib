import numpy as np

import SimPy.EconEval as EconEval

np.random.seed(573)

cost_base = np.random.normal(loc=10000, scale=100, size=1000)
effect_base = np.random.normal(loc=2, scale=.1, size=1000)
cost_intervention = np.random.normal(loc=20000, scale=200, size=1000)
effect_intervention = np.random.normal(loc=1, scale=.2, size=1000)

print('')

# ICER calculation assuming paired observations
ICER_paired = EconEval.ICER_Paired('Testing paired ICER',
                                   cost_intervention, effect_intervention, cost_base, effect_base,
                                   health_measure='d')
print('Paired ICER:\n\tICER: {} \n\tCI (boostrap): {} \n\tCI (Bayesian): {} \n\tPI: '.format(
      ICER_paired.get_ICER(),
      ICER_paired.get_CI(0.05, 1000),
      ICER_paired.get_CI(0.05, 1000, method='Bayesian'),
      ICER_paired.get_PI(0.05)))

# ICER calculation assuming independent observations
ICER_indp = EconEval.ICER_Indp('Testing independent ICER',
                               cost_intervention, effect_intervention, cost_base, effect_base,
                               health_measure='d')
print('Independent ICER (confidence and prediction interval): \n\t{}\n\t{}\n\t{}'.format(
      ICER_indp.get_ICER(),
      ICER_indp.get_CI(0.05, 1000),
      ICER_indp.get_PI(0.05)))

# try NMB
NMB_paired = EconEval.INMB_Paired("Testing paired NMB",
                                  cost_intervention, effect_intervention, cost_base, effect_base,
                                  health_measure='d')
print('Paired NMB (confidence and prediction interval): \n\t{}\n\t{}\n\t{}'.format(
      NMB_paired.get_INMB(wtp=10000),
      NMB_paired.get_CI(wtp=10000, alpha=.05),
      NMB_paired.get_PI(wtp=10000, alpha=.05)))

NMB_indp = EconEval.INMB_Indp("Testing independent NMB",
                              cost_intervention, effect_intervention, cost_base, effect_base,
                              health_measure='d')
print('Independent NMB (confidence and prediction interval): \n\t{}\n\t{}\n\t{}'.format(
      NMB_indp.get_INMB(wtp=10000),
      NMB_indp.get_CI(wtp=10000, alpha=.05),
      NMB_indp.get_PI(wtp=10000, alpha=.05)))

print('')
