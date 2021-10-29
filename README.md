# George Lychock - MS3 Project: uSpice
### Salem State University Fullstack Software Developer Certificate
#### Python Module
-   [View Live Dev Site](https://gl-uspice-dev-01.herokuapp.com/)

<hr>

<h1 align="center"><img src="_documentation/montage.png" /></h1>

## Table of Contents

- [Use Case](#UC)
    - [User Stories](#US)
    - [Requirements](#REQS)
    - [Backlog (Future Requirements)](#BACKLOG)
- [UI/UX](#UXUI)
    - [UI](#UI)
        -   [Wireframes](#UIWF)
    - [UX - Design](#DES)
        -   [Wireframes](#UXWF)
- [Technical Background](#TECH)
- [Testing](TESTRM.md)
- [Known/Resolved Issues](#ISSUES)
- [Product/Project Management](#PROJ)
- [Deployment](#DPLY)
- [Credits](#CREDS)



<a name="UC"></a>

# Use Case

uSpice is a spice rub recipe utility to help users search, rate, build, and buy spice rubs they like.

When I buy expensive pre-made spice rubs I rarely know what all the ingredients are nor do I know what the proportions are for the rub recipe. I would like an app where I can search spice rub recipes, view details about the recipe, and rate the recipe. An added feature would be if the app could help me build my own recipes, based on base rub mixes, that I can customize by adding secondary ingredients and/or changing the base mix proportions. I also would like links to vendors that sell the ingredients to the recipes.


>
> ### Notes
>
>-  The primary focus of this project is to display Python and database skills learned in the Python Essentials Module of the Salem State University / Code Institute Full Stack Software Developer Certificate Program.
>-  

<a name="US"></a>

## User Stories

-   ### Anonymous AND Logged In User Experience
    -   #### **Story 1** As a Site Visitor, I want to be able to search recipes by using a quick search method.
        -  #### *Acceptance Criteria* -- Duplicated in Testing Section
            1.  A search form is presented without leaving the home page
            2.  A minimal number of search criteria is presented to choose from
            3.  When the form is submitted, user is redirected to the advanced search page and presented the results list/table
            
    -   #### **Story 2** As a Site Visitor, I want to see results of my search on a new page that offers sortable headers.
        -  #### *Acceptance Criteria* -- Duplicated in Testing below
            1.  Results are displayed in a list/table, with recipe title, date posted, base ingredient, and author
            2.  The list can be sorted by active headers
            3.  A recipe has a clickable link to display the recipe details

    -   #### **Story 3** As a Site Visitor, I want to see recipe details displayed on a recipe detail page
        -  #### *Acceptance Criteria* -- Duplicated in Testing below
            -   Recipe page includes the following details:
                1.  Recipe Name
                2.  Author
                3.  Ingredients
                4.  Description
                5.  Instructions (commentary)

    -   #### **Story 4** As a Site Visitor, I want to have a similar experience whether on a desktop, tablet, or mobile device, so that I can later access information in a similar manner if I change devices.
        -  #### *Acceptance Criteria* -- Duplicated in Testing below
            1.  All content has to be accessible from desktop, tablet, or mobile device.
            2.  All images should have alt text
            3.  Icons should be consistent across viewports
            4.  Indentation (margins and padding) should be structurally similar across viewports
            5.  Pages and sections use the same names throughout the site ie when referring to Work History, it's not later referred to Work Experience or Job Summary etc somewhere else in the site or on site nav
            6.  All fonts are consistent for each section and element across all viewports
            7.  All documents and links to external sites should open a new tab in the browser
            8.  Any page or internal site links should never open a new browser tab

    -   #### **Story 5** As a Site Visitor, I want to be able to search recipes by using an advanced search method.
        -  #### *Acceptance Criteria* -- Duplicated in Testing Section
            1.  A search form is presented on a new page when a user navigates to the advanced search
            2.  The search form allows input for recipe name, author, main ingredient, and date
            3. The submit button displays a results list/table on the advanced search page

-   ### ONLY Logged In User Experience
    -   #### **Story 6** As a Site Visitor, I want the ability to log in and log out so I can gain access to features that are only for logged in users.
    -  #### *Acceptance Criteria* -- Duplicated in Testing Section
        1.  User can create a profile and log in
        2.  The profile is a user name and a valid email address
        3.  Once logged in, access to rate and build recipes is provided
        4.  User can log out

    -   #### **Story 7** As a Logged In User, I want the ability to create my own recipe and upload to the app.
    -  #### *Acceptance Criteria* -- Duplicated in Testing below
        -   User Input should include the following:
            1.  Recipe Name
            2.  Author
            3.  Ingredients
            4.  Cuisine
            5.  Preparation (commentary)
            6.  Flavor Profile
            7.  Recipe Image Selection (from a predefined set)
        -   User can save recipe
        -   User is routed to the recipe view page once submitted
        -   User can update the recipe
        -   User can delete the recipe

    -   #### **Story 8** As a Logged In User and on the Recipe View page, I want the ability to view a graphcal representation of my recipe ingredient breakdown.
    -  #### *Acceptance Criteria* -- Duplicated in Testing below
        -   User is shown or presented a method to show a graphic depicting the recipe's ingredient ratios

    -   #### **Story 9** As a Logged In User I want to be able to rate recipes.
    -  #### *Acceptance Criteria* -- Duplicated in Testing Section
        1.  User can rate a recipe with a simple 5 star system when logged in and on the recipe page
        2.  A user cannot rate a recipe if they are not logged in

-   ### Administrator User Experience
    -   #### **Story 10** As a Site Administrator, I want to be able to regulate the number of postings for any user globally
        -  #### *Acceptance Criteria* -- Duplicated in Testing Section
            1.  App only allows any user to upload 5 recipes a day


<a name="REQS"></a>
## Requirements
(Alignments to User Stories are in paratheses)
-   Application must be responsive and fully functional to use on any device (US4)
-   Allow users to search recipes, using a quick search (US1)
-   Allow users to log in and log out of the app (US6)
-   Logging in provides user with feature to rate a recipe (US6)
-   Logging in provides user with feature to build a recipe (US6)
-   Allow users to search recipes, using an advanced search. Advanced search should allow user to search by recipe name, main ingredient, author, date (US7)
-   Provide a method for users to build a recipe and submit to the app
-   Monitor/regulate the number of recipes a user can upload per day (US8)
-   Show users the results of the search criteria (US2)
-   Allow users to view details about the recipe including an image (US3)
-   Allow users to rate a recipe (US7)
-   Allow users to view top 5 rated recipes
-   Create a pie chart showing the porportions of the recipe ingredients on the recipe page
-   Display a posted recipes section on the user profile page
-   Allow Users to choose an avatar from a pallet of avatars

<a name="BACKLOG"></a>
## Future Requirements
(Alignments to User Stories are in paratheses, if available)
-   Delete recipe confirmation routine needs to be incorporated, looking at Tkinker but I had issues with a duplicate root window popping up, so I reverted to not having a delete confirmation
-   Add Admin profile for user collection
-   Admin Functionality: Update Ingredients collection functionality
-   Admin Functionality: Update Flavors, Regions(Categories), Measures collection functionality
-   Add second password input field on Registration page to confirm password submitted
-   Any empty data sets (eg user does not have any submitted recipes to be displayed on Profile page) should fire a message to the user confirming data does not exist
-   Provide users links to available spice vendors so the user can purchase recipe ingredients
-   Allow users to print a printable version of the recipe page
-   Provide a method for the user to upload an image for their recipe



# UX/UI
-   ## UI
    <a name="UI"></a>
    -   ### Wireframes
        <a name="UIWF"></a>
        -   UI Map (Site Map aligned to data structures and functions) - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Map-.jpg)
    -   ### Sprints
        -   UI Sprint Map - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Sprints-.jpg)


-   ## UX - Design
    <a name="DES"></a>
    -   ### Wireframes
        <a name="UXWF"></a>
        -   Home Page - Desktop and Tablet Wireframe - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/wireframes/p1-uSpice-desktop-home-page.jpg)

        -   Home Page - Mobile Wireframe - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/wireframes/p2-uSpice-mobile-home-page.jpg)

        -   Advanced Search Page - Desktop and Tablet Wireframe - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/wireframes/p3-uSpice-desktop-advanced-search-page.jpg)

        -   Advanced Search Page - Mobile Wireframe - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/wireframes/p4-uSpice-mobile-advanced-search-page.jpg)

        -   Recipe View Page - Bar Chart - Desktop and Tablet Wireframe - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/wireframes/p5-uSpice-desktop-recipe-page-1.jpg)

        -   Recipe View Page - Pie Chart - Desktop and Tablet Wireframe - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/wireframes/p5-uSpice-desktop-recipe-page-2.jpg)

        -   Recipe View Page - Mobile Wireframe - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/wireframes/p6-uSpice-mobile-recipe-page.jpg)

        -   Recipe Build Page - Desktop and Tablet Wireframe - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/wireframes/p7-uSpice-desktop-build-recipe-page.jpg)

        -   Recipe Build Page - Mobile Wireframe - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/wireframes/p8-uSpice-mobile-build-recipe-page.jpg)


<a name="TECH"></a>
# Technical Background
-   ## Features and Logic
    -   The app uses custom Javascript and localStorage for the add ingredient functionality on the Build Recipe and Edit Recipe pages
    -   The app uses custom Javascript and localStorage for the nav click path arrows functionality
-   ## Sitemap, UI, and Data Structures
    -   UI Sitemap  - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Map-.jpg)
    -   Sprints  - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Sprints-.jpg)
    -   Data Structures  - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/uspice-data-structures.jpg)

-   ## Languages Used

    -   [HTML5](https://en.wikipedia.org/wiki/HTML5)
    -   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    -   [JavaScript](https://www.javascript.com/)
    -   [Python3](https://www.python.org/)

-   ## Frameworks, Libraries, & Programs Used

    1. [Bootstrap 5.1:](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
        - Bootstrap was used to assist with the responsiveness and styling of the website.
    2. [Google Fonts:](https://fonts.google.com/)
        - Google fonts were used to import the 'Montserrat' and 'Raleway' fonts into the style.css file which is used on all pages throughout the project.
    3. [Bootstrap Icons:](https://icons.getbootstrap.com/)
        - Bootstrap Icons was used for all app icons
    4. [jQuery:](https://jquery.com/)
        - jQuery came with Bootstrap and is used in custom JS.
    5. [Git](https://git-scm.com/)
        - Git was used for version control by utilizing Visual Studio on my Linux laptop to commit to Git and Push to GitHub.
    6. [GitHub:](https://github.com/)
        - GitHub is used to store the projects code after being pushed from Git.
    7. [Font Awesome:](https://fontawesome.com/)
        - Font Awesome was used for a few of the icons where I did not like the Bootstrap versions or BS did not have a suitable icon.
    8. [Flask:](https://flask.palletsprojects.com/en/2.0.x/)
        - Micro Framework for Python apps
    9.  [draw.io](https://app.diagrams.net/)
        - Wireframing tool
    10. [Inkscape](https://inkscape.org/)
        - Drawing app used for logo design
    11. [Flaticons](https://www.flaticon.com/authors/flat-icons)
        - Avatar images

-   ### Resources Used
    -   [MDN General Web Docs: ](https://developer.mozilla.org/) For semantic structure reference, arrays, localStorage, fetch.
    -   [W3Schools.com](https://www.w3schools.com/), For Color Picker, html/css/js general refernece, semantic structure reference, arrays, localStorage.
    -   [MindMajix: Mongodb Query Examples](https://mindmajix.com/mongodb-query-and-examples)
    -   [Tkinker Askyesno Tutorial from Pythontutorial.net](https://mindmajix.com/mongodb-query-and-examples)
    -   [MongoDB Documentation, Query Documents](https://docs.mongodb.com/manual/tutorial/query-documents/)
    -   [For Loop Examples from pythonguides.com:](pythonguides.com/python-for-loop-index/)

#   Testing
<a name="TESTING"></a>
-   [See Test ReadMe File](TESTRM.md)

#   Known/Resolved Issues
<a name="ISSUES"></a>
-   [See Test ReadMe File](TESTRM.md)

# Product/Project Management
-   ## UI
    <a name="PROJ"></a>
    -   ### Projected Sprints
        <a name="UIWF"></a>
        -   UI Sprint Map - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/wireframes/Site-UI-Sprints-.jpg)

<a name="DPLY"></a>
# Deployment
-   ## Hosting

    The project was deployed to Heroku hosting service:

    [URL to Heroku Site](https://gl-uspice-dev-01.herokuapp.com/)
    All Python requirements used can be found in the requirements.txt file. Procfile can be be found in Git repo as well. Environmnt variables are stored in a secure uncommitted file.

    ### *CLOANING INFORMATION from CODE INSTITUTE README.md template from User Centric Module, edits have been made for changes in GH UI*
    GitHub Pages
    The project was deployed to GitHub Pages using the following steps...
    1. Log in to GitHub and locate the [Project-Management-Dashboard---MS2 GitHub Repository](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice)
    2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
    4. Under "Source", click the dropdown called "None" and select "Master Branch".
    5. The page will automatically refresh.
    6. Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.

    ### Forking the GitHub Repository

    1. Log in to GitHub and locate the [Project-Management-Dashboard---MS2 GitHub Repository](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice)
    2. At the top of the Repository (not top of page) on the far right, locate the "Fork" Button. Sign in if needed.
    3. You should now have a copy of the original repository in your GitHub account.

    ### Making a Local Clone

    1. Log in to GitHub and locate the [Project-Management-Dashboard---MS2 GitHub Repository](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice)
    2. On the right of the file listings box, click the "Code" button.
    3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
    4. Open Git Bash
    5. Change the current working directory to the location where you want the cloned directory to be made.
    6. Type `git clone`, and then paste the URL you copied in Step 3.

    ```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    ```

    7. Press Enter. Your local clone will be created.

    ```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    > Cloning into `CI-Clone`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
    ```

    Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

<a name="CREDS"></a>
# Credits
## Code Credits
-   RegEx input patterns from W3Schools - https://www.w3schools.com/tags/att_input_pattern.asp
-   Avatar Icons made by [Flaticon](https://www.flaticon.com/)
-   MongoDB queries in def profile(username) from Code Institute, Backend Development, Mini Project lesson
-   The localStorage check code in script.js is from [MDN - Using_the_Web_Storage_API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API). This code checks to make sure that the browser can support localStorage and has it turned on. Find code use indicated by "CODE REUSE - localStorage Check "


## Content

-   All content was written by the developer.

## Media

-   All Images were created by the developer.

## Acknowledgements
-   N/A