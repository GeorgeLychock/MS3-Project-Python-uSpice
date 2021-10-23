# George Lychock - MS3 Project: uSpice - Testing Documentation
### Salem State University Fullstack Software Developer Certificate
#### Backend Development Module

-   [View Live Dev Site](https://georgelychock.github.io/Project-Management-Dashboard---MS2/)

<hr>

<h1 align="center"><img src="_documentation/look-and-feel/montage-screenshot.png" /></h1>

## Table of Contents

-   [Usability](#TESTUSABILITY)
-   [Functionality](#TESTFUNCTIONALITY)
-   [User Stories](#TESTSTORIES)
-   [Validation](#TESTVALID)
-   [Compatibility](#TESTCOMP)

- [Bugs and Fixes](#BUGS)

# Testing
Used test writing guidelines from the following resources:
    [Guru99](https://www.guru99.com/complete-web-application-testing-checklist.html), [softwaretestinghelp.com](https://www.softwaretestinghelp.com/web-application-testing/)
-   NOTE: Usability and Functionality test criteria were written based on development version but then verified once deployed to GitHub Pages.
-   NOTE: All Validation results reported below are based on the deployed app via GitHub Pages.


<a name="BUGS"></a>
## Bugs / Fixes
### Known Bugs
#### OPEN 
-   Field Region does not display correctly on Recipe page
-   Field Flavor does not display correctly on Recipe page

#### FIXED
-   Library Buttons:
    -   A black box appears when a user clicks a library button (also occures in Delete Project modal). Need to adjust Bootstrap styles for buttons.
        -   FIX: Adjusted Bootstrap style for button:focus