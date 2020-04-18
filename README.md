# Djangfolio
Welcome to ```Djangfolio```! A portfolio template website created in [Django](https://www.djangoproject.com). I created this tool to host my own portfolio website. The current version of this project includes:

- A nice header with profile picture and short description of the current function of the user.
- An about me section with optional links to social media platforms and GitHub.
- A timeline including the current career of the user.
- A nice projects page including the project the user has done with respective image and link.
- A contact page where someone is able to contact the user.

All of these sections are optional and automatically hidden if no model objects/settings are present to display the corresponding section. An example of a website using this repository is [my personal website](https://larsvanrhijn.nl).

## Setup
There are three ways you could deploy the code in this repository. You could use the Django application in the repository and run it somewhere yourself. Another method is to use the [Docker image]() and deploy it somewhere yourself. The last way is to use the ```docker-compose.yml.example``` file in this repository and set up a complete Docker environment yourself. This last method is explained below:

### Using ```docker-compose```
1. Make sure [Docker](https://www.docker.com) and ```docker-compose``` are installed on the system you plan to run ```Djangfolio``` on.
2. Clone this repository with ```git clone https://github.com/KiOui/Djangfolio.git``` and change your directory to ```Djangfolio``` (```cd Djangfolio```)
3. There are a couple of files we want to change, specifically all files with the ```.example``` extension. Let's first do the ```docker-compose.yml.example``` file. First clone that file to a normal ```.yml``` file and then access it with your texteditor (I'm using ```nano```).
	- ```cp docker-compose.yml.example docker-compose.yml```
	- ```nano docker-compose.yml```
4. Change the following in the ```docker-compose.yml``` file:
	- ```[django_secret_key]``` to a Django secret key, you can generate one on this [website](https://miniwebtool.com/django-secret-key-generator/).
	- ```[postgres_password]``` to a random password<sup>1</sup>, you can generate one [here](https://passwordsgenerator.net).
	- ```[hostname]``` to the hostname of your website.
	- The following two entries can be set if you want to enable [reCAPTCHA](https://www.google.com/recaptcha/intro/v3.html) on your website (for the contact form). If you are not going to use reCAPTCHA, leave them empty (```''```).
		- ```[recaptcha_public_key]``` to your reCAPTCHA public key.
		- ```[recaptcha_private_key]``` to your reCAPTCHA private key.
	- For enabling the contact form on the website, you also need to specify the email settings for Django:
		- ```[email_host]``` to the email host you are using.
		- ```[email_port]``` to the email port you are using.
		- ```[email_host_user]``` to the username you are using to log into your email provider.
		- ```[email_host_password``` to the password you are using to log into your email provider.
		- ```[email_use_tls]``` to ```True``` if your email provider uses TLS, otherwise to ```False```.
		- ```[email_use_ssl]``` to ```True if your email provider uses SSL, otherwise to ```False```.
5. We need to change one more file located in ```database_init```. Execute ```cp database_init/setup.sql.example database_init/setup.sql``` and edit the file with ```nano database_init/setup.sql```.
6. Change the following in the ```setup.sql``` file:
	- ```[postgres_password]``` to the password set in <sup>1</sup>.
7. Now you are ready to run the server! Run ```docker-compose up -d``` to run the three container specified in the ```docker-compose.yml``` file. You can now access your webpage!
8. To add the first user to your webserver (the "superuser"), you should execute the following commands (while the containers are running, so after executing ```docker-compose up -d```):
	- ```docker exec -it djangfolio_django /bin/bash```
	- ```cd website```
	- ```./manage.py createsuperuser```
	- Now, enter your desired username and credentials. Execute ```exit``` when finished.
9. Congratulations! You can access the settings of the website at ```[your domain]/admin``` after logging in with the account created in step 8.

## Website customization
Website customization can be done via the admin interface (```[your domain]/admin```). There are a couple of this you will have to do to create a functional webpage:

- Create a Profile in the Profiles section. This profile should contain your personal information and settings for the home page.
- Create Career items in the Career section, after creating at least one Career item that corresponds to your profile, the timeline will be shown on the webpage.
- Create Project items in the Project section, after creating at least one Project item that corresponds to your profile, the projects secion will show on the webpage.
