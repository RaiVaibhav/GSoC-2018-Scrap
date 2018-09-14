# Scrap GSoC 2018 data

Scrap all the data of GSoC 2018 projects and display on basis of
technology/languages used and no. of Completed Projects.
This is a initial code it will update in future

## How to run

- Create a postgres sql database.
- run `pip3 install -r requirements.txt`
- Run `python manage.py makemigrations` and `python manage.py migrate`.
- Run `python manage.py import_gsoc_data` command to populate the database.
- Finally run `python manage.py runserver` to get the content in template

Don't forgot to initially create a `virtualenv`

## Update
- Added the mutiple select for `Language/Technology` filter.
- Added initial Django-rest-framework view for the json data of Projects and
  Organization.
- If multiple `Language/Technology` selection doesn't give any organization list
  then it will show a list of organization that contain one of the selected
  `Language/Technology`.


Link to image:
![screenshot from 2018-08-28 03-22-42](https://user-images.githubusercontent.com/22278438/44688799-006e7500-aa73-11e8-8a59-9bfe714598f4.png)


![screenshot from 2018-08-28 03-23-23](https://user-images.githubusercontent.com/22278438/44688853-209e3400-aa73-11e8-8e34-160ef3597999.png)
