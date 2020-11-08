import requests
import json

from bs4 import BeautifulSoup


def getGroups(returnJson=0):
    headers = {'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    url = "http://tplan.madi.ru/tasks/task3,7_fastview.php"

    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.content, 'lxml')

    groups = {}
    for td in soup.findAll("ul"):
        for a in td.findAll("li"):
            groups[a.text.lower()] = a['value']

    if returnJson:
        return json.dumps(groups, ensure_ascii=False)
    return groups

def getGroupsList(returnJson=0):
    headers = {'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    url = "http://tplan.madi.ru/tasks/task3,7_fastview.php"

    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.content, 'lxml')

    groups = {}
    for td in soup.findAll("ul"):
        for a in td.findAll("li"):
            groups[a.text.lower()] = a.text.lower()

    if returnJson:
        return json.dumps(groups, ensure_ascii=False)

    return (groups)

def getDepart(returnJson=0):
    headers = {'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    url = "http://tplan.madi.ru/tasks/task11_kafview.php"

    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.content, 'lxml')

    departaments = {}
    for td in soup.findAll('tr'):
        for t in td.findAll('td'):
            for a in t.findAll('option'):
                departaments[a.text.lower()] = a['value']

    if returnJson:
        return json.dumps(departaments, ensure_ascii=False)

    return (departaments)

def getTeach(returnJson=0):
    headers = {'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    url = "http://tplan.madi.ru/tasks/task8_prepview.php"

    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.content, 'lxml')

    teaches = {}
    for td in soup.findAll('tr'):
        for t in td.findAll('td'):
            for a in t.findAll('option'):
                teaches[a.text.lower()] = a['value']

    if returnJson:
        return json.dumps(teaches, ensure_ascii=False)

    return (teaches)

def getFastPlan(gp_name, gp_id):
    headers = {'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    url = "https://tplan.madi.ru/tasks/tableFiller.php"
    params = {
        'tab': '7',
        'gp_id': gp_id}
    response = requests.post(url=url, data=params, headers=headers)
    response.encoding = 'utf-8'

    table_data = [[cell.text for cell in row()]
                  for row in BeautifulSoup(response.text, 'lxml')("tr")]

    dictOfWords = {i: table_data[i] for i in range(0, len(table_data))}

    return (json.dumps(dict(dictOfWords), ensure_ascii=False))

def getExtPlan(gp_name, gp_id, sem_no, tp_year):
    headers = {'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    url = "http://tplan.madi.ru/tasks/tableFiller.php"
    params = {
        'tab': '7',
        'gp_name': gp_name,
        'gp_id': gp_id,
        'sem_no': sem_no,
        'tp_year': tp_year}
    response = requests.post(url=url, data=params, headers=headers)
    response.encoding = 'utf-8'

    table_data = [[cell.text for cell in row()]
                  for row in BeautifulSoup(response.text, 'lxml')("tr")]

    dictOfWords = {i: table_data[i] for i in range(0, len(table_data))}

    return (json.dumps(dict(dictOfWords), ensure_ascii=False))

def getDeptPlan(dep_name, dep_id, sem_no, tp_year):
    headers = {'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    url = "http://tplan.madi.ru/tasks/tableFiller.php"
    params = {
        'tab': '11',
        'kf_name': dep_name,
        'kf_id': dep_id,
        'sort': 1,
        'sem_no': sem_no,
        'tp_year': tp_year}
    response = requests.post(url=url, data=params, headers=headers)
    response.encoding = 'utf-8'

    table_data = [[cell.text for cell in row()]
                  for row in BeautifulSoup(response.text, 'lxml')("tr")]

    dictOfWords = {i: table_data[i] for i in range(0, len(table_data))}

    return (json.dumps(dict(dictOfWords), ensure_ascii=False))

def getTeachPlan(tp_year, sem_no, teach_id, teach_name):
    headers = {'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    url = "https://tplan.madi.ru/tasks/tableFiller.php"
    #tab=8&tp_year=20&sem_no=1&pr_id=2162&pr_name=%D0%90%D0%B1%D0%B1%D0%B0%D1%81%D0%BE%D0%B2+%D0%AD.%D0%9C.

    params = {
        'tab': '8',
        'tp_year': tp_year,
        'sem_no': sem_no,
        'pr_id': teach_id,
        'pr_name': teach_name
        }
    response = requests.post(url=url, data=params, headers=headers)
    response.encoding = 'utf-8'

    table_data = [[cell.text for cell in row()]
                  for row in BeautifulSoup(response.text, 'lxml')("tr")]

    dictOfWords = {i: table_data[i] for i in range(0, len(table_data))}

    return (json.dumps(dict(dictOfWords), ensure_ascii=False))

def getGroupId(gp_name):
    allGp = getGroups()
    gp_id = allGp.get(gp_name)
    print(gp_id)
    return gp_id

if __name__ == '__main__':
    pr = getTeachPlan(tp_year='20', sem_no='1', teach_id='1711', teach_name='tets' )
    print(pr)

