# Hawksbills-portfolio
The portfolio website for Team Hawksbills of the C Turtles (Pod 3.3.0)!<br />
To view our website, please follow instructions under "Installation" below.

**Check it Out:** https://hawksbills.tech/

## Inspiration 🐢
The theme of our website is inspired by our pod name, the C Turtles. To reflect this, we implemented a swimming turtle on the home screen to greet users when they visit our page.

## What it does 🖥
The user-friendly interface introduces the members of our team, inviting users to get to know each member by clicking through the photos on the page. Each member has a profile page to showcase their personality,  interests, and recent projects.

## How we built it 🛠
To collaborate, we used:
 - Git
 - Discord

To design the website, we used:
 - Figma

To build the website, we used:
 - Flask as the framework
 - HTML for the structure
 - CSS and Bootstrap for the styling

## Challenges we ran into 😡
 - Using Flask, since our team had limited experience with it
 - Figuring out the quirks of CSS, and determining which tools and responsive layout patterns to use. Learning how to adopt a CSS framework was another challenge that we overcame.

## Accomplishments that we're proud of 🌟
 - The collaboration amongst the team. We had pair programming sessions to merge our code and debug together.
- Combining our different domains of knowledge and expertise to build a finished product. We were able to learn from each other and communicate effectively.
- Putting together a website in a short timeframe, despite our limited experience with Flask and web development
-  Familiarizing ourselves with Git and the Git workflow in order to apply its best practices

## What we learned ✏️
 - Flask
   - Routing
   - The Jinja templating system
   - How to pass in and use variables in our templates
 - Styling
    - Implementing a video hero section
    - Flexbox
    - Bootstrap
 - Git/GitHub
    - The importance and purpose of pull requests
    - How to use issues and project board to manage our project
    - Getting code reviews and feedback from our peers

## What's next for the Hawksbills Portfolio 🚀
 - Taking inspiration from what we learned while making this portfolio and implementing that in our future portfolios
 - Improving the responsiveness of the website


## Installation
Below explains how to install Flask in a virtual testing environment and create a simple Flask application only on on Linux and MacOS.
### Prereq: **Make sure you have python3 and pip installed**

## Step 1: Install Virtual Environment
Install virtualenv on MacOS
1. Open the terminal.
2. Install virtualenv on Mac using pip:

 ```
 sudo python2 -m pip install virtualenv
 ```
 
## Step 2: Create an Environment in Linux and MacOS
For Python 3: To create a virtual environment for Python 3, use the venv module and give it a name:

```
python3 -m venv <name of environment>
```

### Step 3: Activate the Environment
Activate the virtual environment before installing Flask. The name of the activated environment shows up in the CLI after activation.
Activate the virtual environment in Linux and MacOS with:
```
. <name of environment>/bin/activate
```
### Step 4: Install Flask
Install Flask within the activated environment using pip(Flask is installed automatically with all the dependencies.):
```
pip install Flask
```
Use the package manager pip to install all dependencies
```
pip install -r requirements.txt
```
### Step 5: Test the Development Environment
Create a .env file using the example.env template
Start flask development server
```$ export FLASK_ENV=development
$ flask run
```
Finally Copy and paste the address it’s running on into the browser to see our website.
