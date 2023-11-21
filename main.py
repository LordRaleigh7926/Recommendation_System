#Imports
from sklearn.neighbors import NearestNeighbors
import pandas as pd
from scipy.sparse import csr_matrix

# Preprocessing
Movie_df = pd.read_csv("movies.csv")
Rating_df = pd.read_csv("ratings.csv")
df = pd.merge(Movie_df, Rating_df,on='movieId')
df_2_=df.dropna(axis=0,subset=["title"])
df_2_ = df_2_.groupby(by = ['title'])['rating'].count().reset_index().rename(columns={"rating":"TotalRating"})
df_3_ = pd.merge(df, df_2_, on='title',how='left')
df_3_ = df_3_.drop(['genres','timestamp'], axis=1)
pd.set_option("display.float_format",lambda x: "%.3f" % x)
threshold = 50
df_3_ = df_3_.query('TotalRating >= @threshold')
pt = df_3_.groupby([ 'title','userId'])['rating'].sum().unstack().fillna(0)
FinalData = csr_matrix(pt.values)

# Making the Model
KNN = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
KNN.fit(FinalData)


# Implementation 
def get_Rec(movie_index): # Gets the list of indexes of recommended movies
    print(movie_index)
    _, indices = KNN.kneighbors(pt.iloc[movie_index,:].values.reshape(1, -1), n_neighbors = 5)
    return indices

row_names = pt.index

def passingMovieName(MovieName): # Displaying the recommended movies
    for i,k in enumerate(row_names):

        k = k.lower().replace(" ", "")

        comma = k.find(",")
        index_of_bracket = k.find("(")


        if comma != -1:
            c = k[comma+1:index_of_bracket]
            d = k[:comma]
            k = c+d
        else:
            if MovieName.find("(") == -1:
                k = k[:index_of_bracket]
            

        if k == MovieName:
            movie_index = i
            break


    rec = get_Rec(movie_index)


    for i,k in enumerate(rec[0]):

        name = row_names[k]
        comma = name.find(",")

        if comma != -1:
            index_of_bracket = name.find("(")
            c = name[comma+2:index_of_bracket]
            d = name[:comma]
            name = c+d+" "+name[index_of_bracket:]

        if  i == 0:
            print(f"Recommendations for {name}:\n")
        else:
            print(f"{i}. {name}")



if __name__ == "__main__":
    
    movie_name = input("Enter Name of Movie \n P.S. - It should be present in training data")
    formatted_movie_name = movie_name.lower().replace(" ", "")
    print(formatted_movie_name)
    passingMovieName(formatted_movie_name)
