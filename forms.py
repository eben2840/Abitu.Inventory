from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
# from app import Person


class RegistrationForm(FlaskForm):
    id = IntegerField('id', validators=[(DataRequired())])
    name = StringField('name', validators=[(DataRequired())])
    yearCompleted= SelectField('yearCompleted', choices=[(2021,2021)])
    nationality = StringField('nationality',validators=[DataRequired()] )
    contact= StringField('contact',validators=[ DataRequired(), Length(min=10, max=10, message="Your number shouldn't be less than 10")])
    email = StringField('email',validators=[(DataRequired() )])
    faculty = SelectField('faculty',  choices=[('Faculty/School','Faculty/School'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    hallofresidence = SelectField('hallofresidence',  choices=[('Halls','Halls'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Register')

class Adduser(FlaskForm):
    fullname = StringField('fullname')
    ministry= SelectField('ministry', choices=[('Ministry','Ministry'),('Media', 'Media'), ('Praise & Worship','Praise & Worship'),('MCC','MCC'),('CJC','CJC'),('Levite Generation','Levite Generation'),('Communion','Communion'),('Protocol','Protocol'),('Discipleship','Discipleship'),('Missons','Missons'),('Counselling','Counselling'),('Prayer Ministry','Prayer Ministry'),('Lords Band','Lords Band') ], default=None )
    gender= SelectField('gender', choices=[('Gender','Gender'),('Male', 'Male'), ('Female','Female') ], default=None )
    program= SelectField('program',choices=[('Program','Program'),('ECONOMICS', 'ECONOMICS'),('PUBLIC HEALTH', 'PUBLIC HEALTH'),
                ('MANAGEMENT & PA', 'MANAGEMENT & PA'),
                ('MARKETING', 'MARKETING'),
                ('ACCOUNTING', 'ACCOUNTING'),
                ('HUMAN RESOURCE', 'HUMAN RESOURCE'),
                ('BANKING & FINANCE', 'BANKING & FINANCE'),
                ('Civil Engineering', 'Civil Engineering'),
                ('Information Technology', 'Information Technology'),
                ('Computer Science', 'Computer Science'),
                ('MKT', 'MKT'),
                ('BKF', 'BKF'),
                ('HRM', 'HRM'),
                ('Nursing', 'Nursing'),
                ('PA Dept.', 'PA Dept.'),
                ('Faculty of Law', 'Faculty of Law'),
                ('Sociology', 'Sociology'),
                ('Vision and Life', 'Vision and Life'),
                ('Social Work', 'Social Work'),
                ('Communications and Laguages Studies', 'Communications and Laguages Studies'),
                ('Theology', 'Theology'),
                ('Psychology', 'Psychology'),
                ('Environment and Development Studies', 'Environment and Development Studies'),
                ('Communications and Languages Studies', 'Communications and Languages Studies'),
                ('Agribusiness', 'Agribusiness'),
                ('Design (Interior, Graphic & Fashion)', 'Design (Interior, Graphic & Fashion)'),
                ('Real Estate', 'Real Estate'),
                ('Architecture', 'Architecture'),
                ('Pharmaceutical Sciences', 'Pharmaceutical Sciences'),
                ('Pharmacy Practice', 'Pharmacy Practice'),
                ('MGT & P.A.', 'MGT & P.A.'),
             
                

                ], default=None )
                
    email= StringField('email')
    telephone= StringField('telephone')
    position= StringField('position')
    submit = SubmitField('Register')
    image_file = StringField('image_file', validators=[FileAllowed(['jpg', 'png'])])
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
 
class LeaderForm(FlaskForm):
    others = StringField('Others', validators=[DataRequired()])
    director = StringField('Director', validators=[DataRequired()])
    directress = StringField('Directress', validators=[DataRequired()])
    ministries = SelectField('ministries', choices=[('Ministry','Ministry'),('Media', 'Media'), ('Praise & Worship','Praise & Worship'),('MCC','MCC'),('CJC','CJC'),('Levite Generation','Levite Generation'),('Communion','Communion'),('Protocol','Protocol'),('Discipleship','Discipleship'),('Missons','Missons'),('Counselling','Counselling'),('Prayer Ministry','Prayer Ministry'),('Lords Band','Lords Band') ], default=None )
    total_number = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Login')
 
class Registration(FlaskForm):
    indexnumber= StringField('indexNumber')
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('SignUp')  
    
    # el4 = SelectField('el4', default='None', choices=[(user.lastname, user.lastname) for user in Person.query.all()])
  
    
    #Program = SelectField('programs', choices=[("one", "one"),("two", "two"),("three", "three")])
    submit =SubmitField('submit')
    

class AddDepartment(FlaskForm):
    name = StringField('Department', validators=[DataRequired()])
    school = StringField('School', validators=[DataRequired()])
    

class AddProgram(FlaskForm):
    name = StringField('Program Name', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    school = StringField('School', validators=[DataRequired()])
    
class AddSchool(FlaskForm):
    name = StringField('Department', validators=[DataRequired()])
    # school = StringField('School', validators=[DataRequired()])

# create a search form
class Search(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
    submit = SubmitField('Search') 
    
class Alumni(FlaskForm):
    email= StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    submit = SubmitField('SignUp')  
    
class AlumniSignin(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    indexnumber = StringField('indexnumber', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('SignUp')  
    
    
    
        
class AlbumForm(FlaskForm):
    image_album= StringField('image_album', validators=[DataRequired()])
    submit = SubmitField('Send')  
    