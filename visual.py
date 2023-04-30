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
import matplotlib.animation as animation


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


def NationalityGraph(df):

    # Group the data by reviewer nationality and count the number of reviews per nationality
    nationality_counts = df.groupby('Reviewer_Nationality').size().reset_index(name='Num_Reviews')
    # Sort the data by the number of reviews in descending order
    nationality_counts = nationality_counts.sort_values('Num_Reviews', ascending=False)
    # Get the top 15 nationalities and combine the rest as "Other"
    top_nationalities = list(nationality_counts.head(15)['Reviewer_Nationality'].values)
    other_nationality_count = nationality_counts[~nationality_counts['Reviewer_Nationality'].isin(top_nationalities)]['Num_Reviews'].sum()
    nationality_counts = nationality_counts[nationality_counts['Reviewer_Nationality'].isin(top_nationalities)]
    nationality_counts = pd.concat([nationality_counts, pd.DataFrame({'Reviewer_Nationality': ['Other'], 'Num_Reviews': [other_nationality_count]})])
    # Plot the data as a bar chart
    plt.bar(nationality_counts['Reviewer_Nationality'], nationality_counts['Num_Reviews'])
    plt.xticks(rotation=90)
    plt.xlabel('Nationality of Reviewer')
    plt.ylabel('Number of Reviews')
    plt.show()


def anim(df):
    df['Review_Date'] = pd.to_datetime(df['Review_Date'])
    fig, ax = plt.subplots(figsize=(8, 6))

    def animate(i):
        start_date = pd.Timestamp('2015-07-01') + pd.DateOffset(months=i)
        end_date = start_date + pd.DateOffset(months=1)
        data = df[(df['Review_Date'] >= start_date) & (df['Review_Date'] < end_date)]
        totalNegRev = data[data['Negative_Review']!="No Negative"]['Negative_Review'].count()
        totalPosRev = data[data['Positive_Review']!="No Positive"]['Positive_Review'].count()
        avg_rating = data['Reviewer_Score'].mean()
        ax.clear()
        ax.set_title(f"Hotel Reviews from {start_date.date()} to {end_date.date()}")
        ax.set_xlabel("Review Type")
        ax.set_ylabel("Number of Reviews / Average Rating")
        ax.bar(["Positive", "Negative"], [totalPosRev, totalNegRev], color=["green", "red"])
        ax.set_ylim(0, data.shape[0])
        ax.legend(labels=['Positive Review', 'Negative Review'], loc='best')
        ax2 = ax.twinx()
        # ax2.plot(["Average Rating"], [avg_rating], marker="o", markersize=8, color="blue")
        ax2.set_ylim(df['Reviewer_Score'].min()-0.5, df['Reviewer_Score'].max()+0.5)
        ax2.set_ylabel("Average Rating")


    def callAnimation():

        anim = animation.FuncAnimation(fig, animate, frames=24)
        anim.save('hotel_reviews_animation.mp4', fps=2, extra_args=['-vcodec', 'libx264'])
        plt.show()
        
    callAnimation()