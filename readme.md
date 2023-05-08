<p>
 <h2 align="center">Student Teacher Portal</h2>
</p>

# Project Requirements

- Python & pip

# Setup

 Sr. No. | Contents                
---------|-------------------------| 
 1       | Python Setup            
 3       | Set virtual environment 
 4       | Migrate Tables          
 5       | Creating an admin user  

## Python and pip Setup

- [Install python](https://www.python.org/)
- Install pip

# Set virtual environment

Run this command in your project folder to create your virtual environment

```sh
python -m venv <path_for_venv>
```

To activate virtual environment
```sh
source <path_for_venv>/bin/activate
```
then run this command in your project terminal to install all dependancies using pip

```sh
pip install -r requirements.txt
```

# That's it, we're done!

```sh
python manage.py runserver
```