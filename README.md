# cturtles3-portfolio
This explains how to install Flask in a virtual testing environment and create a simple Flask application only on on Linux and MacOS.

### Prereq: **Make sure you have python3 and pip installed**

## Installation

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
Finally Copy and paste the address it’s running on into the browser to see the project running

### About the Website:
Get to know our MLH Fellows by clicking on any one of icons to show what we're made of!
