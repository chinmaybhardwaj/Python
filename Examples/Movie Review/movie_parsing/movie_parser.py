import os
from movie_handler import get_movies
from movie_scrapper import get_year

def get_url(df):
    if df is not None:
        
        for index, row in df.iterrows():
            name = row['year']
            url = row['link']
            print('Name:', name, 'URL:', url)
            # Get HTML page for given year URL
            get_year(name, url)
        #Save dataframe
#        save_to_csv(df)
    else:
        print('Error in parsing DataFrame')


#
# Create years.csv with cleaned data
#
def save_to_csv(df):
    outputdir = './dataset'
    if not os.path.exists(outputdir):
        os.mkdir(outputdir)
        
    # Write DataFrame to years.csv
    df.to_csv('./dataset/years.csv', sep=',', index=False, encoding='utf-8')
    print('years.csv created!')
    
    
    
#
# Load dataframe from csv
#
df = get_movies()

get_url(df)

