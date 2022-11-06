import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display_html 

def start(path_player,path_win_org):
    #player_info = pd.read_csv("ungraded/--playerinfo.csv")
    #win_by_org = pd.read_csv("ungraded/winnings_by_org_allYears.csv")
    player_info = pd.read_csv(path_player)
    win_by_org = pd.read_csv(path_win_org)
    process_player(player_info)
    process_org(win_by_org)

def process_player(player_info):
    clean = player_info[["player_name","nationality","player_status"]]
    player_info[["player_name","nationality","team","player_status"]]
    active = clean[clean["player_status"]=="Active"]
    retired = clean[clean["player_status"]=="Retired"]
    
    print("Display of Players and their status")
    active_style = active.style.set_table_attributes("style='display:inline; margin-right:20px;'").set_caption("Active Player")
    retired_style = retired.style.set_table_attributes("style='display:inline'").set_caption("Retired Player")
    display_html(active_style._repr_html_() + retired_style._repr_html_(), raw=True)

def process_org(win_by_org):
    win2019 = win_by_org[win_by_org["year"]==2019]
    win2020 = win_by_org[win_by_org["year"]==2020]
    win2021 = win_by_org[win_by_org["year"]==2021]
    win2022 = win_by_org[win_by_org["year"]==2022]
    yearsum=[0,0,0,0]
    for i in range(0,4):
        if i==0:
            for earnings in win2019["earnings"]:
                yearsum[i]+=earnings
        if i==1:
            for earnings in win2020["earnings"]:
                yearsum[i]+=earnings
        if i==2:
            for earnings in win2021["earnings"]:
                yearsum[i]+=earnings
        if i==3:
            for earnings in win2022["earnings"]:
                yearsum[i]+=earnings
    year_earn_compare = {"year":[2019,2020,2021,2022],"total":yearsum}
    
    print("Display of top 20 earnings in 2019")
    win2019_01 = win2019[win2019["earnings_rank"]<21]
    win2019_f20 = sns.barplot(y=win2019_01["earnings"],x=win2019_01["team"])
    win2019_f20.set(title="Earning of top 20 teams in 2019")
    plt.gcf().set_size_inches(40, 20)
    plt.show()
    
    print("Display of top 20 earnings in 2020")
    win2020_01 = win2020[win2020["earnings_rank"]<21]
    win2020_f20 = sns.barplot(y=win2020_01["earnings"],x=win2020_01["team"])
    win2020_f20.set(title="Earning of top 20 teams in 2020")
    plt.gcf().set_size_inches(40, 20)
    plt.show()
    
    print("Display of top 20 earnings in 2021")
    win2021_01 = win2021[win2021["earnings_rank"]<21]
    win2021_f20 = sns.barplot(y=win2021_01["earnings"],x=win2021_01["team"])
    win2021_f20.set(title="Earning of top 20 teams in 2021")
    plt.gcf().set_size_inches(40, 20)
    plt.show()
    
    print("Display of top 20 earnings in 2022")
    win2022_01 = win2022[win2022["earnings_rank"]<21]
    win2022_f20 = sns.barplot(y=win2022_01["earnings"],x=win2022_01["team"])
    win2022_f20.set(title="Earning of top 20 teams in 2022")
    plt.gcf().set_size_inches(40, 20)
    plt.show()
    
    print("Display of total year earning compare")
    year_comp = sns.barplot(x=year_earn_compare["year"],y=year_earn_compare["total"])
    year_comp.set(title="Earning of all teams each year",ylabel="earnings in 10^6")
    year_comp.bar_label(year_comp.containers[0])
    plt.gcf().set_size_inches(20, 5)
    plt.show()
    
    print("Display of all teams' ranking by year")
    win2019_style = win2019.style.set_table_attributes("style='display:inline; margin-right:20px;'").set_caption("Earning Raank 2019")
    win2020_style = win2020.style.set_table_attributes("style='display:inline; margin-right:20px;'").set_caption("Earning Raank 2020")
    win2021_style = win2021.style.set_table_attributes("style='display:inline; margin-right:20px;'").set_caption("Earning Raank 2021")
    win2022_style = win2022.style.set_table_attributes("style='display:inline'").set_caption("win2022")
    display_html(win2019_style._repr_html_() + win2020_style._repr_html_()+ win2021_style._repr_html_()+ win2022_style._repr_html_(), raw=True)    
    
    