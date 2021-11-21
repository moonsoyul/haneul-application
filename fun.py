import firebase_admin,os
from flask import *
from firebase_admin import credentials
from firebase_admin import db
db_url = 'https://secuhigh-757bf-default-rtdb.firebaseio.com/'
cred = credentials.Certificate(os.path.join('.','schg.json'))
default_app = firebase_admin.initialize_app(cred, {'databaseURL':db_url})

app = Flask(__name__)

ref = db.reference('NOE')
row = ref.get()
row = int(row)

@app.route('/', methods=['GET', 'POST'])
def main():
         if row >3 :
            return render_template('emergency.html')

         else :
             return render_template('normal.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9900,debug=True)
