import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    
    def GET(self, id_usuario, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_usuario) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_usuario, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_usuario) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    
    

    @staticmethod
    def GET_DELETE(id_usuario, **k):
        message = None # Error message
        id_usuario = config.check_secure_val(str(id_usuario)) # HMAC id_usuario validate
        result = config.model.get_usuarios(int(id_usuario)) # search  id_usuario
        result.id_usuario = config.make_secure_val(str(result.id_usuario)) # apply HMAC for id_usuario
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_usuario, **k):
        form = config.web.input() # get form data
        form['id_usuario'] = config.check_secure_val(str(form['id_usuario'])) # HMAC id_usuario validate
        result = config.model.delete_usuarios(form['id_usuario']) # get usuarios data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_usuario = config.check_secure_val(str(id_usuario))  # HMAC user validate
            id_usuario = config.check_secure_val(str(id_usuario))  # HMAC user validate
            result = config.model.get_usuarios(int(id_usuario)) # get id_usuario data
            result.id_usuario = config.make_secure_val(str(result.id_usuario)) # apply HMAC to id_usuario
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/usuarios') # render usuarios delete.html 
