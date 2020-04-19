import click
import simplejson
from flask import Flask, current_app
from flask.cli import FlaskGroup, run_command

from werkzeug.middleware.proxy_fix import ProxyFix

from app.cli import job, review, interview, occupation

class JobCruncherApp(Flask):
    """A custom Flask app"""

    def __init__(self, *args, **kwargs):
        super(JobCruncherApp, self).__init__(__name__, *args, **kwargs)
        # Make sure we get the right referral address even behind proxies like nginx.
        self.wsgi_app = ProxyFix(self.wsgi_app, x_for=1, x_host=1)
        # Configure Redash using our settings
        self.config.from_object("app.settings")

def create_app():
    app = JobCruncherApp()

    return app

def create(group):
    app = current_app or create_app()
    group.app = app

    return app


@click.group(cls=FlaskGroup, create_app=create)
def manager():
    """Management script for JobCruncher"""

manager.add_command(job.manager, "job")
manager.add_command(review.manager, "review")
manager.add_command(interview.manager, "interview")
manager.add_command(occupation.manager, "occupation")
manager.add_command(run_command, "runserver")

@manager.command()
def check_settings():
    """Show the settings as JobCruncher sees them (useful for debugging)."""
    for name, item in current_app.config.items():
        print("{} = {}".format(name, item))