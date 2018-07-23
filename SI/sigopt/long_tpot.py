''' Let TPOT run for a long time '''

import dill as pickle
from tpot import TPOTRegressor
from gaspy.utils import vasp_settings_to_str
from gaspy_regress.regressor import GASpyRegressor


# Settings
fit_blocks = [('CO',)]
train_size = 1
dev_size = None
dim_red = 'pca'
tpot_verbosity = 2
tpot_generations = 25
tpot_population = 64
tpot_offspring = 64
n_jobs = 32
random_state = None
VASP_SETTINGS = vasp_settings_to_str({'gga': 'RP',
                                      'pp_version': '5.4',
                                      'encut': 350})
model_name = 'TPOT'
features = ['coordatoms_chemfp0', 'neighbors_chemfp0']
responses = ['energy']
blocks = ['adsorbate']

# Fit
tpot = TPOTRegressor(generations=tpot_generations,
                     population_size=tpot_population,
                     offspring_size=tpot_offspring,
                     verbosity=tpot_verbosity,
                     random_state=random_state,
                     n_jobs=n_jobs)
model = GASpyRegressor(features=features, responses=responses,
                       blocks=blocks, vasp_settings=VASP_SETTINGS,
                       train_size=train_size, dev_size=dev_size,
                       dim_red=dim_red)
model.fit_tpot(tpot, model_name=model_name, blocks=fit_blocks)

# Save it
with open('model.pkl', 'w') as file_handle:
    pickle.dump(model, file_handle)
