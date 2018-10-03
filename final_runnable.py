import numpy as np
import scipy.sparse as sp
import pandas as pd
import os
import json
from tqdm import tqdm
from collections import Counter
from itertools import product
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import final_fever as fever
import utils
import os.path

percentage = 1


def fit_maxent_classifier(X, y):
    """Wrapper for `sklearn.linear.model.LogisticRegression`. This is also
    called a Maximum Entropy (MaxEnt) Classifier, which is more fitting
    for the multiclass case.

    Parameters
    ----------
    X : 2d np.array
        The matrix of features, one example per row.
    y : list
        The list of labels for rows in `X`.

    Returns
    -------
    sklearn.linear.model.LogisticRegression
        A trained `LogisticRegression` instance.

    """
    mod = LogisticRegression(fit_intercept=True)
    mod.fit(X, y)
    return mod


def word_overlap_phi(claim, evidence):
    """Basis for features for the words in both the premise and hypothesis.
    This tends to produce very sparse representations.

    Parameters
    ----------
    claim : a string
    evidence : a list of sentences

    Returns
    -------
    defaultdict
       Maps each word in both claim and evidence to 1.

    """
    sents = []
    for sent in evidence:
        sents.extend(utils.process_sent(sent))
    overlap = set([w1 for w1 in utils.process_text(claim) if w1 in sents])
    return Counter(overlap)



_ = fever.experiment_sandeep(
    train_reader=fever.SampledTrainReader(samp_percentage=percentage),
    phi=word_overlap_phi,
    # oracle=oracle,
    train_func=fit_maxent_classifier,
    assess_reader=fever.SampledSandeepReader(samp_percentage=percentage),
    random_state=42)

#
#
# def word_cross_product_phi(claim, evidence):
#     """Basis for cross-product features. This tends to produce pretty
#     dense representations.
#
#     Parameters
#     ----------
#     claim : a string
#     evidence : a list of sentences
#
#     Returns
#     -------
#     defaultdict
#         Maps each (w1, w2) in the cross-product of words in claim and
#         evidence to its count. This is a multi-set cross-product
#         (repetitions matter).
#
#     """
#     sents = []
#     for sent in evidence:
#         sents.extend(utils.process_sent(sent))
#     return Counter([(w1, w2) for w1, w2 in product(utils.process_text(claim), sents)])
#
#
# _ = fever.experiment_sandeep(
#     train_reader=fever.SampledTrainReader(samp_percentage=percentage),
#     phi=word_cross_product_phi,
#     # oracle=oracle,
#     train_func=fit_maxent_classifier,
#     assess_reader=fever.SampledSandeepReader(samp_percentage=percentage),
#     random_state=42)
