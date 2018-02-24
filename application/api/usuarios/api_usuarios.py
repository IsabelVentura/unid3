import web
import config
import json


class Api_usuarios:
    def get(self, id_usuario):
        try:
            # http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=get
            if id_usuario is None:
                result = config.model.get_all_usuarios()
                usuarios_json = []
                for row in result:
                    tmp = dict(row)
                    usuarios_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(usuarios_json)
            else:
                # http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=get&id_usuario=1
                result = config.model.get_usuarios(int(id_usuario))
                usuarios_json = []
                usuarios_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(usuarios_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuarios_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)

# http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=put&id_usuario=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, usuario,nombre,direcion,telefono):
        try:
            config.model.insert_usuarios(usuario,nombre,direcion,telefono)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=delete&id_usuario=1
    def delete(self, id_usuario):
        try:
            config.model.delete_usuarios(id_usuario)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=update&id_usuario=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_usuario, usuario,nombre,direcion,telefono):
        try:
            config.model.edit_usuarios(id_usuario,usuario,nombre,direcion,telefono)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuarios_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_usuario=None,
            usuario=None,
            nombre=None,
            direcion=None,
            telefono=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_usuario=user_data.id_usuario
            usuario=user_data.usuario
            nombre=user_data.nombre
            direcion=user_data.direcion
            telefono=user_data.telefono
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_usuario)
                elif action == 'put':
                    return self.put(usuario,nombre,direcion,telefono)
                elif action == 'delete':
                    return self.delete(id_usuario)
                elif action == 'update':
                    return self.update(id_usuario, usuario,nombre,direcion,telefono)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
