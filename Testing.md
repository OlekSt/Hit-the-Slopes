# Hit the Slopes! - TESTING
## Let's Team Up & Hit the Slopes! - TESTING
#### Data Centri development Project - Testing write-up

<img src="assets/images/readme/title_image.jpg" alt="Title image" style="margin: 0 10px;" width="100%"/>

This document is intended to record testing at various stages of development of the project, as well as different functions, functionalities, correct display of the project's page, etc. 

[Main README.md file](README.md)

[View website in GitHub Pages](https://hit-the-slopes.herokuapp.com/)

## Hit the Slopes app

1. [**Automated Testing**](#automated-testing)
    - [**Validation services**](#validation-services)
2. [**Client Stories Testing**](#client-stories-testing)
3. [**Manual Testing**](#manual-testing)
    - [**Testing undertaken on laptop**](#testing-undertaken-on-laptop) 
    - [**Testing undertaken on mobile and pad devices**](#testing-undertaken-on-mobile-and-pad-devices)
    - [**Testing undertaken in DevTools**](#testing-undertaken-in-DevTools)
4. [**Bugs discovered**](#bugs-discovered)
    - [**Solved bugs**](#solved-bugs)
    - [**Unsolved bugs**](#unsolved-bugs)
5. [**Further Testing**](#further-testing)


## Automated Testing

### Validation services
The following validation services were used to check the validity of the website code.
- [W3C Markup Validation]( https://validator.w3.org/) ......
- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) .....
- [JSHint](https://jshint.com/) .......
- [Am I responsive](http://ami.responsivedesign.is/) was used to check responsiveness of the website for various screen sizes - mobile, tab, laptop, desktop. 

## Client stories testing

The user stories are described in the UX section of [README.md](README.md) 

**As a website visitor, I want:**

1. I want to find other people with similar interests to meet them during my skiing holidays
    * I can clearly see what the website is about from the index page, where I see the slogan "Start or Join a snow Team"
    * I can clearly see from the start (on index page) what steps I need to take:
        - Sign Up
        - Post your trips
        - Search other users' trips
        - Team Up with other people
        - Go skiing/snowboarding
    * On Sign Up I can add my name or nickname, and provide info about my age, and where I am from, plus choose a cool avatar for myself
    * I can easily see a list of ski resorts and search for ones I am interested in
    * I can see a list of upcoming trips starting from current/today's dates

2. I want to easily add details of my trip to the DB
    * When I check ski resorts I can see what ski resorts I choose from, with a brief title to give me a general idea about it, in case I am not familiar with it. 
    * From a ski resort's account I can go directly to its official web-site, and to check its location on Google maps
    * I can create my own trip with necessesary info:
        - Dates of my trip
        - To which ski resort I will go
        - Who i will go with, adults, kids, alone, etc. 
        - What I prefer - skiing or snowboarding
        - Provide additional info about me, my friends, or my kids (age, for example), or my interests

3. I want to be able to check for already added trips and see if I’m interested to connect to other people
    * Trips show me:
        - A user who created a trip, including a user's profile, where I can see info about this user, and have an option to contact this user
        - Dates of this planned trip
        - To which ski resort
        - How many adults and go
        - What they prefer - skiing or snowboarding
        - Some additional info posted by a user
    * Based on the provided info described before I can decide which trips/users I am interested in    

4. I would like to contact other users
    * I can check users' profiles from trips they created
    * I can contact users and plan discuss possible meeting at the ski resort

5. I want to add locations if not yet in DB
    * If a ski resort is missing I can create one
                Note: If a user creates a ski resort, and later a manager wants to create a ski resort, the website owner will contact this user, and hand over rights to manager this ski resort's account to its official representative.

6. I want to see all trips for the next two months to a chosen location, and see if I’d plan my trip together with some other people
    * I can easily search trips by a ski resort's name, start and end dates, or any combination of those.
    * I can check for past trips, and contact users' and potentially plan some future trips if they go to locations I like


**As a ski resort manager, I want:**:

1. I want to add my location to the DB so users don’t have to do that
    * I can clearly see what the purpose of the website is
    * I can sign up and create an account for my ski resort for users to plan their trips and them to the list of upcoming trips
    * Only I can modify into on the account or delete the account altogether

2. I want to provide most important info about my location
    * I can add correct name of my ski resort
    * I can provide website and Google map links to the account

3. I want to provide correct links to my website
    * I can provide the correct link to my ski resort website
    * I can provide a correct Google map link to a place within the ski resort I consider the best locator

4. I want to advertise my location and promote upcoming events
    * I can discuss possible advertising options on the web-site with the web-sites' owner

    

## Manual testing


Currently performing testing on the go, while developing various functionalities of the app. 
Result below in Bugs section

### Bugs discovered: 

Navbar:
    -	Active menu item: shows all of them as active

Sign_up.html, Add_skiresort.html:
    - avatar & thumbnail images/names area of select is too narrow, diaplys is distorted.

Trips.html:
    - If a skiresort is deleted, a skiresort's thumbnail is not displayed on a trip in trips.html.

#### Solved bugs:

New user registration:
    - Google message: Passwords are not safe....

Navbar:
    -	Mobile menu: Is not visible, and pressing on menu sandwich does not open menu in mobile view.

Edit_skiresort.html:
    - Google maps info is lost on opening a specific ski resort to be updated. 
    - Does not show logged-in navbar.

Edit_trip.html:
    - Name of the stored resort is not posted to the form.

Trips.html:
    - User's avatar image per trip record is not visible. 
    - User's name is not visible
    - Deleting a trip triggers view distortion. Line of trips become blocks. 

Trips.html - Search by ski Ski_resorts:
    - User's avatar image per trip record is not visible. 
    - Ski resorts' thumbnails are not visible

Signing In:
    - Wrong name should redirect to sign_in_page.html. It just flashes the message: Wrong name. Try again. Also shows the full menu, instead of just Sing-In & Sign-Up menu to be visible for unlogged users.

Add_trip:
    - Does not render trips.html, writes "Collection is not iterble" for {% for trip in trips %}, while a trip is added to the DB correctly

Ski_resorts.html:
    - Each ski resort displayed multiple times.

Signing In:
    - Wrong name should redirect to sign_in_page.html. It just flashes the message: Wrong name. Try again. Also shows the full menu, instead of just Sing-In & Sign-Up menu to be visible for unlogged users.

Add_trip:
    - Does not render trips.html, writes "Collection is not iterble" for {% for trip in trips %}, while a trip is added to the DB correctly

Edit_skiresort.html:
    - Thumbnail info is lost on opening a specific ski resort to be updated.
    - Skiresort choice is lost on saving, if not chosen again.


Sign Up & Sign In on Heroku app:
    - Get this mistake: 'NoneType' object has no attribute 'users'.

Trips.html, Search:
    - Search does not work in combination: Ski resort name + dates (any of them(from or to) or both)
    - Search does not work with two dates: from & to
    - Dates search fields poorly visible on mobile

Trips.html, user's profile:
    - User's profile modal brings info of only one user, no matter if a different user's name clicked
    
#### Unsolved bugs:

Add_skiresort.html, skiresorts.html:
    - Issues with Materialize checkboxes for "spring/autumn/night skiing/glacier" info. Deleted the checkboxes for now. Using strings with "yes/no". If timing will allow, will add checkboxes at the end of the project.
    ** Removed functionality. 

## Further testing: 
...............
!!! TO BE ADDED