from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# usr = "simp-admin"
# password = "}eikQyFK6>ikM[iV"
# db_conn_name = "celestial-torus-385804:us-central1:simp"
# ip ="34.134.129.105"
# db_uri = f'postgresql:///test?host=/cloudsql/{db_conn_name}&user={usr}&password={password}&sslmode=disable'


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://fizo:fizosDBProj@localhost:5432/postgres'
# app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# login_manager = LoginManager()
# login_manager.init_app(app)
import os
app.secret_key = os.urandom(12)


from simpApp import routes