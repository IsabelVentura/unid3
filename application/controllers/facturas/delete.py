import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_factura, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_factura) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_factura, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_factura) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
    

    @staticmethod
    def GET_DELETE(id_factura, **k):
        message = None # Error message
        id_factura = config.check_secure_val(str(id_factura)) # HMAC id_factura validate
        result = config.model.get_facturas(int(id_factura)) # search  id_factura
        result.id_factura = config.make_secure_val(str(result.id_factura)) # apply HMAC for id_factura
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_factura, **k):
        form = config.web.input() # get form data
        form['id_factura'] = config.check_secure_val(str(form['id_factura'])) # HMAC id_factura validate
        result = config.model.delete_facturas(form['id_factura']) # get facturas data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_factura = config.check_secure_val(str(id_factura))  # HMAC user validate
            id_factura = config.check_secure_val(str(id_factura))  # HMAC user validate
            result = config.model.get_facturas(int(id_factura)) # get id_factura data
            result.id_factura = config.make_secure_val(str(result.id_factura)) # apply HMAC to id_factura
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/facturas') # render facturas delete.html 
