from UQpy.run_model.RunModel import RunModel
from UQpy.run_model.model_execution.ThirdPartyModel import ThirdPartyModel
import matplotlib.pyplot as plt
import time
import numpy as np



# Call to RunModel - Here we run the model while instantiating the RunModel object. 
m11 = ThirdPartyModel(model_script='model_script.py', input_template = 'NASA_input.json',   
                      var_names = ['x0','x1','x2','x3','x4','x5','x6','x7','seed'])
#m11.run(samples=x_mcs.samples,)


NASA_model = RunModel(cores_per_task=1, model=m11)
sample_points = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 30]).reshape(1,9)
NASA_model.run(samples=sample_points, )