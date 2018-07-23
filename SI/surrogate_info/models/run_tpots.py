''' Run TPOT 16 times to get a distribution of results '''

import copy
import dill as pickle
from tpot import TPOTRegressor
from gaspy.utils import vasp_settings_to_str
from gaspy_regress.regressor import GASpyRegressor


# Regression settings
VASP_SETTINGS = vasp_settings_to_str({'gga': 'RP',
                                      'pp_version': '5.4',
                                      'encut': 350})
model_name = 'TPOT'
features = ['coordatoms_chemfp0', 'neighbors_chemfp0']
responses = ['energy']
blocks = ['adsorbate']
fit_blocks = [('CO',), ('H',)]
n_models = 16

tpot = TPOTRegressor(generations=1,
                     population_size=16,
                     offspring_size=16,
                     verbosity=2,
                     #random_state=42,
                     scoring='neg_median_absolute_error',
                     n_jobs=16)


# Perform the regression
for n in range(n_models):
    regressor = copy.deepcopy(tpot)
    model = GASpyRegressor(features=features, responses=responses,
                           blocks=blocks, vasp_settings=VASP_SETTINGS,
                           dim_red='pca', train_size=0.9)
    model.fit_tpot(regressor, model_name=model_name, blocks=fit_blocks)
    with open('model_%i.pkl' % n, 'wb') as f:
        pickle.dump(model, f)
