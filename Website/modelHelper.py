import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, budget, popularity, revenue, runtime, vote_count, genre, production_company, production_country, spoken_language, release_year, release_month, release_is_weekend):
        inps = {'budget': 0,
                    'popularity': 0,
                    'revenue': 0,
                    'runtime': 0,
                    'vote_count': 0,
                    'release_year': 0,
                    'release_month': 0,
                    'release_is_weekend': 0,
                    'genre_Action': 0,
                    'genre_Adventure': 0,
                    'genre_Animation': 0,
                    'genre_Comedy': 0,
                    'genre_Crime': 0,
                    'genre_Documentary': 0,
                    'genre_Drama': 0,
                    'genre_Fantasy': 0,
                    'genre_Horror': 0,
                    'genre_Other': 0,
                    'genre_Romance': 0,
                    'production_company_BBC Films': 0,
                    'production_company_Columbia Pictures': 0,
                    'production_company_Lions Gate Films': 0,
                    'production_company_Metro-Goldwyn-Mayer (MGM)': 0,
                    'production_company_Mosfilm': 0,
                    'production_company_New Line Cinema': 0,
                    'production_company_Other': 0,
                    'production_company_Paramount Pictures': 0,
                    'production_company_RKO Radio Pictures': 0,
                    'production_company_Twentieth Century Fox Film Corporation': 0,
                    'production_company_United Artists': 0,
                    'production_company_Universal Pictures': 0,
                    'production_company_Walt Disney Pictures': 0,
                    'production_company_Warner Bros.': 0,
                    'production_country_Canada': 0,
                    'production_country_France': 0,
                    'production_country_Germany': 0,
                    'production_country_Italy': 0,
                    'production_country_Japan': 0,
                    'production_country_Other': 0,
                    'production_country_United Kingdom': 0,
                    'production_country_United States of America': 0,
                    'spoken_language_Chinese': 0,
                    'spoken_language_Deutsch': 0,
                    'spoken_language_English': 0,
                    'spoken_language_Español': 0,
                    'spoken_language_Français': 0,
                    'spoken_language_Italiano': 0,
                    'spoken_language_Japanese': 0,
                    'spoken_language_Other': 0,
                    'spoken_language_Russian': 0}
        #Numeric 
        inps["budget"] = budget
        inps["popularity"] = popularity
        inps["revenue"] = revenue
        inps["runtime"] = runtime
        inps["vote_count"] = vote_count
        inps["release_year"] = release_year
        inps["release_is_weekend"] = release_is_weekend
        inps["release_month"] = release_month

        #Categorical
        inps[f"genre_{genre}"] = 1
        inps[f"production_company_{production_company}"] = 1
        inps[f"production_country_{production_country}"] = 1
        inps[f"spoken_language_{spoken_language}"] = 1


        inps_df=pd.DataFrame([inps])

        model = pickle.load(open('movies_goodness.pkl', 'rb'))
        
        preds = model.predict_proba(inps_df)
        rtn = {"bad_prob": preds[0][0], "good_prob": preds[0][1]}
        return rtn