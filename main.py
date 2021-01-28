from turtle import Turtle, Screen
from PIL import Image
import pandas as pd


screen = Screen()
screen.bgpic("africa_map.gif")
screen.screensize(800, 800)
screen.title('African Countries')
turtle = Turtle()

countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cabo Verde",
             "Central African Republic", "Chad", "Comoros", "Congo", "The Democratic Republic of Congo",
             "Cote d’Ivoire", "Djibouti", "Equatorial Guinea", "Egypt", "Eritrea", "Ethiopia",
             "Gabon", "Gambia", "Ghana", "Guinea",
             "Guinea-Bissau", "Kenya", "The Kingdom of Lesotho", "Liberia", "Libya", "Madagascar", " Malawi", "Mali",
             "Mauritania", "Mauritius", " Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda",
             "Saharawi Arab Democratic Republic", "Sao Tome Principe", "Senegal", "Seychelles", "Sierra Leone",
             "Somalia", "South Africa", "South Sudan", "Sudan", "Swaziland", "Tanzania", "Togo",
             "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

country_dataframe = pd.read_csv("countries.csv")
country_list = country_dataframe['country'].to_list()
print(len(country_list))


i = 0
while i < len(country_list):
    user_input = screen.textinput(title=f'{i}/{len(country_list)} correct choices',
                                  prompt='Enter a country name').title()

    if user_input == 'Exit':
        break

    if user_input in country_list:
        country = country_dataframe[country_dataframe['country'] == user_input]
        x_cor = int(country['x'])
        y_cor = int(country['y'])
        print(x_cor, y_cor)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x_cor, y_cor)
        turtle.write(user_input)
        i += 1

# screen.mainloop()


# # Resize the image
# image = Image.open("map.gif")
# image.thumbnail((800, 1000))
# image.save("africa_map.gif")
#

# def get_x_y_coordinates(x, y):
#     print(x, y)
# screen.onclick(get_x_y_coordinates)