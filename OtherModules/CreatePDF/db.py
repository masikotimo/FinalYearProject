from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'timothy'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mickeygerman1'
app.config['MYSQL_DATABASE_DB'] = 'Finalyear'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
