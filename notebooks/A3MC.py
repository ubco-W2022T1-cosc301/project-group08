# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns#Understanding my variables
import plotly.express as px
import seaborn as sns


def player_infor(path) :
    df = pd.read_csv(path).drop(['earnings_rank'], axis =1 ).rename(columns={'earnings':'award money'})
    sns.displot(y=df['nationality'] ,height = 15, aspect =0.3 ).set(title='Number of Apex Legend players by Nationality')


def org_infor(path) :
    df = pd.read_csv(path).drop(['earnings_rank'],axis = 1).rename(columns={'earnings':'award money'})
    df
    


