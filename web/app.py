from flask import Flask

from models.models import db
from routes.routes import main

import config


app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
app.register_blueprint(main)

with app.app_context():
    # drop all is only used because of scrapper setup in docker-compose.yml
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    # for production, for testing use debug=True
    app.run(debug=False)
