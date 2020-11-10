*Winner of TechTogether Boston 2020 Domain.com Contest

# What is Ambient?
As a member of a community, whether it’s a company, school, or local restaurant, you have a voice. Devices like TP-Link or Google Nest give you the autonomy to control your home temperature from your phone, but ambient allows entire communities to provide feedback on their temperature preferences. 

Ambient gives all employees and customers the right to work and spend quality time in a comfortable atmosphere. With respect to all the requests submitted, ambient will analyze and send the data to the thermostat administrator. The administrator does not have to worry what temperature to set to satisfy everyone; Ambient will do it for them. Join Ambient in helping us all ‘love the air around us’.

# Quick Facts
Technologies Used:
Front-End: Figma, Flask, Bootstrap, HTML/CSS, 
Back-End: AWS DynamoDB, SQLite, 
Other: Wolfram API, Google Cloud Compute Engine
Main Language: Python
BootStrap,html,css, Amazon Web service dynamo db for user database and sqlite for management database, google cloud compute engine to create vm instances and run our entire flask app in the cloud

# The Inspiration
This project came to life as an answer to the rhetorical question: why is it so cold in here? I worked in a large office building last year, and always came to work with a jacket. It would be 90 degrees in the summer, yet the AC was cranked down to what felt like subzero temperatures. I wasn’t the only one who felt this way. From conversations with friends, I learned that many others felt the same way: their offices/schools/place-of-work was too cold in the summer, and too hot in the winter. 


# How We Built “Ambient”
During TechTogether, our group brainstormed many approaches to solving this problem. We chose to implement it as an app that takes in mass data and calculates the optimal temperature change based on these individual preferences (which we quantified). It has three major components: (1) front end mobile app, designed in Figma, that shows what users see, and a Flask web app for greater control/features. (2) database that collects data from each user tap in the app, which would mean connecting the front end to the AmazonDB database. (3) backend that uses the data from the database to calculate the suggested ambient temperature increase/decrease using the Wolfram API in Python. Finally, we learned how to use the Google Cloud Compute Engine to create VM instances and run our entire Flask app in the cloud. We were able to complete part of each component, but we didn’t have enough time to learn how to connect each piece fully together. However, we learned a lot along the way ☺.

# Challenges, and What We Learned Along the Way!
The first challenge was determining what platform to use. Should we do a web app? A mobile app? We spent some time discussing what background we had and what we were willing to teach ourselves this weekend. Overall, every team member had to work with a language/environment that they had never tried before. Moreover, most of us have now used Figma for the first time!
The next challenge was figuring out how to calculate the optimal temperature change. We didn’t have an extensive statistics background to help figure out the best solution using standard deviations or types of averages, but eventually chose to solve our problem by minimizing the sums of squares by setting the derivative of our equation to 0. Once we wrote this down on paper, we then had to figure out how to actually make it work by coding. We realized that the Wolfram API was exactly what we needed! Our team members had to learn how to call the API, and figure out a way to get the right type of API which could solve for unknown variables! We ended up having to scrap the original code and start over multiple times.
Another major challenge was connecting our second and third components together. We chose to run our entire flask app in the cloud using the Google Cloud promotion. We had trouble getting the right packages installed, and had to communicate with a mentor for several hours to get the app to even run. 

# Our Vision (What We Wish We Could Have Accomplished)
“Ambient” has two types of accounts: users and administrators. Users can search for the building they’re located in and essentially, give “feedback” on their temperature preferences. Administrators have access to incoming feedback from users and can automatically adjust the ambient temperature based on group sentiment. Currently, the app requires the administrator to click a button in order to physically adjust the temperature. Our vision is that the app allow administrators to change the settings so that periodic temperature adjustments occur without manual interference. We also planned for specific functionalities such as a maximum temperature adjustment setting, minimum temperature adjustment setting, adjustable user control range, ability for administrators to remove their building from public search, etc. We foresee this being a valuable partnership between companies manufacturing smart thermostats (such as TP-Link, Google Nest, EcoBee, etc.) since our app could be integrated into their current operations.
Not only does this have far-reaching consequences as a community product, but it’ll be a valuable asset in fighting climate change. Many buildings use heating/cooling systems that operate above/below the desired threshold. With ambient’s product goal of actually OPTIMIZING comfort, we are unwittingly saving tremendously in energy costs and carbon emissions.

