import web
import config
import json


class Api_facturas:
    def get(self, id_factura):
        try:
            # http://0.0.0.0:8080/api_facturas?user_hash=12345&action=get
            if id_factura is None:
                result = config.model.get_all_facturas()
                facturas_json = []
                for row in result:
                    tmp = dict(row)
                    facturas_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(facturas_json)
            else:
                # http://0.0.0.0:8080/api_facturas?user_hash=12345&action=get&id_factura=1
                result = config.model.get_facturas(int(id_factura))
                facturas_json = []
                facturas_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(facturas_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            facturas_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(facturas_json)

# http://0.0.0.0:8080/api_facturas?user_hash=12345&action=put&id_factura=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, no_factura,fecha,costo):
        try:
            config.model.insert_facturas(no_factura,fecha,costo)
            facturas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(facturas_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_facturas?user_hash=12345&action=delete&id_factura=1
    def delete(self, id_factura):
        try:
            config.model.delete_facturas(id_factura)
            facturas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(facturas_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_facturas?user_hash=12345&action=update&id_factura=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_factura, no_factura,fecha,costo):
        try:
            config.model.edit_facturas(id_factura,no_factura,fecha,costo)
            facturas_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(facturas_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            facturas_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(facturas_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_factura=None,
            no_factura=None,
            fecha=None,
            costo=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_factura=user_data.id_factura
            no_factura=user_data.no_factura
            fecha=user_data.fecha
            costo=user_data.costo
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_factura)
                elif action == 'put':
                    return self.put(no_factura,fecha,costo)
                elif action == 'delete':
                    return self.delete(id_factura)
                elif action == 'update':
                    return self.update(id_factura, no_factura,fecha,costo)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
