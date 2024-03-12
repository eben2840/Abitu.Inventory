import os
from email.message import EmailMessage
import re
import ssl
import smtplib
import csv
import os
import datetime 
from urllib import response
import uuid
# from datetime import datetime
import urllib.request, urllib.parse
from sqlalchemy import func 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import distinct 
from flask import Flask, redirect, render_template, send_file, url_for,request,jsonify,get_flashed_messages, send_from_directory,make_response
from flask_migrate import Migrate
import json
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_login import login_required,login_user,logout_user,current_user,UserMixin, LoginManager
from flask import(
Flask,g,redirect,render_template,request,session,url_for,flash,jsonify, send_from_directory
)
from flask_cors import CORS
import json
import time
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

#chin of messgae

app=Flask(__name__)
CORS(app)
# 'postgresql://postgres:new_password@45.222.128.55:5432/src'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("CENTRAL_MINISTRY_DB_URL","sqlite:///test.db")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:new_password@45.222.128.55:5432/src'
app.config['SECRET_KEY'] ="thisismysecretkey"
app.config['UPLOADED_PHOTOS_DEST'] ='uploads'
app.config['UPLOAD_FOLDER'] = 'uploads/pdfs' 
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = 'uploads' 


# photos=UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)



login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
migrate = Migrate(app, db)
from forms import *

# mailserver=os.environ.get("presto_mail_server")
# mailport=os.environ.get("presto_mail_port")
# mailpassword=os.environ.get("presto_mail_password")

@login_manager.user_loader
def load_user(user_id):
    return Person.query.get(int(user_id))


def sendtelegram(params):
    url = "" + urllib.parse.quote(params)
    content = urllib.request.urlopen(url).read()
    print(content)
    return content


def sendtelegram(params):
    url = "https://api.telegram.org/bot5787281305:AAE1S8DSnMAyQuzAnXOHfxLq-iyvPwYJeAo/sendMessage?chat_id=-1001556929308&text=" + urllib.parse.quote(params)
    content = urllib.request.urlopen(url).read()
    print(content)
    return content


#person table
class Person(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String())
    email= db.Column(db.String())
    company_email= db.Column(db.String())
    company_name= db.Column(db.String())
    category= db.Column(db.String())
    username= db.Column(db.String())
    phone= db.Column(db.String()    )
    image_file = db.Column(db.String())
    password = db.Column(db.String(128))
    confirm_password = db.Column(db.String(128))
    
    def __repr__(self):
        return f"Person('{self.id}', {self.name}')"

class alumni(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String() )
    name= db.Column(db.String() )
    password= db.Column(db.String() )
    email= db.Column(db.String() )
    indexnumber= db.Column(db.String()  )
    telephone= db.Column(db.String()  )
    def __repr__(self):
        return f"alumni('{self.id}', {self.name}', {self.email})"

class Studenthalls(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    studentName= db.Column(db.String() )
    regno= db.Column(db.String() )
    gender= db.Column(db.String() )
    program= db.Column(db.String() )
    level= db.Column(db.String()  )
    email= db.Column(db.String()  )
    hallname= db.Column(db.String()  )
    def __repr__(self):
        return f"Studenthalls('{self.id}', {self.studentName}', {self.regno})"

class StudentData(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    studentName= db.Column(db.String() )
    studentID= db.Column(db.String() )
    studentnumber= db.Column(db.String() )
    def __repr__(self):
        return f"Studentdata('{self.id}', {self.studentName}', {self.studentnumber})"
    
    
class User(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    fullname= db.Column(db.String()  )
    position= db.Column(db.String()     )
    qualities = db.Column(db.String()     )
    reason = db.Column(db.String()     )
    campus= db.Column(db.String()     )
    image_file = db.Column(db.String(255))
    def __repr__(self):
        return f"User('{self.id}', {self.fullname}, {self.campus}'"
    
class Challenge(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String()  )
    task= db.Column(db.String()     )
    tag = db.Column(db.String()     )
    description = db.Column(db.String())
   
    def __repr__(self):
        return f"Challenge('{self.id}', {self.name}, {self.tag}'"
    

class Getfunds(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    fullname= db.Column(db.String()  )
    ministry = db.Column(db.String())
    program= db.Column(db.String()   )
    email= db.Column(db.String()     )
    telephone= db.Column(db.String()     )  
    
    campus= db.Column(db.String()     )
    def __repr__(self):
        return f"User('{self.id}', {self.fullname}, {self.email}'"
    

class Faq(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    caption= db.Column(db.String()  )
    answers = db.Column(db.String())
    campus= db.Column(db.String()     )
    def __repr__(self):
        return f"User('{self.id}', {self.caption}, {self.answers}'"
    

class Challenges(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String()  )
    number = db.Column(db.String())
    message= db.Column(db.String()     )
    def __repr__(self):
        return f"User('{self.id}', {self.name}, {self.number}'"
    
    
    
    
class Department(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String())
    school= db.Column(db.String())
    slug= db.Column(db.String())
    def __repr__(self):
        return f"Department('{self.id}', {self.name}'"
    
class School(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    slug =db.Column(db.String)
    departments = db.Column(db.String)
    def __repr__(self):
        return f"School('{self.id}', {self.slug}')"
    
        
class Album(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    image_album=db.Column(db.String)
    def __repr__(self):
        return f"year('{self.id}', {self.image_album}'"


class Message(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    message=db.Column(db.String)
    def __repr__(self):
        return f"Message('{self.id}', {self.message}'"
    
    
class Program(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String) 
    school =db.Column(db.String) 
    department =db.Column(db.String) 
    slug =db.Column(db.String) 
    def __repr__(self):
        return f"Program('{self.id}', {self.name}'"
    
     
class Leaders(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    director=db.Column(db.String)
    directress=db.Column(db.String)
    others=db.Column(db.String)
    ministries =db.Column(db.String)
    total_number = db.Column(db.String)
    timestamp = db.Column(db.Float, default=time.time)
    def __repr__(self):
        return f"School('{self.id}', {self.others}')"

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    level = db.Column(db.String())
    schools = db.Column(db.String())
    course = db.Column(db.String())
    year = db.Column(db.String())
    pdf_filename = db.Column(db.String()) 
       
class Ask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ask = db.Column(db.String())
    
class Committee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())    
    description = db.Column(db.String())    

class PDFFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    filename = db.Column(db.String(100), unique=True)
    course = db.relationship('Course', backref=db.backref('pdf_files', lazy=True))
    year = db.Column(db.Integer)

class Waitlist(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)

class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer())
    name = db.Column(db.String())
    items = db.relationship('Item', backref='group', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    quantity = db.Column(db.String())
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id', name='ft_item_group_id'))


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
# @app.route('/backup_database', methods=['GET'])
# def backup_database():
#     source_db_path = 'test.db'  # Replace with the actual path to your SQLite database file.
#     backup_db_path = 'your_database_backup.db'  # Replace with the desired path for the backup file.

#     try:
#         shutil.copy2(source_db_path, backup_db_path)
#         return jsonify({'message': 'Database backup successful'})
#     except Exception as e:
#         return jsonify({'error': str(e)})



# # Connect to the SQLite database
# conn = sqlite3.connect('test.db')

# # SQL query to select data from your table
# query = "SELECT * FROM Person"

# # Read data into a DataFrame
# df = pd.read_sql_query(query, conn)

# # Close the database connection
# conn.close()

# # Export the data to an Excel file (output.xlsx)
# df.to_excel('output.xlsx', index=False)

# print("Data has been exported to output.xlsx.")


# email_sender = 'pay@prestoghana.com'
 
 
 
# @app.route("/sendsms", methods=["POST"])
# def send_sms():
#     if request.method == "POST":
#         data = [{
#         'name': '',  
#         'sender_id': '',
#         'mesaage': '',
#     }]
#     return jsonify (data)



# @app.route('/send_email', methods=['POST'])
# def send_email():
#     if request.method == 'POST':
#         email_receiver = [request.form['email'],'prestoghana@gmail.com', 'ebenmills200@gmail.com']
        
#         subject = '"Does what i do really matter?"'
#         # html_content = render_template('try.html') 
#         html_content = """
#         <!DOCTYPE html>
# <html>
# <head>
#     <style>
#     @font-face {
#         font-family: 'Plus Jakarta';
#         src: url('PlusJakartaSans-VariableFont_wght.woff2') format('woff2-variations'),
#              url('PlusJakartaSans-Italic-VariableFont_wght.woff2') format('woff2-variations');
#         font-weight: 100 900; /* Adjust font weights based on available weights */
#         font-style: normal;
#     }

#     body {
#         font-family: 'Plus Jakarta', sans-serif;
#     }
# </style>

# </head>
# <body>
#  <div class="container">
 
    
#             <h4 class="h1 hero-title">Central University Campus Ministry</h4>
#     <p>Hello there!. 
#     <br/> We are grateful for your patience, your data has been retreived successfully.
#     <br/> Have an amazing day.</p>

#     <h1>
#     </div>
# </body>
# </html>
#         """


#         em = EmailMessage()
#         em['From'] = f"Presto Mail <{email_sender}>"
#         em['To'] = email_receiver
#         em['Subject'] = subject
#         em.set_content('')  
#         em.add_alternative(html_content, subtype='html')

#         context = ssl.create_default_context()

#         with smtplib.SMTP_SSL(mailserver, 465, context=context, ) as smtp:
#             smtp.login(email_sender, mailpassword)
#             smtp.sendmail(email_sender, email_receiver, em.as_string())
    
# #         return redirect(url_for('userbase'))
# new=Committee(name=form.name.data, 
#                   description=form.description.data,
#                   )

@app.route('/group', methods=['GET', 'POST'])
def group():
    form = GroupForm()

    if form.validate_on_submit():
        group = Groups(
            userId=current_user.id,
            name=form.name.data
        )
        db.session.add(group)
        db.session.commit()

        flash("You just added a new catalog")
        return redirect(url_for('main'))

    print(form.errors)
    return render_template('groups.html', form=form)







@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = AddItemForm()
    form.group.choices = [(group.id, group.name) for group in Groups.query.all()]

    if form.validate_on_submit():
        item = Item(
            name=form.item_name.data,
            group_id=form.group.data,
            quantity=form.quantity.data
        )
        db.session.add(item)
        db.session.commit()
        
        # if item.quantity and item.quantity.isdigit():
        #     quantity_value = int(item.quantity)
        #     if quantity_value < 5:
        #         flash(f"Less then 5 units, kindly re-stock {item.name}!")
        #     elif quantity_value < 10:
        #         flash(f"Less then 10 units, kindly re-stock {item.name}")
        # else:

        #     flash("Item added to the group successfully")
        if item.quantity and item.quantity.isdigit():
            quantity_value = int(item.quantity)
            if quantity_value < 5:
                session['low_quantity_flash'] = f"Low quantity (less than 5) of {item.name}!"
            elif quantity_value < 10:
                session['low_quantity_flash'] = f"Low quantity (less than 10) of {item.name}!"
        else:
            session['low_quantity_flash'] = f"Invalid quantity format for {item.name}. Please enter a valid number."

            
        flash("Item added to the group successfully")
        return redirect(url_for('main'))

    print(form.errors)
    return render_template('add_item.html', form=form)

    
radio = 'yboateng057@gmail.com'
email_password = 'hsgtqiervnkabcma'
radio_display_name = ' Abitu Industries'

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        email_receiver = request.form['email']

        subject = 'AbiTrack Inventory'
        
        # HTML content of the email
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
            @font-face {
                font-family: 'Plus Jakarta';
                src: url('PlusJakartaSans-VariableFont_wght.woff2') format('woff2-variations'),
                     url('PlusJakartaSans-Italic-VariableFont_wght.woff2') format('woff2-variations');
                font-weight: 100 900; /* Adjust font weights based on available weights */
                font-style: normal;
            }

            body {
                font-family: 'Plus Jakarta', sans-serif;
            }
            </style>
        </head>
        <body>
                <div class="container">
                    <div style="display:flex; padding:10px; justify-content:space-between;">
                        AbiTrack  🚀
                          </div>
                     <h3 style="text-align:center; font-size:40px;">Welcome to AbiTrack Management System
                   
                </h3>      
                    <img src="https://abitu-ce1b6c8eb118.herokuapp.com/static/asets/images/portfolio/Portfolio.jpg" style="width:100%;">
                          
               
                
                
                
              

               
            </div>
            
            
        </body>
        </html>
        """

    
        em = EmailMessage()
        em['From'] = f'{radio_display_name} <{radio}>'
        # em['From'] = f'{radio_display_name}'
        # em['From'] = f'{radio_display_name} <{radio}>'  # Use both display name and email address
        # em.replace_header('From', radio_display_name)  
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content('')
        em.add_alternative(html_content, subtype='html')
        context = ssl.create_default_context()

       
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(radio, email_password)
            smtp.sendmail(radio, email_receiver, em.as_string())

        return redirect(url_for('main')) 



@app.route('/invite', methods=['GET', 'POST'])
def invite():
    # print("this is super dope")
    
    form=WaitForm()
    if form.validate_on_submit():
        wait=Waitlist(
            email=form.email.data
            )
        db.session.add(wait)
        db.session.commit()
        # send_email()
        print(form.email.data)
        
        flash("Thanks for Joining Our Waiting List")
        return redirect('/main')
    print(form.errors)
    return render_template('preview.html', form=form)



@app.route('/dashboard')
@login_required
def dashboard():
    total_students = User.query.count()
    users_with_positions = db.session.query(User.fullname, User.position).all()
    total_people_with_positions = db.session.query(User).filter(User.position.isnot(None)).count()

    print(users_with_positions)
    total_male = User.query.filter_by(gender='Male').count()
    total_female = User.query.filter_by(gender='Female').count() 
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    total_leaders = Leaders.query.count()
    print(total_leaders)
    print(current_user)
    # flash(f"There was a problem", 'success')
    if current_user == None:
        flash("Welcome to the Dashboard" + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('dashboard.html', title='dashboard',total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, users=users, total_female=total_female, total_male=total_male,total_students=total_students,users_with_positions=users_with_positions)


@app.route('/ministries', methods=['GET', 'POST'])
def ministries():
    total_media = User.query.filter_by(ministry='Media').count()
    media_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Media').scalar()
    mcc_count = db.session.query(func.count(User.id)).filter(User.ministry == 'MCC').scalar()
    praise_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Praise & Worship').scalar()
    cjc_count = db.session.query(func.count(User.id)).filter(User.ministry == 'CJC').scalar()
    lv_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Levite Generation').scalar()
    communion_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Communion').scalar()
    protocol_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Protocol').scalar()
    dis_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Discipleship').scalar()
    missions_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Missons').scalar()
    coun_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Counselling').scalar()
    prayer_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Prayer Ministry').scalar()
    lord_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Lords Band').scalar()
    return render_template('year.html',title='Ministries',total_media=total_media,mcc_count=mcc_count, lord_count=lord_count,prayer_count=prayer_count,coun_count=coun_count,missions_count=missions_count,lv_count=lv_count,cjc_count=cjc_count, praise_count=praise_count,dis_count=dis_count, communion_count=communion_count, media_count=media_count,protocol_count=protocol_count)


@app.route('/query_pdf', methods=['GET', 'POST'])
def query_pdf():
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        level = request.form.get('level')
        year = request.form.get('year')
        course = Course.query.filter_by(name=course_name, level=level).first()
        if course:
            pdf_files = PDFFile.query.filter_by(course=course, year=year).all()
            return render_template('pdf_results.html', course=course, pdf_files=pdf_files)
        else:
            return "Course not found"
    courses = Course.query.all()
    return render_template('query.html', courses=courses)




@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)




# @app.route('/download_pdf/<filename>')
# def download_pdf(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        level = request.form.get('level')
        year = request.form.get('year')
        pdf_file = request.files.get('pdf_file')  

        existing_course = Course.query.filter_by(name=course_name, level=level, year=year).first()
        if existing_course:
            return "Course already exists"

        new_course = Course(name=course_name, level=level, year=year)
        try:
            db.session.add(new_course)
            db.session.commit()
            
            if pdf_file:
                filename = secure_filename(pdf_file.filename)

                timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                unique_filename = f"{timestamp}_{filename}"

                pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
                pdf = PDFFile(course=new_course, filename=unique_filename)
                db.session.add(pdf)
                db.session.commit()
            return redirect('/levels')
        except Exception as e:
            db.session.rollback()
            return f"Error adding the course: {str(e)}"
    return render_template('add_course.html')




@app.route('/level100', methods=['GET', 'POST'])
def level100():
    sendtelegram("New User on Pasco Portal level 100")
    hundred = Course.query.filter_by(level='100').all()
    return render_template('level100.html', hundred=hundred)

@app.route('/level200', methods=['GET', 'POST'])
def level200():
    sendtelegram("New User on Pasco Portal level 200")
    two = Course.query.filter_by(level='200').all()
    return render_template('level200.html', two=two)

@app.route('/level300', methods=['GET', 'POST'])
def level300():
    sendtelegram("New User on Pasco Portal level 300")
    two = Course.query.filter_by(level='300').all()
    return render_template('level300.html', two=two)

@app.route('/level400', methods=['GET', 'POST'])
def level400():
    sendtelegram("New User on Pasco Portal level 400")
    two = Course.query.filter_by(level='400').all()
    return render_template('level400.html', two=two)



@app.route('/uploaded')
def uploaded():
    sendtelegram("Uploading a new Pasco")
    return render_template('uploaded.html')  


@app.route('/levels')
def levels():
    return render_template('list_levels.html') 



@app.route('/pascoadmin', methods=['GET', 'POST'])
def pascoadmin():
    courses = Course.query.all() 
    return render_template('pascoadmin.html', courses=courses) 


@app.route('/blog', methods=['GET', 'POST'])
def blog():
    return render_template('blog.html')

@app.route('/passqo', methods=['GET', 'POST'])
def passqo():
    sendtelegram("New User on Pasco Portal")
    return render_template('passqo.html')


@app.route('/school', methods=['GET', 'POST'])
def school():
    return render_template('school.html')

@app.route('/closed', methods=['GET', 'POST'])
def closed():
    return render_template('closed.html')


@app.route('/message', methods=['GET', 'POST'])
def messages():
    users =Committee.query.order_by(Committee.id.desc()).all()
    return render_template('messages.html',users=users)


@app.route('/analytics', methods=['GET', 'POST'])
def analytics():
    return render_template('analytics.html')


@app.route('/level', methods=['GET', 'POST'])
def level():
    courses = Course.query.all() 
    total_100 = Course.query.filter_by(level='100').count()
    total_200 = Course.query.filter_by(level='200').count()
    total_300 = Course.query.filter_by(level='300').count()
    total_400 = Course.query.filter_by(level='400').count()
    return render_template('level.html', courses=courses, total_100=total_100,total_200=total_200,total_300=total_300,total_400=total_400)



@app.route('/level/<int:userid>', methods=['GET', 'POST'])
def viewlevel(userid):
    print("Fetching one")
    profile=Course.query.get_or_404(userid)
    sendtelegram(profile.name + "" + "New download")
    return render_template("levelid.html", profile=profile, title="list")
 
 



@app.route('/mainquestion', methods=['GET', 'POST'])
def mainquestion():
    return render_template('mainquestion.html')


@app.route('/landing', methods=['GET', 'POST'])
def landing():
    return render_template('landing.html')


@app.route('/pages', methods=['GET', 'POST'])
def pages():
    return render_template('pages.html')

@app.route('/basee', methods=['GET', 'POST'])
def basee():
    return render_template('basee.html')

@app.route('/landingpage', methods=['GET', 'POST'])
def landingpage():
    
    current_hour = datetime.datetime.now().hour
    greeting = ""
    
    if current_hour < 12:
        greeting = "Good morning."
    elif current_hour < 17:
        greeting = "Good afternoon."
    else:
        greeting = "Good evening."
        
    total_message = Committee.query.count()
    form=WaitForm()
    if form.validate_on_submit():
        wait=Waitlist(
            email=form.email.data
            )
        db.session.add(wait)
        db.session.commit()
        send_email()
        print(form.email.data)
        flash("Invitation Sent to" + users.email)
        return redirect('homelook')
    
    
     # all_product= User.query.count()
    low_quantity_flash = session.pop('low_quantity_flash', None)
    total_students = User.query.count()
    total_getfundstudents = Getfunds.query.count()
    total_Faq = Faq.query.count()
    total_challenges = Challenge.query.count()
    total_message = Committee.query.count()
    users_with_positions = db.session.query(User.fullname, User.position).filter(User.position.isnot(None)).all()
    total_people_with_positions = db.session.query(User).filter(User.position != '').count()
    # total_people_with_positions = db.session.query(User).filter(User.position.isnot(None)).count()
    message = Message.query.count()
    print(users_with_positions)
    user =Committee.query.order_by(Committee.id.desc()).all()
    # total_male = User.query.filter_by(gender='Male').count()
    # total_female = User.query.filter_by(gender='Female').count() 
    users=User.query.order_by(User.id.desc()).all()
    challenges=Challenges.query.order_by(Challenges.id.desc()).all()
    print(users)
    total_leaders = Leaders.query.count()
    print(total_leaders)
    online =Person.query.order_by(Person.id.desc()).all()
    print(current_user)
    
    print(form.errors)
    users =Person.query.order_by(Person.id.desc()).all()
    
    print("-------------")
    print(users)
    print("-------------")
    
    return render_template('landingpage.html',total_message=total_message, greeting=greeting, users=users, form=form,
          
                        low_quantity_flash=low_quantity_flash, total_challenges=total_challenges,online=online,message=message,total_Faq=total_Faq, total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, total_students=total_students,users_with_positions=users_with_positions, total_getfundstudents=total_getfundstudents,challenges=challenges                 
                           )


# @app.route('/inventory', methods=['GET', 'POST'])
# def landingpage():
#     return render_template('landingpage.html')




@app.route('/addcommittee', methods=['GET', 'POST'])
def addcommittee():
    form=CommitteeForm()
    if form.validate_on_submit():
            new=Committee(name=form.name.data, 
                   description=form.description.data,  
                  )
            db.session.add(new)
            db.session.commit()
            # send_email()
            return redirect('leadership')
    print(form.errors)
    return render_template("addcommittee.html", form=form)

@app.route('/addalumni', methods=['GET', 'POST'])
def addalumni():
    form=Adduser()
    if form.validate_on_submit():
            new=User(fullname=form.fullname.data,        
                   position=form.position.data,
                   reason=form.reason.data,
                   campus=form.campus.data,
                   qualities=form.qualities.data,
               image_file=form.image_file.data
                  )
            db.session.add(new)
            db.session.commit()
            # send_email()
            flash("You just added a new product",
                  "success")
            return redirect('main')
    print(form.errors)
    return render_template("addAlumni.html", form=form, title='addalumni')


@app.route('/authmessage', methods=['GET', 'POST'])
def authmessage():
    form=CommitteeForm()
    if form.validate_on_submit():
            new=Committee(name=form.name.data, 
                  description=form.description.data,
                  )
            db.session.add(new)
            db.session.commit()
            flash("You just sent a BoardCast",
                  "success")
            return redirect('main')
    print(form.errors)
    return render_template("authmessage.html",title='authmessage',form=form)


@app.route('/authtask', methods=['GET', 'POST'])
def authtask():
    form=ChallengesForm()
    if form.validate_on_submit():
            new=Challenge(name=form.name.data, 
                   tag=form.tag.data,
                   task=form.task.data,
                   description=form.description.data,
                  )
            db.session.add(new)
            db.session.commit()
            flash("You just added a New Task",
                  "success")
            return redirect('main')
    print(form.errors)
    return render_template("authtask.html", form=form)




@app.route('/authchallenge', methods=['GET', 'POST'])
def authchallenge():
    form=FaqForm()
    if form.validate_on_submit():
        
            new=Faq(
                caption=form.caption.data, 
                answers=form.answers.data, 
                campus=form.campus.data, 
                  )
            db.session.add(new)
            db.session.commit()
            # send_email()
           
        
            flash("You just added a New Challenge.",
                  "success")
            return redirect('main')
            
    print(form.errors)
    return render_template("authchallenge.html", form=form)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form=AddGetfunds()
    if form.validate_on_submit():
        
            new=Getfunds(fullname=form.fullname.data, 
                   email=form.email.data, 
                   telephone=form.telephone.data,    
                   program=form.program.data, 
                  campus=form.campus.data, 
                  ministry = form.ministry.data
                  )    
            db.session.add(new)
            db.session.commit()
            # send_email() 
            flash("Thank you for filling the feedback form, Someone from our team will contact you shortly.",
                  "success")
            return redirect('/thank')
            
    print(form.errors)
    return render_template("feedback.html", form=form, title='addalumni')



@app.route('/getfunds', methods=['GET', 'POST'])
def getfunds():
    form=AddGetfunds()
    if form.validate_on_submit():
        
            new=Getfunds(fullname=form.fullname.data, 
                   email=form.email.data,  
                   ministry=form.ministry.data,    
                   program=form.program.data,  
                   telephone=form.telephone.data,       
                   campus=form.campus.data,
                  )
       
            db.session.add(new)
            db.session.commit()
            # send_email()
            
        
            flash("Thank you for filling the Getfund form.", "success")
            return redirect('/')
            
    print(form.errors)
    return render_template("getfunds.html", form=form)




@app.route('/ask', methods=['GET', 'POST'])
def ask():
    form = AskForm()
    if form.validate_on_submit():
        question = Ask(
            ask=form.ask.data,
            
        )
        print(question)
        db.session.add(question)
        db.session.commit()
        flash("Delivered", "success")
        return redirect('/ask')
    ask=Ask.query.order_by(Ask.id.desc()).all()
    return render_template('ask.html',form=form, ask=ask)  

@app.route('/addinfo', methods=['GET', 'POST'])
def leadersadd():
    form = Addinfo()
    if form.validate_on_submit():
        new_course = Course(
            name=form.name.data,
            level=form.level.data,
            schools=form.schools.data,
            year=form.year.data
        )
        if form.pdf_file.data:
            pdf_file = form.pdf_file.data
            filename = secure_filename(pdf_file.filename)
            pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_course.pdf_filename = filename
        
        print(new_course)
        db.session.add(new_course)
        db.session.commit()
        flash("Thank you for adding a pasco", "success")
        return redirect('/uploaded')
    

    print(form.errors)
    return render_template("leadersadd.html", form=form)

@app.route('/src', methods=['GET', 'POST'])
def src():
    form=ChallengesForm()
    if form.validate_on_submit():
        
            new=Challenges(
                name=form.name.data, 
                number=form.number.data, 
                message=form.message.data, 
                  )
            db.session.add(new)
            db.session.commit()
            # send_email()
        
            flash("Thank you for filling the form, We will response as soon as possible.",
                  "success")
            return redirect('/')
    users=Committee.query.order_by(Committee.id.desc()).all()
    faq=Faq.query.order_by(Faq.id.desc()).all()
    return render_template("blogme.html", users=users,faq=faq,form=form)


    
    
@app.route('/aboutsrc', methods=['GET', 'POST'])
def aboutsrc():
    users=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("aboutme.html",users=users)
 

@app.route('/committee', methods=['GET', 'POST'])
def committee():
    users=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("committee.html",users=users)
 

   
@app.route('/leadership/<int:userid>', methods=['GET', 'POST'])
def leadership(userid):
    profile=Committee.query.get_or_404(userid)
    return render_template("leadership.html", profile=profile,)


   
@app.route('/', methods=['GET', 'POST'])
def homme():
    return render_template("homme.html")



@app.route('/thank', methods=['GET', 'POST'])
def thank():
    return render_template("thank.html")


@app.route('/stock', methods=['GET', 'POST'])
def stock():
    return render_template("stock.html")




@app.route('/showchallenge', methods=['GET', 'POST'])
def showchallenge():
    users=Faq.query.order_by(Faq.id.desc()).all()
    return render_template("showchallenge.html",users=users)


@app.route('/task', methods=['GET', 'POST'])
def task():
    users=Challenge.query.order_by(Challenge.id.desc()).all()
    return render_template("task.html",users=users)

@app.route('/auth', methods=['POST','GET'])
def auth():
    users=User.query.order_by(User.id.desc()).all()
    return render_template("auth.html",users=users)
 
       
@app.route('/annoucement', methods=['GET', 'POST'])
def annoucement():
    users=Committee.query.order_by(Committee.id.desc()).all()
    user=User.query.order_by(User.id.desc()).all()
    return render_template("annoucement.html",users=users,user=user)

       
@app.route('/constitution', methods=['GET', 'POST'])
def constitution():
    users=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("consti.html",users=users)
    
        

       
@app.route('/person', methods=['GET', 'POST'])
def person():
    # users=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("person.html")

       
@app.route('/personid', methods=['GET', 'POST'])
def personid():
    # users=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("personid.html")
    
        

 
@app.route('/adminadd', methods=['GET', 'POST'])
def adminadd():
    form=Adduser()
    if form.validate_on_submit():
            new=User(fullname=form.fullname.data,
                    ministry=form.ministry.data,
                   email=form.email.data,  
                   gender=form.gender.data,  
                   program=form.program.data,  
                   telephone=form.telephone.data,      
               image_file=form.image_file.data
                  )
            db.session.add(new)
            db.session.commit()
            flash("New Person added", "success")
            return redirect('main')
    print(form.errors)
    return render_template("adminadd.html", form=form, title='addalumni')




@app.route('/main', methods=['GET', 'POST'])
@login_required
def main():
    current_hour = datetime.datetime.now().hour
    greeting = ""
    
    if current_hour < 12:
        greeting = "Good morning."
    elif current_hour < 17:
        greeting = "Good afternoon."
    else:
        greeting = "Good evening."
        
    form=WaitForm()
    if form.validate_on_submit():
        wait=Waitlist(
            email=form.email.data
            )
        db.session.add(wait)
        db.session.commit()
        send_email()
        print(form.email.data)
       
        flash("Invitation Sent to" + ' ' + wait.email)
        return redirect('main')
    print(form.errors)
   
   
    # all_product= User.query.count()
    # outstock = db.session.query(Item.quantity).filter(Item.quantity < 5).all()
    outstock = db.session.query(Item).filter(Item.quantity < 5).count()
    
   

    # outstock = db.session.query(Item).filter(Item.quantity < 5).count()
    total_students = User.query.count()
    instock = Item.query.count()
    total_getfundstudents = Getfunds.query.count()
    total_Faq = Faq.query.count()
    total_challenges = Challenge.query.count()
    total_message = Committee.query.count()
    total_stock = Item.query.count()
    total_cat = Groups.query.filter_by(userId=current_user.id).count()
    users_with_positions = db.session.query(User.fullname, User.position).filter(User.position.isnot(None)).all()
    total_people_with_positions = db.session.query(User).filter(User.position != '').count()
   
   
    # total_people_with_positions = db.session.query(User).filter(User.position.isnot(None)).count()
    message = Message.query.count()
    print(users_with_positions)
    user =Committee.query.order_by(Committee.id.desc()).all()
    # total_male = User.query.filter_by(gender='Male').count()
    # total_female = User.query.filter_by(gender='Female').count() 
    users=User.query.order_by(User.id.desc()).all()
    challenges=Challenges.query.order_by(Challenges.id.desc()).all()
    print(users)
    total_leaders = Leaders.query.count()
    print(total_leaders)
    online =Person.query.order_by(Person.id.desc()).all()
    print(current_user)
    # flash(f"There was a problem", 'success')
    if current_user == None:
        flash("Welcome to the Dashboard" + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('current.html',outstock=outstock, instock=instock, title='dashboard',user=user, form=form,
                       total_cat=total_cat,  total_stock=total_stock, greeting=greeting, total_challenges=total_challenges,total_message=total_message,online=online,message=message,total_Faq=total_Faq, total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, users=users, total_students=total_students,users_with_positions=users_with_positions, total_getfundstudents=total_getfundstudents,challenges=challenges)


@app.route('/homelook', methods=['GET', 'POST'])
@login_required
def homelook():
    form=WaitForm()
    if form.validate_on_submit():
        wait=Waitlist(
            email=form.email.data
            )
        db.session.add(wait)
        db.session.commit()
        send_email()
        print(form.email.data)
       
        flash("Invitation Sent to" + ' ' + wait.email)
        return redirect('homelook')
    
    print(form.errors)
    
    current_hour = datetime.datetime.now().hour
    greeting = ""
    
    if current_hour < 12:
        greeting = "Good morning."
    elif current_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening."
    
    # all_product= User.query.count()
    
    low_quantity_flash = session.pop('low_quantity_flash', None)
    instock = Item.query.count()
    total_students = User.query.count()
    total_getfundstudents = Getfunds.query.count()
    total_Faq = Faq.query.count()
    total_challenges = Challenge.query.count()
    total_message = Committee.query.count()
    users_with_positions = db.session.query(User.fullname, User.position).filter(User.position.isnot(None)).all()
    total_people_with_positions = db.session.query(User).filter(User.position != '').count()
    # total_people_with_positions = db.session.query(User).filter(User.position.isnot(None)).count()
    message = Message.query.count()
    print(users_with_positions)
    user =Committee.query.order_by(Committee.id.desc()).all()
    # total_male = User.query.filter_by(gender='Male').count()
    # total_female = User.query.filter_by(gender='Female').count() 
    users=User.query.order_by(User.id.desc()).all()
    challenges=Challenges.query.order_by(Challenges.id.desc()).all()
    print(users)
    total_leaders = Leaders.query.count()
    print(total_leaders)
    online =Person.query.order_by(Person.id.desc()).all()
    print(current_user)
    # flash(f"There was a problem", 'success')
    if current_user == None:
        flash("Welcome to the Dashboard" + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('homelook.html',instock = instock, title='dashboard',user=user, 
                        low_quantity_flash=low_quantity_flash, greeting=greeting, 
                         form=form, total_challenges=total_challenges,total_message=total_message,online=online,message=message,total_Faq=total_Faq, total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, users=users, total_students=total_students,users_with_positions=users_with_positions, total_getfundstudents=total_getfundstudents,challenges=challenges)



def get_initials(name):
    # Get the initials of each word in the name
    return ''.join([word[0].upper() for word in name.split()])


@app.route('/app', methods=['GET', 'POST'])
def approute():
    total_students = User.query.count()
    total_getfundstudents = Getfunds.query.count()
    total_message = Committee.query.count()
    total_challenges = Challenges.query.count()
    users_with_positions = db.session.query(User.fullname, User.position).filter(User.position.isnot(None)).all()
    total_people_with_positions = db.session.query(User).filter(User.position != '').count()
    # total_people_with_positions = db.session.query(User).filter(User.position.isnot(None)).count()
    message = Message.query.count()
    print(users_with_positions)
    # total_male = User.query.filter_by(gender='Male').count()
    # total_female = User.query.filter_by(gender='Female').count() 
    users=User.query.order_by(User.id.desc()).all()
    challenges=Challenges.query.order_by(Challenges.id.desc()).all()
    print(users)
    total_leaders = Leaders.query.count()
    print(total_leaders)
    online =Person.query.order_by(Person.id.desc()).all()
    print(current_user)
    # flash(f"There was a problem", 'success')
    if current_user == None:
        flash("Welcome to the Dashboard" + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('app.html', title='dashboard',online=online,total_message=total_message,message=message,total_challenges=total_challenges, total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, users=users, total_students=total_students,users_with_positions=users_with_positions, total_getfundstudents=total_getfundstudents,challenges=challenges)


@app.route('/newpage', methods=['GET', 'POST'])
def newpage():
    return render_template("newpage.html")

@app.route('/userview', methods=['GET', 'POST'])
def userview():   
    return render_template("userview.html")


@app.route('/newdash', methods=['GET', 'POST'])
def newdash():   
    return render_template("newdash.html")

@app.route('/instock', methods=['GET', 'POST'])
def instock():  
    users=Item.query.order_by(Item.id.desc()).all()
    instock = Item.query.count()
    return render_template("instock.html",users=users,instock = instock)

@app.route('/sms', methods=['GET', 'POST'])
def sms():   
    return render_template("sms.html")


@app.route('/choose', methods=['GET', 'POST'])
def choose():   
    return render_template("choose.html")

@app.route('/message', methods=['GET', 'POST'])
def message():
    form=MessageForm()
    if form.validate_on_submit():
        new=Message(message=form.message.data
                    )
        db.session.add(new)
        db.session.commit()
        flash("Thanks for Sending to Anonymous")
        return redirect("/")
    return render_template('message.html', form=form)



@app.route('/album', methods=['GET', 'POST'])
def album():   
    form=Adduser()
    if form.validate_on_submit():
  
            new=User(fullname=form.fullname.data,
                    ministry=form.ministry.data,
                   email=form.email.data,  
                   gender=form.gender.data,  
                   program=form.program.data,  
                   telephone=form.telephone.data,      
               image_file=form.image_file.data
                  )
       
            db.session.add(new)
            db.session.commit()
            flash("New Person added", "success")
            return redirect('main')
    print(form.errors)
    return render_template("album.html", form=form, title='addalumni')



@app.route('/users_by_position')
def users_by_position():
    users_with_positions = db.session.query(User.fullname, User.position).order_by(User.position.desc()).all()
    print(users_with_positions)
    return render_template('position.html', users_with_positions=users_with_positions)


# catergory by ministry
@app.route('/media', methods=['GET', 'POST'])
@login_required
def media():
    media = User.query.filter_by(ministry='CADET CORPS').all()
    return render_template('media.html', media=media)

def load_data():
    data = []
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip header row
            index, name, hall = line.strip().split(',')
            data.append({'index': index, 'name': name, 'hall': hall})
    return data


@app.route('/praise', methods=['GET', 'POST'])
def praise():
    index = request.form['index']
    data = load_data()
    
    # Find the user by index
    user = next((item for item in data if item['index'] == index), None)

    if user:
        return render_template('results.html', user=user)
    else:
        return render_template('not_found.html')
    


    
    

@app.route('/ent', methods=['GET', 'POST'])
def ent():
    mcc = User.query.filter_by(ministry='ENTERTAINMENT COMMITTEE').all()
    return render_template('mcc.html', mcc=mcc)

@app.route('/cjc', methods=['GET', 'POST'])
def cjc():
    cjc = User.query.filter_by(ministry='ORGANIZING COMMITTEE').all()
    return render_template('cjc.html', cjc=cjc)

@app.route('/lg', methods=['GET', 'POST'])
@login_required
def lg():
    lg = User.query.filter_by(ministry='Levite Generation').all()
    return render_template('lg.html', lg=lg)

@app.route('/communion', methods=['GET', 'POST'])
@login_required
def communion():
    communion = User.query.filter_by(ministry='Communion').all()
    return render_template('communion.html', communion=communion)

@app.route('/protocol', methods=['GET', 'POST'])
@login_required
def protocol():
    protocol = User.query.filter_by(ministry='Protocol').all()
    return render_template('protocol.html', protocol=protocol)

@app.route('/dis', methods=['GET', 'POST'])
@login_required
def dis():
    dis = User.query.filter_by(ministry='Discipleship').all()
    return render_template('dis.html', dis=dis)

@app.route('/mission', methods=['GET', 'POST'])
def mission():
   
    return render_template('halls.html', mission=mission)

@app.route('/counselling', methods=['GET', 'POST'])
@login_required
def counselling():
    counselling = User.query.filter_by(ministry='Counselling').all()
    return render_template('counselling.html', counselling=counselling)

@app.route('/prayer', methods=['GET', 'POST'])
@login_required
def prayer():
    prayer = User.query.filter_by(ministry='Prayer Ministry').all()
    return render_template('prayer.html', prayer=prayer)

@app.route('/lords', methods=['GET', 'POST'])
@login_required
def lords():
    lords = User.query.filter_by(ministry='Lords Band').all()
    return render_template('lords.html', lords=lords)



# end of ministry

@app.route('/female_users')
def female_users():
    # female_users = User.query.filter_by(gender='Female').all()
    return render_template('female.html', female_users=female_users)


@app.route('/male_users')
def male_users():
    # male_users = User.query.filter_by(gender='Male').all()
    return render_template('male.html', male_users=male_users)

@app.route('/newreport')
@app.route('/addschool' , methods=['GET', 'POST'])
def addschool():    
    form=AddSchool()
    schools=School.query.order_by(School.id.desc()).all()
    if form.validate_on_submit():
        centralschool= School(name=form.name.data)
        db.session.add(centralschool)
        db.session.commit()
        flash("New School Added", "success")
        return redirect('addschool')
    print(form.errors)
    return render_template('addschool.html',form=form, schools=schools)


@app.route('/adddepartment' , methods=['GET', 'POST'])
def adddepartment():    
    form=AddDepartment()
    departments=Department.query.order_by(Department.id.desc()).all()
    if form.validate_on_submit():
        centralschool= Department(name=form.name.data,school=form.school.data)
        db.session.add(centralschool)
        db.session.commit()
        flash("New School Added", "success")
        return redirect('adddepartment')
    print(form.errors)
    return render_template('adddepartment.html',form=form, departments=departments)


@app.context_processor
def base():
    form=Search()
    return dict(form=form)


@app.route('/search', methods=[ 'POST'])
def search():
    form= Search()
    if request.method == 'POST': 
        posts =Course.query
        if form.validate_on_submit():
            postsearched=form.searched.data
            posts =posts.filter(Course.name.like('%'+ postsearched + '%') )
            posts =posts.order_by(Course.schools).all()
             
            # posts =posts.order_by(User.position).all() 
            flash("You searched for "+ postsearched, "success")  
            print(posts)   
    return render_template("search.html", form=form, searched =postsearched, posts=posts)


@app.route('/list/<int:userid>', methods=['GET', 'POST'])
@login_required
def list(userid):
    print("Fetching one")
    profile=User.query.get_or_404(userid)
    print(current_user)
    return render_template("profileid.html",current_user=current_user, profile=profile, title="list")
 
 
 
@app.route('/list', methods=['GET', 'POST'])
@login_required
def lists():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("list.html", users=users, current_user=current_user, title="list")



 
@app.route('/getlist', methods=['GET', 'POST'])
@login_required
def getlist():
    print("Fetching all")
    users=Getfunds.query.order_by(Getfunds.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("getlist.html", users=users, current_user=current_user, title="list")
 
 
 

@app.route('/leader', methods=['GET', 'POST'])
@login_required
def leader():
    print("Fetching all")
    users=Leaders.query.order_by(Leaders.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("leader.html", users=users, current_user=current_user)
 


@app.route('/logout')
@login_required
def logout():
    if current_user:
        print(current_user.email)
        logout_user()
    else:
        print("Well that didnt work")
    flash('You have been logged out.','danger')
    return redirect(url_for("login"))


@app.route('/report',methods=['GET','POST'])
@login_required
def report():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("report.html", users=users, current_user=current_user, title="report")
 
 
@app.route('/email',methods=['GET','POST'])
@login_required
def email():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("email.html", users=users, current_user=current_user, title="report")


@app.route('/challenges',methods=['GET','POST'])
@login_required
def challenges():
    print("Fetching all")
    users=Challenges.query.order_by(Challenges.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("challenges.html", users=users, current_user=current_user, title="report")
 


@app.route('/allmes')
@login_required
def allmes():
    message = Message.query.count()
    print(message)
    
    users=Message.query.order_by(Message.id.desc()).all()
    return render_template('allmes.html',message=message, users=users)



@app.route('/home',methods=['GET','POST'])
def home():
    persons=Person.query.all()  
    print(persons)
    return render_template('home.html',persons=persons)


@app.route('/members')
@login_required
def members():
    persons=Person.query.all()
    return render_template('members.html', persons=persons)



#CRUD(update and delete routes)
@app.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id):
    form=Addinfo()
    user=Course.query.get_or_404(id)
    if request.method== 'GET':
        form.name.data = user.name
        form.year.data =user.year
        form.schools.data =user.schools
        form.level.data =user.level
         
    if request.method== 'POST':
        new=Course(name=form.name.data,
            level=form.level.data,
            schools=form.schools.data,
            year=form.year.data
                  )
        try:    
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('pascoadmin')) 
        except:
            return"errrrror"
    return render_template("leadersadd.html", form=form)
    
#delete route
@app.route("/delete/<int:id>")
def deleteme(id):
    delete=Getfunds.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect(url_for('main')) 
    except: 
        return "errrrrorrr"


@app.route("/deleteme/<int:id>")
def deletelist(id):
    delete=User.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect(url_for('lists')) 
    except: 
        return "errrrrorrr"
        
    
#delete route
@app.route("/delete/<int:id>")
def delete(id):
    delete=Course.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            flash ('User deleted succesfully' , 'success')
            return redirect(url_for('pascoadmin')) 
    except: 
        return "errrrrorrr"
    

# @app.route('/login', methods=['POST','GET'])
# def login():
#     form = LoginForm()
#     print ('New User')
#     print(form.email.data)
#     print(form.password.data)
    
#     if form.validate_on_submit():
#         print("form Validated successfully")
#         user = Person.query.filter_by(email = form.email.data).first()
#         if user:
#             print("user:" + user.email + "found")
        
#         if user:
#             print(user.password)
#             if user and form.password.data == user.password:
#                 print(user.email + "validored successfully")
#             # if user == None:
#             #     flash(f"There was a problem")   
#                 login_user(user)
#                 flash (f' ' 'Good day,' + ' '+ 'Welcome to your dashboard,' + ' ' + user.name + '' )
#                 session['logged_in'] = True
                
#                 return redirect(url_for('homelook'))
#             # next = request.args.get('next')
#             else:
#                 flash (f'Wrong Password ', 'success')
#         else:
#             flash("User not found", 'danger') 
#     return render_template('login.html', form=form)
 

@app.context_processor
def inject_status():
    status = 'green' if current_user.is_authenticated else 'red'
    return dict(status=status)



@app.route('/mot', methods=['POST','GET'])
def mot():
    return render_template('signup_step1.html')

    
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        user = Person.query.filter_by(email=form.email.data).first()
        if user and user.password==form.password.data:
            login_user(user)
            print ("Logged in:" + user.username + " " + user.email)
            print(form.password.data) 
            return redirect(url_for('main'))
        else:
            flash(f'Incorrect details, please try again', 'danger')
           
    return render_template('login.html', form=form)  



@app.route('/signup', methods=['POST','GET'])
def signup():
    form = Registration()
    print(form.username.data)
    print(form.phone.data)
    print(form.email.data)
    print(form.name.data)
    print(form.company_name.data)
    print(form.password.data)
    # print(form.category.data)
    if form.validate_on_submit():
        checkUser = Person.query.filter_by(email = form.email.data).first()
        checkUser = Person.query.filter_by(company_email = form.company_email.data).first()
        if checkUser:
            flash(f'This Email has already been used','danger')
            return redirect (url_for ('signup'))
        
        # Check if the email is a Gmail address
        if not is_gmail_address(form.email.data):
            flash('Please provide a valid Gmail email address.', 'danger')
            return redirect(url_for('signup'))
        
        if len(str(form.username.data)) != 4:
            flash('Unique Code must be exactly 4 digits.', 'danger')
            return redirect(url_for('signup'))

        password = form.password.data
        if len(password) < 6 or not re.search("[A-Z]", password) or not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
            flash('Password must be at least 6 characters long, contain at least one uppercase letter, and include at least one symbol (!@#$%^&*(),.?":{}|<>).', 'danger')
            return redirect(url_for('signup'))
        else:
            user = Person(password=form.password.data,
                        confirm_password=form.confirm_password.data,
                        company_name=form.company_name.data, 
                        company_email=form.company_email.data, 
                        # category=form.category.data,
                        email=form.email.data,
                        username=form.username.data, 
                        phone=form.phone.data,
                        name=form.name.data)
            db.session.add(user)
            db.session.commit()
            send_email()
            # params = "New Account Created for " + new_user.username
            # sendtelegram(params)
            flash("We sent you a confirmation Email, kindly confirm your email.", 'success')
           
            # user = Person.query.filter_by(email = form.email.data).first()
            login_user(user, remember=True)
            return redirect (url_for('login'))
    else:
        print(form.errors)
    # flash (f'There was a problem', 'danger')
    # form = Registration()
    # print(form.username.data)
    # print(form.phone.data)
    # print(form.email.data)
    # print(form.name.data)
    # print(form.company_name.data)
    # print(form.password.data)
    # if request.method == "POST": 
    #     if form.validate_on_submit():
    #         print('Success')
    #         user =Person(password=form.password.data,
    #                      company_name=form.company_name.data, 
    #                      company_email=form.company_email.data, 
    #                      category=form.category.data,
    #                     #  password=form.password.data,
    #                      email=form.email.data,username=form.username.data, phone=form.phone.data, name=form.name.data)
    #         db.session.add(user)
    #         db.session.commit()
            
    #         login_user(user, remember=True)
    #         print(current_user)
    #         flash ('Created Successfully','success')
         
    #         return redirect(url_for('login'))
    #     else:
    #         print(form.errors)
            
    return render_template('signup.html', form=form)

# @app.route('/test_email_validation/<test_email>')
# def test_email_validation(test_email):
#     is_valid_email = validate_email(test_email, verify=True)
#     return f'The email address {test_email} is {"valid" if is_valid_email else "invalid"}.'



def is_gmail_address(email):
    # Regular expression for a basic check of Gmail email address
    gmail_pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
    return re.match(gmail_pattern, email)



@app.route('/departments/<string:schoolSlug>')
@login_required
def departments(schoolSlug):
    school = School.query.filter_by(slug = schoolSlug).first()
    departments = Department.query.filter_by(school = school.slug).all() 
    print(departments)
    print(school)
    print(session['selectedYear'])
    sendtelegram(current_user.name + " selected Year: " + session['selectedYear'] + " Department " + school.name + ". Found: " + str(len(departments)) + " result(s) ")
    return render_template('userdepartment.html', items=departments, header=school.name, smalltitle="2021", name="", numberofentries="16 entries")


@app.route('/programs/<string:departmentSlug>')
@login_required
def programs(departmentSlug):
    departmentSlug = departmentSlug.lower()
    department = Department.query.filter_by(slug = departmentSlug).first()
    programs = Program.query.filter_by(department = departmentSlug).all()
    # school = department.school
    # print(school)
    print(programs)
    print(department)
    print(session['selectedYear'])
    # sendtelegram(current_user.name + " selected Year: " + session['selectedYear'] + " Department " + school.name + ". Found: " + str(len(departments)) + " result(s) ")
    return render_template('userprograms.html', items=programs, header=department.name, smalltitle="2021", name="", numberofentries="16 entries")


@app.route('/userbase', methods=['POST','GET'])
def userbase():
    print("Fetching all")
    return render_template("userbase.html")
 

@app.route('/logs', methods=['POST','GET'])
def logs():
    return render_template("logs.html")




@app.route('/category', methods=['POST','GET'])
def category():
    return render_template("category.html")
 



@app.route('/authin', methods=['POST','GET'])
def authin():
    form = Registration()
    print(form.phone.data)
    print(form.email.data)
    print(form.name.data)
    if request.method == "POST": 
        if form.validate_on_submit():
            print('Success')
            user =Person(password="central@123", email=form.email.data, phone=form.phone.data, name=form.name.data)
            db.session.add(user)
            db.session.commit()
            
            login_user(user, remember=True)
            print(current_user)
            flash("New User added", "success")
            return redirect(url_for('main'))
        else:
            print(form.errors)
            
    return render_template('authin.html', form=form)
  

@app.route('/authreg', methods=['POST','GET'])
def authreg():
    return render_template("authreg.html")
 
# app.route('/halls', methods=['GET', 'POST'])
# def halls():
#     return render_template('halls.html')


# @app.route('/results', methods=['POST'])
# def results():
#     index = request.form['index']
#     data = load_data()
    
#     # Find the user by index
#     user = next((item for item in data if item['index'] == index), None)

#     if user:
#         return render_template('results.html', user=user)
#     else:
#         return render_template('not_found.html')



#  //ussd   
    
@app.route('/ussd', methods=['GET', 'POST'])
def rancardussd():
    sessionRequest = request.json
    sessionBody = {
    "MSISDN": sessionRequest["msisdn"],
    "USERDATA": sessionRequest["data"],
    # "MSGTYPE": true,
    
    "NETWORK": sessionRequest["mobileNetwork"],
    "SESSIONID": sessionRequest["sessionId"]   
}
    print("---------REQUEST-----------")
    print(sessionRequest)
    print(sessionBody)
    print("--------------------")
    
    message="Hello, Please Enter Your Index Number.\n eg.int/20/01/3356."
    
    # if sessionRequest["message"] != '*844*138': #seconod try?
    if sessionRequest["menu"] != 0: #seconod try?
        userid = sessionRequest["message"]
        print("userid", userid)
        response= findbyid(userid)
        print("response", response)
        indexnumber = sessionRequest["message"]
        if response is not None:
            print(response)
            message = response["studentname"]
           
            hall=response["hallname"]
            response = {
                    "continueSession": False,
                    "message": "Hello" + " " + message  + "\n " + "Your Hall is" + "\n " + hall + "\n\nPowered by PrestoGhana"
                    #Gets and sets by id! 
                     
                }
            try:
                
                newstudent = StudentData( studentName= message,studentID=userid, studentnumber=sessionRequest["msisdn"]  )
                db.session.add(newstudent)
                db.session.commit()
            except Exception as e:
                print(e)
                
            
        else:
            response = {
                    "continueSession": True,
                    # "message": "Hello" + " " + indexnumber + "\n " + "You have been assigned to the following corresponding Hall: " + "\n" + "Integrity - Male." + "\n" +"Faith Hall - Female"
                    "message": "No student found with ID: " + indexnumber + " " + "\n" + "Please check and try again" + "\n\nPowered by PrestoGhana"
                    #Gets and sets by id!  
                }
    else:
        response = {
                "continueSession": True,
                "message": message
                #Gets and sets by id!  
            }
        
    return response


   
@app.route("/readcsv",)
def readcsv():
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        studentbody=[]
        for line in csv_reader:
            studentName=line["StudentName"]
            regno=line["regno"]
            gender=line["gender"]
            program=line["program"]
            level=line["LEVEL"]
            email=line["email"]
            hallname=line['hallname']
            newStudent = Studenthalls(studentName=studentName, regno=regno, gender=gender,
                                      program=program, level=level, email=email,hallname=hallname)
            
            try:
                db.session.add(newStudent)
                db.session.commit()
            except Exception as e:
                print(e)
            
            print(newStudent.id)
            print(newStudent.studentName)
            
            student={
                "studentname":studentName,
                "regno":regno,
                "gender":gender,
                "program":program,
                "level":level,
                "email":email,
                "hallname":hallname
            }
            studentbody.append(student)
            
            # write to db
            
    return studentbody
    
@app.route("/findbyid")
def findbyid(id=None):
    # print("input")
    # input=request.args.get('id')
    # convert to CAPS
    
    print(id)
    id=id.replace('/', '')
    id=id.replace(' ', '')
    student=Studenthalls.query.filter_by(regno=id.upper()).first()   
    print(student) 
    if student == None:
        return None
    student={
        "studentname":student.studentName,
        "regno":student.regno,
        "gender":student.gender,
        "program":student.program,
        "level":student.level,
        "email":student.email,
        "hallname":student.hallname
    }
  
    return student

@app.route('/updateregno', methods=['POST','GET'])
def method_name():
    # for student in Studenthalls.query.order_by(Studenthalls.id.asc()).limit(10).all():
    for student in Studenthalls.query.order_by(Studenthalls.id.asc()).all():
        print(student)
        print(student.regno)
        
        # Replace '/' with an empty string and assign it back to the 'regno' attribute
        student.regno = student.regno.replace('/', '')
        print(student.regno)

        db.session.commit()
        print(student.regno)
    return "Done"


    
    
    

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=4000, debug=True)
    
  