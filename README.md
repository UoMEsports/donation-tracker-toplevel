# donation-tracker-toplevel

This is the top level of UoM Esports' fork of the PUWP's fork of the GamesDoneQuick donation tracker.

In order to deploy the tracker, some boilerplate code is neccessary for configuration and management. The goal of this repository is to make doing so as simple as possible for any given user to get started developing on the tracker.

## Getting a Working Copy of the Tracker

1. [Install Git](http://www.git-scm.com/download). I'm assuming if you're here, you know enough about git and version control to get started. You can check if you have git with the command `which git`, and which version you have with `git --version`.
2. [Install Python](https://www.python.org/downloads/). This version of the tracker requires Python 3.4+ and Django 2.0+.  You can determine if Python is installed with the command `which python`, and which version of Python you have with the command `python -V`.  It may be installed as `python3` depending on your system.
3. [Install pip](https://pip.pypa.io/en/stable/installing/) This is the package management system we use with the tracker, and its generally the best option for getting Python packages.
4. [Install direnv](https://github.com/direnv/direnv). *Optional, Linux/OSX only* This will help set up an isolated development environment.
5. Clone this repository, typically I put it in a folder called `donations`, which is the path to which this repo will be referred for the remainder of these instructions:
    ```> git clone https://github.com/UoMEsports/donation-tracker-toplevel.git donations```
6. Make a copy of `example_local.py` under `donations`, and call it `local.py`. This is where you will enter any deployment-specific settings for your instance of the website.
    ```> cp example_local.py local.py```
    - (optional) Change the `NAME` field under the `DATABASES` variable to point at a different location if you wish.
    - There are some other config variables related to timezone, e-mail, google docs, and giantbomb's API. None of these are neccessary to get started, and mostly can be ignored unless you are interested in that specific feature. Documentation on these fields is lacking, but it shouldn't be too diffficult to figure out how they work if you take a look at `settings.py`.
7. Clone the submodules.
    ```> git submodule update --init```
    - This will clone `tracker` (the main backend and the classic frontend), `tracker_ui` (the fancy new experimental Javascript UI).
8. Download the requirements in using pip:
    ```> pip install -r tracker/requirements.txt```
    - If you are using Windows, you may need to delete the lines containing `psycopg2` and `chromium-compact-language-detector` from `tracker/requirements.txt` (both are optional, and require compilation of C code, which is typically a hassle for people in a Windows environment).
    - If you are under 'nix or Mac, you'll probably need to `sudo` this/run as administrator, unless you're using `direnv` as suggested above.
    - The default pip configuration performs a fresh install of all packages, meaning that previously installed packages will be uninstalled before being reinstalled. If you get any exceptions during uninstallation, you can try the flag `--ignore-installed` to leave those packages alone and continue with other packages.
9. Initialize the database. This app, and all the apps it depends on, can be initialized into the database using django's migrate command, `python manage.py migrate`. Notes:
    - This is the actual command that will create the `db/testdb` file on your machine (if it does not exist already).
    - If you are using a different location, or a different database type, you will need to make sure the permissions and settings are set up correctly.
    - This is the general command to migrate all changes in the app. If you ever update any of the dependent libraries, or the tracker itself, you should run this command again.
10. Create a superuser account for the admin with the command `python manage.py createsuperuser` and follow the prompts. This is the account you'll use to access your testing instance of the app.

## Running the test server

You can run the test server, using the command `python manage.py runserver [port]`. The `port` argument is optional; the default is 8000.

You can navigate to the tracker at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (where `8000` is the the port specified). To view the admin site, go to: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/) and log in using the username/password you set up with `createsuperuser`.

## Server deployment

There are far too many different ways to deploy the server to go over every possibility here, so you should start with [Deploying Django](https://docs.djangoproject.com/en/dev/howto/deployment/).

## Docker (experimental, development environments only)

I haven't tested the Docker deployment at all with this, as we don't use Docker for our deployment.  This was experimental in the GDQ version, so if you want to mess with it, do so at your own risk.
