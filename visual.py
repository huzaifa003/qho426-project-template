"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display a pie chart showing the total number of positive and negative reviews for a specified hotel.
- Display the number of reviews per the nationality of a reviewer. This should by ordered by the number of reviews, highest first, and should show the top 15 + “Other” nationalities.
- Display a suitable animated visualisation to show how the number of positive reviews, negative reviews and the average rating change over time.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here


import matplotlib.pyplot as plt
import pandas as pd

def hotelReviewInPieChart(df, name):
    Hotel_Review = df[df["Hotel_Name"]==name]
    totalNegRev = Hotel_Review[Hotel_Review['Negative_Review']!="No Negative"]['Negative_Review'].count()
    totalPosRev = Hotel_Review[Hotel_Review['Positive_Review']!="No Positive"]['Positive_Review'].count()
    labels = 'Positive Reviews', 'Negative Reviews'
    sizes = [totalPosRev, totalNegRev]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels,autopct='%1.1f%%')
    ax.set_title('Positive and Negative Reviews for '+name)
    plt.show()

