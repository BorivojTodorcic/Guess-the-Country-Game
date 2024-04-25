"""
EuroGuess - A game to guess European countries on a map.

This game presents the player with a map of Europe and prompts them to guess the names of various European countries.
The player inputs their guess, and the game checks if it matches the correct name of the country on the map.

The player earns points for each correct guess and can see the country names update on the map throughout the game.

Controls:
- Input the guessed country name via keyboard
    - The names are not case sensitive but spelling is important

Usage:
1. Run the main.py file.
2. Start guessing the countries by typing their names in the text box.
3. Keep guessing until you're satisfied you have guessed as many as you can.
4. Enter 'exit' into the text box when you are done.
5. Revise the countries_to_learn.csv file which contains a list of the countries you may have missed.
"""


import pandas as pd
import turtle as t


# Store the file path and font setting as variables so that they can be updated easily
image = "./europe_map.gif"
csv = "./europe_countries.csv"
export_csv = "./countries_to_learn.csv"
font = ('Arial', 12, 'normal')


# Screen settings and add europe_map.gif as the background
screen = t.Screen()
screen.bgpic(image)
screen.title("Guess the Country - Europe Version")
screen.setup(height=734, width=1000)


# Create a list of all the countries
country_data = pd.read_csv(csv)
all_countries = country_data.country.to_list()


total_countries = len(all_countries)
correct_answers = []
countries_missed = []


while len(correct_answers) < len(all_countries):
    # Request user to guess a country name
    answer_country = screen.textinput(title=f"Guess the country {len(correct_answers)}/{total_countries}", prompt="Can you guess another country?").title()

    if answer_country == "Exit":
        # Saves all the missed countries to a new csv file when the keyword 'exit' is entered
        for county in all_countries:
            if county not in correct_answers:
                countries_missed.append(county)
            df = pd.DataFrame({"Countries": countries_missed})
            df.to_csv(export_csv)
        break

    elif answer_country in all_countries:

        # Check if the country has already been added
        if answer_country not in correct_answers:
            # Create a new turtle object
            new_text = t.Turtle()
            new_text.hideturtle()
            new_text.penup()
            new_text.color("black")

            # Place country name on the map as per the coordinates on the csv file
            country_info = country_data[country_data.country == answer_country]
            new_text.goto(x=int(country_info.x), y=int(country_info.y))
            new_text.write(f"{answer_country}", font=font, align="center")

            # Add the correct answer to the list of correct answers
            correct_answers.append(answer_country)

    else:
        continue

if len(correct_answers) == len(all_countries):
    print("Well done on correctly guessing all the countries!")
