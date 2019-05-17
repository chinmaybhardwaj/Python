import os
from years_handler import get_years


def clean_df(df):
    if df is not None:
        #
        # Remove unwanted rows
        # Removing rows : (view, talk, edit, 2020s)
        #
        df = df[4:]
        
        #
        # Remove rows that contain string 's'
        #
        df = df[~df['year'].str.contains('s')]
        
        # Sort rows by year
        df = df.sort_values(by ='year')
        
        #Save dataframe
        save_to_csv(df)
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
df = get_years()

clean_df(df)

