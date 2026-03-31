# Homework 8: DevOPs, CD, CI

In this homework I created I put together a previously created pdb-dashboard with a Makefile and docker containers orchestration to add staging before releasing changes to the main dashboard.

## How to Run:
1. Pull or clone the repository 
2. Build the containers using 
```
make staging
```
and 
```
make compose
```
3. This will create images and containers based on the python modules in `requirements.txt` that will be installed via pip, and the docker-compose files 
4. The dashboard runs on `app.py`
5. Future changes to the program can be tested with pytest using
```
pytest test_app.py
```
6. Development can then be staged for further testing, and then added to the main dashboard
7. These final changes can then be pushed to github and will run through the added github actions, to make sure that the program's changes did not break major or important code
