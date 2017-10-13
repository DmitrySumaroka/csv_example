from flask_wtf import Form
from wtforms import StringField
from app import app

class SampleForm(Form):
    trace_id = StringField('trace_id')
    edge_cache = StringField('edge_cache')
    mid_cache = StringField('mid_cache')
