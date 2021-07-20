# Project Achilles

This is a platform for Veterans to be able to come find resources, and connect with fellow Veterans.

## Frontend Repo

[front-end Repository](https://github.com/greggoldman11/project-achilles-client)

## Sites

### Backend Site

[Back-end Deployed Site](https://projectachilles.herokuapp.com)

### Frontend Site

[Front-end Deployed Site](https://greggoldman11.github.io/project-achilles-client/#/)

## Technologies used

-   JavaScript
-   React
-   CSS
-   Axios
-   Python
-   Django
-   PostgeSQL
-   Bootstrap

## Future Versions

Version 2 of this project will allow the user to like other resources, and they will also be able to search for a resource based on its category or name.

## Planning Strategy

I focused on building out the back end first and then worked on the front end.

## Wireframe

![Project Achilles ERD](https://user-images.githubusercontent.com/81181703/126388359-f0fd117f-0786-4433-aae9-ce8a1f476779.png)

## Routes
Verb | URI Pattern | Controller#Action
---- | ------------- | -------------
POST | /sign-up/ | users#signup
POST | /sign-in/ | users#signin
PATCH | /change-password/ | users#changepassword
DELETE | /sign-out/ | users#signout
GET | /resources/ | resources#index
POST | /resources/ | resources#create
GET | /resources/:pk/ | resources#show
PATCH | /resources/:pk/ | resources#update
DELETE | /resources/:pk/ | resources#delete
GET | /comments/ | comments#index
POST | /comments/ | comments#create
GET | /comments/:pk/ | comments#show
PATCH | /comments/:pk/ | comments#update
DELETE | /comments/:pk/ | comments#delete
