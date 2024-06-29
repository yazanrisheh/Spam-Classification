import sys
sys.path.append(r"C:\Users\Asus\Documents\Spam ML")

import pickle
from data_handling.data_transformation import cv, model

pickle.dump(model, open(r"C:\Users\Asus\Documents\Spam ML\pickle_dirspam_model.pkl", "wb"))
pickle.dump(cv, open(r"C:\Users\Asus\Documents\Spam ML\pickle_dircount_vectorizer.pkl", "wb"))
