# NewsRead 

Application for reading, searching through and checking sources of online news articles. 

## Status 

Work in progress. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. 

### Prerequisites

```
Python: 3.12
```

```
Django: 5.0
```

### Installing


1. Clone the repository
```
git clone https://github.com/tomson611/NewsRead.git
```


2. Create your own virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements
```
pip install -r requirements.txt
```

4. Generate a new secret key

  You can use [Djecrety](https://djecrety.ir/) to quickly generate secure secret keys.


5. Make your migrations

In your terminal:
```
$ python manage.py makemigrations$ python manage.py migrate
```
6. Create a new superuser
```
python manage.py createsuperuser
```
7. Get a [NewsAPI](https://newsapi.org/) API key.
8. Create a local_settings.py file in the newsread directory.
9. Create an API_KEY variable and provide the key from step 7.
10. Run the dev server
```
python manage.py runserver
```
## Deployment

You can deploy on any hosting of your choice for example [PythonAnywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Requests](https://requests.readthedocs.io/en/latest/) - HTTP library for Python
* [NewsApi](https://newsapi.org) - News API is a simple, easy-to-use REST API that returns JSON search results for current and historic news articles published by over 80,000 worldwide 
  sources.


## Code of Conduct

[Code of Conduct](https://github.com/tomson611/NewsRead/blob/main/CODE_OF_CONDUCT.md)



## Authors

* **Tomasz Wesołowski** - *Initial work* - [tomson611](https://github.com/tomson611)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/tomson611/NewsRead/blob/main/LICENSE) file for details
