import web
from models import Team
from web import form

render = web.template.render('templates/', base='layout')
db = web.database(dbn='postgres', user='figitaki', pw='', db='mydb')
urls = (
	'/', 'index',
	'/new', 'new',
	'/add', 'add',
	'/static/(.*)', 'static',
)

myForm = form.Form(
	form.Textbox('name', description='Team Name'),
	form.Textbox('number', description='Team Number'),
	form.Textbox('autonomous', description='Autonomous'),
	form.Checkbox('auto_blocks', description='Blocks'),
	form.Checkbox('auto_ir', description='IR'),
	form.Dropdown('auto_consistency', range(0,6), description='Consistency'),
	form.Textbox('tele_op', description='Tele-Op'),
	form.Checkbox('tele_blocks', description='Blocks'),
	form.Checkbox('tele_elevate', description='Raise Blocks'),
	form.Dropdown('tele_speed', range(0,6), description='Block Speed'),
	form.Dropdown('tele_efficency', range(0,6), description='Block Effeciency'),
	form.Dropdown('tele_drive', range(0,6), description='Drive System'),
	form.Textbox('endgame', description='Endgame'),
	form.Checkbox('end_flag', description='Flag'),
	form.Checkbox('end_hang', description='Hang'),
	form.Dropdown('end_speed', range(0,6), description='Speed'),
	form.Dropdown('end_effeciency', range(0,6), description='Effeciency'),
	form.Button('Submit'))

class index:
	def GET(self):
		dbTeams = db.select('teams')
		teams = []
		for dbTeam in dbTeams:
			team = Team()
			team.name = dbTeam.name
			team.number = dbTeam.number
			teams.append(team)
		return render.index(teams)

class new:
	def GET(self):
		f = myForm()
		return render.new(f)

class add:
	def POST(self):
		i = web.input()
		n = db.insert('teams', name=i.name, number=i.number, auto_ir='f')
		return web.seeother('/')


class static:
	def GET(self, file):
		web.header('Content-Type:', 'style/css')
		f = open(file, 'r')
		return f.read()
		
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
