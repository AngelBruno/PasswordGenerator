# Generating the virtual environment 
    python3.12 -m venv --without-pip <virtual_machine_folder_name>

# Activating the virtual environment
    .\<folder_name>\Scripts\Activate.ps1

# If appears an error of UnauthorizedAcces
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned (Power Shell as ADMIN)

# Installing FLASK library 
    pip install Flask

# It's necessary to create a folder called 'static' and put the css and js in there so that they can be found
