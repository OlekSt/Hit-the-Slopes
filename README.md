# Hit the Slopes!
## Let's Team Up & Hit the Slopes!

#### Python & Data Centric Project:
Website for people interested in skiing/snowboarding for planning their trips and meeting other visitors with similar interests. The website is be built using Flask-Python & MongoDB.

<img src="static/readme/hero_title_image.jpg" alt="Title image" style="margin: 0 10px;" width="100%"/>

[Hit the Slopes - Heroku link](https://hit-the-slopes.herokuapp.com/)

************************************************************

<img src="static/readme/amiresponsive_main.jpg" alt="Title image" style="margin: 0 10px;" width="100%"/>

************************************************************

## Table of Contents
1. [**UX**](#ux)
    - [**Goals**](#goals)
    - [**Strategy**](#strategy)
    - [**Scope**](#scope)
    - [**Structure**](#structure)
    - [**Skeleton**](#skeleton)
    - [**Surface**](#surface)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features to be Implemented**](#features-to-be-implemented)

3. [**Technologies used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)
    - [**How to run this project locally**](#how-to-run-this-project-locally)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Images**](#images)
    - [**Code**](#code)
    - [**Acknowledgments**](#acknowledgments)

7. [**Disclaimer**](#disclaimer)

************************************************************


## UX

### GOALS

What is the main goal of this site? 
- To provide easy to use, well-structured application to plan skiing holidays and team up with other people (based on common features, interests: age, family+kids, skiers or snowboarders, solo visitors).
The website will be built to cover only one country, with a possibility of scalability and adding more countries. 

Organizational Goals:
- Create a simple, easy to use website, where people can look for upcoming skiing trips of other people going to same locations on same dates. Based on similar features/interests (age, family-kids, solo, etc.). The website can be used by managers of skiing areas to add their areas to the DB, and attract visitors, as well as potentially promote events, promotions, etc. 

User Goals:
* Users: 
    - Effortlessly create a trip indicating dates, location, and who goes (number of people, age, etc).
    - Easily add a skiing area if not already in DB
    - Find trips and see details, and decide if a user is interested to contact other visitors going to same place on same dates
    - Vote for locations (optional)
    - Communicate with other users (feature to be added in the future)

* Ski location managers:
    - Add location to DB with relevant info
    - Provide info about promotions, possibly events

##### back to [top](#table-of-contents)

* Developer's goals:
    - Learn & practice data-driven full stack development, using HTML, CSS, & Javascript/JQuery, Flask-Python, MongoDb. 
    - Potentially monetize the platform/app by offering advertising options to skiing locations’ managers, restaurants, spas, other businesses in the skiing areas, skiing equipment and outfit brands
    - Extra potential to offer advertising to brands, like Red Bull or Audi who have constant advertising and events sponsorship on skiing locations

* User Interface:
    - Visually simple and easy to navigate
    - Not too crowded or too colorful
    - Clear objectives, instructions, reactions or prompts where needed


### STRATEGY

Create a website where people can look for other people to team up for skiing holidays. For example, a family (age between 30-35) going to ski with one kid (age 6), would be interested to meet similar people, parents of similar age, with a kid of similar age, if both families going to the same location on same dates.  
Reasoning: people can find people (from same or different countries) with similar interests, communicate before the trip, and then have good time during the trip at the location. 

##### back to [top](#table-of-contents)

### SCOPE 

User Stories:
* Visitors:
    - I want to find other people with similar interests to meet them during my skiing holidays
    - I want to easily add details of my trip to the DB
    - I want to be able to check for already added trips and see if I’m interested to connect to other people
    - I would like to contact other users
    - I want to add locations if not yet in DB
    - I want to see all trips for the next two months to a chosen location, and see if I’d plan my trip together with some other people

* Locations’ manager:
    - I want to add my location to the DB so users don’t have to do that
    - I want to provide most important info about my location
    - I want to provide correct links to my website
    - I want to advertise my location and promote upcoming events

### STRUCTURE 

**This is planned structure. Some features or their position on the website were changed during the project implementation due to optimization of either the website's functionality or development process.**

- The main screen will have a background image and a slogan: "Let’s Team Up & Hit the Slopes", plus two buttons: Sign Up & Sign In

- Sing Up screen: 
    - Username, Password, Re-enter password, Choose an avatar
    - Navbar, with the website Name/Logo, Menu: Home, SignUp, SignIn
    - INFO button to open footer modal with copyright info

- Sing In screen: 
    - Username, Password
    - Navbar, with the website Name/Logo, Menu: Home, SignUp, SignIn
    - INFO button to open footer modal with copyright info

- Trips screen: 
    - List of trips with dates, location, user info.
    - Navbar, with the website Name/Logo, Menu: Home, Trips, Add Trip, Locations, Add Location
    - INFO button to open footer modal with copyright info
    - Each trip thumbnail has a user icon, which (onhover or onclick) shows info about a user: age, m/f, from (e.g. Prague), ski/snowboard preference, and option to contact
    - Sidebar with Top locations, and search options (optional)

##### back to [top](#table-of-contents)

- Locations screen: 
    - List of locations with dates, location, user info
    - Navbar, with the website Name/Logo, Menu: Home, Trips, Add Trip, Locations, Add Location
    - INFO button to open footer modal with copyright info
    - Sidebar with upcoming trips, and search options (optional)

- Add Location screen: 
    - Fields to fill in:
        - Name
        - Description
        - Website link
        - Location map link
        - Conditions (spring/autumn skiing, night skiing, glacier or not)
        - Picture upload option
        - Additional info 
    - Navbar, with the website Name/Logo, Menu: Home, Trips, Add Trip, Locations, Add Location
    - INFO button to open footer modal with copyright info

- Add Trip screen: 
    - Fields to fill in:
        - Location name
        - Dates, from - to
        - Number of people – adults, kids
        - Person/Group – skiing or snowboarding
        - Additional info
    - Navbar, with the website Name/Logo, Menu: Home, Trips, Add Trip, Locations, Add Location
    - INFO button to open footer modal with copyright info

- Single Trip screen: 
    - Location name
    - Dates, from – to
    - Number of people – adults, kids
    - Person/Group – skiing or snowboarding
    - Additional info
    - Navbar, with the website Name/Logo, Menu: Home, Trips, Add Trip, Locations, Add Location
    - INFO button to open footer modal with copyright info
    - A user icon, which (onhover or onclick) shows info about a user: age, m/f, from (e.g. Prague), ski/snowboard preference, and option to contact
    - Link – Back to Trips
    - Link - Locations
    - Navbar, with the website Name/Logo, Menu: Home, Trips, Add Trip, Locations, Add Location
    - INFO button to open footer modal with copyright info.

##### back to [top](#table-of-contents)

- Single Location screen: 
    - Location name
    - Description
    - Image/Thumbnail 
    - Conditions (spring/autumn skiing, night skiing, glacier or not)
    - Other info 
    - Website link
    - Map link
    - Link to check upcoming trips to this location- 
    - Link – Back to Locations
    - Navbar, with the website Name/Logo, Menu: Home, Trips, Add Trip, Locations, Add Location
    - INFO button to open footer modal with copyright info


### SKELETON

[Balsamiq](https://balsamiq.com/) wireframes software was used to create wireframes for this project:

* [All screens - Computer view](static/readme/wireframes/laptop_view_wireframes.pdf)

* [All screens - Mobile phone view](static/readme/wireframes/mobile_view_wireframes.pdf)



### SURFACE 

Design choices:
- Make very simple easy to use and navigate website with minimum details, fields, colors, etc.
- Main introductory screen will have a slogan “Let’s Team Up and Hit the Slopes”, plus two buttons: Sign Up, Sign In, no Navbar.
- Initial screens (Sign In, Sign Up) Nav bar will have a minimal menu: Home, Sign In, Sign Up.
- All signed in screen will have Navbar menu: Trips, Add Trip, Locations, Add Location. Click on logo will take a user to Trips page, which will work as Home page when logged in.

Colors:
- Color schemed was decided to start from three colors from the background image – skis’ color, and two different shades of the sky in the background, and deriving palettes from these three colors.
Color choosing: 
<img src="static/readme/palette/color_ picking.jpg" alt="Color Picking" style="margin: 0 10px; align-self: center;" width="100%"/>

##### back to [top](#table-of-contents)

Palettes derived from the chosen colors: 
 
<img align="center" src="static/readme/palette/matching_palette.jpg" alt="Matching Palette" style="margin: 0 10px; align-self: center;" width="80%"/>

<table>
    <tr>
        <td><img src="static/readme/palette/highlight_palette.jpg" alt="Highlight Palette" style="float: left; margin-rigth: 10px;" width="100%"/></td>
        <td><img src="static/readme/palette/spot_palette.jpg" alt="Spot Palette" style="float: left; margin-rigth: 10px;" width="100%"/></td>
    </tr>
</table>


Fonts: 
* Roboto font was chosen for the website due its simplicity but great look and readability.

Images:
- Background image was chosen to convey the idea about going skiing/snowboarding, featuring slopes, mountains, skiers.
- Avatars for user were chosen for their looks as human interest in skiing/snowboarding or interests related to this recreational activity/sport.
- Thumbnail for ski resorts were chosen featering mountains, ski lifts or skit cottages/huts to convey the idea of a ski resort. 

##### back to [top](#table-of-contents)


## FEATURES
### EXISTING FEATURES

#### FOR NON-LOGGED IN USERS

1. MAIN PAGE:
- The introduction screen with the slogan "Join/Start a snow team" with a list of actions required: Sign up, Post Trips, Search Trips, Team Up, Hit the slopes (each with a descriptive icon).
- SignUp action is a link to sign_up.html, and Post Trips, Search Trips, Team Up actions point to sign_in.html. 
- The navbar has the Logo and links to Sign Up and Sing In.

<img src="static/readme/main_screen.png" alt="Main screen" style="margin: 0 10px;" width="70%"/>

2. SIGN UP screen:
- The navbar has the Logo and links to Sign Up and Sing In.
- The Sign UP card has the following fields:
    * Card title "SIGN UP"
    * Name
    * Password
    * Gender (dropdown menu)
    * Age (dropdown menu)
    * Home town/country
    * Avatar (dropdown menu)
    * Button "SIGN UP"

3. SIGN IN screen:
- The navbar has the Logo and links to Sign Up and Sing In.
- The Sign UP card has the following fields:
    * Card title "SIGN IN"
    * Name
    * Password
    * Button "SIGN IN"

<table>
    <tr>
        <td><img src="static/readme/sign_up_screen.png" alt="Sign Up screen" style="float: left; margin-rigth: 10px;" width="100%"/></td>
        <td><img src="static/readme/sign_up_screen.png" alt="Sign In screen" style="float: left; margin-rigth: 10px;" width="100%"/></td>
    </tr>
</table>

##### back to [top](#table-of-contents)

#### FOR LOGGED IN USERS

<img align="center" src="static/readme/trips.png" alt="Trips screen" style="float: left; margin-rigth: 10px;" width="80%"/>

1. TRIPS:
- Navbar has the following:
    * The Logo
    * Trips 
    * New Trip
    * Ski resorts
    * New Ski Resort 
    * Copyright/about
    * Sign Out
*On mobile devices the navbar has only the logo and burge menu button, which opens a mobile view menu with the respective options*

- Flashed message area: 
    * After sign up: "Welcome, 'username'!"
    * After login: "Welcome back, 'username'!"
    * After trips search show relevant messages
- Search area with:
    * Title "Search Upcoming Trips"
    * Ski resort name field
    * Date from field (open calendar picker)
    * Date to field (open calendar picker)
    * Reset button
    * Search button
- Trips (list of trips in chronological order starting from current/today's date)
- Each trip card has:
    * User's name with a popup suggestion bubble(which opens a profile in a modal)
    * Avatar
    * Ski resort name with a popup suggestion bubble(works as a link to ski resorts)
    * Ski resort thumbnail
    * Date from 
    * Date to
    * Adults (number)
    * Kids (number)
    * Ski or Snowboard preference
    * Additional info (posted by a creator of a trip)
    * ONLY for a creator of a trip: Edit & Delete buttons.

##### back to [top](#table-of-contents)

<table>
    <tr>
        <td><img src="static/readme/trips_search.png" alt="Sign Up screen" style="float: left; margin-rigth: 10px;" width="100%"/></td>
        <td><img src="static/readme/user_profile.png" alt="Sign In screen" style="float: left; margin-rigth: 10px;" width="100%"/></td>
    </tr>
</table>

2. NEW TRIP:
- Navbar (as described above in point 1)
- New Trip card with:
    * Card title "New Trip"
    * Choose ski resort field (dropdown menu with the list of registered ski resorts)
    * Date from (opens a calendar datepicker)
    * Date to (opens a calendar datepicker)
    * Adults (number field)
    * Kids (number field)
    * Ski or Snowboard preference (dropdown menu)
    * Additional info field
    * Button "Save Trip"

<table>
    <tr>
        <td><img src="static/readme/new_trip01.png" alt="New Trip" style="float: left; margin-rigth: 10px;" width="100%"/></td>
        <td><img src="static/readme/new_trip02.png" alt="New Trip" style="float: left; margin-rigth: 10px;" width="100%"/></td>
    </tr>
</table>

3. SKI RESORTS:
- Navbar (as described above in point 1)
- Search area with:
    * Title "Search Ski Resorts"
    * Ski resort name field
    * Reset button
    * Search button
- Ski resorts (list, alphabetically displayed)
- Each ski resort card has:
    * Name
    * Brief descriptive title
    * Thumbnail
    * Glacier: Yes/No
    * Night skiing: Yes/No
    * Link to its official website
    * Link to a map wesbite (e.g. Google maps)
    * ONLY for a creator of a ski resort: Edit & Delete buttons.


##### back to [top](#table-of-contents) 

<table>
    <tr>
        <td><img src="static/readme/skiresorts.png" alt="New Trip" style="float: left; margin-rigth: 10px;" width="100%"/></td>
        <td><img src="static/readme/new_skiresort.png" alt="New Trip" style="float: left; margin-rigth: 10px;" width="100%"/></td>
    </tr>
</table>

4. NEW SKI RESORT:
- Navbar (as described above in point 1)
- New Ski Resort card with:
    * Card title "New Ski Resort"
    * Name field
    * Short description field
    * Field for a website
    * Field for a map link
    * Glacier info (dropdown menu)
    * Night skiing (dropdown menu)
    * Additional info field
    * Thumbnail (dropdown menu)
    * Button "Add Ski Resort"

5. Copyright modal
- A mini hero image 
- The website's title "Hit the Slopes!"
- Text: Desgined & Developed
- Designer/Developer's name "Ol.Statsenko", which works as a link to the developer's Github profile/repositories.


##### back to [top](#table-of-contents)


### FEATURES TO BE IMPLEMENTED

- Archiving of old trips:
    * Add a function of auto-archiving trips older than XX weeks/days.

- Delete a trip:
    * Feature to be added to ask a user for confirmation if he/she really wants to delete a trip.

- Delete a ski resort:
    * Feature to be added to ask a user for confirmation if he/she really wants to delete a ski resort.

- Lost password:
    * Add a feature to allow users to restore or change their passwords.

- Ski resorts search: 
    * To add a feature to search by an initial/two/three letter/s.

- Ski resorts:
    * Add a button "New Trip" to each ski resort, which would take a user to a New Trip page with a pre-selected ski resort.


##### back to [top](#table-of-contents)


## INFORMATION ARCHITECTURE
### DATABASE
For the purpose of the project MongodDB will be used as required by the project's task and requirements. 

The types of data stored in MongoDB for this project are:
- ObjectId
- String
- Datetime
- Object

### Collections Data Structure
The Family Hub website relies on the following DB collections:
* NOTE: The Data structure has been changed slightly changed during the development of the project. 

#### Users Collection
| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Name | username | text, `maxlength="40"` | string
Password | password | text, `maxlength="15"` | string
Gender | male or female | text | string
**Age Range** | ageRange | | **object**
18 to 25 years | age18to25 | choice | string
26 to 32 years | age26to32 | choice | string
32 to 40 years | age33to40 | choice | string
41 to 48 years | age41to48 | choice | string
49 years and up | age49up | choice | string
From | from | text, `maxlength="40"` | string
**Avatar Choice** | avatar | | **object**
Avatar01 | image path | text | string
Avatar02 | image path  | text | string
Avatar03 | image path  | text | string
Avatar04 | image path  | text | string
Avatar05 | image path  | text | string
Avatar06 | image path  | text | string
Avatar07 | image path  | text | string
Avatar08 | image path  | text | string

##### back to [top](#table-of-contents)

#### Trip/s Collection
| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Activity ID | _id | None | ObjectId 
Username | username |text, `maxlength="45"` | string
Location name | title | text, `maxlength="50"` | string
From | start | datepicker | datetime
To | end | datepicker | datetime
Adults| adults | text | string
Kids| kids | text | string
Ski or Snowboard | ski_snowboard| text | string
Other info | info | text, `maxlength="200"` | string


#### Location/s Collection
| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Activity ID | _id | None | ObjectId 
Location name | locationName |text, `maxlength="100"` | string
Short description | description |text, `maxlength="80"` | string
Website | url | url, `maxlength="100"` | string
Map link | map | url, `maxlength="100"` | string
Night | night | text | string
Glacier | glacier | text | string
**Thumbnail Choice** | thumbnail | | **object**
Thumbnail01 | image path | text | string
Thumbnail02 | image path | text | string
Thumbnail03 | image path | text | string
Thumbnail04 | image path | text | string
Thumbnail05 | image path | text | string
Thumbnail06 | image path | text | string
Thumbnail07 | image path | text | string
Thumbnail08 | image path | text | string
Thumbnail09 | image path | text | string
Thumbnail10 | image path | text | string
Other info | info | text, `maxlength="200"` | string

##### back to [top](#table-of-contents)


## TECHNOLOGIES USED 
This project is built using HTML, CSS, JavaScript, Python programming languages plus MongoDB.

- [JQuery](https://jquery.com) to simplify DOM manipulation
- [Gitpod](https://gitpod.io/) for coding the project.
- [GitHub](https://github.com/) to store & share the project's code. 
- [ChromeDevtools](https://developers.google.com/web/tools/chrome-devtools) to check created code and possible inconsistencies, find best parameters for various code items. 
- [Materialize](https://materializecss.com/) for navbar, calendar datepicker, icons, and other elements.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify some parts of the website's structure. 
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) for icons.
- [Flask microframework](https://www.fullstackpython.com/flask.html) -  to build and connect Jinja templates, Werkzeug for hashing & checking passwords.
- [Google Fonts](https://fonts.google.com/) for fonts.
- [AutoPrefixer](https://autoprefixer.github.io/) to make sure css prefixes cover all browser versions.
- [Am I responsive](http://ami.responsivedesign.is/) was used to check responsiveness of the website for various screen sizes - mobile, tab, laptop, desktop.
- [Balsamiq](https://balsamiq.com/) was used to create wireframes.
- [ColorSpace](https://mycolor.space/) for matching colors


## TESTING
Testing information can be found in separate [Testing.md](Testing.md) file.

##### back to [top](#table-of-contents)

## DEPLOYMENT

[Hit the Slope on Heroku](https://hit-the-slopes.herokuapp.com/)

Gitpod was used to code this project. It was then committed and pushed to Github using the command line and deployed on Heroku PaaS platform.
All versions and branches of the code are stored on [Github repository](https://github.com/OlekSt/Hit-the-Slopes).

## How to run this project locally

In order to clone this project, it is necessary to follow these steps:

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- If you use Code Institute template, all the above will be already installed
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine. 
    - How to set up your Mongo Atlas account [here](https://docs.atlas.mongodb.com/).

### Instructions
1. Install all required modules with the command 
```pip3 freeze -r requirements.txt```

2. In your local IDE create a file called `env.py`

3. Inside the env.py file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database `hit_the_slopes`, with collections `users`, `skiresorts`, and `trips`

4. Make sure to add env.py to a .gitignore file so it's not pushed to the repository

4. You can now run the application with the command
```python app.py```

9. You can visit the website at `https://8080-b781839f-058d-4b52-8df7-2319d1b0a0f7.ws-eu01.gitpod.io/`

##### back to [top](#table-of-contents)


## Heroku Deployment
To deploy the project to Heroku, follow these steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

##### back to [top](#table-of-contents)


## CREDITS
#### CONTENT
The website is created by Alexey Statsenko, using the media described below. 

#### IMAGES
- Main background image is from [Pexels](https://www.pexels.com/). 
- Avatar and Thumbnail images/icons are [Freepik from Flaticon](https://www.flaticon.com/). 

#### CODE
- Materialize Select fields validation is from [CI's Flask Mini Project Video](https://www.youtube.com/watch?v=CG36uQtAzkU&feature=youtu.be).
- Code for info bubble above a user’s name and a ski resort’s name is taken from [Kevin Powell's video](https://www.youtube.com/watch?v=xoRbkm8XgfQ).


#### ACKNOWLEDGMENTS 
1. Tim Nelson, CI tutor for a lot of help with various parts of the project, & sharing learning materials, and general advice on coding.
2. Stephen Moody, CI tutor for help with code and some general advice on coding.  
3. Igor Basuga, CI tutor for help with the project.
4. My mentor, Adegbenga Adeye, for advice and help with planning and creating the website; checking the project and giving advice during the project's calls - checking the code, fixing problems, giving general advice how to organize the website in a better way.
5. My brother Andrey, and friends - Mario, Chris, Katja, for testing the game on various devices, info on possible fixes, and advice for improvement. 

##### back to [top](#table-of-contents)