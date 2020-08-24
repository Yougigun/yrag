# YRAG aims to build up Machine-Learning Web-API easily!

## Install :
pip install yrag


## Usage:
### First :
Create a folder named <b>models</b>

### Seconde : 
In models folder, 
Create function named <b>model_[your-model-name]</b> 
in <b>model_[your-model-name].py</b> 

### Third : 
yrag build

### Forth <Requirement: Docker> :
yrag run   
<br/>

## Package included: 
### Data Science package
- numpy            -      1.18.4
- pandas           -     1.0.3
- scipy            -      1.4.1
- scikit-learn     -      0.23.0
- tensorflow       -      2.2.0
- torch            -      1.4.0+cpu
- transformers     -      2.9.1

### Database package
- pymssql          -      2.1.4
- PyMySQL          -      0.9.3
- redis            -      3.5.2
- requests         -      2.23.0


## Note
- Build package : python setup.py sdist bdist_wheel
- Upload package : python -m twine upload dist/*   
