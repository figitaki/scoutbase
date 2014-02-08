import web
from models import Team
from web import form

render = web.template.render('templates/', base='layout')
db = web.database(dbn='postgres', user='figitaki', pw='', db='mydb')
urls = (
	'/', 'index',
	'/new', 'new',
	'/add', 'add',
	'/team/(.*)', 'view',
	'/edit/(.*)', 'edit',
	'/static/(.*)', 'static',
)

myForm = form.Form(
	form.Textbox('name', description='Team Name', size='36'),
	form.Textbox('number', description='Team Number', size='36'),
	form.Textbox('autonomous', description='Autonomous', size='4', value='0.0'),
	form.Checkbox('auto_blocks', description='Blocks', value='false'),
	form.Checkbox('auto_ir', description='IR', value='false'),
	form.Checkbox('auto_ramp', description='Ramp', value='false')
	form.Dropdown('auto_consistency', range(0,6), description='Consistency'),
	form.Textbox('tele_op', description='Tele-Op', size='4', value='0.0'),
	form.Checkbox('tele_blocks', description='Blocks', value='false'),
	form.Checkbox('tele_elevate', description='Raise Blocks'),
	form.Dropdown('tele_speed', range(0,6), description='Block Speed'),
	form.Dropdown('tele_efficiency', range(0,6), description='Block Effeciency'),
	form.Dropdown('tele_drive', range(0,6), description='Drive System'),
	form.Textbox('endgame', description='Endgame', size='4', value='0.0'),
	form.Checkbox('end_flag', description='Flag', value='false'),
	form.Checkbox('end_hang', description='Hang', value='false'),
	form.Dropdown('end_speed', range(0,6), description='Speed'),
	form.Dropdown('end_effeciency', range(0,6), description='Effeciency'),
	form.Textarea('notes', description='Notes'))

class index:
	def GET(self):
		field = web.input(field='id')
		order = web.input(order='ASC')
		dbTeams = db.select('teams', order='%s %s' % (field.field, order.order))
		return render.index(dbTeams)

class new:
	def GET(self):
		f = myForm()
		return render.new(f)

class view:
	def GET(self, team):
		teams = list(db.select('teams', where='number=\'%s\'' % team))
		myTeam = ''
		return render.view(teams[0])

class edit:
	def GET(self, team):
		teams = list(db.select('teams', where='number=\'%s\'' % team))
		f = myForm()
		return render.edit(f, teams[0])
	def POST(self, team):
		f = myForm()
		if f.validates():
			n = db.update('teams', where='number=\'%s\'' % team, **f.d)
		return web.seeother('/')

class add:
	def POST(self):
		f = myForm()
		if f.validates():
			n = db.insert('teams', **f.d)
		return web.seeother('/')


class static:
	def GET(self, file):
		web.header('Content-Type:', 'style/css')
		f = open(file, 'r')
		return f.read()
		
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
