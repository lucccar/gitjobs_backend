# Introduction 

This repo is a very simple interface for the (soon deprecated, RIP) Github jobs webpage. This is the backend of the application, therefor it depends on the githubjobs_frontend repo (link below). It was build using flask following a Data Access Object pattern and sqlite. 
The choice of sqlite and a simple file as db was for simplicity. So whoever decides run this project locally can do it without further configurations.

# How to run

## Dependencies

The user interface for this project is:
- [Github Jobs Frontend Repository](https://github.com/lucccar/gitjobs_frontend/) 

It also depends on a few python libraries that are listed in ``` src/requirements.txt```.


## Starting the app

To start the project:
``` flask run ```


## The API

This app has 2 routes. 

### /get_jobs/<string:location>/<string:description>
A get endpoint that receives queries the location and the description of the job and sends and html table as response.

### /record_search
A post endpoint that registers the search parameters used and logs it into the dqlite3 database.



## Further developments

1. Introduce unit testing for the route function and flask application itself.
2. Log the ip address of the user in the database.
3. Add docker.



