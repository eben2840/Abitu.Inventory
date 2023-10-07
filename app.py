
import os
from email.message import EmailMessage
import ssl
import smtplib
import os
import secrets
import urllib.request, urllib.parse
from sqlalchemy import func 
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request,jsonify,get_flashed_messages
from flask_migrate import Migrate
import json
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_login import login_required,login_user,logout_user,current_user,UserMixin, LoginManager
from flask_marshmallow import Marshmallow
from flask import(
Flask,g,redirect,render_template,request,session,url_for,flash,jsonify
)
from flask_cors import CORS
import json
import time


app=Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:new_password@45.222.128.55:5432/cuministry'

app.config['SECRET_KEY'] =" thisismysecretkey"
app.config['UPLOADED_PHOTOS_DEST'] ='uploads'

# photos=UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


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

        subject = 'SRC - Recruitment Portal'
        
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
                         <img src="static/images/cd.png" style="width:50px;" alt="">
                       
                          </div>
                          
                <h3 style="text-align:center; font-size:30px;">Central University SRC
                    <br><span style="font-size:10px;">SRC Recuitment Portal</span></h3>
                </h3>
                
                <div style="text-align:left;  font-size:13px; color:rgb(69 90 100);"><p>
                    Dear Student,
                    <br><br>
                    I hope this message finds you well and refreshed after your well-deserved vacation. As your President, I want to extend a warm and hearty welcome to each one of you as we embark on a new academic season together.
<br><br>
Vacations are a time to rejuvenate, recharge, and reflect on our goals and aspirations. I hope you had the opportunity to spend quality time with loved ones, explore new experiences, and return with a sense of enthusiasm and purpose.
<br><br>
As we begin this new chapter, let's carry the positive energy and determination from our vacations into our academic journey. Remember that each day is an opportunity to learn, grow, and make a positive impact on our community.
<br><br>
Our university is a place of learning, collaboration, and innovation. Together, we will face new challenges, discover new opportunities, and create lasting memories. I encourage you to engage in your studies, seek out new friendships, and participate in extracurricular activities that align with your interests and passions.
<br><br>
Our faculty and staff are here to support you every step of the way, and your fellow students are your partners on this incredible journey. Let's work together to make this academic year the best one yet.
<br><br>
If you ever have questions, concerns, or ideas to share, please don't hesitate to reach out. Your voices matter, and we are committed to ensuring your success.<br><br>
Wishing you a productive and fulfilling semester ahead!
<br><br>
Warm regards,
<br><br>
President</p>

                 
                </div>

                <div style="background-color:#ca181e; ">
                    <h2 style="padding:50px; color:#fff; ">
                    Central University SRC Portal</h2>
    
                    </div>
                    <p style="text-align:center;">Powered by Prestoghana</p>
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
    
    
# @app.route('/live_data')
# def live_data():
#     gender = request.args.get('gender')  
#     users = User.query.filter_by(gender=gender).all()  
#     data = [{
#         'timestamp': user.id,  
#         'value': random.randint(0, 100)
#     } for user in users]
#     return jsonify(data)


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
                   campus=form.reason.data,
                   qualities=form.qualities.data,
               image_file=form.image_file.data
                  )
       
            db.session.add(new)
            db.session.commit()
            send_email()
        
            flash("Thank you for filling the form, Please check your email for a message from the President.", "success")
            return redirect('/')
            
    print(form.errors)
    return render_template("addAlumni.html", form=form, title='addalumni')



@app.route('/leadersadd', methods=['GET', 'POST'])
def leadersadd():
    form=LeaderForm()
    if form.validate_on_submit():
  
            new=Leaders(director=form.director.data,
                 directress=form.directress.data,
                 others=form.others.data,
                   ministries=form.ministries.data,  
                   total_number=form.total_number.data,  
                         
               
                  )
       
            db.session.add(new)
            db.session.commit()
            flash("Thank you for filling the form", "success")
            return redirect('/')
    print(form.errors)
    return render_template("leadersadd.html", form=form, title='addalumni')



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
    return render_template('current.html', title='dashboard',message=message, total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, users=users, total_female=total_female, total_male=total_male,total_students=total_students,users_with_positions=users_with_positions)




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
    media = User.query.filter_by(ministry='Media').all()
    return render_template('media.html', media=media)

@app.route('/praise', methods=['GET', 'POST'])
@login_required
def praise():
    praise = User.query.filter_by(ministry='Praise & Worship').all()
    return render_template('praise.html', praise=praise)

@app.route('/mcc', methods=['GET', 'POST'])
@login_required
def mcc():
    mcc = User.query.filter_by(ministry='MCC').all()
    return render_template('mcc.html', mcc=mcc)

@app.route('/cjc', methods=['GET', 'POST'])
@login_required
def cjc():
    cjc = User.query.filter_by(ministry='CJC').all()
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
        posts =User.query
        if form.validate_on_submit():
            postsearched=form.searched.data
            posts =posts.filter(User.fullname.like('%'+ postsearched + '%') )
            posts =posts.order_by(User.ministry).all() 
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


@app.route('/report')
@login_required
def report():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("report.html", users=users, current_user=current_user, title="report")
 


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
    form=Adduser()
    user=User.query.get_or_404(id)
    if request.method== 'GET':
        form.fullname.data = user.fullname
        form.indexnumber.data = user.indexnumber
        form.gender.data = user.gender
        form.school.data = user.school
        form.department.data = user.department
        form.completed.data = user.completed
        form.admitted.data = user.admitted
        form.email.data = user.email   
        form.telephone.data = user.telephone  
        form.hall.data = user.hall  
        form.nationality.data = user.nationality   
        form.address.data = user.address  
        form.work.data = user.work 
        form.guardian.data = user.guardian   
        form.marital.data = user.marital   
        form.extra.data = user.extra  
        form.image_file.data = user.image_file 
    if request.method== 'POST':
        new=User(fullname=form.fullname.data,
                 indexnumber=form.indexnumber.data,
                   gender=form.gender.data, 
                    school=form.school.data,
                    department=form.department.data,
                   completed=form.completed.data,
                   admitted=form.admitted.data,
                   email=form.email.data,  
                   telephone=form.telephone.data,  
                   hall=form.hall.data,  
                   nationality=form.nationality.data,  
                   address=form.address.data,  
                   work=form.work.data,  
                   guardian=form.guardian.data,  
                  marital=form.marital.data,
                  extra=form.extra.data,    
               image_file=form.image_file.data
                  )
        try:    
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('list')) 
        except:
            return render_template("main.html")
    return render_template("addAlumni.html", form=form)
    
    
    
#delete route
@app.route("/delete/<int:id>")
def delete(id):
    delete=User.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect(url_for('list')) 
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


@app.route('/', methods=['POST','GET'])
def userbase():
    print("Fetching all")
    total_students = User.query.count()
    total_male = User.query.filter_by(gender='Male').count()
    total_female = User.query.filter_by(gender='Female').count()
    image=User.query.order_by(User.id.desc()).all()
    print(image)
    return render_template("userbase.html",total_male=total_male,total_female=total_female,  header="Information Technology", smalltitle="2021", name="- CCSITA", numberofentries="16 entries",image=image,total_students=total_students)
 

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=4000, debug=True)
    
    
