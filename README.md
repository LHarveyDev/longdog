![Am I Responsive](media/screengrabs/amiresponsive.jpg)
# Longdog
Longdog is my submission for Milestone Project 4.Longdog is an e-commerce site dedicated to the needs of Sighthound owners and their dogs. The site will sell clothing, toys and accessories, in fact anything a Longdog might require!
The basic features of browsing the content and making a purchase can be carried out without registering, however the user is encouraged to register in order to make future ordering simpler and they will also be able to contribute to the site by leaving feedback in the form of product reviews.

## Table Of Contents:
1. [Design & Planning](#design-&-planning)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)
    
2. [Features](#features)
    * [Navigation](#Navigation-bar)
    * [Home page](#home-page)
    * [About Us page](#about-page)
    * [Products page](#products-page)
    * [Bag page](#bag-page)
    * [Checkout page](#checkout-page)
    * [Profile page](#profile-page)
   
   

3. [Technologies Used](#technologies-used)
4. [Libraries](#libraries-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgment](#acknowledgment)

## Design & Planning:

### User Stories
- #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the purpose of the site and be able to navigate to the areas I want to use.
    2. As a First Time Visitor, I want to learn about the company and its values.
    3. As a First Time Visitor, I want to be able to view the products on offer.
    4. As a First Time Visitor, I want to be able to assess the quality and prices of the products on offer.
    5. As a First Time Visitor, I want to register.
    6. As a First Time Visitor, I want to add an item to my basket.
    7. As a First Time Visitor, I want to view/amend/delete the contents of my basket.
    8. As a First Time Visitor, I want to checkout my basket.

- #### Returning Visitor Goals

    1. As a Returning Visitor, I want to log in and view my profile and past purchases.
    2. As a Returning Visitor, I want to make a new or repeat purchase.

- #### Frequent Visitor Goals

    1. As a Frequent Visitor, I want to log in and view my profile and past purchases.
    2. As a Frequent Visitor, I want to make a new or repeat purchase.

### Wireframes
  - Home Page Wireframe - [View](media/wireframes/home.png)
  - About Us Page Wireframe - [View](media/wireframes/about_us.png)
  - Products Page Wireframe - [View](media/wireframes/products.png)
  - Product Detail Page Wireframe - [View](media/wireframes/product_detail.png)
  - FAQs Page Wireframe - [View](media/wireframes/faqs.png)
  - Bag Page Wireframe - [View](media/wireframes/bag.png)
  - Checkout Page Wireframe - [View](media/wireframes/checkout.png)
  - Profile Page Wireframe - [View](media/wireframes/profile.png)

### Typography
The font I have used for the majority of my site is Patrick Hand SC from [Google Fonts](https://fonts.google.com/specimen/Patrick+Hand+SC). I choose this font because it has an informal, handwritten style whilst still being easy to read.
### Colour Scheme
I have stuck to a very simplistic black and white colour scheme. The pops of colour come from the products and the hero images on the Home, About Us and FAQs pages. The site could easily be adapted in the future to reflect a specific branding but I like the elegant, uncluttered feel it has currently.
### DataBase Diagram
Image of the database diagram for your project

## Features:
- ### Top Header
  The top of my site has the Longdog brand name top left. The search bar is situated in the middle of the screen in a prominent position. The 'My Account' and 'Shopping bag' icons are in the top right corner. This layout will be familiar to most users of e-commerce sites and will allow them to navigate the site intuitively.
  
  ![Nav bar mobile](media/screengrabs/top_header.jpg)
- ### Navigation Bar    
  I used Bootstrap to build my navigation bar, it collapses down on mobile screens and becomes a burger menu. The options available are HOME/ABOUT US/CLOTHING/HOMEWARE/FAQS

  ![Nav bar mobile](media/screengrabs/navbar_mobile.jpg)    
  On desktop the user has the same options apart from Home as the Longdog logo at top left will return users to the home page

  ![Nav bar desktop](media/screengrabs/navbar_desktop.jpg)    

  I chose to keep the search option available to non-registered users as I wanted first-time visitors to be able to explore the site and its products before committing to registering.    


  - ### Home Page    
  ![Home page](/documentation/uxhome_mobile.jpg)    
  The home page is simple and directs visitors towards either the search function in the nav bar or the invitation to join the Kitchen Cupboard community. The wording used aims to be friendly, welcoming and informal.    
  The use of the tablecloth image for the background creates uniformity within the pages of the site but also allows the content to be the focus.    
  The font used for the heading conjures up the 1950's feel that I wanted for the site, I chose "Pacifico" from google fonts.    
  The social media links are in the footer but they are very much in the background should people wish to find them rather than the focal point.


  - ### Search Page    
  ![Search page](/documentation/uxsearch_mobile.jpg)  
  The search page is probably the first place that new visitors will navigate to. There is no need to be registered so I anticipate they will explore whether the site is for them by using the search feature first.    
  Users can search by keyword. I chose this option as I feel it is quick and simple. I did consider having dropdown menus to select Difficulty Level and Cuisine but I abandoned this as it over-complicated things and made the interface cluttered especially on mobiles. I think it would be more useful to add this as an option to filter the results once a keyword search has been performed.    
  The keyword search interrogates two fields in my database, the name and ingredients. This picks up any recipe that uses the keyword as an ingredient within it, even though it may not be specifically mentioned in the title. There is a minimum length required of 3 characters. If the user tries to perform a search without entering a search term a pop-up informs them that it is a required field. 
  The search results are returned and displayed using Materialize's card component. The class rule dictates that the results are displayed 4 side-by-side on desktops, 2 side-by-side on tablets and stacked singly on mobiles.  
    
  ![Mobile view](/documentation/uxresults_mobile.jpg)
  
  ![Tablet view](/documentation/uxresults_ipad.jpg)   
  
  ![Desktop view](/documentation/uxresults_desktop.jpg)  

  The results cards display the recipe image, name and difficulty level not the full details. This should be enough for the user to decide whether they would like to read further and the image and title are a link that will then open the individual recipe up in a modal.    
  Originally the recipes opened up full-screen in a separate page and then the user had to navigate back to the results by clicking a 'Back to results' link. I changed this to the full recipe details opening in a Materialize pop-up modal. This modal window can be dismissed by clicking the 'close' button in the footer or clicking outside of the modal on the results screen behind. I feel this gives a better user experience and helps to eliminate the user navigating backwards using the browser back button.        
  Once open, the full recipe details are then displayed - Image, name, difficulty level, ingredients, method and created by. As users are also allowed to upload their own recipes some of the fields may have been ommitted and these will not then be displayed, if there has been no image uploaded a placeholder image will be displayed instead to preserve the uniformity of the display style.


  - ### Recipe Details Modal   
  ![Desktop view](/documentation/uxdetail_desktop.jpg)    
  The individual recipe modal window details the ingredients and method in full. The styling is aligned with the rest of the site and utilises soft pastel colours and the Pacifico font for its headings. If the content is larger than the window a scroll bar appears on the right-hand side. The modal has been designed with a mobile first approach in mind.         
  If the user has not supplied an image url when they added their recipe then the placeholder image will be displayed.    
  Once the user has finished with the individual recipe they can use the 'close' button in the footer of the modal to return to their search results or alternatively just click outside of the modal.     


  - ### Register Page    
  ![Register page](/documentation/uxregister_mobile.jpg)  
  The register page has a simple layout where the user is presented with a form to fill in consisting of two fields, username and password. The placeholder text explains that the chosen username must contain at least five characters.    
  The form is based on the code from the Code Institute non-relational mini project. I really liked the idea of the input fields changing colour from red to green once a valid username and password have been selected. If an invalid word is chosen a pop-up prompt reminds the user of the minimum character rule. I have used font awesome icons to illustrate what the fields are for.    
  The text under the form provides a link to 'Sign In' for registered users who might have found themselves in the wrong place.    
  The form looks just as good on mobile devices with all information visible without having to scroll down.


  - ### Sign In Page    
  ![Sign in page](/documentation/uxsignin_mobile.jpg)  
  The sign in page repeats the layout and features of the 'Register' page, this keeps the site looking uniform. If an incorrect username is entered a flash message is displayed 'Not yet registered' and the user is redirected to the 'Register' page. If an incorrect password is used a flash message 'Incorrect password and/or username' is displayed. This message does not specify if it was the username or password that was incorrect to avoid malicious attempts to guess the password based a correct username. Extra layers of security and complexity could be added dependent on how the site evolves and the user data it contains. I have used Werkzeug for password hashing to protect registered users data.    
  The text under the form provides a link to 'Register' for new users who might have found themselves in the wrong place.    
  The form looks just as good on mobile devices with all information visible without having to scroll down.


  - ### Profile Page    
  ![Profile page](/documentation/uxprofile_mobile.jpg)  
  The signed in user is automatically re-directed to their profile page where they are greeted by a welcome message. The profile page contains the dashboard which displays their own recipes and offers the ability to edit or delete their own recipes if desired. Once signed in the 'Add Recipe' option is displayed in the navigation bar.


  - ### Add Recipe Page    
  ![Add recipe page](/documentation/uxaddrecipe_mobile.jpg)    
  This page allows the registered user to add their own recipes which will then be searchable by other users. The form follows the format of the other forms on the site for uniformity and brand identity. A text box explains the purpose of the form and then there are input fields for image, name, ingredients and method followed by a submit button.    
  The recipe image field allows for a user to input an image url. There is a pop-up help box directing users to a free image hosting site called ImgBB which they can use without registering first. The uploading of an image url is optional and if no image is provided a placeholder image will be displayed in its place. In future versions of the site I would like to enable image uploads but this is beyond the scope of this project.   
  The recipe name field is restricted in length to 50 characters which should be ample, this accomodates up to three lines of text.
  The ingredients input field contains placeholder text asking the user to list each ingredient on a separate line. This is because I have written code that will split each line and store it in an array. When the recipe is called back up from the database the individual items in the array are then displayed as a list. The Materialize text-area class has been applied, this enables the size of the input box to expand to the amount of content within it.    
  The method input field contains placeholder text asking the user to list each step on a separate line. This is because I have written code that will split each line and store it in an array. When the recipe is called back up from the database the individual items in the array are then displayed as a list. The Materialize text-area class has been applied, this enables the size of the input box to expand to the amount of content within it.    
  The submit button posts the information to my Mongodb database.    


  - ### Edit Recipe Page    
  ![Edit recipe page](/documentation/uxeditrecipe_mobile.jpg)    
  The edit recipe page is only available to signed in users. The edit and delete buttons are only visible on your own recipes preventing access to other users material. This is where the current user can update the contents of their recipe including uploading a new image url if desired. The updated information is sent to the database and overwrites the original data except for where there is no change.    


  - ### CRUD    
  Within my site users have the ability to 
  * CREATE by adding their own recipes
  * READ by searching for recipes within the database
  * UPDATE by editing their own recipes
  * DELETE their own recipes    

## Technologies Used
1. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the [wireframes](#wireframes) during the design process
1. [dbdiagram:](https://dbdiagram.io)
   - dbdiagram was used to create the [database schema](/documentation/database_schema.png) during the design process
1. [Django:](https://www.djangoproject.com/)
   - Django was used to create the Python web framework.
1. [Djecrety:](https://djecrety.ir/)
   - Djecrety was used to create the Secret Key.
1. [Bootstrap:](https://getbootstrap.com/)
   - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [JQuery:](https://releases.jquery.com/)
   - jQuery was used in conjunction with Bootstrap to add interactivity.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
   - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
   - Google fonts were used to import the 'Patrick Hand SC' font into the style.css file which is used for my text throughout.
1. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Favicon.io:](https://favicon.io/)
   - Favicon.io was used to create the icon on the web page tab.
1. [I Love IMG:](https://www.iloveimg.com/resize-image)
   - I Love IMG was used to crop and resize all images to enhance performance and increase Lighthouse scores during testing.
1. [Gitpod](https://gitpod.io)
   - Gitpod was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
   - GitHub was used to store the projects code after being pushed from Git.
1. [AWS:](https://aws.amazon.com/)
   - AWS was used to store my statis and media images.
1. [ElephantSQL:](https://elephantsql.com/)
   - Elephant SQL was used as my PostgreSQL database.
1. [Heroku:](https://heroku.com/)
   - Heroku was used to deploy my project.
## Testing
Important part of your README!!!
### Google's Lighthouse Performance
Screenshots of certain pages and scores (mobile and desktop)
### Browser Compatibility
I have tested compatibility on the following browsers. Safari, Chrome, Edge and Firefox.
### Responsiveness
Responsive on all device sizes - This was checked using [Am I Responsive](https://ui.dev/amiresponsive) and by asking friends and family to test it on their devices. The devices checked included Samsung Galaxy, iPhone 8 and 10, iPad Air, Chromebook, Laptop and PC.
### Code Validation
Validate your code HTML, CSS, JS & Python - display screenshots
### Manual Testing user stories
Test all your user stories, you an create table 
User Story |  Test | Pass
--- | --- | :---:
paste here you user story | what is visible to the user and what action they should perform | &check;
- attach screenshot
### Manual Testing features
Test all your features, you can use the same approach 
| Status | feature
|:-------:|:--------|
| &check; | description
- attach screenshot
## Bugs
List of bugs and how did you fix them, you can create simple table
| Bug | Fix
|:-------:|:--------|
|   |    |
## Deployment
This website is deployed to Heroku from a GitHub repository, the following steps were taken:

#### Creating Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository from template**.
- Once the repository was created, I clicked the green **gitpod** button to create a workspace in gitpod so that I could write the code for the site.
  
#### Making a Local Clone
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/LHarveyDev/longdog)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/LHarveyDev/longdog
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/LHarveyDev/longdog
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

#### Forking the Github Repository 
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/LHarveyDev/longdog.git)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

#### Creating an app on Heroku
- After creating the repository on GitHub, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Deploying to Heroku.
- In GitPod CLI, the root directory of the project, run: pip3 freeze --local > requirements.txt to create a requirements.txt file containing project dependencies.
- In the Gitpod project workspace root directory, create a new file called Procfile, with capital 'P'. Open the Procfile. - Inside the file, check that web: gunicorn freedog.wsgi:application has been added when creating the file Save the file.
- Push the 2 new files to the GitHub repository
- Login to Heroku, select Create new app, add the name for your app and choose your closest region.
- Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository and click 'connect'.
- Navigate to the settings tab, click reveal config vars and input the following:


| Key | Value
|:-------:|:--------|
| DATABASE_URL  |    |
| IP  |    |
|  PORT |    |
|  SECRET_KEY   |     |

Actual Enviroment variables not disclosed for security
## Credits
### Code
- How to make card images the same size as each other [Stack Overflow](https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width)
- Resetting db in Django by Farheen Shahid[Scaler.com](https://www.scaler.com/topics/django/resetting-db-in-django/)
### Content
- Photo by <a href="https://unsplash.com/@sapegin?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Artem Sapegin</a> on <a href="https://unsplash.com/photos/short-coated-brown-dog-Ugg-EIfzy0c?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
- Photo by <a href="https://unsplash.com/@mitchorr?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Mitchell Orr</a> on <a href="https://unsplash.com/photos/brown-and-white-short-coated-dog-on-gray-rock-Cnqze55CDa8?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
Photo by <a href="https://unsplash.com/@sjung56?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">S J</a> on <a href="https://unsplash.com/photos/a-brown-and-white-dog-sitting-on-top-of-a-white-floor-508khDxcc5I?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
    
## Acknowledgments

- My Mentor Can Sucullu for continuous helpful feedback.
- Tutor support at Code Institute for their support.