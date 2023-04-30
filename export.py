import process
from abc import ABC, abstractmethod

class allReviews():
    def __init__(self, df):
        self.df = df
     
    def getAllReviews(self):
        all_reviews = self.df[['Hotel_Name','Positive_Review','Negative_Review']]
        all_reviews.to_json("All_Reviews.json")
    @abstractmethod
    def getByHotel(self, name):
        pass
    
class selectedReviews(allReviews):
    def __init__(self, df):
        super().__init__(df)
        
    def getByHotel(self, name):
        hotel = process.HotelReview_ByHotelName(self.df,name)
        hotel.to_json(name + "_Review.json")
    

    
    
    