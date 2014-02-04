
class Team(object):
	"""docstring for Team"""
	name = ''
	number = ''
	autonomous = 0.0
	auto_blocks = False
	auto_ir = False
	auto_ramp = False
	auto_consistency = 0
	auto_notes = ''
	tele_op = 0.0
	tele_blocks = False
	tele_elevate = False 
	tele_speed = 0
	tele_efficiency = 0
	tele_drive = 0
	tele_notes = ''
	endgame = 0.0
	end_flag = False
	end_hang = False
	end_speed = 0
	end_effenciency = 0
	end_notes = ''
	collaboration = 0.0
	overall = 0.0
	notes = ''

	def __init__(self, data):
		print data
		self.name = data['name']
		self.number = data['number']
		self.autonomous = data['autonomous']

	def insert(self, db):
		db.insert('teams',
			name=self.name,
			number=self.number,
			auto_ir=self.auto_ir)