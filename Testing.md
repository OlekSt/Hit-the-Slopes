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
...............
!!! TO BE ADDED

## Manual testing

Currently performing testing on the go, while developing various functionalities of the app. 
Result below in Bugs section

### Bugs discovered: 

Navbar:
    -	Active menu item: shows all of them as active
    -	Mobile menu: Is not visible, and pressing on menu sandwich does not open menu in mobile view.

Edit_skiresort.html:
    -	Thumbnail (stored in DB) is not visible on the edit page. If not chosen upon updating, the initially save one is deleted, when saved after editing. 

New user registration:
    - Google message: Passwords are not safe....

Trips.html:
    -  User's avatar image per trip record is not visible. 
    - User's name is not visible
    - Deleting a trip triggers view distortion. Line of trips become blocks. 

Add_skiresort.html, skiresorts.html:
    - Issues with Materialize checkboxes for "spring/autumn/night skiing/glacier" info. Deleted the checkboxes for now. Using strings with "yes/no". If timing will allow, will add checkboxes at the end of the project.
    - Date field don't trigger calendar view date choice.

Signing In:
    - Wrong name should redirect to sign_in_page.html. It just flashes the message: Wrong name. Try again. Also shows the full menu, instead of just Sing-In & Sign-Up menu to be visible for unlogged users.

Add_trip:
    - Does not render trips.html, writes "Collection is not iterble" for {% for trip in trips %}, while a trip is added to the DB correctly

Edit_skiresort.html:
    - Thumbnail info is lost on opening a specific ski resort to be updated.




#### Solved bugs:

Edit_skiresort.html:
    - Google maps info is lost on opening a specific ski resort to be updated. 
    - Does not show logged-in navbar.

#### Unsolved bugs:
...............
!!! TO BE ADDED

## Further testing: 
...............
!!! TO BE ADDED