# This shell script should be run within backend

# Run the following command if "Permission denied"
# chmod +x dev.sh

# The server will be running at http://localhost:5000/

# The flask server will only restart if changes to the app directory are made

. venv/bin/activate
sudo systemctl start mongod
sudo systemctl status mongod
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_RUN_PORT=5000
export FLASK_DEBUG=1
flask run
