# Recommendation system stuff
import csv
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from .models import Product
from scipy import sparse


# Export products data to csv
def export_ru(products):
    with open('ru_products.csv', 'w') as csv_file:     
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Id',  'Price','Description'])
        
        for product in products.translated('ru').values_list('translations__name','id', 'new_price', 'translations__description'):
            writer.writerow(product)

def export_en(products):
    with open('en_products.csv', 'w') as csv_file:     
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Id',  'Price','Description'])
        for product in products.translated('en').values_list('translations__name','id', 'new_price', 'translations__description'):
            writer.writerow(product)

def export_tk(products):
    with open('tk_products.csv', 'w') as csv_file:     
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Id',  'Price','Description'])
        for product in products.translated('tk').values_list('translations__name','id', 'new_price', 'translations__description'):
            writer.writerow(product)

def export():
    products = Product.objects.all()    
    export_en(products)
    export_ru(products)
    export_tk(products)

    
   
        
        


def give_rec(title, sig, indices, df1):
    # Get the index corresponding to original title
    #print("In Give")
    # print("TItle", title)
    # print("sig", sig)
    # print("indices", indices)
    # print("df1", df1)
    try:
        idx=indices[title]
    except:
        title=1
    idx = indices[title]
    #print("NOt in idx")
    # Get the pairwise similarity scores
    sig_scores=list(enumerate(sig[idx]))
    #print("NOt in sig scores")
    # Sort the products
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    #print("NOt in sig scores 2")
    # Scores of the 10 most similar products
    sig_scores = sig_scores[1:11]
    #print("NOt in sig scores 3")
    # Product indexes
    product_indices = [i[0] for i in sig_scores]
    #print("NOt in product indices", product_indices)
    # Top 10 most similar products
    return df1['Id'].iloc[product_indices]


def get_reccommendation(id, lang_code):
    file_name = f'{lang_code}_products.csv'
    df1 = pd.read_csv(file_name)
    #print("We are in recommendations", id)
    #print("We are in file name", file_name)
    tfv = TfidfVectorizer(min_df=3, max_features=None,
                strip_accents='unicode', analyzer='word', token_pattern=r'\w{1,}', 
                ngram_range=(1, 3), stop_words='english')
    #print("Problem not in tfv")
    tfv_matrix = tfv.fit_transform(df1['Description'])
    #print("Problem not in first")
    other_matrix = tfv.fit_transform(df1['Name'])
    #print("Problem not in second")
    combined_matrix=sparse.hstack((tfv_matrix, other_matrix))
    #print("Problem not in matrixes")
    sig = sigmoid_kernel(combined_matrix, combined_matrix)
    #print("Problem not in sig")
    indices = pd.Series(df1.index, index=df1['Id'])
    #print("Problem not in indices")
    res = give_rec(title=id, sig=sig, indices=indices, df1=df1)
    #print("Problem not in res", res)
    return res






# def recommend_movies_based_on_plot(name, mapping, similarity_matrix, df1):
#     product_index = mapping[name]
#     #get similarity values with other products
#     #similarity_score is the list of index and similarity matrix
#     similarity_score = list(enumerate(similarity_matrix[product_index]))
#     #sort in descending order the similarity score of product inputted with all the other products
#     similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
#     # Get the scores of the 15 most similar movies. Ignore the first movie.
#     similarity_score = similarity_score[1:15]
#     #return product names using the mapping series
#     product_indices = [i[0] for i in similarity_score]
#     return (df1['Name'].iloc[product_indices])

# def get_reccommendation(request):
#     # export()
#     with open('products.csv', 'r') as csv_file:
#         df1 = pd.read_csv(csv_file)
#         # TfidfVectirizer converts text to (numerical) 0s and 1s
#         # Because computers understand only then
#         tfidf = TfidfVectorizer(min_df=3, max_features=None,
#                     strip_accents='unicode', analyzer='word', token_pattern=r'\w{1,}', 
#                     ngram_range=(1, 3), stop_words='english')
#         df1['Description'] = df1['Description'].fillna('')

#         description_matrix = tfidf.fit_transform(df1['Description'])
#         similarity_matrix = linear_kernel(description_matrix,description_matrix)
#         mapping = pd.Series(df1.index, index = df1['Name'])
#         print("Mapping", mapping)
#         res = recommend_movies_based_on_plot('Staff history.', mapping, similarity_matrix, df1)
#         print(res)
#         # res = give_rec(title='New products', sig=sig, indices=indices, df1=df1)
#         return HttpResponse("Ok")
      