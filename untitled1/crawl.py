import requests
from lxml import html
import ocr
from Results.models import Student, Marks
import xlrd
i = 1
gpa = 0
name = []
names = []
result = []
lsubs = []
loc = ("USN.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
while True:
    try:
        USN = sheet.cell_value(i, 0)
        batch = USN[3:5]
    except:
        break
    gpa = 0
    s = requests.Session()
    headers = {'Referer': 'http://results.vtu.ac.in/vitaviresultcbcs2018/index.php',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                   'Upgrade-Insecure-Requests': '1',  'Cookie': 'PHPSESSID=u47uot7eg9j6eglqm951e3nfr7'
            , 'Connection': 'keep-alive'}
    image = s.get("http://results.vtu.ac.in/resultsvitavicbcs_19/captcha_new.php", headers=headers)
    with open("snap.png", 'wb') as file:
        file.write(image.content)
    cap = ocr.get_ocr("snap.png")
    #USN = "1BI17CS"+str(format(i, '03d'))
    url = "http://results.vtu.ac.in/resultsvitavicbcs_19/resultpage.php"
    payload = {'lns': USN, 'captchacode': str(cap),
                   'token': 'SkZEaFZ0NHlScGZrZTNPc05SaU5zMGxySUQ2OUVNSndJV0NTMnN2MGx3djdVVmlEQkU5YWRFMTZCaEVvT0M0LzVYQ0NOY3Zxd1VKR2lKQkJNR21ERWc9PTo6mTLywDmsbx4cz1V4K2gfNw==',
                   'current_url': 'http://results.vtu.ac.in/resultsvitavicbcs_19/index.php'}
    page = s.post(url, data=payload, headers=headers)
    tree = html.fromstring(page.content)
    print("Sent USN:-"+USN)
   # print("Sent USN:-1BI17CS"+str(format(i, '03d')))
    print("Sent Captcha:"+ocr.get_ocr("snap.png"))
    if "Invalid captcha code !!!" in page.text:
        print("Invalid captcha code !!!")
        continue
    else:
        i += 1
    if "Redirecting to VTU Results Site" in page.text:
        print("Alert:-Token Expired!!:Update new token in Payload")
        exit(2)
    if "University Seat Number is not available or Invalid..!" in page.text:
        print("University Seat Number is not available or Invalid..!")
        exit(-1)
    temp = page.text.find("Student Name")
    name.clear()
    while (page.text[temp + 61] != "<"):
        name.insert(len(name), page.text[temp + 61])
        temp += 1
    names.insert(len(names), ''.join(name))
    if("Semester : 5" in page.text):
        iresult = {
            "USN": "-",
            "Name": "-",
            "sub1": "-",
            "sub2": "-",
            "sub3": "-",
            "sub4": "-",
            "sub5": "-",
            "sub6": "-",
            "sub7": "-",
            "sub8": "-",
            "15CS51": [0, 0, 0, 0],
            "15CS52": [0, 0, 0, 0],
            "15CS53": [0, 0, 0, 0],
            "15CS54": [0, 0, 0, 0],
            "15CSL57": [0, 0, 0, 0],
            "15CSL58": [0, 0, 0, 0],
            "15ME562": [0, 0, 0, 0],
            "15CS564": [0, 0, 0, 0],
            "15CS562": [0, 0, 0, 0],
            "15PHY561": [0, 0, 0, 0],
            "15CS553": [0, 0, 0, 0],
        }
        imarks1 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[3]')[0].text)
        imarks2 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/div[3]')[0].text)
        imarks3 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div[3]')[0].text)
        imarks4 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[5]/div[3]')[0].text)
        imarks5 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[6]/div[3]')[0].text)
        imarks6 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[7]/div[3]')[0].text)
        imarks7 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[8]/div[3]')[0].text)
        imarks8 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[9]/div[3]')[0].text)
        emarks1 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[4]')[0].text)
        emarks2 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/div[4]')[0].text)
        emarks3 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div[4]')[0].text)
        emarks4 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[5]/div[4]')[0].text)
        emarks5 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[6]/div[4]')[0].text)
        emarks6 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[7]/div[4]')[0].text)
        emarks7 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[8]/div[4]')[0].text)
        emarks8 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[9]/div[4]')[0].text)
        tmarks1 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[5]')[0].text)
        tmarks2 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/div[5]')[0].text)
        tmarks3 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div[5]')[0].text)
        tmarks4 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[5]/div[5]')[0].text)
        tmarks5 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[6]/div[5]')[0].text)
        tmarks6 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[7]/div[5]')[0].text)
        tmarks7 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[8]/div[5]')[0].text)
        tmarks8 = int(tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[9]/div[5]')[0].text)
        result1 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[6]')[0].text
        result2 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/div[6]')[0].text
        result3 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div[6]')[0].text
        result4 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[5]/div[6]')[0].text
        result5 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[6]/div[6]')[0].text
        result6 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[7]/div[6]')[0].text
        result7 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[8]/div[6]')[0].text
        result8 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[9]/div[6]')[0].text
        sub1 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]')[0].text
        sub2 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/div[1]')[0].text
        sub3 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div[1]')[0].text
        sub4 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[5]/div[1]')[0].text
        sub5 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[6]/div[1]')[0].text
        sub6 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[7]/div[1]')[0].text
        sub7 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[8]/div[1]')[0].text
        sub8 = tree.xpath('/html/body/div[2]/form/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[9]/div[1]')[0].text
        iresult["USN"] = USN
        iresult["Name"] = ''.join(name)
        iresult[sub1] = [imarks1, emarks1, tmarks1, result1]
        iresult[sub2] = [imarks2, emarks2, tmarks2, result2]
        iresult[sub3] = [imarks3, emarks3, tmarks3, result3]
        iresult[sub4] = [imarks4, emarks4, tmarks4, result4]
        iresult[sub5] = [imarks5, emarks5, tmarks5, result5]
        iresult[sub6] = [imarks6, emarks6, tmarks6, result6]
        iresult[sub7] = [imarks7, emarks7, tmarks7, result7]
        iresult[sub8] = [imarks8, emarks8, tmarks8, result8]
        iresult['sub1'] = sub1
        iresult['sub2'] = sub2
        iresult['sub3'] = sub3
        iresult['sub4'] = sub4
        iresult['sub5'] = sub5
        iresult['sub6'] = sub6
        iresult['sub7'] = sub7
        iresult['sub8'] = sub8
        result.insert(len(result), iresult)
    else:
        continue
count = 1
for i in result:
    length = len(result)
    s1 = i['sub1']
    s2 = i['sub2']
    s3 = i['sub3']
    s4 = i['sub4']
    s5 = i['sub5']
    s6 = i['sub6']
    s7 = i['sub7']
    s8 = i['sub8']
    print(str(count)+"/"+str(length))
    count += 1
    student = Student()
    student.usn = i["USN"]
    student.name = i["Name"]
    student.save()
    marks1 = Marks()
    marks1.usn = student
    marks1.sub_code = i['sub1']
    marks1.internal = i[s1][0]
    marks1.external = i[s1][1]
    marks1.total = i[s1][2]
    marks1.result = i[s1][3]
    marks1.save()
    marks2 = Marks()
    marks2.usn = student
    marks2.sub_code = i['sub2']
    marks2.internal = i[s2][0]
    marks2.external = i[s2][1]
    marks2.total = i[s2][2]
    marks2.result = i[s2][3]
    marks2.save()
    marks3 = Marks()
    marks3.usn = student
    marks3.sub_code = i['sub3']
    marks3.internal = i[s3][0]
    marks3.external = i[s3][1]
    marks3.total = i[s3][2]
    marks3.result = i[s3][3]
    marks3.save()
    marks4 = Marks()
    marks4.usn = student
    marks4.sub_code = i['sub4']
    marks4.internal = i[s4][0]
    marks4.external = i[s4][1]
    marks4.total = i[s4][2]
    marks4.result = i[s4][3]
    marks4.save()
    marks5 = Marks()
    marks5.usn = student
    marks5.sub_code = i['sub5']
    marks5.internal = i[s5][0]
    marks5.external = i[s5][1]
    marks5.total = i[s5][2]
    marks5.result = i[s5][3]
    marks5.save()
    marks6 = Marks()
    marks6.usn = student
    marks6.sub_code = i['sub6']
    marks6.internal = i[s6][0]
    marks6.external = i[s6][1]
    marks6.total = i[s6][2]
    marks6.result = i[s6][3]
    marks6.save()
    marks7 = Marks()
    marks7.usn = student
    marks7.sub_code = i['sub7']
    marks7.internal = i[s7][0]
    marks7.external = i[s7][1]
    marks7.total = i[s7][2]
    marks7.result = i[s7][3]
    marks7.save()
    marks8 = Marks()
    marks8.usn = student
    marks8.sub_code = i['sub8']
    marks8.internal = i[s8][0]
    marks8.external = i[s8][1]
    marks8.total = i[s8][2]
    marks8.result = i[s8][3]
    marks8.save()