from wtforms import DateField, Form, BooleanField, HiddenField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NumberRange
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
    image_file = StringField('image_file', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Send')
    
class WaitForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    submit = SubmitField('Update Moji')
    
    
class LogForm(FlaskForm):
    tag = SelectField('tag', choices=[('Tag','Tag'),('High', 'High'), ('Medium','Medium'), ('Low','Low') ], default=None )
    activity = StringField('activity')
    implementation = StringField('implementation')
    email = StringField('Email', validators=[DataRequired()])
    challenges = StringField('challenges')
    future = StringField('future')
    date = DateField('Date', validators=[DataRequired()])
    
   
    submit = SubmitField('Send')
    
class ChallengesForm(FlaskForm):
    name = StringField('name')
    tag = SelectField('tag', choices=[('Tag','Tag'),('High', 'High'), ('Medium','Medium'), ('Low','Low') ], default=None )
    task = StringField('task')
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    submit = SubmitField('Send')
    
    
class CislForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    date = DateField('Date of Incident', validators=[DataRequired()])

    time = StringField('task', validators=[DataRequired()])
    incident = SelectField('tag', choices=[
    ('Incident', 'Incident'),
    ('Employee Accident', 'Employee Accident'),
    ('Fire', 'Fire'),
    ('Burglary or Robbery', 'Burglary or Robbery'),  # Added a comma here
    ('Motor Accident', 'Motor Accident'),
    ('Employee Theft or Embezzlement', 'Employee Theft or Embezzlement'),
    ('Explosion', 'Explosion'),
], default=None)
    description = StringField('description', validators=[DataRequired()])
    casualties = SelectField('tag', choices=[('Choose','Choose'),('Yes', 'Yes'), ('No','No')], default=None )
    employees = SelectField('tag', choices=[('Choose','Choose'),('Yes', 'Yes'), ('No','No')], default=None )
    reason = StringField('reason', validators=[DataRequired()])
    
    police = SelectField('tag', choices=[('Choose','Choose'),('Yes', 'Yes'), ('No','No')], default=None )
    fire_force = SelectField('tag', choices=[('Choose','Choose'),('Yes', 'Yes'), ('No','No')], default=None )
    cost = SelectField('tag', choices=[('Cost','Cost'),('Below 1,000', 'Below 1,000'), ('1,000 - 10,000','1,000 - 10,000'), ('10,000 - 50,000','10,000 - 50,000'), ('50,000 - 100,000','50,000 - 100,000'), ('Above 100,000','Above 100,000')], default=None )
    
    claim = SelectField('tag', choices=[('Agree','Agree'),('Yes', 'Yes')], default=None, validators=[DataRequired()] )
    name_of_contact = StringField('name_of_contact', validators=[DataRequired()])
    contact_number = StringField('name_of_contact', validators=[DataRequired()])
    
    submit = SubmitField('Send')
    



class AddGetfunds(FlaskForm):
    fullname = StringField('fullname')
    ministry = SelectField('ministry', choices=[
    ('Level', 'level'),
    ('100', '100'),
    ('200', '200'),
    ('300', '300'),
    ('400', '400'),
    ('500', '500'),
    
], default=None)

    campus= StringField('campus')
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
   
   
    telephone= StringField('telephone')

    submit = SubmitField('Register')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
    
class CommitteeForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    submit = SubmitField('submit')


class FaqForm(FlaskForm):
    caption = StringField('caption', validators=[DataRequired()])
    answers = StringField('answer', validators=[DataRequired()])
    campus= SelectField('tag', choices=[('Tag','Tag'),('High', 'High'), ('Medium','Medium'), ('Low','Low') ], default=None )
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
   
    submit = SubmitField('submit')
    


    

class Addinfo(FlaskForm):
    name = StringField('name')
    pdf_file = FileField('PDF File', validators=[FileAllowed(['pdf'], 'PDF files only!')])
    level = SelectField('level', choices=[('Level','Level'),('100','100'),('200', '200'), ('300','300'), ('400','400') ], default=None)
    schools = SelectField('school',choices=[('School','School'),
                ('ECONOMICS', 'ECONOMICS'),
                ('PUBLIC HEALTH', 'PUBLIC HEALTH'),
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
    year = SelectField('year', choices=[('Year','Year'),('2021','2021'),('2022', '2022'), ('2023','2023') ], default=None )
    submit = SubmitField('submit')


class GroupForm(FlaskForm):
    name = StringField('Group Name')
    submit = SubmitField('Auto Fill')
    
class Budgetform(FlaskForm):
    budget = StringField('Budget')
    # item_name = StringField('Item Name')
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddItemForm(FlaskForm):
    group = SelectField('Select Group', coerce=int)
    item_name = StringField('Item Name')
    quantity = StringField('Quantity')
    des= StringField('Description')
    # start_date = DateField('Start Date', validators=[DataRequired()])
    tag= SelectField('tag', choices=[('Tag','Tag'),('High', 'High'), ('Medium','Medium'), ('Low','Low') ], default=None )
    price = StringField('Price', validators=[DataRequired()])
    submit = SubmitField('Add Item')
    
class Registration(FlaskForm):
    indexnumber= StringField('indexNumber')
    email = StringField('Email', validators=[DataRequired()])
    latitude = HiddenField('Latitude')  
    longitude = HiddenField('Longitude')    
    password = PasswordField('password_hash', validators=[DataRequired()]) 
    # password = PasswordField('password_hash', validators=[DataRequired(), EqualTo('confirm_password', message='Password Must Match!')]) 
    # confirm_password = PasswordField('confirm password', validators=[DataRequired()]) 
    company_name = StringField('company_name', validators=[DataRequired()]) 
    # category = SelectField('category', choices=[('Category','Category'),('Manufacturing','Manufacturing'),('Cooperate', 'Cooperate'), ('Retail','Retail'),('Personal','Personal') ])
    category = SelectField('category', choices=[('Category','Category'),('Business','Business'),('Personal','Personal') ])
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
    
    
    
class AskForm(FlaskForm):
    ask= StringField('ask', validators=[DataRequired()])
    submit = SubmitField('Send')  
    