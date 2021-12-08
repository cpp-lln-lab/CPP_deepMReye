# Import modules and add library to path
import os
import sys

import pandas as pd
import numpy as np
import pickle

# Change to os.environ["CUDA_VISIBLE_DEVICES"] = "0" if you have access to a GPU
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# DeepMReye imports
from deepmreye import architecture, train, analyse, preprocess
from deepmreye.util import util, data_generator, model_opts


# Define paths to functional data
experiment_folder = (
    "../inputs/rest_blnd_can_fmriprep/"  # Replace this path to your downloaded files
)

model_weights = "/inputs/models/dataset1_guided_fixations.h5"


(eyemask_small, eyemask_big, dme_template, mask, x_edges, y_edges, z_edges) = preprocess.get_masks()

# Loop across participants and extract eye mask
for participant in participants:
    if participant.startswith('s'):
        print('Running participant {}'.format(participant))
        participant_folder = functional_data + participant
        for run in os.listdir(participant_folder):
            if run.startswith('run'):
                fp_func = participant_folder + os.path.sep + run # Filepath to functional
                preprocess.run_participant(fp_func, dme_template, eyemask_big, eyemask_small, x_edges, y_edges, z_edges)