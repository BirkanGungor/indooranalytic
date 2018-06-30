from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import MySQLdb


def calCal(val,scaleDis, maxVal):
    if val<= maxVal and val>=maxVal-(scaleDis*1):
        return "#800026"
    elif val>maxVal-(scaleDis*1) and val>=maxVal-(scaleDis*2):
        return "#bd0026"
    elif val>maxVal-(scaleDis*2) and val>=maxVal-(scaleDis*3):
        return "#e31a1c"
    elif val>maxVal-(scaleDis*3) and val>=maxVal-(scaleDis*4):
        return "#fc4e2a"
    elif val>maxVal-(scaleDis*4) and val>=maxVal-(scaleDis*5):
        return "#fd8d3c"
    elif val>maxVal-(scaleDis*5) and val>=maxVal-(scaleDis*6):
        return "#feb24c"
    elif val>maxVal-(scaleDis*6) and val>=maxVal-(scaleDis*7):
        return "#fed976"
    elif val>maxVal-(scaleDis*7) and val>=maxVal-(scaleDis*8):
        return "#ffeda0"
    else:
        return "#ffffcc"
    
def legend(maxVal,scaleDis,draw):
    font = ImageFont.truetype("arial.ttf", 40)
    
    scale = str(maxVal) +"-"+str(int(maxVal-(scaleDis*1)))
    draw.rectangle(((900, 1800), (1200, 1850)), fill="#800026")
    draw.text((1200,1800),scale,font=font,fill="black")
    
    draw.rectangle(((900, 1850), (1200, 1900)), fill="#bd0026")
    scale = str(int(maxVal-(scaleDis*1)-1)) +"-"+str(int(maxVal-(scaleDis*2)))
    draw.text((1200,1850),scale,font=font,fill="black")
    
    draw.rectangle(((900, 1900), (1200, 1950)), fill="#e31a1c")
    scale = str(int(maxVal-(scaleDis*2)-1)) +"-"+str(int(maxVal-(scaleDis*3)))
    draw.text((1200,1900),scale,font=font,fill="black")
    
    draw.rectangle(((900, 1950), (1200, 2000)), fill="#fc4e2a")
    scale = str(int(maxVal-(scaleDis*3)-1)) +"-"+str(int(maxVal-(scaleDis*4)))
    draw.text((1200,1950),scale,font=font,fill="black")
    
    draw.rectangle(((900, 2000), (1200, 2050)), fill="#fd8d3c")
    scale = str(int(maxVal-(scaleDis*4)-1)) +"-"+str(int(maxVal-(scaleDis*5)))
    draw.text((1200,2000),scale,font=font,fill="black")
    
    draw.rectangle(((900, 2050), (1200, 2100)), fill="#feb24c")
    scale = str(int(maxVal-(scaleDis*5)-1)) +"-"+str(int(maxVal-(scaleDis*6)))
    draw.text((1200,2050),scale,font=font,fill="black")
    
    draw.rectangle(((900, 2100), (1200, 2150)), fill="#fed976")
    scale = str(int(maxVal-(scaleDis*6)-1)) +"-"+str(int(maxVal-(scaleDis*7)))
    draw.text((1200,2100),scale,font=font,fill="black")
    
    draw.rectangle(((900, 2150), (1200, 2200)), fill="#ffeda0")
    scale = str(int(maxVal-(scaleDis*7)-1)) +"-"+str(int(maxVal-(scaleDis*8)))
    draw.text((1200,2150),scale,font=font,fill="black")
    
    draw.rectangle(((900, 2200), (1200, 2250)), fill="#ffffcc")
    scale = str(int(maxVal-(scaleDis*8)-1)) +"-"+str(int(maxVal-(scaleDis*9)))
    draw.text((1200,2200),scale,font=font,fill="black")
    

def cagirFonk():
   
    img = Image.open('bitirme_guncel_foto.jpg')
    maxVal = 0
    scaleDis = 0
    point = []

    dsn_database = "userinformation"    # e.g. "MySQLdbtest"
    dsn_hostname = "localhost"          # e.g.: "mydbinstance.xyz.us-east-1.rds.amazonaws.com"
    dsn_port = 3306                     # e.g. 3306 
    dsn_uid = "root"                    # e.g. "user1"
    dsn_pwd = "123birkan"               # e.g. "Password123"

    conn = MySQLdb.connect(host=dsn_hostname, port=dsn_port, user=dsn_uid, passwd=dsn_pwd, db=dsn_database)

    cursor=conn.cursor()
    cursor.execute("""SELECT COUNT(koordinat), koordinat FROM dbson GROUP by koordinat ORDER by koordinat ASC""")

    rows = cursor.fetchall()
    for val in list(rows):
        #print(val)
        point.append(val[0])
          

    maxVal = max(point)
    scaleDis = maxVal/9

    draw = ImageDraw.Draw(img)
    legend(maxVal,scaleDis, draw)

    for index , val in enumerate(point):
        currentIndex = index+1
        color = calCal(val,scaleDis,maxVal)
        if currentIndex == 1:
            draw.ellipse(((1081, 331), (1151, 401)), fill=color) #1
        elif currentIndex == 2:
            draw.ellipse(((887, 403), (957, 473)), fill=color) #2
        elif currentIndex == 3:
            draw.ellipse(((955, 403), (1025, 473)), fill=color) #3
        elif currentIndex == 4:
            draw.ellipse(((1033, 403), (1103, 473)), fill=color) #4
        elif currentIndex == 5:
            draw.ellipse(((1111, 403), (1181, 473)), fill=color) #5
        elif currentIndex == 6:
            draw.ellipse(((247, 477), (317, 542)), fill=color) #6
        elif currentIndex == 7:
            draw.ellipse(((325, 477), (395, 547)), fill=color) #7
        elif currentIndex == 8:
            draw.ellipse(((403, 477), (473, 547)), fill=color) #8
        elif currentIndex == 9:
            draw.ellipse(((887, 477), (957, 547)), fill=color) #9
        elif currentIndex == 10:
            draw.ellipse(((959, 477), (1029, 547)), fill=color) #10 
        elif currentIndex == 11:
            draw.ellipse(((1033, 477), (1103, 547)), fill=color) #11
        elif currentIndex == 12:
            draw.ellipse(((247, 555), (317, 625)), fill=color) #12
        elif currentIndex == 13:
            draw.ellipse(((325, 555), (395, 625)), fill=color) #13
        elif currentIndex == 14:
            draw.ellipse(((888, 555), (958, 625)), fill=color) #14
        elif currentIndex == 15:
            draw.ellipse(((959, 555), (1029, 625)), fill=color) #15
        elif currentIndex == 16:
            draw.ellipse(((1033, 555), (1103, 625)), fill=color) #16
        elif currentIndex == 17:
            draw.ellipse(((919, 594), (989, 564)), fill=color) #17
        elif currentIndex == 18:
            draw.ellipse(((325, 633), (395, 703)), fill=color) #18
        elif currentIndex == 19:
            draw.ellipse(((403, 633), (473, 703)), fill=color) #19
        elif currentIndex == 20:
            draw.ellipse(((481, 633), (551, 703)), fill=color) #20
        elif currentIndex == 21:
            draw.ellipse(((559, 633), (629, 703)), fill=color) #21
        elif currentIndex == 22:
            draw.ellipse(((637, 633), (707, 703)), fill=color) #22
        elif currentIndex == 23:
            draw.ellipse(((715, 633), (785, 703)), fill=color) #23
        elif currentIndex == 24:
            draw.ellipse(((793, 633), (863, 703)), fill=color) #24
        elif currentIndex == 25:
            draw.ellipse(((871, 633), (941, 703)), fill=color) #25
        elif currentIndex == 26:
            draw.ellipse(((949, 633), (1019, 703)), fill=color) #26
        elif currentIndex == 27:
            draw.ellipse(((1004, 633), (1074, 703)), fill=color) #27
        elif currentIndex == 28:
            draw.ellipse(((403, 694), (473, 764)), fill=color) #28
        elif currentIndex == 29:
            draw.ellipse(((481, 694), (551, 764)), fill=color) #29
        elif currentIndex == 30:
            draw.ellipse(((559, 694), (629, 764)), fill=color) #30
        elif currentIndex == 31:
            draw.ellipse(((637, 694), (707, 764)), fill=color) #31
        elif currentIndex == 32:
            draw.ellipse(((715, 694), (785, 764)), fill=color) #32
        elif currentIndex == 33:
            draw.ellipse(((986, 694), (1056, 764)), fill=color) #33
        elif currentIndex == 34:
            draw.ellipse(((559, 772), (629, 842)), fill=color) #34
        elif currentIndex == 35:
            draw.ellipse(((637, 772), (707, 842)), fill=color) #35
        elif currentIndex == 36:
            draw.ellipse(((908, 772), (978, 842)), fill=color) #36
        elif currentIndex == 37:
            draw.ellipse(((986, 772), (1056, 842)), fill=color) #37
        elif currentIndex == 38:
            draw.ellipse(((820, 799), (890,869)), fill=color) #38
        elif currentIndex == 39:
            draw.ellipse(((1064, 799), (1134,869)), fill=color) #39
        elif currentIndex == 40:
            draw.ellipse(((403, 850), (473,920)), fill=color) #40
        elif currentIndex == 41:
            draw.ellipse(((481, 850), (551,920)), fill=color) #41
        elif currentIndex == 42:
            draw.ellipse(((559, 850), (629,920)), fill=color) #42
        elif currentIndex == 43:
            draw.ellipse(((752, 850), (822,920)), fill=color) #43
        elif currentIndex == 44:
            draw.ellipse(((1113, 850), (1183,920)), fill=color) #44
        elif currentIndex == 45:
            draw.ellipse(((360, 928), (430,998)), fill=color) #45
        elif currentIndex == 46:
            draw.ellipse(((559, 928), (629,998)), fill=color) #46
        elif currentIndex == 47:
            draw.ellipse(((715, 928), (785,998)), fill=color) #47
        elif currentIndex == 48:
            draw.ellipse(((1142, 928), (1212,998)), fill=color) #48
        elif currentIndex == 49:
            draw.ellipse(((350, 1003), (420,1073)), fill=color) #49
        elif currentIndex == 50:
            draw.ellipse(((574, 1003), (644,1073)), fill=color) #50
        elif currentIndex == 51:
            draw.ellipse(((651, 1003), (721,1073)), fill=color) #51
        elif currentIndex == 52:
            draw.ellipse(((715, 1003), (785,1073)), fill=color) #52
        elif currentIndex == 53:
            draw.ellipse(((1156, 1003), (1226,1073)), fill=color) #53
        elif currentIndex == 54:
            draw.ellipse(((1234, 1003), (1304,1073)), fill=color) #54
        elif currentIndex == 55:
            draw.ellipse(((350, 1081), (420,1151)), fill=color) #55
        elif currentIndex == 56:
            draw.ellipse(((574, 1081), (644,1151)), fill=color) #56
        elif currentIndex == 57:
            draw.ellipse(((651, 1081), (721,1151)), fill=color) #57
        elif currentIndex == 58:
            draw.ellipse(((715, 1081), (785,1151)), fill=color) #58
        elif currentIndex == 59:
            draw.ellipse(((1156, 1081), (1226,1151)), fill=color) #59
        elif currentIndex == 60:
            draw.ellipse(((1270, 1081), (1340,1151)), fill=color) #60
        elif currentIndex == 61:
            draw.ellipse(((350, 1159), (420,1229)), fill=color) #61
        elif currentIndex == 62:
            draw.ellipse(((423, 1159), (493,1229)), fill=color) #62
        elif currentIndex == 63:
            draw.ellipse(((520, 1159), (590,1229)), fill=color) #63
        elif currentIndex == 64:
            draw.ellipse(((760, 1159), (830,1229)), fill=color) #64
        elif currentIndex == 65:
            draw.ellipse(((1075, 1159),(1145, 1229)), fill=color)   #65
        elif currentIndex == 66:
            draw.ellipse(((1156, 1159),(1226, 1229)), fill=color)   #66
        elif currentIndex == 67:
            draw.ellipse(((1270, 1159),(1340, 1229)), fill=color)   #67
        elif currentIndex == 68:
            draw.ellipse(((350, 1237),(420, 1307)), fill=color)#68
        elif currentIndex == 69:
            draw.ellipse(((511, 1237),(581, 1307)), fill=color)#69
        elif currentIndex == 70:
            draw.ellipse(((762, 1237),(832, 1307)), fill=color)#70
        elif currentIndex == 71:
            draw.ellipse(((840, 1237),(910, 1307)), fill=color)#71
        elif currentIndex == 72:
            draw.ellipse(((919, 1237),(989, 1307)), fill=color)#72
        elif currentIndex == 73:
            draw.ellipse(((997, 1237),(1067, 1307)), fill=color)#73
        elif currentIndex == 74:
            draw.ellipse(((1075, 1237),(1145, 1307)), fill=color)#74
        elif currentIndex == 75:
            draw.ellipse(((1156, 1237),(1226, 1307)), fill=color)#75
        elif currentIndex == 76:
            draw.ellipse(((1270, 1237),(1340, 1307)), fill=color)#76
        elif currentIndex == 77:
            draw.ellipse(((350, 1315),(420, 1385)), fill=color)#77
        elif currentIndex == 78:
            draw.ellipse(((511, 1315),(581, 1385)), fill=color)#78
        elif currentIndex == 79:
            draw.ellipse(((762, 1315),(832, 1385)), fill=color)#79
        elif currentIndex == 80:
            draw.ellipse(((840, 1315),(910, 1385)), fill=color)#80
        elif currentIndex == 81:
            draw.ellipse(((997, 1315),(1067, 1385)), fill=color)#81
        elif currentIndex == 82:
            draw.ellipse(((1240, 1315),(1310, 1385)), fill=color)#82
        elif currentIndex == 83:
            draw.ellipse(((1275, 1315),(1345, 1385)), fill=color)#83
        elif currentIndex == 84:
            draw.ellipse(((1109, 1346),(1179, 1416)), fill=color)#84
        elif currentIndex == 85:
            draw.ellipse(((1193, 1346),(1263, 1416)), fill=color)#85
        elif currentIndex == 86:
            draw.ellipse(((1193, 1379),(1263, 1449)), fill=color)#86
        elif currentIndex == 87:
            draw.ellipse(((1263, 1380),(1333, 1450)), fill=color)#87
        elif currentIndex == 88:
            draw.ellipse(((350, 1393),(420, 1463)), fill=color)#88
        elif currentIndex == 89:
            draw.ellipse(((511, 1393),(581, 1463)), fill=color)#89
        elif currentIndex == 90:
            draw.ellipse(((589, 1393),(659, 1463)), fill=color)#90
        elif currentIndex == 91:
            draw.ellipse(((667, 1393),(737, 1463)), fill=color)#91
        elif currentIndex == 92:
            draw.ellipse(((745, 1393),(815, 1463)), fill=color)#92
        elif currentIndex == 93:
            draw.ellipse(((823, 1393),(893, 1463)), fill=color)#93  
        elif currentIndex == 94:
            draw.ellipse(((974, 1393),(1044, 1463)), fill=color)#93
        elif currentIndex == 95:
            draw.ellipse(((1048, 1393),(1118, 1463)), fill=color)#94
        elif currentIndex == 96:
            draw.ellipse(((1129, 1393),(1199, 1463)), fill=color)#95
        elif currentIndex == 97:
            draw.ellipse(((279, 1471),(349, 1541)), fill=color)#96
        elif currentIndex == 98:
            draw.ellipse(((350, 1471),(420, 1541)), fill=color)#97
        elif currentIndex == 99:
            draw.ellipse(((511, 1471),(581, 1541)), fill=color)#98
        elif currentIndex == 100:
            draw.ellipse(((605, 1471),(675, 1541)), fill=color)#98
        elif currentIndex == 101:
            draw.ellipse(((667, 1471),(737, 1541)), fill=color)#100
        elif currentIndex == 102:
            draw.ellipse(((745,1471),(815, 1541)), fill=color)#101
        elif currentIndex == 103:
            draw.ellipse(((823, 1471),(893, 1541)), fill=color)#102
        elif currentIndex == 104:
            draw.ellipse(((901, 1471),(971, 1541)), fill=color)#103
        elif currentIndex == 105:
            draw.ellipse(((974, 1471),(1044, 1541)), fill=color)#104
        elif currentIndex == 106:
            draw.ellipse(((279, 1549),(349, 1619)), fill=color)#105
        elif currentIndex == 107:
            draw.ellipse(((332, 1549),(402, 1619)), fill=color)#106
        elif currentIndex == 108:
            draw.ellipse(((511, 1549),(581, 1619)), fill=color)#107
        elif currentIndex == 109:
            draw.ellipse(((745, 1549),(815, 1619)), fill=color)#108
        elif currentIndex == 110:
            draw.ellipse(((823, 1549),(893, 1619)), fill=color)#109
        elif currentIndex == 111:
            draw.ellipse(((901, 1549),(971, 1619)), fill=color)#110
        elif currentIndex == 112:
            draw.ellipse(((333, 1627),(403, 1697)), fill=color)#111
        elif currentIndex == 113:
            draw.ellipse(((511, 1627),(581, 1697)), fill=color)#112
        elif currentIndex == 114:
            draw.ellipse(((333, 1705),(403, 1775)), fill=color)#113
        elif currentIndex == 115:
            draw.ellipse(((511, 1705),(581, 1775)), fill=color)#114
        elif currentIndex == 116:
            draw.ellipse(((333, 1783),(403, 1853)), fill=color)#115
        elif currentIndex == 117:
            draw.ellipse(((511, 1783),(581, 1853)), fill=color)#116
        elif currentIndex == 118:
            draw.ellipse(((424, 1825),(494, 1895)), fill=color)#117
        elif currentIndex == 119:
            draw.ellipse(((333, 1861),(403, 1931)), fill=color)#118
        elif currentIndex == 120:
            draw.ellipse(((511, 1861),(581, 1931)), fill=color)#119
        elif currentIndex == 121:
            draw.ellipse(((333, 1939),(403, 2009)), fill=color)#120
        elif currentIndex == 122:
            draw.ellipse(((511, 1939),(581, 2009)), fill=color)#121
        elif currentIndex == 123:
            draw.ellipse(((589, 1939),(659, 2009)), fill=color)#122
        elif currentIndex == 124:
            draw.ellipse(((333, 2017),(383, 2087)), fill=color)#123
        elif currentIndex == 125:
            draw.ellipse(((511, 2017),(581, 2087)), fill=color)#124
        elif currentIndex == 126:
            draw.ellipse(((589, 2017),(659, 2087)), fill=color)#125
        elif currentIndex == 127:
            draw.ellipse(((355, 2056),(425, 2126)), fill=color)#126
        elif currentIndex == 128:
            draw.ellipse(((234, 2104),(304, 2174)), fill=color)#127
        elif currentIndex == 129:
            draw.ellipse(((312, 2104),(382, 2174)), fill=color)#128
        elif currentIndex == 130:
            draw.ellipse(((234, 2182),(304, 2252)), fill=color)#129
        elif currentIndex == 131:
            draw.ellipse(((312, 2182),(382, 2252)), fill=color)#130
        elif currentIndex == 132:
            draw.ellipse(((427, 2080),(497, 2150)), fill=color)#131
        elif currentIndex == 133:
            draw.ellipse(((422, 2182),(492, 2252)), fill=color)#132
        elif currentIndex == 134:
            draw.ellipse(((422, 2260),(492, 2330)), fill=color)#133

    img.save("C:/Users/Birkan/Desktop/proje/static/imagetest.jpg","JPEG")
    return 1
