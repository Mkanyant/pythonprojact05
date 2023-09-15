#return not values
#หมายถึง การสิ้นสุดหรือจบการทำงานของ Block Scope การทำงานหนึ่ง เมื่อมันถูกทำงาน

def func1( ) :
    print('AAA')
    print('BBB')
    return
    print('ccc')

def func2( x ) :
    return
    print(f'X is {x}')

func1( )
func2( 10 )