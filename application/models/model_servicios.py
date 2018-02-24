import web
import config

db = config.db


def get_all_servicios():
    try:
        return db.select('servicios')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_servicios(id_servicio):
    try:
        return db.select('servicios', where='id_servicio=$id_servicio', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_servicios(id_servicio):
    try:
        return db.delete('servicios', where='id_servicio=$id_servicio', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_servicios(servicio):
    try:
        return db.insert('servicios',servicio=servicio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_servicios(id_servicio,servicio):
    try:
        return db.update('servicios',id_servicio=id_servicio,
servicio=servicio,
                  where='id_servicio=$id_servicio',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
