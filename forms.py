#from wtforms import Form
from wtforms import Form
#from wtforms import StringField, TelField, IntegerField
from wtforms import StringField,TelField,IntegerField
#from wtforms import EmailField
from wtforms import StringField,TelField,IntegerField
#from wtforms.validators import DataRequired, Email
from wtforms.validators import DataRequired,Email
from wtforms import Form
from wtforms import SelectField, RadioField


class UserForm(Form):
    nombre = StringField('nombre')
    email = StringField("email")
    apaterno = TelField("apaterno")
    amaterno = StringField('amamterno')
    edad = IntegerField('edad') 
   
class distanciasForm(Form):
    x1 = IntegerField("x1")
    x2 = IntegerField("x2")
    y1 = IntegerField("y1")
    y2 = IntegerField('y2')
    d = IntegerField('d')