# TB2_linus_scherrer_exam_project
## This is my repo for Tech Basics II. This Readme File is designed to support my MVP for my Final TBII Project.

# Queer Security International - Usage Guide

## Overview
Queer Security International is a GUI application designed to provide insights into the safety and inclusiveness of countries for the LGBTQ+ community. Built using Python and the Tkinter library, this application allows users to view and contribute ratings and reviews on LGBTQ+ friendliness of countries around the world.

## Getting Started
To use this application, ensure you have Python installed on your computer. Clone or download the repository to your local machine.

## Dependencies
+ Python 3.x
+ Tkinter (usually comes with Python installation)

## Running the Application
1. Open a terminal or command prompt.
2. Navigate to the directory where you've saved the application files.
3. Activate the virtual environment. 
4. Run the application by executing python mvp.py 

## Navigating the Application
***Initial Setup:*** Upon launching, the application displays a world map. Select a continent to view countries within that region.

***Selecting a Country:*** Click on the button corresponding to your country of interest to access detailed information and user-contributed content.

***Rating a Country:*** Use the provided entry box to rate the country on a scale of 1 to 5, then click "Submit" to store your rating.

***Writing a Review:*** Enter your text review in the space provided beneath the "Write your review:" label. Submit your review by clicking the "Submit Review" button. Your review will then be displayed on the country's page.

***Viewing Reviews:*** Scroll through the reviews section to read insights shared by other users.

***Returning to the World Map:*** Click the "<- Back" button at any time to return to the world map view and select a different continent or country.

### Navigating through the Pages
+ Page 1 (***World Map***): 
  + This is the initial view upon launching the application. It presents a global map, allowing users to select a continent of interest. The interface is designed to be intuitive, with clickable regions corresponding to each continent. Selecting a continent navigates the user to the respective continent page.
  
+ Page 2 (***Continent pages***):
  + After selecting a continent from the World Map, users are directed to a page that lists the countries within that continent. Each country is represented as a clickable button or link. This intermediate page serves as a gateway, enabling users to dive deeper into specific country-level details. It's an overview page that consolidates the countries under the chosen continent, simplifying the selection process for the user.
  
+ Page 3 (***Country Pages***):
  + Clicking on a country from the continent page leads users to the country-specific page. Here, detailed information regarding LGBTQ+ rights, safety, and community support within the selected country is displayed. Additionally, this page hosts two key interactive features:
    1. Rating System: Users can submit their ratings on the country's LGBTQ+ friendliness. These ratings are unique to each country and persistently stored, ensuring that users' contributions remain available for the community.
    2. Review Functionality: Beyond numerical ratings, users can write and submit text reviews detailing their experiences or insights regarding LGBTQ+ inclusivity in the country. These reviews are displayed on the page, offering valuable qualitative feedback to other users.

## Features
***Country-Specific Information:*** Access detailed LGBTQ+ rights and safety information for selected countries.

***Persistent Reviews and Ratings:*** Contributions by users are stored and displayed persistently, enriching the database with community insights.

***Dynamic Content Management:*** The application's backend supports the addition of new countries and information, facilitating continuous growth and relevance.

## Contributing
Users are encouraged to contribute by submitting ratings and text reviews for countries they are familiar with. This collective effort is crucial for building a comprehensive and reliable resource for the LGBTQ+ community.

#### License
This project is open-source and owned by Linus Scherrer.

