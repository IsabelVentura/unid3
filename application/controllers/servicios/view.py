import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    
    def GET(self, id_servicio):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_servicio) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                return self.GET_VIEW(id_servicio) # call GET_VIEW() function
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_servicio):
        id_servicio = config.check_secure_val(str(id_servicio)) # HMAC id_servicio validate
        result = config.model.get_servicios(id_servicio) # search for the id_servicio data
        return config.render.view(result) # render view.html with id_servicio data
