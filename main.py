"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""

from lib2to3.pgen2.parse import ParseError
import tui
import pandas as pd
import process
import visual
import tabulate

# Task 11: Import required modules and create an empty list named 'reviews_data'.
# This will be used to store the data read from the source data file.
# TODO: Your code here
reviews_data = []


def run():
    # pd.set_option('max_colwidth', 800)
    # pd.set_option('display.expand_frame_repr', False)
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()
    # Task 13: Load the data.

    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    tui.progress("Loading Data", 0)
    try:
        # - Load the data. Each line in the file should represent a review in the list 'reviews_data'.
        reviews_data = pd.read_csv("./data/hotel_reviews.csv")
        df = pd.DataFrame(reviews_data)
    # You should appropriately handle the case where the file cannot be found or loaded.
    except FileNotFoundError:
        tui.error("File Not Found")
        return
    except pd.errors.ParserError:
        tui.error("Error Loading")
        return
    except:
        tui.error("ERROR IN GETTING FILE")
        return

    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many reviews have
    tui.total_reviews(process.Count_All_Reviews(df))

    # been loaded and that the data loading operation has completed.
    tui.progress("Loading Data", 100)

    while True:

        # Task 14: Using the appropriate function in the module 'tui', display the main menu

        # Assign the value returned from calling the function to a suitable local variable

        opt = tui.main_menu()
        if (opt == 4):
            break

        # TODO: Your code here

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        if (opt == 1):
            tui.progress("Data Processing", 0)

        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
            # To process the data, do the following:
            # - Use the appropriate function in the module 'tui' to display a sub-menu of options for processing the data
            # (menu variant 1).

            sub_opt = tui.sub_menu(opt)
            # - Check what option has been selected

            #   - If the user selected the option to retrieve reviews by hotel name then
            if (sub_opt == 1):
                 #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has started
                tui.progress("Review Retrieval", 0)

                #        - Use the appropriate function in the module 'process' to retrieve the review and then appropriately

                name = tui.hotel_name()
                print(process.HotelReview_ByHotelName(df, name).to_markdown())

        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has
        #       completed.

                tui.progress("Reivew Retreival", 100)
        #
        #   - If the user selected the option to retrieve reviews by review dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve the reviews
        #       - Use the appropriate function in the module 'tui' to display the retrieved reviews.
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has completed.
        #
            if (sub_opt == 2):
                    #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has started
                tui.progress("Review Dates", 0)

                #        - Use the appropriate function in the module 'process' to retrieve the review and then appropriately

                d = tui.review_dates()
                for date in d:
                    print(process.HotelReviewsByDate(
                        df, date).to_markdown())

            #       display it.
            #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has
            #       completed.

                tui.progress("Reivew Dates", 100)

            #   - If the user selected the option to group reviews by nationality then
            #       - Use the appropriate function in the module 'tui' to indicate that the grouping
            #       process has started.
            #       - Use the appropriate function in the module 'process' to group the reviews
            #       - Use the appropriate function in the module 'tui' to display the groupings.
            #       - If required, you may add a suitable function to the module 'tui' to display the groupings
            #       - Use the appropriate function in the module 'tui' to indicate that the grouping
            #       process has completed.

            if (sub_opt == 3):
                    #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has started
                tui.progress("Review Nationality", 0)

                #        - Use the appropriate function in the module 'process' to retrieve the review and then appropriately

            
                print(process.grpbyReviewsNationatlity(df))

            #       display it.
            #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has
            #       completed.

                tui.progress("Reivew Nationality", 100)

            #
            #   - If the user selected the option to summarise the reviews then
            #       - Use the appropriate function in the module 'tui' to indicate that the summary
            #       process has started.
            #       - Use the appropriate function in the module 'process' to summarise the reviews.
            #       - Add a suitable function to the module 'tui' to display the summary
            #       - Use your function in the module 'tui' to display the summary
            #       - Use the appropriate function in the module 'tui' to indicate that the summary
            #       process has completed.
            
            if (sub_opt == 4):
                    #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has started
                tui.progress("Review Summary", 0)

                #        - Use the appropriate function in the module 'process' to retrieve the review and then appropriately

            
                print(process.summarizeData(df).to_markdown())

            #       display it.
            #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has
            #       completed.

                tui.progress("Reivew Summary", 100)
                
            tui.progress("Review Processing", 100)
    
        # TODO: Your code here
        elif opt == 2:
            
            tui.progress("Data Visualization", 0)
            sub_opt = tui.sub_menu(2)
            
            
            
            if (sub_opt == 1):
                
                tui.progress("Positive Negative Pie Chart", 0)
                name = tui.hotel_name()
                visual.hotelReviewInPieChart(df,name)
                
                tui.progress("Positive Negative Pie Chart", 100)
                
            elif (sub_opt == 2):
                
                tui.progress("Nationality Graph", 0)
                visual.NationalityGraph(df)
                
                tui.progress("Nationality Graph", 100)
            
            elif (sub_opt == 3):
                tui.progress("Animation", 0)
                
                visual.anim(df)
                tui.progress("Animation", 100)
            tui.progress("Data Visualization", 100)
            
            
        # Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual' to display the visual
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TODO: Your code here

        # Task 25: Check if the user selected the option for exporting reviews.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve what reviews are to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the reviews (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the reviews, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the reviews (either all or only those for a specific country/region) to a JSON file.
        # TODO: Your code here

        # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here

        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here

        pass  # can remove


if __name__ == "__main__":
    run()
