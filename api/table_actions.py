import requests
from proxy import proxyDict
def getFastPlanTable(gp_name, gp_id):
    headers = {'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    url = "http://tplan.madi.ru/tasks/tableFiller.php"
    params = {
        'tab': '7',
        'gp_name': gp_name,
        'gp_id': gp_id}
    response = requests.post(url = url, data = params, headers=headers, proxies=proxyDict)
    response.encoding = 'utf-8'

    return(response.text)

def getExtPlanTable(gp_name, gp_id, sem_no, tp_year):
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
    response = requests.post(url = url, data = params, headers=headers, proxies=proxyDict)
    response.encoding = 'utf-8'

    return(response.text)


def getDeptPlanTable(dep_name, dep_id, sem_no, tp_year):
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
    response = requests.post(url = url, data = params, headers=headers, proxies=proxyDict)
    response.encoding = 'utf-8'

    return(response.text)


def getTeachPlanTable(teach_name, teach_id, sem_no, tp_year):
    headers = {'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    url = "http://tplan.madi.ru/tasks/tableFiller.php"
    params = {
        'tab': '8',
        'pr_name': teach_name,
        'pr_id': teach_id,       
        'sem_no': sem_no,
        'tp_year': tp_year}
    response = requests.post(url = url, data = params, headers=headers, proxies=proxyDict)
    response.encoding = 'utf-8'

    return(response.text)


if __name__ == '__main__':
    getFastPlanTable()


