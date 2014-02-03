CREATE TABLE teams (
		id serial primary key,
		name varchar(64),
		number varchar(16),
		autonomous float default 0.0,
		auto_blocks boolean default 'f',
		auto_ir boolean default 'f',
		auto_ramp boolean default 'f',
		auto_consistency integer default 0,
		auto_notes text,
		tele_op float default 0.0,
		tele_blocks boolean default 'f',
		tele_elevate boolean default 'f',
		tele_speed integer default 0,
		tele_efficiency integer default 0,
		tele_drive integer default 0,
		tele_notes text,
		endgame float default 0.0,
		end_flag boolean default 'f',
		end_hang boolean default 'f',
		end_speed integer default 0,
		end_effeciency integer default 0,
		end_notes text,
		collaboration float default 0.0,
		overall float default 0.0,
		notes text )
		
