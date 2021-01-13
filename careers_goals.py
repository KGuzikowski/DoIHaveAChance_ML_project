import pandas as pd
df = pd.read_csv("DoIHaveAChance_ML_project/Speed_Dating_Data.csv",encoding = "ISO-8859-1")
def fooCareer(col):
    selected_df = df[col]
    career_c = {"lawyer":1.,
               "law":1.,
               "Economics":7.,
               "tech professional":5.
               }
    
    for x, row in selected_df.iterrows():
            career = df.at[x,col[0]]
            if career in career_c:
                df.at[x, col[1]] = career_c[career]
def fooGoal(col):
    selected_df = df[col]
    goal_c = {1:1,
              2:1,
              3:1,
              4:0,
              5:1,
              6:1}
    
    for x, row in selected_df.iteritems():
        goal = df.at[x, col]
        if goal in goal_c:
            df.at[x, col] = goal_c[goal]

fooCareer(["career","career_c"])
fooGoal("goal")
df.to_csv('filtered_data.csv', index=False)
