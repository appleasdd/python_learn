import pygsheets #導入函式庫pygsheets
while True:
    try:
        gc = pygsheets.authorize(service_account_file = 'dht22-16877-da55a691f139.json')#取得金鑰
        gs_url ='https://docs.google.com/spreadsheets/d/17E901RYy4J4pnvWEUOROIx9rz06Gu9dnI0DBVr0IHv0/edit?usp=sharing'#輸入googlesheet位置
        sh = gc.open_by_url(gs_url)#開啟google sheets
        ws = sh.worksheet_by_title('工作表2')#開啟工作表2
        A7 = ws.get_value('A7')
        B7 = ws.get_value('B7')
        C7 = ws.get_value('C7')
        if bool(A7) == True:
            A3 = ws.get_value('A3')
            ws.update_value('A2',A3)
            B3 = ws.get_value('B3')
            ws.update_value('B2',B3)
            C3 = ws.get_value('C3')
            ws.update_value('C2',C3)

            A4 = ws.get_value('A4')
            ws.update_value('A3',A4)
            B4 = ws.get_value('B4')
            ws.update_value('B3',B4)
            C4 = ws.get_value('C4')
            ws.update_value('C3',C4)

            A5 = ws.get_value('A5')
            ws.update_value('A4',A5)
            B5 = ws.get_value('B5')
            ws.update_value('B4',B5)
            C5 = ws.get_value('C5')
            ws.update_value('C4',C5)

            A6 = ws.get_value('A6')
            ws.update_value('A5',A6)
            B6 = ws.get_value('B6')
            ws.update_value('B5',B6)
            C6 = ws.get_value('C6')
            ws.update_value('C5',C6)

            A7 = ws.get_value('A7')
            ws.update_value('A6',A7)
            B7 = ws.get_value('B7')
            ws.update_value('B6',B7)
            C7 = ws.get_value('C7')
            ws.update_value('C6',C7)

            ws.update_value('A7','')
            ws.update_value('B7','')
            ws.update_value('C7','')
    except:
        break
