# COP-4521-Summer-2024-Project

# install docker-desktop 
# install WSL2 on windows

# Create an account on https://hub.docker.com/
# Click on profile, located top right of the screen
# Navigate to account settings 
# Navigate to security
# Create a new access token, and copy down the token
# Token is only generated once, so save it 

# use the command below to login with the token
docker login

# If you can't login, navigate to the config.json file
cd ~/.docker
# make a copy of the file and delete it
rm config.json
# run docker login again

# Commands to run
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient
./setup.sh

# Once everything is installed, run docker-setup
./docker-setup

# TO access the web server
# Run find_ip.bat, this should return a 1 to 3 addresses
# One of those addresses should be the correct address
# Once you find the correct address
# http://<address>:5000/, paste this into a web browser 

# To connect to the mysql server
docker exec -it mysql_db mysql -uroot -p
# password: password