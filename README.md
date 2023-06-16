## Project 5

# Madame Musette

The Project is deployed [here](https://madamemusette.herokuapp.com/) 

GitHub repository is [here](https://github.com/fitabigail/Madame-Musette) 

![I am responsive](/images_reademe/Iamresponsive.png)

## TABLE OF CONTENTS
- [Aim of the website](#aim-of-the-website)
- [Web Marketing](#web-marketing)
- [User Experience/User Interface](#user-experience-or-user-interface)
- [Agiles](#agiles)
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

> ## Web Marketing
</br>
Madame Musette is a B2C e-commerce application. Selling directly to consumers means that the site is designed to sell quickly, on impulse, to people who want to have more stylished shoes and accessories. While wholesale is a possible future goal, the website was not yet intended to sell to other businesses. For this reason, a large amount of the functionality is focused on the user experience and the ability to purchase products quickly and effectively.

</br>
<details>

### Marketing Strategy
</br>


**Social Media Marketing: Facebook**

As Madame Musette is a start-up business, the budget for marketing is limited. However, there are several ways that Madame Musette can market itself to help increase sales and brand awareness. Using Facebook to pump out content and drive traffic is the first and most straightforward. The use of paid ads allows the business to target specific demographics and increase brand awareness. The use of social media is also a great way to get feedback from customers and to help with customer service. There is an image of the Facebook page below and a link to the page.

- Facebook page link:  [MadameMusette Facebook here](https://www.facebook.com/profile.php?id=100091938860938)
    - Social page image:  <details>![madameMusette Facebook](/images_reademe/madameMusette_facebook.png)</details>
</br>

**Email Marketing**
The second method would then be sending regular news letters to the mailing list obtained via the signup form. The newsletter would contain links to special offers and new arrived products, and promotions. This would help with brand awareness building a community around the brand. The email template is for future implement. 
- Mailchimp Audience : <details>![madameMusette Mailchimp](/images_reademe/mailchimp-audience.png)</details>
</br>

**Google Adds**
The third  is the use of google ads which are a great way to increase brand awareness and help with SEO. The use of google ads can also help with the use of long-tail keywords and help with the ranking of the site.
</br>

**Media Influencers**
The final is the use of influencers. Influencers are a great way to increase brand awareness. Free samples could be sent to popular influencers on Instagram in exchange for a mention/hashtag/ link in the description. This further helps raise brand awareness because the posts could be posted on Facebook too and the influencer tagged in the post, which with the help of the Facebook algorithm, would help bring an organic audience to the Facebook page and the store.
</br></br>

### Search Engine Optimization
</br>
SEO research is key to driving traffic from a browser based search i.e. Google to the website. The keyword research has played a crucial role in incorporating words that users typically search for when seeking to purchase art online. To help improve the search engine ranking I ensured the site carries meta tags for a description and keywords which encapsulate the general content and focus of this B2C site.

**Keywords:**
<br>
Keywords are relevant to the e-commerce itself. A keyword strategy was involve selecting high-performing keywords that drive relevant traffic to business like shoes, pumps, sneakers, sales.

[wordtracker](https://www.wordtracker.com/)
</br></br>

**XML Sitemap**
</br>
Additionally to help the search engines crawl the website, I've added an XML sitemap file to the main root directory. The file was created using the free service through XML-Sitemaps.com. A sitemap is a way of organizing a website, identifying the URLs and the data under each section. Previously, the sitemaps were primarily geared for the users of the website. However, Google's XML format was designed for the search engines, allowing them to find the data faster and more efficiently.

A robots.txt file has also be included in the build to tell the search engine crawlers which URLs the crawler can access on this site. This is used mainly to avoid overloading the site with requests.

- [xml-sitemap](https://www.xml-sitemaps.com/)
</details>
</br></br>


> ## User Experience or User Interface
---
</br>

- Madame Musette was designed to be a friendly and informative site for users to easily browse and find products they would be interested in purchasing. The graphical elements and overall design of the site provide the user with a fun and enjoyable environment.
</br>

### Site Goals

- To provide the site owner with a place to sell his work.
- To provide users with an enjoyable and easy to use site for purchases.

### Site User

- Someone looking to purchase shoe or accessories
- Someone looking for customised products 
- As User I want to be able to visualize and navigate through the sections of the app
- As User I want to browse through the list of products
- As User I want to been able to add and remove products from my cart
- As User I want to been able to put my order through the site.
- As User I want to be able to complete a form for customised products
- As User I want to be able to check who is the designer of the product
- As User I want to subscribe to the store newletters 
- As User I want to contact the staff if I require help or clarification of a process
- As User I want to see the reviews of the products
- As Registered User I want to be able to leave a product review

### Registred/Unregistred User and Admin/Staff User
  </br> 
<details>

</br>

### Unregistered User
<br>

- As Unregistered User I want to see clear the purpose of the site when landing in it
- As Unregistered User, I want to be able to register so that I can create my account and access to the registered user features
- As a Unregistered User I want to see the detail information of the products
- As User I want to contact the staff if I require help or clarification of a process 
<br>

### Registered User
<br>

- As Registered User I want to keep my information saved so that in a next purchase for future purchases
- As Registered User I want to be able to update my information if needed
- As Registered User I want to have  access to customised form for personalized products    
- As Registered User I want to be able to leave a product review 
- As Registered User I want to keep a history of my orders
</br>

### Admin User
<br>

- As Admin/Staff User I want to access to a panel where I can manage the store's products database 
- As Admin/Staff  User I want to be able to manage the DB from the front-end 

<br>
</details>
</br></br>

> ## Agiles 
---
</br>
The plan for this project was carried out using the Agile Methodology in Github. User Stories were created using the issues on the git hub. Each user story explicitly explains the purpose of the issues. Each user story is segmented into acceptance criteria and tasks. It was prioritised using GitHub labels with different colors. The labels are should have, could have, must have and duplicate. Once the issues are created they are moved to the User Stories kanban board. The Kanban board has three main columns, To Do, In Progress and Done. Once you start working with the user story, you move it to the To Do column and when finished move it to the Done column. Following this pattern of work gives you a full-on idea about the progress of the project.</br></br>



### Epic

The epics were created using the milestones on github. Each epic was created and related issues were added to it.  
</br>
<details>

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

- Epic: Reviews and Likes  :

    - USER STORY: Add Review and Rating [[#39](https://github.com/fitabigail/Madame-Musette/issues/39)]
    - USER STORY: Delete a Review [[#37](https://github.com/fitabigail/Madame-Musette/issues/37)]    
    - USER STORY: Like and unlike [[#20](https://github.com/fitabigail/Madame-Musette/issues/20)]
      
</details>
 </br></br>


> ## Flowchart
</br>
Flowchart here:
<details>

![Flowchart](/images_reademe/flowchart.png)
</details>
</br></br>

> ## Design
---

</br>
I tried different color palettes while building the website and settled on a simple combination  gradient of gold.
Black and white are used for text color and contrast well with primary colors.
</br>

### **Navigation color scheme** 

<details>

![Navigation color](/images_reademe/design-nav-color.png)


</details>

### **Typography**

- I choose 'Open Sans' as the font for the site,  
- Navigatiobar 'Playfair'.


### **Wireframes** 
  
  <details> 

![Balsamic Wireframes](/images_reademe/wire-home-desk.png)  
![Balsamic Wireframes](/images_reademe/wire-home-mobile.png) 


</details>  

</details> 
</br></br>

> ## Features
---
</br>

### Existing Futures by Page
</br>
The list and screenshot about them can be found here:
<details>

## **Navbar**

From navigation bar the user can:
- return to home page by clicking logo,
- navigate trough diffrent categories,
- search for diffrent products,
- can access his profile,
- can register, login and logout,
- can see the number of items had on the cart,
- the admin/staff can access the product page to add product.

<details>

### Navbar Home page
![Home Page Navigation](/images_reademe/Navbar-home.png)
</br>

### Navbar Products
![Products Page Navigation](/images_reademe/Navbar-products.png)
</br>

### Full page search bar
![PFull page search bar](/images_reademe/search-home.png)
</br>

</details>

## **Messages**
<br>
This feature will be displayed for all the users, triggered by user's actions. It provides feedback to the users on the result of them.
<br>
<details>

![Messages](/images_reademe/messages.png)
</details>
<br>

## **Footer**
<br>
From Footer the user can:

- subscribe,
- access on Info menu the About Us page and Privacy Policy,
- check for social media,
- can contact the staff by contact form,
- can find the store location.

<br>
<details>

 ### Footer
![Footer](/images_reademe/footer.png)
</br>
<br>

### Subscribe form button footer
![Subscribe-Footer](/images_reademe/subscribe.png)
</br>
<br>

### Info menu footer
![Info-Menu-Footer](/images_reademe/info.png)
</br>
<br>

### Contact form footer
![Contact-us-Footer](/images_reademe/contact.png)


</details></br>

## **Landing Page**
<br>
On landing page the user can:

- navigate through diffrent sections to get easy access to diffent products.
<br>
<details>

## **Buttons to internal navigations from home page**

</br>

### Find your perfect shoes button

![INTERNAL-LINK-BTN](/images_reademe/find-btn.png)
</br>

### Discover button

![INTERNAL-LINK-BTN](/images_reademe/dicover-btn.png)
</br>

### Categories buttons
![INTERNAL-LINK-BTN](/images_reademe/categories-btn.png)
</br>
</br>

### Sales button
![INTERNAL-LINK-BTN](/images_reademe/sales-btn.png)
</details>
</br>


## **Products Page**
<br>
The products page is intuitive. The user can:
- search by subcategoies,
- fillter the products with fillter by,
- see the breadcrumbs,
- go home page by home icon,
- like a product,
- navigate to product details page,
- the admin/staff can edit/remove a product,
- and contains a pagination which allow only 16 products per page to display. 
<br>
<details>

### Products Page

![Products Page](/images_reademe/products-page.png)
</br>
<br>

### Admin Edit/Delete buttons

![!Admin Edit/Delete buttons](/images_reademe/edit-delete-product.png)
</br>

<br>

### Fillter subcategories

![Fillter subcategories](/images_reademe/sort-menu.png)
</br>

### Breadcrumbs
![Breadcrumbs](/images_reademe/breadcrumb.png)
</br>

### Likes button
![Likes button](/images_reademe/likes.png)
</br>

### Paginations
![Paginations](/images_reademe/paginations.png)

</details>
</br>

## **Products Details**

From product details page the user can: 
- add to cart the product and follow the steps an finish the order,
- can navigate to about page to see designer profile on Facebook, and Twitter,
- can request a customised product,
- can add a review,
- admin/staff can edit/delete product
<br>
<details>

### Product Details Page
</br>

![Product Details Page](/images_reademe/prodduct-details.png)
</br>

### Reviews
</br>

![Reviews](/images_reademe/review.png)
</br>

### ADD Review
</br>

![ADD Review](/images_reademe/add-review.png)
</br>

### Customise Product
</br>

![Customise Product](/images_reademe/product-custmform.png)
</br>

### Customise Product Form
</br>

![Customise Product Form](/images_reademe/preview.png)
</br>

### Customise product message
</br>

![Customise product message](/images_reademe/customise-message.png)
</br>

### Go to cart
</br>

![Go to cart](/images_reademe/pop-up-shopping-cart.png)
</br>

### Shopping Cart
</br>

![Cart](/images_reademe/shopping-cart.png)
</br>

### Order Checkout 
</br>

![Order Checkout](/images_reademe/order-check-out.png)
</br>

### Order Resume
</br>

![Order Resume](/images_reademe/order-resum.png)
</br>


### Dashboard and Order History
</br>

![Dashboard and Order History](/images_reademe/profile-page.png)
</br>

</details>
</br>



### About Us
</br>
On About page the user get informations about company, navigate to contact us button and can see designers profiles
<details>

![About Us](/images_reademe/about-us.png)
</details>
</br>

## **Customise Page**

Customise form gives to the user to preview the choices before submision. I use [django-formtool plugin](https://pypi.org/project/django-formtools/).

<details>

![Customise](/images_reademe/preview.png)
</details>

## **Subcribe with MailChimp**

Subscription form use service form [Mailchimp](https://mailchimp.com/)

<details>

![MailChimp](/images_reademe/subscribe.png)
![MailChimp](/images_reademe/mailchimp-confirm.png)
![MailChimp](/images_reademe/mailchimp-audience.png)
</details>

## **Product Manager**

The admin can add, update and delete a product from front-end.

<details>

![MailChimp](/images_reademe/product-manager.png)
![MailChimp](/images_reademe/update_with_image.png)

</details>
</details>
</br>


### Features to Implement in Future
</br>

As the time frame was affected by external factors out of my control, some of the 'could have' features had been left for future implementation.
However fields and some of the need elements for them had been set in place since the beginning, and are there for when can be done.
- A wishing list;
- Singup/Login with Facebook and Google : added but not functional yet;
- Forgot password need to be added;
- Customise Product now have an unique form for all products. For future will be two forms one for products which has size and one for the rest of products;
- For review section in future to be implement a review replay from the admin/staff;
- A service for renting specials designer products to be add;
- A page with Q&A and Term and Conditions of the business;
- On User Dashboard to be displayed all his request for customised products, and the reviews writen by him;
- Unregistred user to be allow to like a products and be counted;


</br>
</details>
</details>
</br></br>

> ## Database
---

</br></br>
For the data base had been used ElephantSQL, and the diagram is as below.
<details>

![DB Scheme](/images_reademe/DB-Scheme.png)
</details>
</br></br>

> ## Testing
---
</br>

##   Testing Strategy
</br>

### **Responsiveness**
<bt>

The site had been test for the following devices:

Mobile: 360 * 640 / 390 * 844 / 414 * 896

Tablet: 768 * 1024 / 820 * 1180 / 1366 * 768

Monitor: 1280 * 1024 / 1600 * 900 / 1950 & UP

The site had been test in Chrome seeming all according to the design. In Firefox. In Internet Explorer all seems to work as the design.
<br>

### **Manual Testing**

</br>

I utilised a manual testing strategy for the development of the site. Seperate to the functionality testing of the site, and the testing of the code, User Story tests were implemented to ensure that the criteria of the user stories listed above were met. 

<br>



<details>

 ## Top bar
<br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Logo| Land Home Page| Pass|
|Account icon| Land Register or Login Page| Pass|
|Cart Icon| Land Shopping Cart Page and show the cart item no| Pass|
|Logout| Log out the user| Pass|
|Search on mobile|Open search bar|Pass|
</br>

## Navbar
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Shoes|Display Subcategory| Pass|
|Handbags|Display Subcategory| Pass|
|Accessories|Display Subcategory| Pass|
|Special Offers|Display Subcategory Pass|
|Pumps|Show all Pumps|Pass|
|Sandals|Show all Sandals|Pass|
|Sneakers|Show all Sneakers|Pass|
|All Shoes|Show all Shoes|Pass|
|Shoulder Bags|Show all Shoulder Bags|Pass|
|Cluch&Evening Bags|Show all Cluch&Evening Bags|Pass|
|Backpacks|Show all Sneakers shoes|Pass|
|All Handbags|Show all Handbags|Pass|
|Belts|Show all Belts|Pass|
|Wallets|Show all Wallets|Pass|
|All Accessories|Show all Accessories|Pass|
|All Sales|Show all Sales|Pass|
|New Arrivals|Show all New Arrivals|Pass|
|All Special Offers|Show all Special Offers|Pass|
|Search icon|Open the search|Pass|



</br>

## Home
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Find your perfect shoes button|Land Product Page| Pass|
|Discover button|Shows New Arrivals Category| Pass|
|Pumps button|Shows Pumps Category| Pass|
|Bags button|Shows Bags Category| Pass|
|Accessories button|Shows Accessories Category| Pass|
|Buy now button|Shows Sales Category| Pass|
|Scroll up button| Scroll up the page | Pass|
</br>

## Footer
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Social links|Land social pages| Pass|
|Subscribe button|Pop up subscribe form| Pass|
|Subscribe form| Register the suscription | Pass|
|Info button|Drop menu| Pass|
|About nav| Land About page | Pass|
|Privacy Policy nav| Land Privacy Policy page | Pass|
|Contact Us button|Pop up contact form form| Pass|
|Contact Form|Register the Contact form| Pass|
|Location link| Open Google map on new page | Pass|

</br>

## Navbar Shop
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|All Categories|Drop down all categories by friendly name| Pass|
|Each Category from drop down menu|Show products by category| Pass|
|Categories Filters Bar| Display the Categories filters | Pass|
</br>

## Product page
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Home icon|Go back to home page| Pass|
|Categories Filters Bar| Display the Categories filters | Pass|
|Product Image|Land Product Detail pages| Pass|
|If Admin|
|Edit link|Land Edit Product page | Pass|
|Delete link| Delete Product | Pass|
|If Registred User|
|Like button|Register the Userlike and count| Pass|
|If Unregistred User|
|Like button|Can not like| Pass|


</br>

## Product Detail page
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Quantity|Increase and descrease the quantity| Pass|
|Add to cart button| Add product to shopping bag | Pass|
|Keep Shooping|Land Product pages| Pass|
|Designer name link|Land About pages| Pass|
|Add Review|Open add review form|Pass|
|Review Form| Add review and display on site and admin panel|Pass|
|Delete review| Remove teh review| Pass|
|If Admin|
|Edit link|Land Edit Product page | Pass|
|Delete link| Delete Product | Pass|
|If Registred User|
|Customise Product|Open the Customise product| Pass|
|If Unregistred User|
|Customised Product|Must go to login/singup| Pass|


## Shopping Cart
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Quantity|Increase and descrease the quantity| Pass|
|Update link|Update Quantity| Pass|
|Remove link|Remove the product from shopping cart| Pass|
|Secure Ckeckout|Land the Checkout Page| Pass|
|Keep Shopping| Land Productspage | Pass|


</br>

## Oder page
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|User fiels|Collect data about name, delivery address, and card| Pass|
|Create Account link|Open Sing-up page| Pass|
|Login|Open the Login Page| Pass|
|Adjust Cart|Return to shopping cart Page| Pass|
|Complete Order button| Land Order Complete page if all the required fieldswas corect completed | Pass|

</br>

## Oder page
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Order Details|Display Order Summary| Pass|
|Go To Your Profile|Open Use Profile  page| Pass|
|See Ours New Deals|Open the New Arrivals| Pass|

</br>

## User Profile page
</br>

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|User Details|Display USER Summary| Pass|
|Update button|Update Use Profile| Pass|
|Order history link| Display Order History|Fail|

## Customised Product

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Preview button|Display Summary if all required fiels was corect completed| Pass|
|Submit button|Submit the form| Pass|

## Product Management

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Add Product button|Add product if all required fiels was corect completed| Pass|
|Cancel button|Redirect to Products Page| Pass|

## Messages
<br>
The features will be displayed for all the users, as marked in features pag



| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
| Message in top right of screen| Floating message according to the user action| Pass|
<br>

Here images:
<details>

![message](/images_reademe/messages.png)
![message](/images_reademe/sing-up-confirm.png)
</details>
<br>

## Singup Page

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Sing Up button|Register the user if all required fiels was corect completed and send confirmation email| Pass|

Here images:
<details>

![confirm](/images_reademe/Confirm_email_registration.png)
![emailconfirm](/images_reademe/confirm_email_website_reg.png)
</details>
</br>

## Product Management

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Facebook button|Login/Singup with Facebook| Fail|
|Google button|Login/Singup with Google| Fail|
|Sing In| Log in user if correcte credentials| Pass|
|Go home button| Land Home page|Pass|
|Sing Up link| Go to Singup Page| Pass|


## Emails confirmations

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Registration Email|Send confirmation email link| Pass|
|Order  confirm email from gitpod |Show order details| Pass|
|Order  confirm email from heroku |Show order details| Fail|

<details>

![Emails](/images_reademe/emails.png)
![Email-registration](/images_reademe/Confirm_email_registration.png)

![Email-order-terminal](/images_reademe/confirm-order.png)
![Email-order-heroku](/images_reademe/email-order-heroku.png)

</details>
</br>

## User story test

## Register & Login and Logout

| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|User Account Registration|Create an user account| Pass|
|Login and Logout|Log in or out a user| Pass|
|Personalized Account Profile|Create personalised profile wich can be updadated| Pass|

</br>

## Viewing and Navigation


| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|See products|See a list of products| Pass|
|Product Details|See products details| Pass|
|Indentify Deals |Easy find deals by a click| Pass|
|Select a specific category|Could see products from only one category| Pass|
|See number of items on the cart|View number of item on cart| Pass|
 
</br>

## Sorting and Searching


| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Sort multiple categories|View products from multiple categories| Pass|
|Sort a category|Sort products from a category| Pass|
|Sorting Products |Sorting products by diffrent filters|Pass|
|Search products|Search for specific products| Pass|
|View the search results|View searched product| Pass|
 
</br>
 
## Purchasing and Checkout


| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Select quantity and size|Add quntity and size for product| Pass|
|Customise a product|Customize a product choice| Pass|
|Shopping Cart View |See the products on shopping cart|Pass|
|Update shopping cart |Update quantity or remove the products| Pass|
|Secure payments|Secure checkout| Pass|
|Payment information |Show payment informations|Pass|
|Order confirmation  |Confirm order| Pass|
|Order email confirmation|Confirm order email receive| Pass|
</br>
     
## Admin and Store Management


| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Add products|Add product from front end| Pass|
|Edit products|Update a product details| Pass|
|Delete products |Delete product from database|Pass|

</br>
 
## Contact and Social Links


| Feature   	| Expected Action   	| Result   	|
|---	|---	|---	|
|Contact form|Contact a staff by contact form| Pass|
|Social Media|Links to social media| Pass|
|Sing up for newsletter |Suscribe to newsletter|Pass|
|See creators team |Check details of designers|Pass|

</br>

</details>



</br></br>

### BUGS
</br>

### Fixed bugs

 - Profile icon dropdown did not fit on small screens - fixed with class = mx-5,
 - On deployment on Heroku, my project had over maximum allowed slug size (after compression) 500 MB to 579MB. This was reduce by adding a .slugignore file. 
 - On console the mailchimp subscribe gave me an error, fixed by moving the javascript code to bottom of the page,
 - The static files folder was not loading on heroku. Fixed by removing them from slugignor file, and all static media images was linked with AWS url,
 - The webhook was not working propely. I found two mistakes on my code one the stripe_elements.js did not have the right path, and the second the confirmation_emails folder was not on orders folder,

</br></br>

### Not Fixed bugs

</br>

- Product manager page ratings fields alow negative values,
- Like button is not allowing unregistred user to like, and no message allow him to know must be registred to like a product,
- A user can write more than one review per product,
- The profile drop down on mobile should moved to left for better view:
<details>

 ![Profile-DropMenu](/images_reademe/profile-drop.png),
</details>

- Login/singup with Facebook, Google buttons are not funtional, 
- The order confirmations email if is send from gitpod is showing the costs of product but send from heroku is not shows the values:
 <details>

![Email-order-terminal](/images_reademe/confirm-order.png)
![Email-order-heroku](/images_reademe/email-order-heroku.png)
</details>


</br></br>

> ## Validation
---

</br>
<details>

## **Python**

All the files with .py extension had been validate with CI pep8  for each app had pass by the validation. Mostly came out clean but some trail lines and minor issues that were left be solve on future as do not afect the code. Below an example of the results.
<br>

![Python](/images_reademe/python-valid.png)

## **HTML**

### **PAGES**
<br>

**Validation for Landing Page**
<br>
The validation for this page hava errors flags referent to the duplicate attribute, which is nesting inside the contact form.py, and will be on all pagesas the contact form is on footer. No solution found.
<br>

![Home](/images_reademe/home-html-validator.png)

**Validation for Products Page**
<br>

<br>

![](/images_reademe/products-html-validator.png)


**Validation for Products Detail Page**
<br>
Products Detail has error of stray end tag for form and div which I corrected, but unforunely still appears. No solution found.
<br>

![](/images_reademe/prod-details-validator.png)

**Validation for Cart, Order, Add Reviews pages**
<br>
They has error of duplicate id. No solution found.
<br>

![](/images_reademe/shopping-cart-valid.png)
![](/images_reademe/order-html-valid.png)
![](/images_reademe/add-review-valid.png)
![](/images_reademe/about-validator.png)

**Validation for User Profile page**
<br>
Have only warrnings and eror duplicate class find on footer.
<br>

![](/images_reademe/user-profile-valid.png)


## **CSS**

All the files with .css extension had been validate with W3C Validator, the files for each app had pass by the validation and come clean.

</br>

![](/images_reademe/css-valid.png)
![](/images_reademe/css-profile-valid.png)
![](/images_reademe/css-order-valid.png)

</br>

## **Js**

All the files with .js extension had been validate with JsHint, the files for each app had pass by the validation in a first instance. Below an example of the results.
<br>

![](/images_reademe/js-valid.png)

</br>
</details>
</br></br>


> ## LightHouse
----
</br>
The Light score is low. In the absence of the necessary time to fix the errors, I decided to leave them for future work.
<details>

**Landing Page - Mobile**

![](/images_reademe/home-mobile.png)
<br>

**Landing Page - Desktop**

![](/images_reademe/desk-home.png)

<br>

**Products Page - Mobile**

![](/images_reademe/mobile-products.png)
<br>

**Products Page - Desktop**

![](/images_reademe/products-desk.png)

<br>

**Product Detail Page - Mobile**

![](/images_reademe/prod-detai-mob.png)
<br>

**Product Detail Page - Desktop**

![](/images_reademe/product-detil-desk.png)

<br>

**Abot Page - Mobile**

![](/images_reademe/about-mob.png)
<br>

**About Page - Desktop**

![](/images_reademe/about-desk.png)

<br>

**Customise Page - Mobile**

![](/images_reademe/custom-mob.png)
<br>

**Customise Page - Desktop**

![](/images_reademe/custom-desk.png)

<br>

</details>


</br></br>

> ## Technologies Used
----
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

- [CKEDITOR](https://pypi.org/project/django-ckeditor/) 

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
- [Stripes](https://stripe.com/) - to implement card payments
- [Lucid](https://lucid.app/) was used to create wireframes for this project.
- [Allauth](https://django-allauth.readthedocs.io/)
- [DjangoCrispyForms](https://django-cryptography.readthedocs.io/)
- [Cloudinary Media](https://cloudinary.com/) 
- [DjangoFormtools](https://pypi.org/project/django-formtools/)
</br></br>

</details>
</br></br>



> ## Deployment Host
---
</br>
This project was use Heroku service for deployment. [Heroku](https://id.heroku.com/login)

The folowing steps have to be done:
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

### Database ElephantSql

 Follow the next steps to install database:
- In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to your external database.Type on terminal : pip3 install dj_database_url==0.5.0 psycopg2
- Update your requirements.txt file with the newly installed packages: pip freeze > requirements.txt
- In your settings.py file, import dj_database_url underneath the import for os:
 import os
 import dj_database_url

- Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL in the position indicated:

 # DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }
     
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
    
 -DO NOT commit this file with your database string in the code, this is temporary so that we can connect to the new database and make migrations. We will remove it in a moment.

- In the terminal, run the showmigrations command to confirm you are connected to the external database:  python3 manage.py showmigrations
- If you are, you should see a list of all migrations, but none of them are checked off
- a terminal showing migrations that have not been applied
- Migrate your database models to your new database:  python3 manage.py migrate
- Load in the fixtures. Please note the order is very important here. We need to load categories first:  python3 manage.py loaddata categories. Then products, as the products require a category to be set:  python3 manage.py loaddata products
- Create a superuser for your new database:  python3 manage.py createsuperuser
- Follow the steps to create a your superuser username and password. The email address can be left blank.
- On the ElephantSQL page for your database, in the left side navigation, select “BROWSER”
- Click the Table queries button, select auth_user
- When you click “Execute”, you should see your newly created superuser details displayed. This confirms your tables have been created and you can add data to your database


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
---

</br>
For this project, I have seen and read many tutorials from where I had tried to get some understading of the logic more than copy the code itself, but still could not avoid in certain cases taken code and adapt it to the project and its necessities.

 - Boutque Ado - basic framework, shopping cart and checkout apps with some twists to fit better the project,
 - [Musette](https://musette.ro/) - inspiration for layout , and products description,
 - [Pexel](https://www.pexels.com/) - images,
 - [Unsplash](https://unsplash.com/) - images,
 - [Social Footer](https://mdbootstrap.com/docs/standard/extended/social-media-icons-footer/) - code copied from mdbootstrap,
 - [BugBytes](https://www.youtube.com/watch?v=d5YlrHe0uzw) - for customise form,
 - [Stack Overflow](https://stackoverflow.com) - finding answers to specific questions,
 - [Udemy](https://www.udemy.com/course/django-course/learn/lecture/34829606#overview) - for like function.

</br></br>
 > ## Acknowledgement

 Finally to my mentor Ronan McClelland , thanks so much for all your guidance and support through not just this project but all the course.