#import the necessary libraries and functions from other files
import tkinter as tk
from src.helpers import clear_widgets, set_background

#define the necessary global variables
current_country = None
info_label = None
warning_label = None
review_entry = None
country_ratings = {}
country_reviews = {}

# Define a function to add a review input section to the GUI for a specific country.
def add_review_input(root, current_country):
    # Create a label widget within the 'root' window, instructing users to write their review.
    review_label = tk.Label(root, text="Write your review:", font="Arial 12")
    review_label.place(x=5, y=35)
    # Create a text widget allowing users to input their review.
    review_text = tk.Text(root, height=5, width=50)
    review_text.place(x=5, y=65)
    # Create a button that users will click to submit their review.
    submit_review_btn = tk.Button(root, text="Submit Review",
                                  command=lambda: submit_text_review(current_country, review_text.get("1.0", "end-1c"),root))
    submit_review_btn.place(x=5, y=140)

def display_reviews(current_country, root):
    global country_reviews
    # Assuming you have a frame or specific area where reviews are displayed, clear it first

    reviews_frame = tk.Frame(root)
    reviews_frame.place(x=5, y=175)

    if current_country in country_reviews:
        for review in country_reviews[current_country]:
            tk.Label(reviews_frame, text=review, wraplength=400, justify="left").pack()

def submit_text_review(current_country, review, root):
    global country_reviews
    # Add the review to the country_reviews dictionary
    if current_country in country_reviews:
        country_reviews[current_country].append(review)
    else:
        country_reviews[current_country] = [review]

    # Refresh the display to show the new review
    display_reviews(current_country, root)
def submit_review():
    global warning_label, review_entry
    rating = review_entry.get()
    # Handle the submitted review
    rating = float(rating)
    if 1 <= rating <= 5:
        # Destroy the warning label if it exists
        if warning_label:
            warning_label.destroy()

        country_ratings.setdefault(current_country, []).append(rating)
        avg_rating = get_average_rating()
        avg_rating_label.config(text=f"Average Rating: {avg_rating:.2f}")
    else:
        # Create a warning label if it doesn't exist
        warning_label = tk.Label(text="Please enter a rating between 1 and 5.", font="Arial 12", fg="red")
        warning_label.place(x=250, y=30)

# Function to calculate average rating
def get_average_rating():
    ratings = country_ratings.get(current_country, [])
    if ratings:
        return sum(ratings) / len(ratings)
    else:
        return 0.0

# adds the components of the rating functionality
def rating_function(root):
    global review_entry, avg_rating_label
    # Add review functionality
    review_label = tk.Label(root, text="Rate your experience (1-5):", font="Arial 12")
    review_label.place(x=250, y=0)
    review_entry = tk.StringVar()
    review_box = tk.Entry(root, textvar = review_entry)
    review_box.place(x=470, y=0)
    submit_button = tk.Button(text="Submit", bg='Red', fg='black', font='arial 10',
                              command=submit_review
                              )
    submit_button.place(x=400, y=0)
    # Display average rating
    avg_rating = get_average_rating()
    avg_rating_label = tk.Label(root, text=f"Average Rating: {avg_rating:.2f}", font="Arial 12")
    avg_rating_label.place(x=400, y=30)

#function to add the back button
def back_button(root):
    back = tk.Button(text="<- Back",
                          bg='Red',
                          fg='black',
                          font='arial 10',
                          command=lambda: back_to_world(root)
                          )
    back.place(x=0, y=0)

# general function to create a new page
def new_page_setup(root, image_file_path):
    clear_widgets(root)
    set_background(root, image_file_path)
    back_button(root)

# launches the initial setup of the GUI
def initial_setup(root):
    set_background(root, image_file_path='images/world_map.jpeg')

    # Buttons for different continents
    asia_button = tk.Button(text="Asia",
                            bg='Red',
                            fg='black',
                            font='arial 10',
                            command=lambda: asia(root)
                            )
    asia_button.place(x=420, y=130)

    europe_button = tk.Button(text="Europe",
                              bg='Red',
                              fg='black',
                              font='arial 10',
                              command=lambda: europe(root)
                              )
    europe_button.place(x=300, y=100)

    australia_button = tk.Button(text="Australia",
                                 bg='Red',
                                 fg='black',
                                 font='arial 10',
                                 command=lambda: australia(root)
                                 )
    australia_button.place(x=530, y=330)

    namerica_button = tk.Button(text="North America",
                                bg='Red',
                                fg='black',
                                font='arial 10',
                                command=lambda: namerica(root)
                                )
    namerica_button.place(x=50, y=130)

    samerica_button = tk.Button(text="South America",
                                bg='Red',
                                fg='black',
                                font='arial 10',
                                command=lambda: samerica(root)
                                )
    samerica_button.place(x=120, y=280)

    africa_button = tk.Button(text="Africa",
                              bg='Red',
                              fg='black',
                              font='arial 10',
                              command=lambda: africa(root)
                              )
    africa_button.place(x=315, y=250)


# Function to show country information based on continent
def show_country_info(root):
    global info_label, current_country

    country = entry.get().lower()  # Get the country name from the input box

    # Remove the previously displayed information (if any)
    if info_label:
        info_label.destroy()

    #code to show country information
    country = entry.get()  # Get the country name from the input box
    if current_continent == "Asia":
        # Code for checking countries in Asia and displaying information
        if country.lower() == "japan":
            current_country = "Japan"
            new_page_setup(root, image_file_path='images/japan.jpg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''Japan has made progress in recognizing LGBTQ+ rights, with same-sex relationships being legal and some municipalities offering partnership certificates. However, nationwide protections against discrimination are limited, and achieving full equality remains a challenge.'''
        elif country.lower() == "china":
            current_country = "China"
            new_page_setup(root, image_file_path='images/china.jpeg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''LGBTQ+ rights in China face challenges, with limited legal protections against discrimination. LGBTQ+ individuals often encounter societal stigma, but there are emerging support networks and communities striving for greater acceptance.'''
        else:
            info_text = "Unfortunately, we don't have information about LGBTQ rights in this country."
    elif current_continent == "Europe":
        # Code for checking countries in Europe and displaying information
        if country.lower() == "germany":
            current_country = "Germany"
            new_page_setup(root, image_file_path='images/germany.jpeg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''Germany has made great progress in LGBTQ+ rights, legalizing same-sex marriage in 2017 and implementing comprehensive anti-discrimination laws. The country embraces a vibrant LGBTQ+ community with active organizations promoting inclusion and equality.'''
        elif country.lower() == "poland":
            current_country = "Poland"
            new_page_setup(root, image_file_path='images/poland.jpeg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''LGBTQ+ rights in Poland have faced significant challenges and controversies. The country has seen the rise of "LGBT-free zones" in some municipalities, sparking international criticism. Same-sex partnerships are not legally recognized and LGBTQ+ individuals face discrimination and social stigma.'''
        else:
            info_text = "Unfortunately, we don't have information about LGBTQ rights in this country."
    elif current_continent == "Australia":
        if country.lower() == "australia":
            current_country = "Australia"
            new_page_setup(root, image_file_path='images/australia.jpeg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''Australia has made strides in LGBTQ+ rights, legalizing same-sex marriage in 2017 and implementing comprehensive anti-discrimination laws. The country has a vibrant LGBTQ+ community and active organizations promoting equality and acceptance.'''
        elif country.lower() == "new zealand":
            current_country = "New Zealand"
            new_page_setup(root, image_file_path='images/new_zealand.jpeg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''New Zealand is a progressive leader in LGBTQ+ rights, legalizing same-sex marriage in 2013 and implementing comprehensive anti-discrimination laws. The country celebrates a vibrant LGBTQ+ community with organizations working towards equality and inclusion.'''
        else:
            info_text = "Unfortunately, we don't have information about LGBTQ rights in this country."
    elif current_continent == "North America":
        if country.lower() == "usa":
            current_country = "USA"
            new_page_setup(root, image_file_path='images/usa.jpeg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''The USA has made strides in LGBTQ+ rights, legalizing same-sex marriage nationwide in 2015 and implementing federal anti-discrimination laws. The country has a vibrant LGBTQ+ community with active advocacy organizations promoting equality and acceptance.'''
        elif country.lower() == "mexico":
            current_country = "Mexico"
            new_page_setup(root, image_file_path='images/mexico.jpeg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''Mexico has made strides in LGBTQ+ rights, legalizing same-sex marriage nationwide in 2015 and implementing anti-discrimination laws. The country has a vibrant LGBTQ+ community with active organizations promoting equality and inclusion.'''
        else:
            info_text = "Unfortunately, we don't have information about LGBTQ rights in this country."
    elif current_continent == "South America":
        if country.lower() == "brazil":
            current_country = "Brazil"
            new_page_setup(root, image_file_path='images/brazil.jpeg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''Brazil has made progress in LGBTQ+ rights, legalizing same-sex marriage in 2013 and implementing anti-discrimination laws. The country has a vibrant LGBTQ+ community with active organizations promoting equality and acceptance.'''
        elif country.lower() == "bolivia":
            current_country = "Bolivia"
            new_page_setup(root, image_file_path='images/bolivia.jpeg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''Bolivia has made progress in LGBTQ+ rights, recognizing the rights of transgender individuals and having active organizations advocating for equality and inclusion. Same-sex marriage is not yet legal, but public support is growing.'''
        else:
            info_text = "Unfortunately, we don't have information about LGBTQ rights in this country."
    elif current_continent == "Africa":
        if country.lower() == "zambia":
            current_country = "Zambia"
            new_page_setup(root, image_file_path='images/zambia.jpeg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''LGBTQ+ rights in Zambia face challenges, with same-sex sexual activity being illegal and no legal protections against discrimination. LGBTQ+ individuals experience social stigma and discrimination in the country.'''
        elif country.lower() == "rwanda":
            current_country = "Rwanda"
            new_page_setup(root, image_file_path='images/rwanda.jpeg')
            rating_function(root)
            add_review_input(root, current_country)
            info_text = '''LGBTQ+ rights in Rwanda face significant challenges, with same-sex sexual activity being criminalized and no legal protections against discrimination. Same-sex marriage is not recognized, and LGBTQ+ individuals often experience social stigma and discrimination.'''
        else:
            info_text = "Unfortunately, we don't have information about LGBTQ rights in this country."
    else:
        info_text = "This feature is not yet supported for the selected continent."
        # Display the information in a label
    info_label = tk.Label(root, text=info_text, font="Arial 12", wraplength=500, justify="center")
    info_label.place(x=75, y=270)

# Function to go back to the world map view
def back_to_world(root):
    set_background(root, image_file_path='images/world_map.jpeg')

    # Buttons for different continents
    asia_button = tk.Button(text="Asia",
                            bg='Red',
                            fg='black',
                            font='arial 10',
                            command=lambda:asia(root)
                            )
    asia_button.place(x=420, y=130)

    europe_button = tk.Button(text="Europe",
                              bg='Red',
                              fg='black',
                              font='arial 10',
                              command=lambda:europe(root)
                              )
    europe_button.place(x=300, y=100)

    australia_button = tk.Button(text="Australia",
                                 bg='Red',
                                 fg='black',
                                 font='arial 10',
                                 command=lambda:australia(root)
                                 )
    australia_button.place(x=530, y=330)

    namerica_button = tk.Button(text="North America",
                                bg='Red',
                                fg='black',
                                font='arial 10',
                                command=lambda:namerica(root)
                                )
    namerica_button.place(x=50, y=130)

    samerica_button = tk.Button(text="South America",
                                bg='Red',
                                fg='black',
                                font='arial 10',
                                command=lambda:samerica(root)
                                )
    samerica_button.place(x=120, y=280)

    africa_button = tk.Button(text="Africa",
                              bg='Red',
                              fg='black',
                              font='arial 10',
                              command=lambda:africa(root)
                              )
    africa_button.place(x=315, y=250)

#sets up the asia page
def asia(root):
    global current_continent, entry, avg_rating_label  # Update the global variable
    current_continent = "Asia"
    # remove redundant components and places back button add Image of the new map
    new_page_setup(root, image_file_path='images/asia.jpeg')
    # Add input box for country names
    entry = tk.Entry(root)
    entry.place(x=250, y=200)
    # Add button to show country information
    show_info_button = tk.Button(text="Show Info",
                                 bg='Red',
                                 fg='black',
                                 font='arial 10',
                                 command=lambda: show_country_info(root)
                                 )
    show_info_button.place(x=300, y=230)

#sets up the europe page
def europe(root):
    global current_continent, entry, avg_rating_label  # Update the global variable
    current_continent = "Europe"
    # remove redundant components and adds Image and back button of the new map
    new_page_setup(root, image_file_path='images/europe.jpeg')
    # Add input box for country names
    entry = tk.Entry(root)
    entry.place(x=250, y=200)
    # Add button to show country information
    show_info_button = tk.Button(text="Show Info",
                                 bg='Red',
                                 fg='black',
                                 font='arial 10',
                                 command=lambda:show_country_info(root)
                                 )
    show_info_button.place(x=300, y=230)

#sets up the australia page
def australia(root):
    global current_continent, entry, avg_rating_label  # Update the global variable
    current_continent = "Australia"
    # remove redundant components
    new_page_setup(root, image_file_path='images/australia_continent.jpeg')
    # Add input box for country names
    entry = tk.Entry(root)
    entry.place(x=250, y=200)
    # Add button to show country information
    show_info_button = tk.Button(text="Show Info",
                                 bg='Red',
                                 fg='black',
                                 font='arial 10',
                                 command=lambda: show_country_info(root)
                                 )
    show_info_button.place(x=300, y=230)
#sets up the north america page
def namerica(root):
    global current_continent, entry, avg_rating_label  # Update the global variable
    current_continent = "North America"
    # remove redundant components
    new_page_setup(root, image_file_path='images/namerica.jpeg')

    # Add input box for country names
    entry = tk.Entry(root)
    entry.place(x=250, y=200)

    # Add button to show country information
    show_info_button = tk.Button(text="Show Info",
                                 bg='Red',
                                 fg='black',
                                 font='arial 10',
                                 command=lambda: show_country_info(root)
                                 )
    show_info_button.place(x=300, y=230)
#sets up the south america page
def samerica(root):
    global current_continent, entry, avg_rating_label  # Update the global variable
    current_continent = "South America"
    # remove redundant components
    new_page_setup(root, image_file_path='images/samerica.jpeg')

    # Add input box for country names
    entry = tk.Entry(root)
    entry.place(x=250, y=200)
    # Add button to show country information
    show_info_button = tk.Button(text="Show Info",
                                 bg='Red',
                                 fg='black',
                                 font='arial 10',
                                 command=lambda: show_country_info(root)
                                 )
    show_info_button.place(x=300, y=230)

#sets up the africa page
def africa(root):
    global current_continent, entry, avg_rating_label  # Update the global variable
    current_continent = "Africa"
    # remove redundant components
    new_page_setup(root, image_file_path='images/africa.jpeg')

    # Add input box for country names
    entry = tk.Entry(root)
    entry.place(x=250, y=200)
    # Add button to show country information
    show_info_button = tk.Button(text="Show Info",
                                 bg='Red',
                                 fg='black',
                                 font='arial 10',
                                 command=lambda: show_country_info(root)
                                 )
    show_info_button.place(x=300, y=230)