"""
This module is responsible for processing the data.  Each function in this module will take a list of reviews,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of reviews (where each review is a list of data values) as a parameter.
- Process the list of reviews appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:



- Retrieve the reviews for a hotel where the hotel name is specified by the user.
- Retrieve the reviews for the dates specified by the user.
- Retrieve all the reviews grouped by the reviewer’s nationality.
- Retrieve a summary of all the reviews. This should include the following information for each date in ascending order:
    - the total number of negative reviews on that date
    - the total number of positive reviews on that date
    - the average rating on that date
"""

import pandas as pd
#- Retrieve the total number of reviews that have been loaded.

def Count_All_Reviews(df):
    return str(df['Review_Date'].count())

def HotelReview_ByHotelName(df, name):
    HotelReviews=df[['Hotel_Name','Positive_Review','Negative_Review']]
    Get_review = HotelReviews[HotelReviews["Hotel_Name"]==name]
    return Get_review

def HotelReviewsByDate(df,date):
    GetReviewByDate=df[["Review_Date",'Hotel_Name','Positive_Review','Negative_Review']]
    getReview=GetReviewByDate[GetReviewByDate["Review_Date"]==date]
    return getReview

def grpbyReviewsNationatlity(df):
    reviews_by_nationality = df.groupby("Reviewer_Nationality").agg(list).head()
    return reviews_by_nationality

def summarizeData(df):
    
    # Convert the Review_Date column to datetime format
    df['Review_Date'] = pd.to_datetime(df['Review_Date'])
    # Group the DataFrame by Review_Date and count the number of positive and negative reviews
    summary = df.groupby('Review_Date').agg({'Negative_Review': 'count', 'Positive_Review': 'count', 'Reviewer_Score': 'mean'})
    # Rename the columns
    summary = summary.rename(columns={'Negative_Review': 'Total Negative Reviews', 'Positive_Review': 'Total Positive Reviews', 'Reviewer_Score': 'Average Rating'})
    # Sort the summary DataFrame by Review_Date in ascending order
    summary = summary.sort_values(by='Review_Date', ascending=True)
    return summary
