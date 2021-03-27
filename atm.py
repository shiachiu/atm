
from datetime import *
td=datetime.today()   #傳回當下的日期和時間

def check(amount):    #自訂函數check:確認輸入金額是整數
    try:
        int(amount)
    except:
        result=False
    else:
        result=True
    finally:
        return result


account={}  #設立帳戶名稱和密碼的字典
money={}    #設立帳戶名稱和帳戶金額的字典        
number={}   #設立帳戶名稱和密碼輸入次數的字典
end=1
a=0
import getpass
import os
while True:      #主要程式迴圈
    a=0
    end=1
    print("歡迎使用ATM,很高興為你服務~")
    name = input("請輸入你的帳戶名稱\n還未有帳戶者,請先輸入0開戶(按 'Q' 離開ATM):")  
    if name == "0":   #還未有帳號，輸入0創建帳戶
        name = input("請輸入你的帳戶名稱:")
        while True:
            if name not in account:       #確認此帳戶名稱是否重複
                password = getpass.getpass('請輸入帳戶密碼：')    #設定密碼
                account[name]=password
                money[name]=0
                number[name]=0
                break
            else:   #已有的帳號，會請使用者輸入其他帳號名稱
                name = input("請輸入另一個帳戶名稱, 此名稱已被其他人使用:")
                
        while True:
            initial_amount=input("請輸入開戶金額:")    #輸入開戶金額
            if(not check(initial_amount)):      #確認是否為整數
                print("輸入錯誤的數字金額")
                continue
            elif int(initial_amount)<0:      #確認是否為正數
                print("輸入錯誤的數字金額")
                continue
            else:
                money[name] = int(initial_amount)   #成功建立帳戶
                print("帳戶名稱 %s 已建立"%(name))
                print()
                break
                os.system("cls")

    elif name == "Q":   #離開ATM
        break
    else:   #進入帳戶
        if name not in account:  #確認有此帳戶    
            print("此帳號尚未開戶")
            print()
            continue
        while a==0:
            password =getpass.getpass("\n請輸入帳戶密碼(輸入'1'進入另一個帳戶):")
            if password == "1":     #進入另一個帳戶
                break
            elif password!=account[name]:       #若輸入密碼錯誤，則累加輸錯的次數
                number[name]+=1
                if number[name]<3:              #輸錯3次內顯示將鎖卡提示、輸錯次數
                    print("密碼輸入錯誤,輸入三次將鎖卡")
                    print("已輸入",number[name],"次")
                else:          
                    print('密碼輸入錯誤,此帳戶已鎖卡。請洽至本銀行ATM使用金融卡變更密碼') #輸錯密碼3次，顯示鎖卡
                    account[name]='assdfgerv123-----'
                    print()
                    break
            else:
                number[name]=0  #如果輸入密碼成功，累加輸錯的次數會變成0
                while end!=0:       #進入ATM功能迴圈
                    print()
                    print('請選擇需要的業務:')
                    function=input("1:提款\n2:存款\n3:轉帳\n4:更改密碼\n5:餘額查詢\n") #功能表

                    while function=="1" or function=="2" or function=="3" or function=="4" or function=="5":
                        #1：提款
                        if function=="1":
                            withdraw_amount=input("請輸入提款金額:")   #輸入金額
                            if(not check(withdraw_amount)):            #檢查是否為整數
                                print("輸入錯誤的數字金額")
                                continue
                            elif int(withdraw_amount)<=0:            #檢查是否為正數
                                print("輸入錯誤的數字金額")
                                continue
                            elif money[name]<int(withdraw_amount):   #若輸入提款金額高於存款，顯示餘額不足
                                print("餘額不足")
                                print("\n是否要進行其他交易")
                                ree=input("輸入是:1或否:2")           #確認是否進行其他交易
                                if ree=="1":                          #回到功能選單
                                    break
                                else:
                                    print("\n結束交易,歡迎下次使用")  #結束功能
                                    function="end"
                                    end=0
                                    a=1
 
                            else:
                                money[name]-=int(withdraw_amount)       #從存款中扣除提款金額
                                print("將提出 %s 元"%(withdraw_amount))
                                print("請確認是否執行")
                                re=input("輸入是:1或否:2")               #確認是否提款
                                if re=="1":                              #印出執行結果
                                    print("已提出 %s 元,帳戶剩餘 %s 元"%(withdraw_amount,money[name]))
                                elif re=="2":                            #取消交易
                                    money[name]+=int(withdraw_amount)
                                    print("取消交易")
                                print("\n是否要進行其他交易")            #確認是否進行其他交易
                                ree=input("輸入是:1或否:2")
                                if ree=="1":                             #回到功能選單
                                    break
                                else:                                   
                                    print("\n結束交易,歡迎下次使用\n")   #結束功能
                                    function="end"
                                    end=0
                                    a=1

                        #2:存款
                        if function=="2":
                            deposit_amount=input("請輸入存款金額：")     #輸入金額
                            if(not check(deposit_amount)):               #檢查是否為整數
                                print("輸入錯誤的數字金額")
                                continue
                            elif int(deposit_amount)<0:               #檢查是否為正數
                                print("輸入錯誤的數字金額")
                                continue
                            else:
                                money[name]+=int(deposit_amount)         #加入存款金額
                                print("將存入 %s 元"%(deposit_amount))
                                print("\n請確認是否執行")                #確認是否存款
                                re=input("輸入是:1或否:2")
                                if re=="1":                              #印出執行結果
                                    print("\n已存入 %s 元,帳戶剩餘 %s元"%(deposit_amount,money[name]))
                                elif re=="2":                            #取消交易
                                    money[name]-=int(deposit_amount)
                                    print("取消交易")
                                print("\n是否要進行其他交易")            #確認是否進行其他交易
                                ree=input("輸入是:1或否:2")
                                if ree=="1":                             #回到功能選單
                                    break
                                else:
                                    print("\n結束交易,歡迎下次使用\n")   #結束功能
                                    function="end"
                                    end=0
                                    a=1
                                
                        #3:轉帳
                        if function=="3":
                            fee=15       #手續費
                            transfername = input("\n請輸入轉入帳戶名稱:")   #輸入轉入帳戶
                            while transfername not in account:              #確認有此帳戶
                                print("無此帳戶")
                                transfername = input("\n請輸入轉入帳戶名稱:")
                            transfer_amount = input("請輸入轉帳金額:")      #輸入轉帳金額
                            if(not check(transfer_amount)):       #確認是否為整數
                                print("輸入錯誤的數字金額")
                                continue
                            elif int(transfer_amount)<0:       #確認是否為正數
                                print("輸入錯誤的數字金額")
                                continue
                            else:
                                if money[name] >= int(transfer_amount)+fee:         #帳戶餘額大於轉帳金額加手續費
                                    money[transfername] += int(transfer_amount)     #進行轉帳
                                    money[name] -= int(transfer_amount)
                                    money[name] -= fee
                                    print("\n確認內容\n交易日期時間:",td,"\n轉出帳戶:",name, "\n轉入帳戶:",transfername,"\n轉帳金額:",transfer_amount,"\n手續費:",fee,"\n帳戶餘額:",money[name],"\n\n是否確認進行此項交易")
                                    re = input("輸入是:1或否:2")     #確認是否轉帳   
                                    if re == "1":                    #確認轉帳，印出結果
                                        print()
                                        print("交易結果-交易成功\n交易日期時間:",td,"\n轉出帳戶:",name,"\n轉入帳戶:",transfername,"\n轉帳金額:",transfer_amount,"\n手續費:",fee,"\n帳戶餘額:",money[name])
                                        print("\n是否要進行其他交易") #確認是否進行其他交易
                                        ree=input("輸入是:1或任意鍵結束交易")
                                        if ree=="1":                  #回到功能選單
                                            break
                                        else:
                                            print("\n結束交易,歡迎下次使用\n")  #結束功能
                                            function="end"
                                            end=0
                                            a=1

                                    else:
                                        print("取消交易")          #取消轉帳
                                        money[transfername] -= int(transfer_amount)
                                        money[name] += int(transfer_amount)
                                        money[name] += fee
                                        print("\n是否要進行其他交易")    #確認是否進行其他交易
                                        ree=input("輸入是:1或任意鍵結束交易")
                                        if ree=="1":                     #回到功能選單
                                            break
                                        else:                            #結束功能
                                            print("\n結束交易,歡迎下次使用\n") 
                                            function="end"
                                            end=0
                                            a=1

                                else:
                                    print("餘額不足")  #帳戶餘額小於轉帳金額加手續費
                                    print("\n是否要進行其他交易")  #確認是否進行其他交易
                                    ree=input("輸入是:1或任意鍵結束交易")  
                                    if ree=="1":                   #回到功能選單
                                        break
                                    else:                          #結束功能
                                        print("\n結束交易,歡迎下次使用\n")  
                                        function="end"
                                        end=0
                                        a=1


                        #4:更改密碼
                        if function == "4":
                            npassword = input("請輸入新的密碼：")               #輸入新密碼
                            npassword_check = input("請再輸入一次新的密碼：")   #檢查
                            while npassword != npassword_check:                 #密碼不符
                                print("輸入的新密碼與確認新密碼不符\n")         
                                npassword = input("請輸入新的密碼：")           #重新輸入密碼
                                npassword_check = input("請再輸入一次新的密碼：")
                            print("更改成功\n")                                 #檢查正確則更改成功
                            account[name]=npassword
                            print("是否要進行其他交易")                         #確認是否進行其他交易 
                            ree=input("輸入是:1或任意鍵結束交易")
                            if ree=="1":                                        #回到功能選單
                                break
                            else:
                                print("\n結束交易,歡迎下次使用\n")              #結束功能
                                function="end"
                                end=0
                                a=1

                        #5:餘額查詢
                        if function == "5":
                            re=input('\n帳戶餘額將: 1.顯示於螢幕 2.列印在明細表上')  #選擇呈現方式
                            if re=="1":                                              #顯示於螢幕
                                print('該帳戶餘額為',money[name],'元')
                                print("\n是否要進行其他交易")                        #確認是否進行其他交易  
                                ree=input("輸入是:1或任意鍵結束交易")
                                if ree=="1":                                         #回到功能選單
                                    break
                                else:                                                #結束功能
                                    print("\n結束交易,歡迎下次使用\n")    
                                    function="end"
                                    end=0
                                    a=1

                            elif re=="2":                               #列印在明細表
                                print('\n明細表列印中,請稍後...')        
                                print('[明細表]')
                                print('帳戶名稱:',name)
                                print('帳戶餘額$:',money[name])
                                print('交易日期時間:',td)
                                print("\n是否要進行其他交易")
                                ree=input("輸入是:1或任意鍵結束交易")            #確認是否進行其他交易
                                if ree=="1":                           #回到功能選單
                                    break
                                else:                                  #結束功能
                                    print("\n結束交易,歡迎下次使用\n")
                                    function="end"
                                    end=0
                                    a=1

                            else:        #如果沒選到1或2，會請使用者再選擇呈現方式
                                continue
                            
