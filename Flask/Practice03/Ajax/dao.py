# emp01 table의 crud 로직을 전담하는 class
import cx_Oracle

class EmpDAO:
    def empone(self, empno):  
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from emp01 where empno=:empno", empno=empno)  
                row = cur.fetchone()
                # print(row)
                
                data = '{"ename":"' + row[1] + '", "sal":' + str(row[2]) +'}'
                # print(data)

            except Exception as e:  
                print(e)  
        finally:
            cur.close()  
            conn.close()

        return data

# if __name__ == "__main__":
#     dao = EmpDAO()
#     print(dao.empone(7369))