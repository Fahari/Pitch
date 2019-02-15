## Impress me
### Impress me is a web application that gives users the chance to post their first minute impressions under various categories. Be it pickuplines all the way to funny first time lines.
#### 13 February 2019
#### By **Kironji Kevin**

## Description
Impress me is simple in the form that you post what you feel you would have said in the scenario of being in a situation for the first time. Take for example you met a beautiful guy/lady while you were out minding your business, what would you say to him/her as a first impression? or you met your boss in the hallway,what would you say to him/her?

### User Stories
1. As a user, I would like to see the pitches other people have posted.
2. As a user, I would like to be signed in for me to leave a comment
3. As a user, I would like to receive a welcoming email once I sign up.
4. As a user, I would like to view the pitches I have created in my profile page.
5. As a user, I would like to comment on the different pitches and leave feedback.
6. As a user, I would like to submit a pitch in any category.
7. As a user, I would like to view the different categories.

### Front-end/User Interface Logic Objectives
* By default the page will load and provide three categories and a sign up option.
1. Home or landing page
2. Pickuplines, category for viewing and posting pickuplines
3. Funny, category for viewing and posting funny lines
4. Cheesy, category for viewing and posting cheesy and sneaky lines


### Behaviour-Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View Home |  | Loads the home page. |
|  Home | Click on a Category | Loads pitches for that category |
| Pickuplines | Click for Pickuplines category | Pickuplines pitches loads |
| Funny | Click for Funny category | Funny pitches loads |
| Cheesy | Click for cheesy category | cheesy pitches loads |


## Technologies Used
1. Python 3.6
2. HTML and CSS
3. Flask
4. Postgres
5. Heroku for deployment

## Application link
click [here](https://impress-me.herokuapp.com/)

## Set up and Installation

To access this application on your command line, you need to clone it.
`git clone https://github.com/Fahari/Pitch.git`

### Prerequisites
A user will require git, flask, postgresql and python3.6+ installed in their machine.
To install these two, you can use the following commands
```
#git
$ sudo apt install git-all

#python3.6
$ sudo apt-get install python3.6.

#flask
$ pip install flask

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```
## Known bugs
No known bugs as at the completion of the project.

## Support and contact details
Feel free to reach me at karonjekevin67@gmail.com

### License
The project is under the [MIT](https://github.com/Fahari/Pitch/blob/master/LICENSE) licence
Copyright (c) 2019 **Kironji Kevin**
