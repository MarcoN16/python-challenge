# python-challenge
This repository contains two Python scripts. The first script focuses on analyzing the financial records of a company, while the second script aims to modernize the vote-counting process in a small town.

# Finacial Analysis script overview

This project utilizes the 'budget_data.csv' dataset in CSV format, containing information in two columns: Date and Profit/Losses. The data is collected consistently during the second week of each month, allowing for comparisons of profits and losses within a 30-day time period. The script, developed using Visual Studio Code, is designed to showcase the following calculations:

•	Total number of data points included in the dataset

•	Net total amount of "Profit/Losses" over the entire period

•	Changes in "Profit/Losses" over the entire period, followed by the calculation of the average change

•	Greatest increase in profits (date and amount) observed over the entire period

•	Greatest decrease in profits (date and amount) observed over the entire period

Additionally, the script presents the analysis within the terminal and exports a text file containing the results to the analysis folder. Result:

![Financial_Analysis](https://github.com/MarcoN16/python-challenge/assets/150491559/945d52bc-29a5-458f-89b2-814d0dc7d525)

 
# Analysis of Election Poll Data

This project utilizes a dataset in CSV format named 'election_data.csv', containing information in three columns: Ballot ID, County, and Candidate. Developed using Visual Studio Code, the built-in function is tailored to construct a dictionary encompassing candidate names, their corresponding percentages, and the total number of votes garnered. The 'counting' function necessitates three inputs: 1st input – The list of unique candidate names; 2nd input – the list of the votes with the candidate’s name; 3rd input – The total count of votes cast. In this example the script showcases the following calculations:

•	The total number of votes cast

•	A complete list of candidates who received votes

•	The percentage of votes each candidate won

•	The total number of votes each candidate won

•	The winner of the election based on popular vote

Furthermore, the script presents the analysis within the terminal and exports a text file containing the results to the 'analysis' folder. Result:

![Election_results](https://github.com/MarcoN16/python-challenge/assets/150491559/b649a5cb-9e99-4629-b4fe-455454c7a83f)





