from appbase import zfApp
from app import views
from .main import main as main_blueprint
def create_app(config=None, test=False, admin_instance=None, **settings):
    app1 = zfApp('zf')

    app1.register_blueprint(main_blueprint)
    return app1
