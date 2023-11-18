

import os
from email.message import EmailMessage
import ssl
import smtplib
import os
import uuid
from datetime import datetime
import urllib.request, urllib.parse
from sqlalchemy import func 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import distinct 
from flask import Flask, redirect, render_template, send_file, url_for,request,jsonify,get_flashed_messages, send_from_directory
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


app=Flask(__name__)
CORS(app)
# 'postgresql://postgres:new_password@45.222.128.55:5432/src'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("CENTRAL_MINISTRY_DB_URL","sqlite:///test.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:new_password@45.222.128.55:5432/src'
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
    
    contact= db.Column(db.Integer())
    email= db.Column(db.String())
    
    password= db.Column(db.String())
    
    email= db.Column(db.String())
   
    indexnumber=db.Column(db.String())
    password=db.Column(db.String)
    phone= db.Column(db.String()    )
    
    telephone= db.Column(db.String()   )
    yearCompleted= db.Column(db.Integer()  )
    
    form=db.Column(db.String())
    extra= db.Column(db.String()     )
    image_file = db.Column(db.String())
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
  
    
    
class User(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    fullname= db.Column(db.String()  )
    ministry = db.Column(db.String())
    gender= db.Column(db.String()    )
    program= db.Column(db.String()   )
    email= db.Column(db.String()     )
    telephone= db.Column(db.String()     )  
    position= db.Column(db.String()     )
    qualities = db.Column(db.String()     )
    reason = db.Column(db.String()     )
    campus= db.Column(db.String()     )
    image_file = db.Column(db.String(255))
    def __repr__(self):
        return f"User('{self.id}', {self.fullname}, {self.gender}'"
    

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
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    filename = db.Column(db.String(100), unique=True, nullable=False)
    course = db.relationship('Course', backref=db.backref('pdf_files', lazy=True))
    year = db.Column(db.Integer)
    
    

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
    
#         return redirect(url_for('userbase'))

    
radio = 'yboateng057@gmail.com'
email_password = 'hsgtqiervnkabcma'
radio_display_name = ' Central University SRC'

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        email_receiver = request.form['email']

        subject = 'CU - SRC Portal'
        
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
                        <img src="https://www.central.edu.gh/static/img/Central-Uni-logo.png" style="width:100px;" loading="lazy" >
    
                          </div>
                          
                <h3 style="text-align:center; font-size:20px;">Central University SRC
                    
                </h3>
               <b> 🛑  Announcement: SRC Handover Ceremony 🛑</b>
                
                <div style="text-align:left;  font-size:13px; color:rgb(69 90 100);"><p>
                    Dear Student,
                    <br><br>
                    I hope this message finds you well and refreshed.
                    
                    
<br><br>
We are thrilled to invite you to our upcoming SRC Handover Ceremony, a momentous event that signifies the transition of leadership and the promise of a new chapter in our student body.
<br><br>
🗓️ Date: Thursday 26th October, 2023<br>
🕒 Time: 10am <br>
🏛️ Venue: Senate room<br>
<br><br>
Let's come together to applaud our outgoing SRC members for their outstanding service and extend a warm welcome to the new leaders who will carry the torch of our institution's progress.
<br><br>
We look forward to your presence at this important event. Together, we'll continue to build a brighter future for Central University. <br><br>

See you there!
<br>
Warm regards,
<br><br>
-Signed-<br>
CU-SRC</p>

                 
                </div>
               

                
                    <h3 style="text-align:center; ">
                    Powered by PrestoGhana</h3>
    
                   
                    
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
        return redirect(url_for('userbase')) 





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


@app.route('/pages', methods=['GET', 'POST'])
def pages():
    return render_template('pages.html')

@app.route('/basee', methods=['GET', 'POST'])
def basee():
    return render_template('basee.html')




 


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
                   email=form.email.data,  
                   ministry=form.ministry.data,  
                   gender=form.gender.data,  
                   program=form.program.data,  
                   telephone=form.telephone.data,      
                   position=form.position.data,
                   reason=form.reason.data,
                   campus=form.campus.data,
                   qualities=form.qualities.data,
               image_file=form.image_file.data
                  )
       
            db.session.add(new)
            db.session.commit()
            # send_email()
           
        
            flash("Thank you for filling the form, Please check your email for a message from the President.",
                  "success")
            return redirect('/')
            
    print(form.errors)
    return render_template("addAlumni.html", form=form, title='addalumni')



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

@app.route('/', methods=['GET', 'POST'])
def src():
    users=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("blogme.html", users=users)
    
    
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

@app.route('/thank', methods=['GET', 'POST'])
def thank():
    return render_template("thank.html")


 
 
       
@app.route('/annoucement', methods=['GET', 'POST'])
def annoucement():
    users=Committee.query.order_by(Committee.id.desc()).all()
    user=User.query.order_by(User.id.desc()).all()
    return render_template("annoucement.html",users=users,user=user)

       
@app.route('/constitution', methods=['GET', 'POST'])
def constitution():
    users=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("consti.html",users=users)
    
        

 
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
    total_students = User.query.count()
    total_getfundstudents = Getfunds.query.count()
    users_with_positions = db.session.query(User.fullname, User.position).filter(User.position.isnot(None)).all()
    total_people_with_positions = db.session.query(User).filter(User.position != '').count()
    # total_people_with_positions = db.session.query(User).filter(User.position.isnot(None)).count()
    message = Message.query.count()
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
    return render_template('current.html', title='dashboard',message=message, total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, users=users, total_female=total_female, total_male=total_male,total_students=total_students,users_with_positions=users_with_positions, total_getfundstudents=total_getfundstudents)




@app.route('/newdash', methods=['GET', 'POST'])
def newdash():   
    return render_template("newdash.html")

@app.route('/sms', methods=['GET', 'POST'])
def sms():   
    return render_template("sms.html")

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

@app.route('/praise', methods=['GET', 'POST'])
@login_required
def praise():
    praise = User.query.filter_by(ministry='Praise & Worship').all()
    return render_template('praise.html', praise=praise)

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
@login_required
def mission():
    mission = User.query.filter_by(ministry='Misson').all()
    return render_template('mission.html', mission=mission)

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
    female_users = User.query.filter_by(gender='Female').all()
    return render_template('female.html', female_users=female_users)


@app.route('/male_users')
def male_users():
    male_users = User.query.filter_by(gender='Male').all()
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
    

@app.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    print ('try')
    print(form.email.data)
    print(form.password.data)
    
    if form.validate_on_submit():
        print("form Validated successfully")
        user = Person.query.filter_by(email = form.email.data).first()
        if user:
            print("user:" + user.email + "found")
        
        if user:
            print(user.password)
            if user and form.password.data == user.password:
                print(user.email + "validored successfully")
            # if user == None:
            #     flash(f"There was a problem")   
                login_user(user)
                flash (f' ' 'Welcome,' + user.name + '' )
                return redirect(url_for('main'))
            # next = request.args.get('next')
            else:
                flash (f'Wrong Password ', 'success')
        else:
            flash("User not found", 'danger') 
    return render_template('login.html', form=form)
 

#signup route
@app.route('/signup', methods=['POST','GET'])

def signup():
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
         
            return redirect(url_for('login'))
        else:
            print(form.errors)
            
    return render_template('signup.html', form=form)


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
 

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=4000, debug=True)
    
    
