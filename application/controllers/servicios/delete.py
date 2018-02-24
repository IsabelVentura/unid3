import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_servicio, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_servicio) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_servicio, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_servicio) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
    

    @staticmethod
    def GET_DELETE(id_servicio, **k):
        message = None # Error message
        id_servicio = config.check_secure_val(str(id_servicio)) # HMAC id_servicio validate
        result = config.model.get_servicios(int(id_servicio)) # search  id_servicio
        result.id_servicio = config.make_secure_val(str(result.id_servicio)) # apply HMAC for id_servicio
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_servicio, **k):
        form = config.web.input() # get form data
        form['id_servicio'] = config.check_secure_val(str(form['id_servicio'])) # HMAC id_servicio validate
        result = config.model.delete_servicios(form['id_servicio']) # get servicios data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_servicio = config.check_secure_val(str(id_servicio))  # HMAC user validate
            id_servicio = config.check_secure_val(str(id_servicio))  # HMAC user validate
            result = config.model.get_servicios(int(id_servicio)) # get id_servicio data
            result.id_servicio = config.make_secure_val(str(result.id_servicio)) # apply HMAC to id_servicio
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/servicios') # render servicios delete.html 
