import web

db_host = 'localhosttviw6wn55xwxejwj.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'wqv8nyode7nnl8yv'
db_user = 'yo553nj9odgp9a1y'
db_pw = 'ea8t3uha78f6bhmq'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
    