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
    ministry = SelectField('ministry', choices=[
    ('Committee', 'Committee'),
    ('ACADEMIC AND EDITORIAL COMMITTEE', 'ACADEMIC AND EDITORIAL COMMITTEE'),
    ('WOMENS COMMISSION COMMITTEE', 'WOMENS COMMISSION COMMITTEE'),
    ('BUSINESS DEVELOPMENT AND SPONSORSHIP COMMITTEE', 'BUSINESS DEVELOPMENT AND SPONSORSHIP COMMITTEE'),
    ('COMMUNICATIONS AND PUBLIC RELATIONS COMMITTEE', 'COMMUNICATIONS AND PUBLIC RELATIONS COMMITTEE'),
    ('ENTERTAINMENT COMMITTEE', 'ENTERTAINMENT COMMITTEE'),
    ('FINANCE COMMITTEE', 'FINANCE COMMITTEE'),
    ('INTERNATIONAL STUDENTS COMMITTEE', 'INTERNATIONAL STUDENTS COMMITTEE'),
    ('LOCAL NUGS SECRETARIAT', 'LOCAL NUGS SECRETARIAT'),
    ('LOCAL PUSAG SECRETARIAT', 'LOCAL PUSAG SECRETARIAT'),
    ('PROJECT AND PLANNING COMMITTEE', 'PROJECT AND PLANNING COMMITTEE'),
    ('STUDENTS CHAPLAINCY COMMITTEE', 'STUDENTS CHAPLAINCY COMMITTEE'),
    ('SPORTS COMMITTEE', 'SPORTS COMMITTEE'),
    ('TRANSPORT COMMITTEE', 'TRANSPORT COMMITTEE'),
    ('WELFARE AND PROTOCOL COMMITTEE', 'WELFARE AND PROTOCOL COMMITTEE'),
    ('PROCUREMENT COMMITTEE', 'PROCUREMENT COMMITTEE'),
    ('ORGANIZING COMMITTEE', 'ORGANIZING COMMITTEE'),
    ('CADET CORPS', 'CADET CORPS')
], default=None)

    gender= SelectField('gender', choices=[('Gender','Gender'),('Male', 'Male'), ('Female','Female') ], default=None )
    campus= SelectField('campus', choices=[('Campus','Campus'),('Miotso', 'Miotso'), ('Kumasi','Kumasi'), ('Christ Temple','Christ Temple') ], default=None )
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
                # ('Communications and Laguages Studies', 'Communications and Laguages Studies'),
                ('Theology', 'Theology'),
                ('Psychology', 'Psychology'),
                ('Environment and Development Studies', 'Environment and Development Studies'),
                ('Communications and Media Studies', 'Communications and Media Studies'),
                ('Agribusiness', 'Agribusiness'),
                ('Design (Interior, Graphic & Fashion)', 'Design (Interior, Graphic & Fashion)'),
                ('Real Estate', 'Real Estate'),
                ('Architecture', 'Architecture'),
                ('Doctor of Pharmacy', 'Doctor of Pharmacy'),
                # ('Pharmacy Practice', 'Pharmacy Practice'),
                ('MGT & P.A.', 'MGT & P.A.'),
             
                

                ], default=None )
                
    email= StringField('email')
   
    reason= StringField('reason')
    qualities= StringField('qualities')
    telephone= StringField('telephone')
    position= StringField('position')
    submit = SubmitField('Register')
    image_file = StringField('image_file', validators=[FileAllowed(['jpg', 'png'])])
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
    

    

class Addinfo(FlaskForm):
    name = StringField('name')
    level = SelectField('level', choices=[('100','100'),('200', '200'), ('300','300'), ('400','400') ], default=None)
    schools = SelectField('schools',choices=[('Information Technology','Information Technology'),('Doctor of Pharmacy', 'Doctor of Pharmacy'), ('Nursing','Nursing') ], default=None)
    year = SelectField('year', choices=[('2021','2021'),('2022', '2022'), ('2023','2023') ], default=None )
    submit = SubmitField('submit')




class Registration(FlaskForm):
    indexnumber= StringField('indexNumber')
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()]) 
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
    
    
class MessageForm(FlaskForm):
    message= StringField('message', validators=[DataRequired()])
    submit = SubmitField('Send')  
    