# George Lychock - MS3 Project: uSpice
### Salem State University Fullstack Software Developer Certificate
#### Python Module
-   [View Live Dev Site](https://www.georgelychock-career.com/pages/_sandbox/MS3/index.html)

<hr>

<h1 align="center"><img src="_documentation/look-and-feel/montage-screenshot.png" /></h1>

## Table of Contents

- [Use Case](#UC)
    - [User Stories](#US)
    - [Requirements](#REQS)
- [UI/UX](#UXUI)
    - [UI](#UI)
        -   [Wireframes](#UIWF)
    - [UX - Design](#DES)
        -   [Wireframes](#UXWF)
- [Technical Background](#TECH)
- [Testing](TESTRM.md)
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
>-   The primary focus of this project is to display Python and database skills learned in the Python Essentials Module of the Salem State University / Code Institute Full Stack Software Developer Certificate Program.

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
-   Provide a method for the user to upload an image for their recipe
-   Monitor/regulate the number of recipes a user can upload per day (US8)
-   Show users the results of the search criteria (US2)
-   Allow users to view details about the recipe including an image (US3)
-   Allow users to rate a recipe (US7)
-   Allow users to view top 10 rated recipes
-   Provide users links to available spice vendors so the user can purchase recipe ingredients
-   Allow users to print a printable version of the recipe page
-   Create a pie chart showing the porportions of the recipe ingredients on the recipe page

# UX/UI
-   ## UI
    <a name="UI"></a>
    -   ### Wireframes
        <a name="UIWF"></a>
        -   UI Map (Site Map aligned to data structures and functions) - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Map.jpg)
    -   ### Sprints
        -   UI Sprint Map - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Sprints.jpg)


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
-   ## Sitemap, UI, and Data Structures
    -   UI Sitemap  - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Map.jpg)
    -   Sprints  - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/Site-UI-Sprints.jpg)
    -   Data Structures  - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/ui/uspice-data-structures.jpg)

-   ## Languages Used

    -   [HTML5](https://en.wikipedia.org/wiki/HTML5)
    -   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    -   [JavaScript](https://www.javascript.com/)

-   ## Frameworks, Libraries, & Programs Used

    1. [Bootstrap 4.6:](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
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
    8. [Toastr:](https://github.com/CodeSeven)
        - A notifications library recommended by my mentor Maranatha Ilesanmi.

-   ### Resources Used
    -   [jQuery: How do I test whether an element exists?](https://learn.jquery.com/using-jquery-core/faq/how-do-i-test-whether-an-element-exists/). Used this method to check if the project panel was already added to the dashboard.
    -   [MDN General Web Docs: ](https://developer.mozilla.org/) For semantic structure reference, arrays, localStorage, fetch.
    -   [W3Schools.com](https://www.w3schools.com/), For Color Picker, html/css/js general refernece, semantic structure reference, arrays, localStorage.
    -   [MDN - CSS Scrollbars](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Scrollbars)
    -   [How To Create a Custom Scrollbar (w3schools.com)](https://www.w3schools.com/howto/howto_css_custom_scrollbar.asp)
    -   [Numeric Inputs – A Comparison of Browser Defaults](https://css-tricks.com/numeric-inputs-a-comparison-of-browser-defaults/), to adjust presence of spinner controls in FF

-   ### APIs Used
    -   [GitHub API: ](https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api) The GitHub API code came from Code Institute, see Code Credits, but information was used from the GitHub link provided here.

#   Testing
<a name="BUGS"></a>
(link to testing.md)

# Product/Project Management
-   ## UI
    <a name="PROJ"></a>
    -   ### Projected Sprints
        <a name="UIWF"></a>
        -   UI Sprint Map - [View](https://github.com/GeorgeLychock/MS3-Project-Python-uSpice/blob/master/_documentation/wireframes/Site-UI-Sprints-.jpg)

<a name="DPLY"></a>
# Deployment
-   ## Hosting

    The project was deployed to GitHub Pages hosting service:

    [URL to GitHub Pages Site](https://github.com/GeorgeLychock/Project-Management-Dashboard---MS2)

    ### *CLOANING INFORMATION from CODE INSTITUTE README.md template from User Centric Module, edits have been made for changes in GH UI*
    GitHub Pages
    The project was deployed to GitHub Pages using the following steps...
    1. Log in to GitHub and locate the [Project-Management-Dashboard---MS2 GitHub Repository](https://github.com/GeorgeLychock/Project-Management-Dashboard---MS2)
    2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
    4. Under "Source", click the dropdown called "None" and select "Master Branch".
    5. The page will automatically refresh.
    6. Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.

    ### Forking the GitHub Repository

    1. Log in to GitHub and locate the [Project-Management-Dashboard---MS2 GitHub Repository](https://github.com/GeorgeLychock/Project-Management-Dashboard---MS2)
    2. At the top of the Repository (not top of page) on the far right, locate the "Fork" Button. Sign in if needed.
    3. You should now have a copy of the original repository in your GitHub account.

    ### Making a Local Clone

    1. Log in to GitHub and locate the [Project-Management-Dashboard---MS2 GitHub Repository](https://github.com/GeorgeLychock/Project-Management-Dashboard---MS2)
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
-   All Reused styles are in reused-styles.css
-   Scrollbar CSS Styling: from Digital Ocean: https://www.digitalocean.com/community/tutorials/css-scrollbars, in reused-styles.css

-   GitHub Widget Code from [Code Institute](https://codeinstitute.net/)
    -   This code originated from Code Institute's Interactive Frontend Development module for the Full Stack Software Developer course. Modifcations were mostly applied for struture and style.
    -   All JS code is in the github-information.js file.

-   The localStorage check code in script.js is from [MDN - Using_the_Web_Storage_API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API). This code checks to make sure that the browser can support localStorage and has it turned on. Find code use indicated by "CODE REUSE - localStorage Check "

-   Progress bars in the Project Panels came from Bootstrap Documentation: https://getbootstrap.com/docs/4.6/components/progress/:
    Find code use indicated by "CODE REUSE - Progress Bar"

-   Clear form
        Clearing loop reused from W3Schools.com: https://www.w3schools.com/js/tryit.asp?filename=tryjs_form_elements 
        
        var x = document.getElementById("projectFormModal");
        var i;
        for (i = 0; i < x.length ;i++) {
        x.elements[i].value = "";`
        }
-   Tooltips
    -   Used the CSS based tooltips code from W3Schools: https://www.w3schools.com/css/css_tooltip.asp
-   fetch
    -   Based on https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch, but customized 
-   timestamp conversion, customized to capture AM/PM to control weather background; from Convert UNIX Timestamp https://www.w3resource.com/javascript-exercises/javascript-date-exercise-17.php

## Content

-   All content was written by the developer.

## Media

-   All Images were created by the developer.

## Acknowledgements
-   N/A