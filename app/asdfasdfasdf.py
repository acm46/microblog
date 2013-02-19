# from flask import Flask
# from flask.ext.pymongo import PyMongo

# app = Flask(__name__)
# app.config['MONGO_DBNAME'] = 'citiesapp'
# mongo = PyMongo(app)


# @app.route('/')
# def home_page():
# 	online_users = tojson(mongo.db.users.find()[0])
# 	print online_users.name
# 	return '<p>online_users</p>'


# if __name__ == '__main__':
#     app.run(debug=True)