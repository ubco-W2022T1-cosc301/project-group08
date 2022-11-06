# Method Chaining
import pandas as pd
import seaborn as sns
import numpy as np
import os
import matplotlib.pyplot as plt

def load_and_process(url_or_path_to_csv_file):
    df=pd.read_csv(url_or_path_to_csv_file)
    return df

def load_Hot_Game(df):
    # All hot game
    df_hot=df[["Team","prize money","Apex Legends","CS:GO","Dota2","Fortnite","League of Legends","Valorant"]]
    return df_hot

def load_Apex(df_hot):
    # Apex Legends
    df_Apex=df_hot[["Team","prize money","Apex Legends"]]
    df_Apex=df_Apex[df_Apex["Apex Legends"]>=0]
    return df_Apex

def load_Valorant(df_hot):
    # Valorant
    df_Valorant=df_hot[["Team","prize money","Valorant"]]
    df_Valorant=df_Valorant[df_Valorant["Valorant"]>=0]
    return df_Valorant

def load_CS(df_hot):
    # CS:GO
    df_CS=df_hot[["Team","prize money","CS:GO"]]
    df_CS=df_CS[df_CS["CS:GO"]>=0]
    return df_CS

def load_Dota2(df_hot):
    # Dota2
    df_Dota2=df_hot[["Team","prize money","Dota2"]]
    df_Dota2=df_Dota2[df_Dota2["Dota2"]>=0]
    return df_Dota2

def load_Fortnite(df_hot):
    # Fortnite
    df_Fortnite=df_hot[["Team","prize money","Fortnite"]]
    df_Fortnite=df_Fortnite[df_Fortnite["Fortnite"]>=0]
    return df_Fortnite

def load_LOL(df_hot):
    # League of Legends
    df_LOL=df_hot[["Team","prize money","League of Legends"]]
    df_LOL=df_LOL[df_LOL["League of Legends"]>=0]
    return df_LOL