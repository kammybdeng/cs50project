# Weather Forecast Application
A weather forecast application that allows users to search for a city's weather. Logged in users can save and delete their favorite cities. The application retrieves weather data from a third party API[Open Weather API](https://openweathermap.org/api).
Final Project for Harvard's [CS50x](https://cs50.harvard.edu/x/2021/)

## Features
- Users can search cities with a dynamic dropdown selection as they type in the city name
- Logged in users can maintain a list of Saved cities by saving and deleting cities.
- Users can register for accounts


## Structure and Design
- Two tables: Users and Cities, to record the list of cities saved/unsaved by users with **CRUD**.
- **SQLlite** serves as the Database
- Implemented **AJAX** calls with jQuery to allow users to request for a different city weather without having to reload the page.
- Usage of **Flask-Bcrypt** for Password encrytion.
- Created updated_city.list.json to remove duplicated cities and countries from the original json file listed in the third party website.
- Ajax call on each user character input for filtering the Dropdown selection
- Dropdown selection that allow users to distinguish cities with same names.

## Features in development
- Have a default city or a preferred city customized by user in the Landing page
- Ability to add and delete cities in dashboard
- Ability to use Google map to select location

## Struggles and Challenges
- Removed stacks implemented in my previous project and adapt the topics discussed in CS50x. This includes replacing all the Flask-WTF forms with native HTML and Javascript, and deprecating the usage of SQLalchemy and replacing it with plain SQLite.
- Implemented the selection dropdown with Ajax.
- Adapting jQuery syntax
- Create hyperlinks on the cities in the Account page to link back to homepage and trigger an Ajax call
- Generate the correct saved/added status on each ajax call on a new city.
- Redesign database schema and table modifications with plain SQLite syntax

## Redesign of previous project
This is a redesign of my previous project https://github.com/kammybdeng/weather_flask_webapp
after completing CS50x.
The previous project was mainly based on a [Youtube tutorial](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&index=5&ab_channel=CoreySchafer) and a lot of self googling to customize different features. The old project have successfully deployed on Heroku, whereas the current project have not yet.
