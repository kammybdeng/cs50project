# Weather Forecast Application
A weather forecast application that allows users to search for a city's weather. Logged in users can save and delete their favorite cities. The application retrieves weather data from a third party API[openweather].

## Features
# Search city with dropdown selection
- Users can search cities with a dynamic dropdown selection as they type in the city name
- Logged in users can maintain a list of Saved cities by saving and deleting cities.
- Users can register for accounts


## Structure and Design
- Two tables: users and cities to record the list of cities saved/unsaved by users with **CRUD** operation.
- **SQLlite** serves as the Database
- Implemented **AJAX** calls with jQuery to allow users to request for a different city weather without having to reload the page.
- Usage of **Flask-Bcrypt** for Password encrytion.
- Created updated_city.list.json to remove duplicated cities and countries from the original json file listed in the third party website.
- Ajax call on each user character input for filtering the Dropdown selection
- Dropdown selection allows users to distinguish cities with same names.

## Features in development
- Landing page of default city
- Ability to modify cities in dashboard
- Ability to use Google map to select location

## Struggles and Challenges
- Removed stacks implemented in my previous project and adapt the topics discussed in CS50. This includes replacing all the wt-flask forms with native HTML and Javascript, and deprecated the usage of SQLalchemy and replace with plain SQLite.
- Implemented the selection dropdown with Ajax.
- jQuery syntax
- Create correct parameter functions from links in Account to homepage and to trigger an Ajax call
- Generate the correct saved status and on each ajax call.
- Redesign database schema with plain SQLite syntax

## Redesign of previous project
This is a redesign of my previous project https://github.com/kammybdeng/weather_flask_webapp
after completing CS50.
