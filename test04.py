#รับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้
#และคำนวณหาผลรวมและค่าเฉลี่ยของข้อมูลที่รับเข้ามาเป็นเท่าใด
#แล้วแสดงผลทางหน้าจอ

#ขอ 4 ฟังก์ชัน ดังนั้นหาให้ได้4 feature

#=========================================
#Program Average 5Number
#=========================================
#Enter number 1 : <input>
#Enter number 2 : <input>
#Enter number 3 : <input>
#Enter number 4 : <input>
#Enter number 5 : <input>
#=========================================
#Sum of 5 number is : <output>
#Average of 5 number is : <output> (ทศนิยม 4 ตำแหน่ง)

def inputnumber( ) :
    n1= int(input('ใส่เลขที่ 1 : '))
    n2= int(input('ใส่เลขที่ 2 : '))
    n3= int(input('ใส่เลขที่ 3 : '))
    n4= int(input('ใส่เลขที่ 4 : '))
    n5= int(input('ใส่เลขที่ 5 : '))
    return n1, n2, n3, n4, n5

def Sumofnumber(n1, n2, n3, n4, n5) :
    Sumofnumber = ((n1 + n2 + n3 + n4 + n5))
    return Sumofnumber

def Averageofnumber(n1, n2, n3, n4, n5) :
    Averageofnumber = ((n1 + n2 + n3 + n4 + n5)/5)
    return Averageofnumber

def Show(n1, n2, n3, n4, n5, Sumofnumber, Averageofnumber) :
    print(f'ผลรวมเลขทั้ง 5 : {Sumofnumber} ')
    print(f'ค่าเฉลี่ยเลขทั้ง 5 : {Averageofnumber:.4f} ')


print('===============================================')
print('=========Program Average 5 Number==============')
print('===============================================')
n1, n2, n3, n4, n5 = inputnumber( )
print('===============================================')
Sumofnumber = Sumofnumber(n1, n2, n3, n4, n5)
Averageofnumber = Averageofnumber(n1, n2, n3, n4, n5)
Show(n1, n2, n3, n4, n5, Sumofnumber, Averageofnumber)
print('===============================================')