import web
import config
import json


class Api_servicios:
    def get(self, id_servicio):
        try:
            # http://0.0.0.0:8080/api_servicios?user_hash=12345&action=get
            if id_servicio is None:
                result = config.model.get_all_servicios()
                servicios_json = []
                for row in result:
                    tmp = dict(row)
                    servicios_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(servicios_json)
            else:
                # http://0.0.0.0:8080/api_servicios?user_hash=12345&action=get&id_servicio=1
                result = config.model.get_servicios(int(id_servicio))
                servicios_json = []
                servicios_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(servicios_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            servicios_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(servicios_json)

# http://0.0.0.0:8080/api_servicios?user_hash=12345&action=put&id_servicio=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, servicio):
        try:
            config.model.insert_servicios(servicio)
            servicios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(servicios_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_servicios?user_hash=12345&action=delete&id_servicio=1
    def delete(self, id_servicio):
        try:
            config.model.delete_servicios(id_servicio)
            servicios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(servicios_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_servicios?user_hash=12345&action=update&id_servicio=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_servicio, servicio):
        try:
            config.model.edit_servicios(id_servicio,servicio)
            servicios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(servicios_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            servicios_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(servicios_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_servicio=None,
            servicio=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_servicio=user_data.id_servicio
            servicio=user_data.servicio
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_servicio)
                elif action == 'put':
                    return self.put(servicio)
                elif action == 'delete':
                    return self.delete(id_servicio)
                elif action == 'update':
                    return self.update(id_servicio, servicio)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
