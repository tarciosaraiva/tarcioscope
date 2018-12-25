import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError as err:
        app.logger.error(err)
        pass

    from tarcioscope import api
    app.register_blueprint(api.bp)

    return app
