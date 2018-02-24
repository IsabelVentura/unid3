import web
import config

db = config.db


def get_all_facturas():
    try:
        return db.select('facturas')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_facturas(id_factura):
    try:
        return db.select('facturas', where='id_factura=$id_factura', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_facturas(id_factura):
    try:
        return db.delete('facturas', where='id_factura=$id_factura', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_facturas(no_factura,fecha,costo):
    try:
        return db.insert('facturas',no_factura=no_factura,
fecha=fecha,
costo=costo)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_facturas(id_factura,no_factura,fecha,costo):
    try:
        return db.update('facturas',id_factura=id_factura,
no_factura=no_factura,
fecha=fecha,
costo=costo,
                  where='id_factura=$id_factura',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
