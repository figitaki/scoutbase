import web
from web import form

urls = (
	'/', 'index',
)

myForm = form.Form(
	form.Textbox('name', description='Team Name'),
	form.Textbox('number', description='Team Number'),
	form.Checkbox('ir', description='IR'),
	form.Checkbox('lift', description='Lift'),
	form.Checkbox('flag', description='Flag'),
	form.Dropdown('auto', [1,2,3,4,5,6,7,8,9,10]),
	form.Button('Submit'))

class index:
	def GET(self):
		f = myForm()
		return f.render()
		
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
