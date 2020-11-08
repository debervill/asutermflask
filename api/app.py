from flask import Flask, redirect, request
from manual import man
import actions
import table_actions as t_actions

app = Flask(__name__)
groups = actions.getGroups()
dept = actions.getDepart()
teach = actions.getTeach()

@app.route('/')
def hello():
    return redirect("/api/v1.0/manual", code=302)

@app.errorhandler(404)
def not_found(e):
  return redirect("/api/v1.0/manual", code=302) 

@app.route('/api/v1.0/tplan1', methods=['GET'])
def getTplan1():
    # http://127.0.0.1:5000/api/v1.0/tplan1?gp_name=2мбд1
    gp_name = request.args.get('gp_name', None)
    gp_id = groups[gp_name.lower()]
    return actions.getFastPlan(gp_name, gp_id)

@app.route('/api/v1.0/table/tplan1', methods=['GET'])
def getTableTplan1():
    # http://127.0.0.1:5000/api/v1.0/table/tplan1?gp_name=2мбд1
    gp_name = request.args.get('gp_name', None)
    gp_id = groups[gp_name.lower()]
    return t_actions.getFastPlanTable(gp_name, gp_id)

@app.route('/api/v1.0/tplan2', methods=['GET'])
def getTplan2():
    # http://127.0.0.1:5000/api/v1.0/tplan2?gp_name=2мбд1&sem_no=1&tp_year=19
    gp_name = request.args.get('gp_name', None)
    sem_no = request.args.get('sem_no', None)
    tp_year = request.args.get('tp_year', None)
    gp_id = groups[gp_name.lower()]
    return actions.getExtPlan(gp_name, gp_id, sem_no, tp_year)

@app.route('/api/v1.0/table/tplan2', methods=['GET'])
def getTableTplan2():
    # http://127.0.0.1:5000/api/v1.0/table/tplan2?gp_name=2мбд1&sem_no=1&tp_year=19
    gp_name = request.args.get('gp_name', None)
    sem_no = request.args.get('sem_no', None)
    tp_year = request.args.get('tp_year', None)
    gp_id = groups[gp_name.lower()]
    return t_actions.getExtPlanTable(gp_name, gp_id, sem_no, tp_year)

@app.route('/api/v1.0/dep_plan', methods=['GET'])
def getDplan():
    # http://127.0.0.1:5000/api/v1.0/dep_plan?dep_name=физики&sem_no=1&tp_year=19
    dep_name = request.args.get('dep_name', None)
    sem_no = request.args.get('sem_no', None)
    tp_year = request.args.get('tp_year', None)
    dep_id = dept[dep_name.lower()]
    return actions.getDeptPlan(dep_name, dep_id, sem_no, tp_year)

@app.route('/api/v1.0/table/dep_plan', methods=['GET'])
def getTableDplan():
    # http://127.0.0.1:5000/api/v1.0/table/dep_plan?dep_name=физики&sem_no=1&tp_year=19
    dep_name = request.args.get('dep_name', None)
    sem_no = request.args.get('sem_no', None)
    tp_year = request.args.get('tp_year', None)
    dep_id = dept[dep_name.lower()]
    return t_actions.getDeptPlanTable(dep_name, dep_id, sem_no, tp_year)

@app.route('/api/v1.0/teach_plan', methods=['GET'])
def getTeacPlan():
    # http://127.0.0.1:5000/api/v1.0/teach_plan?teach_name=суркова%20н.е.&sem_no=1&tp_year=19
    teach_name = request.args.get('teach_name', None)
    sem_no = request.args.get('sem_no', None)
    tp_year = request.args.get('tp_year', None)
    teach_id = teach[teach_name.lower()]
    return actions.getTeachPlan(tp_year, sem_no, teach_id, teach_name)

@app.route('/api/v1.0/table/teach_plan', methods=['GET'])
def getTableTeacPlan():
    # http://127.0.0.1:5000/api/v1.0/table/teach_plan?teach_name=суркова%20н.е.&sem_no=1&tp_year=19
    teach_name = request.args.get('teach_name', None)
    sem_no = request.args.get('sem_no', None)
    tp_year = request.args.get('tp_year', None)
    teach_id = teach[teach_name.lower()]
    return t_actions.getTeachPlanTable(teach_name, teach_id, sem_no, tp_year)

@app.route('/api/v1.0/groups', methods=['GET'])
def getGroupsDict():
    # http://127.0.0.1:5000/api/v1.0/groups
    return actions.getGroups(returnJson = 1)

@app.route('/api/v1.0/groupslist', methods=['GET'])
def getGroupsListDict():
    # http://127.0.0.1:5000/api/v1.0/groups
    return actions.getGroupsList(returnJson = 1)

@app.route('/api/v1.0/departaments', methods=['GET'])
def getDepartDict():
    # http://127.0.0.1:5000/api/v1.0/departaments
    return actions.getDepart(returnJson = 1)

@app.route('/api/v1.0/teaches', methods=['GET'])
def getTeachDict():
    # http://127.0.0.1:5000/api/v1.0/teaches
    return actions.getTeach(returnJson = 1)

@app.route('/api/v1.0/manual', methods=['GET'])
def getManual():
    # http://127.0.0.1:5000/api/v1.0/manual
    return man()

if __name__ == '__main__':
    app.run(debug=True, port=5501)
