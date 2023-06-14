# django my-school-band

This is a production-ready setup for running  the django project on Docker. It's a simple way to run Django projects on production servers
    
Quick start
---
---
add your server details here
deploy_production

***

That's it—you now have a fully Dockerized Django project running on a production server. Read below for details on configuring the project and managing the development workflow


Installation
---
---

***
First install docker
next clone to this repo
$ github.com/Mellisa-Mugiyo/django_proj.git
$ cd myschoolband

(Mac users should clone it to a directory under /Users because of a Docker bug involving Mac shared directories.)

You can also fork this repo or pull it as image from Docker Hub 

Update the origin to point to your own Git repo:

***
$ git remote set-url origin (The url)



Configure the project
----
----

Project settings live in config.ini. It contains sensitive data, so it's excluded in .gitignore and .dockerignore. Copy config.ini.sample to config.ini

$ cp config.ini.sample config.ini

Edit config.ini. At a minimum, change these settings:

*DOCKER_IMAGE_NAME: change to <yourname>/some-image-name.
*ROOT_PASSWORD: this is the password for a Django superuser with username root. Change it to something secure.

Run docker ps to make sure your Docker host is running. If it's not, run:

$ docker-machine start <dockerhostname>
$ eval "$(docker-machine env <dockerhostname>)"

***
Build the Docker image (you should be in the myschoolband/ directory, which contains the Dockerfile):

$ docker build -t <yourname>/django-proj .

Run the Docker image you just created (the command will be explained in the Development workflow section below):

$ docker run -d -p 80:80 

Run docker ps to verify that the Docker container is running:

CONTAINER ID        IMAGE                      COMMAND                  CREATED             STATUS              PORTS                          NAMES
2830610e8c87        <yourname>/myschoolband   "/usr/bin/supervisord"   25 seconds ago      Up 25 seconds       0.0.0.0:80->80/tcp, 8000/tcp   focused_banach

***
You should now be able to access the running app through a web browser. Run docker-machine ls to get the local IP address for your Docker host:

NAME           ACTIVE   DRIVER       STATE     URL                         SWARM
mydockerhost   *        virtualbox   Running   tcp://192.168.99.100:2376


Deployment
---
---
your server must be running now 
If your repository is private on Docker Hub, you'll have to run docker login first on the remote host.

The project can be deployed with a single Fabric command. Make sure Fabric is installed (do pip install fabric), and then run:

$ fab deploy_production

This builds the Docker image, pushes it to Docker Hub, pulls it on the production server, and starts a container with the production settings

Verify that your production settings (not the development settings!) are active. Navigate to http://<ip address>/spamalot. You should see the basic Nginx "not found" page. If you see the full Django error page, that means that DEBUG = True, which probably means that your production settings are not loaded.


 

