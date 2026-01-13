from flask import Flask, render_template

from backend.models.models import db_setup, User
from flask_migrate import Migrate
import logging

logger = logging.getLogger(__name__)


def register_time_table_views(app):
    from backend.test_functions.test_complete import test_complete
    from backend.test_functions.test2 import test_router
    from backend.test_functions.components import components

    app.register_blueprint(test_complete, url_prefix=f"/api/test-complete")
    app.register_blueprint(test_router, url_prefix=f"/api/test-router")
    app.register_blueprint(components, url_prefix=f"/api/components")


def create_app(config_name='backend.models.config'):
    """Application factory pattern for better testing and configuration"""

    app = Flask(
        __name__,
        static_folder="static",
        static_url_path="/"
    )

    # Configuration
    app.config.from_object(config_name)

    # Initialize extensions
    db = db_setup(app)
    migrate = Migrate(app, db)

    # Register all blueprints and routes
    register_time_table_views(app)
    return app


app = create_app()


@app.route('/')
def home():
    users = User.query.count()
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run()
