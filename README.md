# Star Wars 101

This is the backend for my Star Wars 101 project, an app meant for Star Wars newbies. It is paired with the starwars_frontend repo (https://github.com/alexiscait142/starwars_frontend_react).

This app is also fully deployed at:
https://starwars101mod4.herokuapp.com/
https://starwars101mod4.firebaseapp.com/


## Getting Started/Installing

Fork and clone this repo. This is a Django app so it will require the latest versions of Python and Django. As long as the below packages are installed, run the following command:

```
pipenv shell
```

to go into the virtual environment. Once in the directory with manage.py, run:

```
python manage.seed
```

to seed the database. Then you can run

```
python manage.py runserver
```

to start the server.


### Prerequisites

The required packages are:

```
django
```
```
django-rest-framework
```
```
django-rest-knox
```
```
requests
```
```
django-cors-headers
```
```
pip
```


## Resources

* [Star Wars API](https://swapi.co/) - data from the Star Wars universe

## Authors

* **Alexis Chilinski**

## Acknowledgments

* Flatiron School
