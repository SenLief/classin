# Usage

## Require

- Python>=3.4

## Install

- pip install -r requirements.txt

## Debug

- export FLASK_APP=lesson
- export FLASK_ENV=development
- flask run

## Run

- waitress-serve --call 'lesson:create_app'

## Browser

- open "http://localhost:8080"
- input lessonkey
- download urls