import os

import xlsxwriter


def make_report(f,headers,table):
    workbook = None

    try:
        # workbook = xlsxwriter.Workbook('reports\\report'+str(datetime.datetime.today())+'.xlsx')
        workbook = xlsxwriter.Workbook(f)
        worksheet = workbook.add_worksheet()

        for i, header in enumerate(headers):
            worksheet.write(0, i, header)
        for i in range(table.rowCount()):
            for j in range(table.columnCount() - 1):
                text = table.item(i, j).text()
                worksheet.write(i + 1, j, text)


    except Exception as e:

        return
    finally:
        workbook.close()
    os.system("start " + '\"' + f + '\"')
