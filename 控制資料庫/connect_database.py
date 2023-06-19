import mariadb
from mysql.connector import Error
user_setting = {
    "user" : "411077018",
    "password" : "411077018",
    "host" : "140.127.74.226",
    "database" : "411077018"
}

try:
    connection = mariadb.connect(**user_setting)
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    print("Connect Successful")
    while True:
        print("1.Find the customer who has bought the most (by price) in the past year.")
        print("2.Find the top 2 products by dollar-amount sold in the past year.")
        print("3.Find those products that are out-of-stock at every store in Kaohsiung.")
        print("4.Find those packages that were not delivered within the promised time.")
        print("5.Assume the package shipped by USPS with tracking number 123456 is reported to have been destroyed in an accident. Find the contact information for the customer. Also, find the contents of that shipment and create a new shipment of replacement items.")
        print("6.exit")
        print("Give my question number")
        check = input()
        if check == '1':
            cursor.execute("SELECT `線上客戶`.`名字`,`店內客戶`.`名字` as n FROM `訂單` JOIN `客戶` JOIN `線上客戶` JOIN `店內客戶` ON `訂單`.`身分證字號` = `客戶`.`身分證字號` AND `客戶`.`店內客戶id` = `店內客戶`.`店內客戶id` AND `客戶`.`線上客戶id` = `線上客戶`.`線上客戶id` GROUP by `訂單`.`身分證字號` HAVING SUM(`訂單`.`總價格`) order by n limit 1;")
            for (名字1, 名字2) in cursor:
                if 名字1 == 'NULL':
                    print("名字: %s" % (名字2))
                if 名字2 == 'NULL':
                    print("名字: %s" % (名字1))
                else:
                    print("名字: %s" % (名字1))
        if check == '2':
            cursor.execute("select `產品名稱`, `總價格` from `訂單` order by `總價格` desc limit 2")
            for (產品名稱,總價格) in cursor:
                print("產品名稱: %s, 總價格: %d" %(產品名稱,總價格))
        if check == '3':
            cursor.execute("SELECT `庫存`.`門市` , `庫存`.`產品id` , `庫存`.`產品名稱` FROM `庫存` WHERE `庫存`.`縣市` = '高雄' AND `庫存`.`產品數量` = 0;")
            for (門市,產品id,產品名稱) in cursor:
                number = cursor.rowcount
                cursor1.execute("SELECT COUNT(DISTINCT `庫存`.`門市`) FROM `庫存` WHERE `庫存`.`縣市` = '高雄';")
                for(number1) in cursor1:
                    number1_1 = int(number1[0])
                    if number == number1_1:
                        print("門市: %s , 產品名稱: %s" % (門市,產品名稱))
        if check == '4':
            cursor.execute("SELECT `追蹤號碼`,`產品名稱` FROM `訂單` WHERE `狀態` = '延誤';")
            for(追蹤號碼,產品名稱) in cursor:
                print("追蹤號碼: %s, 產品名稱: %s" %(追蹤號碼,產品名稱))
        if check == '5':
            cursor.execute("select `產品名稱`,`數量`,`促銷品` from `訂單` where `追蹤號碼` = 123456;")
            for(產品名稱,數量,促銷品) in cursor:
                print("產品名稱: %s, 數量: %s,促銷品: %s" %(產品名稱,數量,促銷品))
            cursor.execute("select `線上客戶`.`電話` , `店內客戶`.`電話` , `線上客戶`.`住址` , `店內客戶`.`住址` from `客戶` JOIN `訂單` JOIN `線上客戶` JOIN `店內客戶` on `客戶`.`身分證字號` = `訂單`.`身分證字號` AND `客戶`.`線上客戶id` = `線上客戶`.`線上客戶id` AND `客戶`.`店內客戶id` = `店內客戶`.`店內客戶id` where `訂單`.`追蹤號碼` = '123456' LIMIT 1;")
            for(電話1,電話2,住址1,住址2) in cursor:
                if 電話1 == 'NULL':
                    print("電話: %s 住址: %s" % (電話2,住址2))
                if 電話2 == 'NULL':
                    print("電話: %s 住址: %s" % (電話1,住址1))
                else:
                    print("電話: %s 住址: %s" % (電話1,住址1))
        if check == '6':
            break

except Error as e:
    print("Connect False.")
finally:
    cursor.close()
    connection.close()
    print("Close Database")