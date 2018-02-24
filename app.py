# Author : Salvador Hernandez Mendoza
# Email  : salvadorhm@gmail.com
# Twitter: @salvadorhm
import web
import config


#activate ssl certificate
ssl = False

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    '/users', 'application.controllers.users.index.Index',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/usuarios', 'application.controllers.usuarios.index.Index',
    '/usuarios/view/(.+)', 'application.controllers.usuarios.view.View',
    '/usuarios/edit/(.+)', 'application.controllers.usuarios.edit.Edit',
    '/usuarios/delete/(.+)', 'application.controllers.usuarios.delete.Delete',
    '/usuarios/insert', 'application.controllers.usuarios.insert.Insert',
    '/api_usuarios/?', 'application.api.usuarios.api_usuarios.Api_usuarios',
    '/servicios', 'application.controllers.servicios.index.Index',
    '/servicios/view/(.+)', 'application.controllers.servicios.view.View',
    '/servicios/edit/(.+)', 'application.controllers.servicios.edit.Edit',
    '/servicios/delete/(.+)', 'application.controllers.servicios.delete.Delete',
    '/servicios/insert', 'application.controllers.servicios.insert.Insert',
    '/api_servicios/?', 'application.api.servicios.api_servicios.Api_servicios',
    '/facturas', 'application.controllers.facturas.index.Index',
    '/facturas/view/(.+)', 'application.controllers.facturas.view.View',
    '/facturas/edit/(.+)', 'application.controllers.facturas.edit.Edit',
    '/facturas/delete/(.+)', 'application.controllers.facturas.delete.Delete',
    '/facturas/insert', 'application.controllers.facturas.insert.Insert',
    '/api_facturas/?', 'application.api.facturas.api_facturas.Api_facturas',
)

app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'kuorra'
    web.config.session_parameters['timeout'] = 10
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


def InternalError(): 
    raise config.web.seeother('/')


def NotFound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = False # hide db transactions
    web.config.debug = False # hide debug print
    web.config.db_printing = False # hide db transactions
    app.internalerror = InternalError
    app.notfound = NotFound
    app.run()
