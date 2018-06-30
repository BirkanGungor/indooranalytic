from flask import Flask, render_template
from flask_mysqldb import MySQL
import os
import Denemeler
import json
from bson import json_util
from bson.json_util import dumps
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

app = Flask(__name__)

#1app.config['MYSQL_HOST'] = 'localhost'
#2app.config['MYSQL_USER'] = 'root'
#3app.config['MYSQL_PASSWORD'] = '123birkan'
#4app.config['MYSQL_DB'] = 'userinformation'
#5mysql = MySQL(app)
#(1-2-3-4-5) Flask frameworkünde veritabani bağlantısı için yazıldı ama gerek kalmadı daha sonra.


@app.route('/heatmap', methods=['GET', 'POST'])
def heatmap():
    #cur = mysql.connection.cursor()
    #cur.execute('''SELECT koordinat from dbson''')
    #rv = cur.fetchall()
    #return str(rv)

    sonuc = Denemeler.cagirFonk()
    if sonuc == 1:
        return render_template('sonuc.html')
    else:
        print("Sayfa yüklenemedi!")
        return str(0)
    

@app.route('/')
def users():
    #1process = subprocess.Popen(['python', 'Denemeler.py'], stdout=subprocess.PIPE) #farklı bir script çağırmak için yazdım.
    #2out, err = process.communicate()
    #3print(out)
    #4os.system("Denemeler.py") #(1-2-3-4) işe yaramadı!
    #subprocess.call(['python', 'Denemeler.py'])
    #img = Image.open('bitirme_guncel_foto.jpg')
    return render_template('index.html')

    
if __name__ == '__main__':
    app.run(debug=True)