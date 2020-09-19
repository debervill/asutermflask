import requests
import json


def getCountTable(table):
    a = 0
    # print(table)
    for i in table:
        if table[int(a)] == '':
            if table[int(a+1)] == '':
                if table[int(a+2)] == '':
                    a = a + 1
                    a = a + 1
                    break
        a = a + 1
    # print("A =================== ",int(a))
    return int((a)/6)


def getCountTable1(table):
    # print("1111111111111",table)
    a = 0
    # print(table)

    try:
        for i in range(len(table)):
            if table[i] == '':
                break

            else:
                a += 1
                # print("a === ",a)
    except TypeError:
        print("ошибка")
        a = 0
    # for i in table:
    #     if table[int(a)] == '':
    #         if table[int(a+1)] == '':
    #             a = a + 1
    #             break

        # a = a + 1
    # print("A =================== ",int(a))
    return int(a/6)


def GetPrep():
    # gp = requests.get('http://127.0.0.1:5501/api/v1.0/dep_plan?dep_name=%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%20%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F&sem_no=1&tp_year=20').json()
    gp = requests.get('http://127.0.0.1:5501/api/v1.0/teaches').json()
    return gp


def getGroup():
    gr = requests.get('http://127.0.0.1:5501/api/v1.0/groups').json()
    return gr


def getPrepRasp(NamePrep, DayOfWeek="Понедельник"):

    # print("Name Prep === ",NamePrep)
    try:
        grn = requests.get('http://127.0.0.1:5501/api/v1.0/teach_plan?teach_name=' +
                           NamePrep + '&sem_no=1&tp_year=20').json()
    except TypeError:
        grn = requests.get(
            'http://127.0.0.1:5501/api/v1.0/teach_plan?teach_name=баринов к.а.&sem_no=1&tp_year=20').json()
        table = ["", "", ""]
        return table
    a = 0
    j = 0
    table = ["", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", ""]

    # f = False
    for i in grn:

        # print(DayOfWeek)
        try:
            if grn[i][0] == DayOfWeek:
                #    print(i)
                #    print("find day of week, i = ",i)
                a = int(i) + 1
                if a > 36:
                    return table
                for j in grn:
                    a = a + 1
                    # print('j = ', int(j))
                    # print(a)

                    # print(len(grn[str(a)]))

                    if len(grn[str(a)]) == 1:
                        # print(table)
                        return table

                    table[6 * int(j)] = (grn[str(a)][0])
                    table[1 + 6 * int(j)] = (grn[str(a)][1])
                    table[2 + 6 * int(j)] = (grn[str(a)][2])
                    table[3 + 6 * int(j)] = (grn[str(a)][3])
                    table[4 + 6 * int(j)] = (grn[str(a)][4])
                    table[5 + 6 * int(j)] = (grn[str(a)][5])
        except KeyError:
            print("KeyError")
            for i in range(48):
                table[i] == ''
            return table


def getGroupRasp(NameGroup, DayOfWeek="Понедельник"):

    try:
        grn = requests.get(
            'http://127.0.0.1:5501/api/v1.0/tplan1?gp_name=' + NameGroup).json()
    except TypeError:
        grn = requests.get(
            'http://127.0.0.1:5501/api/v1.0/tplan1?gp_name=' + '1басу1').json()
        table = ["", "", ""]
        return table

    # print(DayOfWeek)
    # table = ["","","","","",""]
    a = 0
    j = 0
    table = ["", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", ""]

    # f = False
    for i in grn:
        try:
            # print(DayOfWeek)
            if grn[i][0] == DayOfWeek:
                #    print(i)

                a = int(i) + 1
                if a > 36:
                    return table
                for j in grn:
                    a = a + 1
                    # print('j = ', int(j))
                    # print(a)

                    # print(len(grn[str(a)]))
                    if len(grn[str(a)]) == 1:
                        return table

                    table[6 * int(j)] = (grn[str(a)][0])
                    table[1 + 6 * int(j)] = (grn[str(a)][1])
                    table[2 + 6 * int(j)] = (grn[str(a)][2])
                    table[3 + 6 * int(j)] = (grn[str(a)][3])
                    table[4 + 6 * int(j)] = (grn[str(a)][4])
                    table[5 + 6 * int(j)] = (grn[str(a)][5])
                # print(table)
                # print(len(grn[a + 1]))
                # if len(grn[str(a + 1)]) == 1:
                #     return table
        except KeyError:
            print("KeyError")
            for i in range(48):
                table[i] == ''
            return table


def getPrep(NamePrep):
    url = 'https://bazis.madi.ru/stud/schedule.php?teacher='
    tch = 'Остроух А.В.'
    req = url + tch
    prep = requests.get(req).json()
    print(prep)

    try:
        grn = requests.get('http://127.0.0.1:5501/api/v1.0/teach_plan?teach_name=' +
                           NamePrep + '&sem_no=1&tp_year=20').json()
    except TypeError:
        grn = requests.get(
            'http://127.0.0.1:5501/api/v1.0/teach_plan?teach_name=баринов к.а.&sem_no=1&tp_year=20').json()
        table = ["", "", ""]
        return table
    a = 0
    j = 0
    table = ["", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", "",
             "", "", "", "", "", ""]
    print(grn)
    f = False
    # for i in grn:

    #     # print(DayOfWeek)
    #     if grn[i][0] == DayOfWeek:
    #     #    print(i)

    #        a = int(i) + 1
    #        if a > 36:
    #            return table
    #        for j in grn:
    #             a = a + 1
    #             print('j = ', int(j))
    #             print(a)

    #             print(len(grn[str(a)]))
    #             if len(grn[str(a)]) == 1:
    #                 return table

    #             table[6 * int(j)] = (grn[str(a)][0])
    #             table[1 + 6 * int(j)] = (grn[str(a)][1])
    #             table[2 + 6 * int(j)] = (grn[str(a)][2])
    #             table[3 + 6 * int(j)] = (grn[str(a)][3])
    #             table[4 + 6 * int(j)] = (grn[str(a)][4])
    #             table[5 + 6 * int(j)] = (grn[str(a)][5])

# def getRaspPrep():
#     url = 'http://127.0.0.1:5501/api/v1.0/dep_plan?dep_name=%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%20%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F&sem_no=1&tp_year=20'
#     prep = requests.get(url).json()
#     print(prep)

# def getAllPrep():
#     allprep = requests.get('https://bazis.madi.ru/stud/schedule.php?teachers=1').json()
#     print(allprep)


if __name__ == '__main__':
    getPrep()
