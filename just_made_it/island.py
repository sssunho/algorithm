import subprocess
from subprocess import PIPE
from bs4 import BeautifulSoup as BS
import urllib.parse

f = subprocess.Popen("curl -s -k -X GET https://url.you.want", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, error = f.communicate()
html = BS(output, 'html.parser')

# 내가 얻고싶은 요소
viewstate = html.find('input', attrs={'id': '__VIEWSTATE'})
eventvalidation = html.find('input', attrs={'id': '__EVENTVALIDATION'})

def send_mail(mail_to, subject, message, mail_from='sunny@ciceron.me'):
    # 주어진 messasge를 메일로 날려준다.
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    content = MIMEText(message, 'html', _charset='utf-8')
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = '<%s>' % mail_from
    msg['To'] = str(mail_to)
    msg.attach(content)

    a = smtplib.SMTP('smtp.gmail.com:587')
    a.ehlo()
    a.starttls()
    a.login('abc@email.com', 'password')
    a.sendmail('abc@email.com', str(mail_to), msg.as_string())
    a.quit()

def check_ticket(month, date):
    # 검색 조건
    data = {
        'F_Port': 10110,
        'T_Port': 96380,
        'f_year': 2017,
        'f_month': month,
        'f_day': date,
        'btnSearch.x': 72,
        'btnSearch.y': 1,
        'Header1$CheckLoc_Row': 2,
        'Header1$CheckLoc_Row2': 4,
        'Side_new1$CheckLoc_Row': 4,
        '__EVENTVALIDATION': eventvalidation['value'],
        '__VIEWSTATE': viewstate['value'],
        '__EVENTTARGET': None,
        '__EVENTARGUMENT': None
    }
    query_string = urllib.parse.urlencode(data)

    url = 'https://url.you.want'
    f = subprocess.Popen("curl -s -k -d '"+query_string+"' -X POST "+url, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, error = f.communicate()
    html = BS(output, 'html.parser')

    pnlFareDetail = html.find('div', attrs={'id': 'pnlFareDetail'})
    text = pnlFareDetail.get_text()
    text = text.split()

    # 내가 원했던 이메일 보내는 조건
    if text[8] != '0' or text[17] != '0':
        mail_content = """
        {} 월 {} 일 자리났습니다!
        """.format(month, date)

        send_mail(
            'abcde@email.com',
            '예매하세요!!!',
            mail_content
        )
