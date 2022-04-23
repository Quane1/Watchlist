# Watchlist

This project aims to create an interactive Anime watchlist with multiple different features to complete the experince. The program can add to, delete from, sort, update and display the numerous title on this list that is stored on a seperate text file. 

anime_list is a text file that holds my current anime watchlist. This file is negligible. If anime_list  did not exist, Watchlist.py would generate anotber text file in its place.

As of 4/14/2022, the add, delete, and display functions are all comeplete. The next steps are to focus on the sort and update features. The sort would be alphabetical, by their title's length, episode count or by chronological order to their addition on the list with a reverse function available. The update or current feature ask what show the user is watching. If the show is new to the list, it is simply added on to the end. If the show already exist in the list, the program will then ask the user what episode they are on to judge if they are finished or not. This feature relies on the use of APIs to easily pull the series length data.

As of 4/23/2022, more subfeatures were added to the sort function. There is now the option to reverse which simply flips the list. 