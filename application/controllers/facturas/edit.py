import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_factura, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_factura) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/facturas') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_factura, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_factura) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/facturas') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html  
            

    @staticmethod
    def GET_EDIT(id_factura, **k):
        message = None # Error message
        id_factura = config.check_secure_val(str(id_factura)) # HMAC id_factura validate
        result = config.model.get_facturas(int(id_factura)) # search for the id_factura
        result.id_factura = config.make_secure_val(str(result.id_factura)) # apply HMAC for id_factura
        return config.render.edit(result, message) # render facturas edit.html

    @staticmethod
    def POST_EDIT(id_factura, **k):
        form = config.web.input()  # get form data
        form['id_factura'] = config.check_secure_val(str(form['id_factura'])) # HMAC id_factura validate
        # edit user with new data
        result = config.model.edit_facturas(
            form['id_factura'],form['no_factura'],form['fecha'],form['costo'],
        )
        if result == None: # Error on udpate data
            id_factura = config.check_secure_val(str(id_factura)) # validate HMAC id_factura
            result = config.model.get_facturas(int(id_factura)) # search for id_factura data
            result.id_factura = config.make_secure_val(str(result.id_factura)) # apply HMAC to id_factura
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/facturas') # render facturas index.html
