def man():
    return(
        '''
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <title>Инструкция к API "Расписание МАДИ"</title>
            </head>
            <body>
                <h2>Получить список групп</h2>                
                <p><a href=/api/v1.0/groups>/api/v1.0/groups</a></p>

                <h2>Получить список кафедр</h2>
                <p><a href=/api/v1.0/departaments>/api/v1.0/departaments</a></p>

                <h2>Получить список преподавателей</h2>
                <p><a href=/api/v1.0/teaches>/api/v1.0/teaches</a></p>

                <h2>Получить расписание для группы в json (метод GET)</h2>                
                <p><a href=/api/v1.0/tplan1?gp_name=2мбд1>/api/v1.0/tplan1?&ltgp_name&gt</a></p>
                
                <h2>Получить расписание для группы в HTML (метод GET)</h2>
                <p><a href=/api/v1.0/table/tplan1?gp_name=2мбд1>/api/v1.0/table/tplan1?&ltgp_name&gt</a></p>

                <h2>Получить расширенное расписание для группы в json (метод GET)</h2>                
                <p><a href=/api/v1.0/tplan2?gp_name=2мбд1&sem_no=1&tp_year=19>/api/v1.0/tplan2?&ltgp_name&gt&&ltsem_no&gt&&lttp_year&gt</a></p>
                
                <h2>Получить расширенное расписание для группы в HTML (метод GET)</h2>
                <p><a href=/api/v1.0/table/tplan2?gp_name=2мбд1&sem_no=1&tp_year=19>/api/v1.0/table/tplan2?&ltgp_name&gt&&ltsem_no&gt&&lttp_year&gt</a></p>

                <h2>Получить расписание по кафедре в json (метод GET)</h2>                
                <p><a href=/api/v1.0/dep_plan?dep_name=физики&sem_no=1&tp_year=19>/api/v1.0/dep_plan?&ltdep_name&gt&&ltsem_no&gt&&lttp_year&gt</a></p>
                
                <h2>Получить расписание по кафедре в HTML (метод GET)</h2>
                <p><a href=/api/v1.0/table/dep_plan?dep_name=физики&sem_no=1&tp_year=19>/api/v1.0/table/dep_plan?&ltdep_name&gt&&ltsem_no&gt&&lttp_year&gt</a></p>

                <h2>Получить расписание по преподавателю в json (метод GET)</h2>                
                <p><a href=/api/v1.0/teach_plan?teach_name=суркова%20н.е.&sem_no=1&tp_year=19>/api/v1.0/teach_plan?&ltteach_name&gt&&ltsem_no&gt&&lttp_year&gt</a></p>
                
                <h2>Получить расписание по преподавателю в HTML (метод GET)</h2>
                <p><a href=/api/v1.0/table/teach_plan?teach_name=суркова%20н.е.&sem_no=1&tp_year=19>/api/v1.0/table/teach_plan?&ltteach_name&gt&&ltsem_no&gt&&lttp_year&gt</a></p>

            </body>
            </html>
        '''
    )