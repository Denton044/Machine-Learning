NBA Machine-Learning: contains the data and code used to train and fit various ML algorithms in order to predict NBA All-League Teams.

Machine-Learning/NBA Machine Learning/Code:
  1. NBA Season Totals.ipynb uses beautiful soup module in python to scrape data from basketball reference.
     Contructs dataframe of total counting stats of all players played in the NBA from 1990 to 2016 and saves dataframe to csv.
  2. NBA All-Team Awards.ipynb uses beautiful soup module in python to scrape data from basketball reference. 
     Constructs dataframe of winners of NBA All-League Teams from 1990 to 2016 and saves dataframe to csv.
  3. Combine Winners & Totals into 1 dataframe.ipynb uses pandas sql module in python to join above dataframes into 1 and saves to csv.
  4. Model fitting tries to fit the winners and losers of an ALL-Team Award. Uses logistic regression. Future work will be to separate by 4 clusters. Clusters will be losers, 1st team, 2nd team and 3rd team. Perhaps a cluster model, random forest, svm model will be able to handle this request.
