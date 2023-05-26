## Project 5

# Madame Musette

The Project is deployed [here](#) 

GitHub repository is [here](https://github.com/fitabigail/Madame-Musette) 

![I am responsive](#)

## TABLE OF CONTENTS
- [Aim of the website](#aim-of-the-website)
- [User Experience/User Interface](#user-experience-or-user-interface)
- [Web Marketing](#web-marketing)
- [Flowchart](#flowchart)
- [Design](#design)
- [Features](#features)
- [Database](#database)
- [Testing](#testing)
- [Validation](#validation)
- [LightHouse](#lighthouse)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment) 
- [Credits](#credits)
- [Acknowledgement](#acknowledgement)

</br></br>

> ## Aim of the website
---
</br>
Madame Musette is a fully functional E-Commerce store built in Django using Python, JavaScript, CSS, Bootstrap4, HTML and it incorporates stripe payments. The site includes  user authentication and Full CRUD functionality for products. 
Madame Musette is a website for selling ladies shoes and accessories. The user can quickly search for a specific categories, through the search bar on home page, or by more specific fields on the home and products page. 
This version has been built for project 5 of the Code Institute Diploma in Software Development and therefore doesn't accept real payments and any orders made won't be fulfilled.
  </br></br>


> ## User Experience or User Interface
---
</br>

- Madame Musette was designed to be a friendly and informative site for users to easily browse and find products they would be interested in purchasing. The graphical elements and overall design of the site provide the user with a fun and enjoyable environment.
</br>

### Site User

- Someone looking to purchase shoe or accessories
- Someone looking for customised products 

### Site Goals

- To provide the site owner with a place to sell his work.
- To provide users with an enjoyable and easy to use site for making purchases.


</br>


### Agiles 
The plan for this project was carried out using the Agile Methodology in Github. User Stories were created using the issues on the git hub. Each user story explicitly explains the purpose of the issues. Each user story is segmented into acceptance criteria and tasks. It was prioritised using GitHub labels with different colors. The labels are should have, could have, must have and duplicate. Once the issues are created they are moved to the User Stories kanban board. The Kanban board has three main columns, To Do, In Progress and Done. Once you start working with the user story, you move it to the To Do column and when finished move it to the Done column. Following this pattern of work gives you a full-on idea about the progress of the project.</br></br>



### Epic
</br></br>
The epics were created using the milestones on github. Each epic was created and related issues were added to it.  



- EPIC : Register & Login and Logout

    
    - USER STORY: User Account Registration[[#1](https://github.com/fitabigail/Madame-Musette/issues/1)]    
    - USER STORY: Login and Logout [[#2](https://github.com/fitabigail/Madame-Musette/issues/2)]
    - USER STORY: Password Recover [[#3](https://github.com/fitabigail/Madame-Musette/issues/3)]
    - USER STORY: Account Email Confirmation [[#4](https://github.com/fitabigail/Madame-Musette/issues/4)]
    - USER STORY: Personalized Account Profile [[#5](https://github.com/fitabigail/Madame-Musette/issues/5)]

    </br></br>

- EPIC : Viewing and Navigation

    
    - USER STORY: See products[[#6](https://github.com/fitabigail/Madame-Musette/issues/6)]    
    - USER STORY: Product Details [[#7](https://github.com/fitabigail/Madame-Musette/issues/7)]
    - USER STORY: Indentify Deals [[#11](https://github.com/fitabigail/Madame-Musette/issues/11)]
    - USER STORY: Select a specific category [[#33](https://github.com/fitabigail/Madame-Musette/issues/33)]
    - USER STORY: See number of items on the cart [[#34](https://github.com/fitabigail/Madame-Musette/issues/34)]

    </br></br>

- EPIC : Sorting and Searching
    
    - USER STORY: Sort multiple categories[[#14](https://github.com/fitabigail/Madame-Musette/issues/14)]    
    - USER STORY: Sort a category [[#13](https://github.com/fitabigail/Madame-Musette/issues/13)]
    - USER STORY: Sorting Products [[#12](https://github.com/fitabigail/Madame-Musette/issues/12)]
    - USER STORY: Search products [[#15](https://github.com/fitabigail/Madame-Musette/issues/15)]
    - USER STORY: View the search results [[#16](https://github.com/fitabigail/Madame-Musette/issues/16)]

    </br></br>

- EPIC : Purchasing and Checkout
    
    - USER STORY: Select quantity and size [[#23](https://github.com/fitabigail/Madame-Musette/issues/23)]
    - USER STORY: Customise a product [[#27](https://github.com/fitabigail/Madame-Musette/issues/27)]    
    - USER STORY: Shopping Cart View [[#24](https://github.com/fitabigail/Madame-Musette/issues/24)]
    - USER STORY: Update shopping cart [[#25](https://github.com/fitabigail/Madame-Musette/issues/25)]    
    - USER STORY: Secure payments [[#30](https://github.com/fitabigail/Madame-Musette/issues/30)]
    - USER STORY: Payment information [[#29](https://github.com/fitabigail/Madame-Musette/issues/29)]
    - USER STORY: Order confirmation [[#31](https://github.com/fitabigail/Madame-Musette/issues/31)]    
    - USER STORY: Order email confirmation [[#32](https://github.com/fitabigail/Madame-Musette/issues/32)]

    </br></br>

- EPIC : Admin and Store Management
    
    - USER STORY: Add products [[#8](https://github.com/fitabigail/Madame-Musette/issues/8)]
    - USER STORY: Edit products [[#9](https://github.com/fitabigail/Madame-Musette/issues/9)]    
    - USER STORY: Delete products [[#10](https://github.com/fitabigail/Madame-Musette/issues/10)]
   

    </br></br>

- EPIC : Contact and Social Links
    
    - USER STORY: Contact form [[#19](https://github.com/fitabigail/Madame-Musette/issues/19)]
    - USER STORY: Social Media [[#35](https://github.com/fitabigail/Madame-Musette/issues/35)]    
    - USER STORY: Sing up for newsletter [[#20](https://github.com/fitabigail/Madame-Musette/issues/20)]
    - USER STORY: See creators team [[#18](https://github.com/fitabigail/Madame-Musette/issues/18)]    
    
    </br></br>

> ## Web Marketing
</br>
Madame Musette is a B2C e-commerce application. Selling directly to consumers means that the site is designed to sell quickly, on impulse, to people who want to have more stylished shoes and accessories. While wholesale is a possible future goal, the website was not yet intended to sell to other businesses. For this reason, a large amount of the functionality is focused on the user experience and the ability to purchase products quickly and effectively.

</br>

Marketing Strategy
</br>
<details>
As Madame Musette is a start-up business, the budget for marketing is limited. However, there are several ways that Madame Musette can market itself to help increase sales and brand awareness. Using Facebook to pump out content and drive traffic is the first and most straightforward. The use of paid ads allows the business to target specific demographics and increase brand awareness. The use of social media is also a great way to get feedback from customers and to help with customer service. There is an image of the Facebook page below and a link to the page.

- Facebook page image: <details>![madameMusette Facebook](/images_reademe/madameMusette_facebook.png)</details>
- Social link:  [here](https://www.facebook.com/profile.php?id=100091938860938) 
</br>
The second method would then be sending regular news letters to the mailing list obtained via the signup form. The newsletter would contain links to special offers and new arrived products, and promotions. This would help with brand awareness building a community around the brand.
</br>
The third  is the use of google ads which are a great way to increase brand awareness and help with SEO. The use of google ads can also help with the use of long-tail keywords and help with the ranking of the site.
</br>
The final is the use of influencers. Influencers are a great way to increase brand awareness. Free samples could be sent to popular influencers on Instagram in exchange for a mention/hashtag/ link in the description. This further helps raise brand awareness because the posts could be posted on Facebook too and the influencer tagged in the post, which with the help of the Facebook algorithm, would help bring an organic audience to the Facebook page and the store.
</br></br>

### Search Engine Optimization
</br>
SEO research is key to driving traffic from a browser based search i.e. Google to the website. The keyword research has played a crucial role in incorporating words that users typically search for when seeking to purchase art online. To help improve the search engine ranking I ensured the site carries meta tags for a description and keywords which encapsulate the general content and focus of this B2C site.
</br></br>

###  XML Sitemap
</br>
Additionally to help the search engines crawl the website, I've added an XML sitemap file to the main root directory. The file was created using the free service through XML-Sitemaps.com. A sitemap is a way of organizing a website, identifying the URLs and the data under each section. Previously, the sitemaps were primarily geared for the users of the website. However, Google's XML format was designed for the search engines, allowing them to find the data faster and more efficiently.

A robots.txt file has also be included in the build to tell the search engine crawlers which URLs the crawler can access on this site. This is used mainly to avoid overloading the site with requests.

</details>
</br></br>

> ## Flowchart
</br>


> ## Design

<summary>Navigation color scheme</summary>
<details>

![Navigation](/images_reademe/design-nav-color.png)

</details>
</br></br>

> ## Features
</br></br>

> ## Database

</br></br>

> ## Testing
---
</br>

##   Testing Strategy
</br>
I utilised a manual testing strategy for the development of the site. Seperate to the functionality testing of the site, and the testing of the code, User Story tests were implemented to ensure that the criteria of the user stories listed above were met. 
</br>

</br>
<details>

 ## Top bar
<br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Logo| Land Home Page| Pass|
|Account icon| Land Register or Login Page| Pass|
|Cart Icon| Land Shopping Cart Page and show the cart item no| Pass|
|Dashboard| Land Dashboard page| Pass|
|Logout| Log out the user| Pass|
</br>

## Navbar
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Logo|Land Home page| Pass|
|Home|Land Home page| Pass|
|Cars|Land Cars page| Pass|
|Services|Land Services| Pass|
|Contact|Land Contact page|Pass|
|Search icon|Open the search bar| Pass|
</br>

## Home
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Caroussel Slide Arow|Swich to next image| Pass|
|Caroussel Button|Land Car page| Pass|
|Latest Cars Arow|Slick to next car| Pass|
|Lates Car Item|Land Car Details page| Pass|
|Sale label, Miles, Year, Transmission and Car Title|Land Car Details page| Pass|
|Team social accounts|Land Facebook and Twitter page| Pass|
|Questions button|Land Contact page|Pass|
|Scroll up button| Scroll up the page | Pass|
</br>

## Footer
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Social links|Land social pages| Pass|

</br>
</details>
</br></br>

## **BUGS**
</br>

### Fixed bugs
- - profile icon dropdown does not fit on screen - fixed with class = mx-5

</br></br>

### Not Fixed bugs
</br></br>

- Products Admin page search product field is not rendering the search
- Shopping cart is not display in line the quantity field on mobile view - fixed by changed the width to w-30
- Empty Shopping cart footer was not stick to bottom - fixed by adding on base.css container height : auto
- Empty products page footer is not sticky to bottom
- cart shop on xsmall screens the quantity button is not in line
- products detail page for no size products display problems
 
- footer buttons need media query between 992 and 770

> ## LightHouse
</br></br>


> ## Validation

</br></br>

> ## Technologies Used

<details>

### Languages

- [HTML](https://html.com/)

- [CSS](https://www.w3.org/Style/CSS/)

- [Python](https://www.python.org/)

- [JavaScript](https://www.javascript.com/)
</br></br>

## Frameworks and Libraries

- [Django](https://www.djangoproject.com/)
Documentation for [here](https://docs.djangoproject.com/en/4.1/intro/)

- [Summernote](https://summernote.org/) 

- [CKeditor](https://pypi.org/project/django-ckeditor/) - used for rich text editor

- [Jquery](https://jquery.com/) 

- [Boostrap](https://getbootstrap.com/)

- [Gunicorn](https://gunicorn.org/)

- [psycopg2](https://www.psycopg.org/docs/)
</br></br>

### Other Technologies

- [Gitpod](https://www.gitpod.io/) - as the IDE
- [Github](https://github.com/) - to store code in the repository
- [Heroku](https://www.heroku.com/) - to deploy on a cloud based platform
- [Google Fonts](https://fonts.google.com/)- for the fonts
- [Draw.io](https://app.diagrams.net/)- for flowchart and database
- [Fontawesome](https://fontawesome.com/) - for icons
- [Favicon](https://favicon.io/) - to create the favicon
- [W3C Markup Validation Service](https://validator.w3.org/) - to validate html
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - to validate css
- [PEP8](https://peps.python.org/pep-0008/) - to validate python code
- [CSS Gradient](https://cssgradient.io/) - for navbar gradient color
- [Conversion](https://www.xconvert.com/) - used to compress and convert the images from jpeg to webp
- [Stipes](https://stripe.com/) - to implement card payments
- [Balsamiq](https://www.balsamiq.com) was used to create wireframes for this project.

</br></br>

</details>
</br></br>



> ## Deployment
---
</br>
This project was use Heroku service for deployment. The folowing steps have to be done:
</br></br>

<details>

<ol>
<li>Log in Github.</li>
<li>Open the repo to deploy.</li>
<li>Log in Heroku.</li>
<li>Click in the "New" button in the top right.</li>
<li>Select "Create New App"</li>
<li>Give a name to the App and choose a region.</li>
<li>Click in "Create App" button.</li>
<li>Click in Settings.</li>
<li>Click in Reveal Config.</li>
<li>Add Vars Config (keys):</li>
<ol>
<li>Cloudinary (Media Storage)</li>
<li>DataBase Elephant (DataBase Host)</li>
<li>PORT 8000</li></ol>
<li>Django (Framework)</li>
<ol>
<li>Go to Deploy in the nav bar. In Deploment Method, select GitHub/Connect to GitHub.</li>
<li>In Connect to GitHub, write the repository name and click in search.</li>
<li>Once the route for the repo appears under the search, click in "Connect" button.</li>
<li>The deployment can be Manual or Automatic, select the one of your preference. Automatic has the advantage of updating your deployed site as you push the commit in GitHub.</li>
<li>Verify that "Branch to deploy" is master/main.</li>
<li>Click Deploy.</li>
</ol>
</ol>
</br></br>

### Opening the Repository 

1. Open your preferred IDE (VSCode, Atom, PyCharm, etc).
2. Navigate to the chosen directory where the Repository was Cloned/Extracted.
3. You will now have offline access to the contents of the project.

**Steps to use this repository**:

- Access to the repo in GitHub [here](https://github.com/fitabigail/Madame-Musette).
- It can be "Fork" following the steps [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo).
- It can be "Clone" following the steps [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository).

#### Forking
  
  
  1. Go to the Github page that hosts the repository you wish to fork.
  2. On the top-right of the page there is a button "Fork".
  3. Click this button.
  4. This creates a repository in your Github home page which is a copy of the original. You can submit and receive changes to the code by using pull requests 
  and/or syncing with the upstream repository.

### Cloning the Repository

1. Visit Hard Driver's [GitHub Repository](https://github.com/fitabigail/Madame-Musette).
2. Click the "Code" dropdown box above the repository's file explorer. 
3. Under the "Clone" heading, click the "HTTPS" sub-heading.
4. Click the clipboard icon, or manually copy the text presented: `https://github.com/fitabigail/Madame-Musette`
5. Open your preferred IDE (VSCode, Atom, PyCharm, etc).
6. Ensure your IDE has support for Git, or has the relevant Git extension.
7. Open the terminal, and create a directory where you would like the Repository to be stored.
8. Type `git clone` and paste the previously copied text (`https://github.com/fitabigail/Madame-Musette`) and press enter.
9. The Repository will then be cloned to your selected directory. 

### Manually Downloading the Repository

1. Visit Hard Driver's [GitHub Repository](https://github.com/fitabigail/Madame-Musette).
2. Click the "Code" dropdown box above the repository's file explorer. 
3. Click the "Download ZIP" option; this will download a copy of the selected branch's repository as a zip file.
4. Locate the ZIP file downloaded to your computer, and extract the ZIP to a designated folder which you would like the repository to be stored.


</details>
</br></br>

> ## Credits
 
 - [Social Footer](https://mdbootstrap.com/docs/standard/extended/social-media-icons-footer/) - code copied from mdbootstrap

 > ## Acknowledgement