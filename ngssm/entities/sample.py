from base import Base
from run import Run
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

class Sample(Base):
	__tablename__ = 'sample'
	id = Column(Integer, primary_key=True)
	run_id = Column(Integer, ForeignKey('run.id'), nullable=False)
	shipped = Column(String)
	received = Column(String)
	project = Column(String)
	sff = Column(String)
	mid = Column(String)
	sample = Column(String)
	collector = Column(String)
	year = Column(String)
	month = Column(String)
	day = Column(String)
	week = Column(String)
	year_week = Column(String)
	location = Column(String)
	city = Column(String)
	province = Column(String)
	crop = Column(String)
	source = Column(String)
	treatment = Column(String)
	substrate = Column(String)
	target = Column(String)
	primer_forward = Column(String)
	primer_reverse = Column(String)
	pcr_type = Column(String)
	taq = Column(String)
	purification = Column(String)
	rep_num = Column(String)
	cycle_num = Column(String)
	dna_dil = Column(String)
	annealing = Column(String)
	dna_ug = Column(String)
	notes = Column(String)
	tm_c_max = Column(String)
	tm_c_min = Column(String)
	tm_c_avg = Column(String)

	def __repr__(self):
		return '<Sample: %r>' % (self.sample)

