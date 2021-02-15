#python -m virtualenv env  (make a venv)
#env\scripts\activate 
import shelve, uuid
from flask import *
from flask_bootstrap import Bootstrap
from datetime import timedelta
from Forms import *
from Accounts import *
from Patient import *
from Inventory import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'SuperSecretKey'
app.permanent_session_lifetime = timedelta(days=7)

#Landing Page
@app.route('/')
def index():

    return render_template("index.html")

#Account Management [IC: Arvin]
@app.route('/login', methods=['GET', 'POST'])
def login():
    #Check if there is an existing session
    if "session_id" in session:
        return redirect(url_for(dashboard_routing()))

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        account_dict = {}
        try:
            db = shelve.open('storage.db', 'r')
        except:
            print("ERROR: DataBase don't exist.")

        try:
            account_dict = db['Accounts']
        except:
            print("ERROR: Failed to retrive Accounts from storage.db")
        db.close()

        #Check if email and password is correct
        for uid, account in account_dict.items():
            if form.email.data == account.get_email() :
                if check_password_hash(account.get_password(), form.password.data):
                    #Creating Client-Sided Session
                    session['session_id'] = uid
                    session.permanent = form.remember.data
                    return redirect(url_for(dashboard_routing()))
        
        return "<h1> Invalid Username or Password </h>"

    return render_template('login.html', form=form, title='Log In')

@app.route('/logout')
def logout():
    session.pop('session_id', None)
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        account_dict = {}
        particulas_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            account_dict = db['Accounts']
            particulas_dict = db['Account_particulas']
        except:
            print("ERROR: Failed to retrive Accounts from storage.db")

        #Create and save admin user in a new db.
        if len(account_dict) == 0:
            admin_account = Account('Admin', '', 'Admin', generate_password_hash('Admin', method="sha256"), 'A')
            account_dict[uuid.uuid4()] = admin_account
            db['Accounts'] = account_dict

        uid = account_id_generator()
        account_dict[uid] = Account(form.first_name.data, form.last_name.data, form.email.data, generate_password_hash(form.password.data, method="sha256"))
        particulas_dict[uid] = None
        db['Accounts'] = account_dict
        db['Account_particulas'] = particulas_dict

        # Test codes
        account_dict = db['Accounts']
        for uid, account in account_dict.items():
            if account.get_email() == form.email.data:
                n_account = account_dict[uid]
                testing = uid
        print(n_account.get_first_name(), n_account.get_last_name(), "was stored in storage.db successfully with uid",testing)

        db.close()
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form, title='Registration')

@app.route('/updateAccount/<uid>', methods=['GET', 'POST'])
def update_account(uid):
    form = AdminAccountUpdate(request.form)
    if form.validate_on_submit():
        account_dict = {}
        db = shelve.open('storage.db', 'w')
        account_dict = db['Accounts']

        usr_account = account_dict.get(uuid.UUID(uid))
        usr_account.set_email(form.email.data)
        usr_account.set_account_type(form.account_type.data)

        db['Accounts'] = account_dict
        db.close()

        return redirect(url_for('admin_dashboard'))
    else:
        account_dict = {}
        db = shelve.open('storage.db', 'r')
        account_dict = db['Accounts']
        db.close()

        usr_account = account_dict[uuid.UUID(uid)]
        form.email.data = usr_account.get_email()
        form.account_type.data = usr_account.get_account_type()

        return render_template('updateAccount.html', form=form, uid=uid)

@app.route('/deleteAccount/<uid>', methods=['POST'])
def delete_account(uid):
    account_dict = {}
    db = shelve.open('storage.db', 'w')
    account_dict = db['Accounts']
    account_dict.pop(uuid.UUID(uid))

    db['Accounts'] = account_dict
    db.close()

    if 'session_id' in session:
        return redirect(url_for('admin_dashboard'))

    return redirect(url_for('testSite'))

#Dashbaord Management
@app.route('/admin_dashboard')
def admin_dashboard():
    if verify_account_type('A'):
        account_dict = {}
        db = shelve.open('storage.db', 'r')
        account_dict = db['Accounts']
        db.close()

        accounts_list = []
        for uid, account in account_dict.items():
            accounts = [uid, account]
            accounts_list.append(accounts)

        return render_template('admin_dashboard.html', name='Admin', count=len(accounts_list), users_list=accounts_list, title='Admin Dashboard')
    else:
        return redirect(url_for('login'))

@app.route('/patient_dashboard')
def patient_dashboard():
    if verify_account_type('P'):
        account_dict = {}
        particulas_dict = {}
        db = shelve.open('storage.db', 'r')
        
        try:
            account_dict = db['Accounts']
            particulas_dict = db['Account_particulas']
        except:
            print("Error in retrieving data from storage.db.")

        db.close()

        for uid, account in account_dict.items():
            if session['session_id'] == uid:
                patient_acc = account
                acc_id = uid

        patient_info = particulas_dict.get(acc_id)
        
        return render_template('patient_dashboard.html', name=patient_acc.get_full_name(), title='Patient Profile', patient_acc=patient_acc, patient_info=patient_info, acc_id=acc_id)
    else:
        return redirect(url_for('login'))

@app.route('/doctor_dashboard')
def doctor_dashboard():
    if verify_account_type('D'):
        account_dict = {}
        particulas_dict = {}
        db = shelve.open('storage.db', 'r')
        
        try:
            account_dict = db['Accounts']
            particulas_dict = db['Account_particulas']
        except:
            print("Error in retrieving data from storage.db.")

        db.close()

        for uid, account in account_dict.items():
            if session['session_id'] == uid:
                doc_acc = account
                acc_id = uid
        #retrieve all patient acc and info 
        doc_info = particulas_dict.get(acc_id)
        return render_template('doctor_dashboard.html', name=doc_acc.get_full_name(), title='Doctor Profile', doc_acc=doc_acc, doc_info=doc_info, acc_id=acc_id)
    else:
        return redirect(url_for('login'))

@app.route('/staff_dashboard')
def staff_dashboard():
    if verify_account_type('S'):
        account_dict = {}
        particulas_dict = {}
        db = shelve.open('storage.db', 'r')
        
        try:
            account_dict = db['Accounts']
            particulas_dict = db['Account_particulas']
        except:
            print("Error in retrieving data from storage.db.")

        db.close()

        for uid, account in account_dict.items():
            if session['session_id'] == uid:
                staff_acc = account
                acc_id = uid

        staff_info = particulas_dict.get(acc_id)
        return render_template('staff_dashboard.html', name=staff_acc.get_full_name(), title='Staff Profile', acc_id=acc_id)
    else:
        return redirect(url_for('login'))

def dashboard_routing():
    account_dict = {}
    db = shelve.open('storage.db', 'r')
    account_dict = db['Accounts']
    db.close()

    account_uid = session["session_id"]

    for uid, account in account_dict.items():
        if uid == account_uid:     
            #Check Account Type
            if account.get_account_type() == 'A':
                return 'admin_dashboard'
            elif account.get_account_type() == 'D':
                return 'doctor_dashboard'
            elif account.get_account_type() == 'S':
                return 'staff_dashboard'
            elif account.get_account_type() == 'P':
                return 'patient_dashboard'

def verify_account_type(acc_type):
    account_dict = {}
    db = shelve.open('storage.db', 'r')
    account_dict = db['Accounts']
    db.close()

    if "session_id" in session:
        account_uid = session["session_id"]
        for uid, account in account_dict.items():
            if uid == account_uid:
                if account.get_account_type() == acc_type:
                    return True
                else:
                    break
    
    return False

def account_id_generator():
    account_dict = {}
    db = shelve.open('storage.db', 'r')
    account_dict = db['Accounts']
    db.close()

    while True:
        uid = uuid.uuid4()
        if uid not in account_dict.keys():
            return uid

@app.route('/view_patient_information')
def view_patient_information():
    account_dict = {}
    particulars_dict = {}
    db = shelve.open('storage.db', 'r')

    try:
        account_dict = db['Accounts']
        particulars_dict= db['Account_particulas']
    except:
        print("Error in retrieving P from storage.db")

    db.close()

    account_list = []
    particulars_list = []

    patient_uid = []

    #Get a list of all patient accounts (omit other account type)
    for uid, account in account_dict.items():
        if account.get_account_type() == 'P':
            patient_uid.append(uid)
            patient_acc = [uid, account]
            account_list.append(patient_acc)

    #Get a list of all pateint's information
    for uid, particulars in particulars_dict.items():
        if uid in patient_uid:
            patient_particulars = [uid, particulars]
            particulars_list.append(patient_particulars)

    return render_template('view_patient_information.html',  title='Patient Informations', account_list=account_list, particulars_list=particulars_list)

#Patient Information [IC: Poh Loon]
@app.route('/createPatient/<uid>', methods=['GET', 'POST'])
def create_patient(uid):
    create_patient_information = PatientInformationForm(request.form)

    if create_patient_information.validate_on_submit():
        particulas_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            particulas_dict = db['Account_particulas']
        except:
            print("Error in retrieving Account_particulas from storage.db.")

        patient = Patient(create_patient_information.birth_cert.data, create_patient_information.home_addr.data, create_patient_information.telephone.data, create_patient_information.medication.data)
        particulas_dict[uuid.UUID(uid)] = patient
        db['Account_particulas'] = particulas_dict

        db.close()

        return redirect(url_for('patient_dashboard'))

    return render_template('createPatient.html', form=create_patient_information, title="Patient Information")

@app.route('/updatePatient/<uid>/', methods=['GET', 'POST'])
def update_patient(uid):
    update_patient_information = PatientAccountUpdate(request.form)

    if update_patient_information.validate_on_submit():
        account_dict = {}
        particulas_dict = {}
        db = shelve.open('storage.db', 'w')
        account_dict = db['Accounts']
        particulas_dict = db['Account_particulas']
        db.close()

        usr_account = account_dict[uuid.UUID(uid)]
        usr_info = particulas_dict[uuid.UUID(uid)]

        usr_account.set_first_name(update_patient_information.first_name.data)
        usr_account.set_last_name(update_patient_information.last_name.data)
        usr_account.set_email(update_patient_information.email.data)
        usr_info.set_birth_cert(update_patient_information.birth_cert.data)
        usr_info.set_home_addr(update_patient_information.home_addr.data)
        usr_info.set_telephone(update_patient_information.telephone.data)
        usr_info.set_medication(update_patient_information.medication.data)

        db['Accounts'] = account_dict
        db['Account_particulas'] = particulas_dict
        db.close()

        return redirect(url_for('patient_dashboard'))
    else:
        account_dict = {}
        particulas_dict = {}
        db = shelve.open('storage.db', 'r')
        account_dict = db['Accounts']
        particulas_dict = db['Account_particulas']
        db.close()

        usr_account = account_dict[uuid.UUID(uid)]
        usr_info = particulas_dict[uuid.UUID(uid)]
        
        update_patient_information.first_name.data = usr_account.get_first_name()
        update_patient_information.last_name.data = usr_account.get_last_name()
        update_patient_information.email.data = usr_account.get_email()
        update_patient_information.birth_cert.data = usr_info.get_birth_cert()
        update_patient_information.home_addr.data = usr_info.get_home_addr()
        update_patient_information.telephone.data = usr_info.get_telephone()
        update_patient_information.medication.data = usr_info.get_medication()

        return render_template('updatePatient.html', form=update_patient_information)

#Inventory Management [IC: Xue Qi]
@app.route('/medicine_storage')
def medicine_storage():
    inventories_dict = {}

    try:
        db = shelve.open('storage.db', 'r')
        inventories_dict = db['Inventories']
        db.close()
    except:
        print("Error in retrieving Inventories from storage.db")

    inventories_list = []
    for key in inventories_dict:
        inventory = inventories_dict.get(key)
        inventories_list.append(inventory)

        
    return render_template('medicine_storage.html',  title='Medicine Storage', inventories_list=inventories_list)

@app.route('/createMed', methods=['GET', 'POST'])
def create_med():
    create_med_form = CreateMedForm(request.form)
    if request.method == 'POST' and create_med_form.validate():
        inventories_dict = {}
        inventories_count_id = 0
        db = shelve.open('storage.db', 'c')

        try:
            inventories_dict = db['Inventories']
            inventories_count_id = int(db['inventories_count_id'])
        except:
            print("Error in retrieving Inventories from storage.db.")

        inventory = Inventory(create_med_form.med_name.data, create_med_form.quantity.data, create_med_form.med_type.data)

        inventories_count_id += 1
        inventory.set_med_id(inventories_count_id)
        db['inventories_count_id'] = inventories_count_id
        inventories_dict[inventory.get_med_id()] = inventory
        db['Inventories'] = inventories_dict

        db.close()

        return redirect(url_for('medicine_storage'))
    return render_template('createMed.html', form=create_med_form)

@app.route('/deleteInventories/<int:id>', methods=['POST'])
def delete_inventories(id):
    inventories_dict = {}
    db = shelve.open('storage.db', 'w')
    inventories_dict = db['Inventories']

    inventory = inventories_dict.pop(id)

    db['Inventories'] = inventories_dict
    db.close()

    return redirect(url_for('medicine_storage'))

#Testing route
@app.route('/testSite')
def testSite():
    account_dict = {}
    db = shelve.open('storage.db', 'r')
    account_dict = db['Accounts']
    db.close()

    accounts_list = []
    for uid, account in account_dict.items():
        accounts = [uid, account]
        accounts_list.append(accounts)
        
    return render_template('testSite.html', name='Test_User', count=len(accounts_list), users_list=accounts_list, title='Temp')
    
if __name__ == "__main__":
    app.run(debug=True)