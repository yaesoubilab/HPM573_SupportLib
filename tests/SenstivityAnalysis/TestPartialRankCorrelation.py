from numpy.random import rand

from SimPy.SensitivityAnalysis import SensitivityAnalysis

# prepare data
param1 = rand(100) * 20
param2 = rand(100) * -1
output = param1 + 2*param2 + rand(100) * 10

dic_par_values = {'Par1': param1, 'Par2': param2}

sa = SensitivityAnalysis(dic_parameter_values=dic_par_values, output_values=output)

sa.print_corr(corr='r')
sa.print_corr(corr='rho')
sa.print_corr(corr='p')
sa.print_corr(corr='pr')
sa.export_to_csv(corrs=['r', 'rho', 'p', 'pr'], decimal=4)
