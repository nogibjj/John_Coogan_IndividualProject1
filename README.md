[![Test workflow for Python template](https://github.com/johncoogan53/PythonDataScience/actions/workflows/pythonapp.yml/badge.svg?branch=dev&event=push)](https://github.com/johncoogan53/PythonDataScience/actions/workflows/pythonapp.yml)
### Test of a dynamic YAML badge:
![Dynamic YAML Badge](https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fgithub.com%2Fjohncoogan53%2FPythonDataScience%2Fblob%2Fmain%2F.github%2Fworkflows%2Fpythonapp.yml)

## This is a workflow for a python script which performs descriptive statistics on a csv file
### This project has the following dependencies:
* ruff linter
* pytest
* pandas
* black python formatter 
* (nbval is included in requirements for future implementation)
### This project uses a csv file located in the src directory called data.cvs to test functionality. Any .csv file can be inserted into the script or the jupyter notebook 
### This workflow will perform the following actions on any push to a branch in this repository:
* Establish a virtual environment for python3
* Install the dependencies listed above
* Lint the pushed code with ruff
* Format with black
* (a test has yet to be implemented)

### This is the front end of a potential CD pipeline which will quality control continuously developed code into a deployment environment. Future iterations will build on this baseline best practice and scale into projects of higher complexity.

