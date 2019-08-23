# My Simple Webapp
Simple Flask Python app, connected to a MongoDB database.
What's missing?? The Dockerfile to build the image...
## Requirements for making the Dockerfile
 - base image: python (the lastest)
 - copy all the content under /app folder
 - run this command:
 ```sh
 pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
 ```
 - set the entrypoint as python
 - expose the 8080 port
 - the command to launch is app.py
## Expected Environment variable
   - DB_URI (default: mydb) is the name of the db Service in Openshift (it can be whatever you want)
   - DB_USER is the db username
   - DB_PASSWORD is the db user password
   - DB_DATABASE is the name of the collection in MongoDB
