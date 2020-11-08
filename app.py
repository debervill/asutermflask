from flask import Flask, render_template, request, redirect
from getApi import getGroup, GetPrep, getGroupRasp, getCountTable, getCountTable1, getPrepRasp
from data_func import getDays, getDayWeek, getWeek
from forms import SelectGroupForm, LoginForm, addPrepForm
import os



UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///terminal.sqlite3'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER



@app.route('/')
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html', days=getDays(), day_week=getDayWeek(), wek=getWeek())


@app.route('/rasp_group.html', methods=['GET', 'POST'])
def rasp_group():
    getGroup()

    raspform = SelectGroupForm(request.form)
    grp = getGroup()
    for i in grp:
        raspform.group.choices.append(i)

    raspform.day.choices = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']
    if request.method == 'POST':
        pass
        #print(raspform.group.data)
        #print(raspform.day.data)
        # print(getGroupRasp(raspform.group.data, raspform.day.data))
    # getCountTable(getGroupRasp(raspform.group.data))   

    return render_template('rasp_group.html', days=getDays(),
                           day_week=getDayWeek(),
                           dataGr=getGroup(),
                           form=raspform,
                           daysOfWeek=raspform.day,
                           table=getGroupRasp(raspform.group.data, raspform.day.data),
                           countStr=getCountTable(getGroupRasp(raspform.group.data, raspform.day.data)))


@app.route('/rasp_prep.html',methods=['GET', 'POST'])
def rasp_prep():

    GetPrep()
    raspform = addPrepForm(request.form)

    grp = GetPrep()
    # print(grp)
    j = 0
    raspform.stepenField.choices = []
    for i in grp:
        j += 1
        if j <= 6:
            continue
        # print("i = ",i)
        raspform.stepenField.choices.append(i)
    raspform.day.choices = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']
    if request.method == 'POST':
        pass
    
    # return render_template('rasp_group.html', days=getDays(), day_week=getDayWeek(), dataGr=getGroup(), daysOfWeek=raspform.day,
    #                        table=getGroupRasp(raspform.group.data, raspform.day.data),
    #                        countStr=getCountTable(getGroupRasp(raspform.group.data, raspform.day.data)))

    
    return render_template('rasp_prep.html',form=raspform,daysOfWeek=raspform.day,days=getDays(),day_week=getDayWeek(),
                                                table=getPrepRasp(raspform.stepenField.data, raspform.day.data),wek=getWeek(),
                                                countStr=getCountTable1(getPrepRasp(raspform.stepenField.data, raspform.day.data)))



@app.route('/rasp_dop.html')
def rasp_dop():
    return render_template('rasp_dop.html')


@app.route('/rasp_ekz.html')
def rasp_ekz():
    return render_template('rasp_ekz.html')


@app.route('/raspform.html', methods=['GET', 'POST'])
@app.route('/raspform', methods=['GET', 'POST'])
def frm():
    raspform = SelectGroupForm(request.form)
    grp = getGroup()
    for i in grp:
        raspform.group.choices.append(i)

    raspform.day.choices = ['Понедельник', 'Вторнник']
    if request.method == 'POST':
        print(raspform.group.data)
        print(raspform.day.data)

    return render_template('form.html', form=raspform)


@app.route('/adminloigned')
def adminLogined():

    return render_template('admin.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = LoginForm()
    if request.method == "POST":
        if form.username.data == 'malon':
            return redirect('/adminlogined')

    return render_template('adminLogin.html', form=form)



@app.route('/addsql',  methods=['GET', 'POST'])
def addsql():
    form = addPrepForm(request.form)
    if request.method == 'POST':
        fio = form.fioField.data
        dolgnost = form.dolgnostField.data
        stepen = form.stepenField.data
        photo = form.photoField.data
        file = request.files['file[]']
        #image_data = photo.filename
        print(fio, dolgnost, stepen, file)
        #photo.save(os.path.join(app.instance_path, 'photos', filename))


    return render_template('addsql.html', form=form)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3800)
