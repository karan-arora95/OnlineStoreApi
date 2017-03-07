from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

@api.route('/<string:todo_id>', methods = ['GET', 'PUT','DELETE','POST'])
class TodoSimple(Resource):
	def get(self, todo_id):
		return {todo_id: todos[todo_id]}
	def post(self,todo_id):
		todos[todo_id] = request.form['data']
		return {'message':'CHak De Fatte'}

	def put(self, todo_id):
		todos[todo_id] = request.form['data']
		return {todo_id: todos[todo_id]}

	def delete(self, todo_id):
		del todos[todo_id]        
		return {'deleted':'Chak De Fatte 2'}
 
if __name__ == '__main__':
	app.run(debug=True)