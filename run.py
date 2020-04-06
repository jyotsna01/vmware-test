#!flask/bin/python

# Import app variable from our app package
from app import app

# Invokes the run method to start the server
### DEVELOPMENT (Internal-facing, Debug on)
app.run(debug=True)
### PRODUCTION (External-facing, Debug off)
#app.run(debug=False, host='0.0.0.0')
