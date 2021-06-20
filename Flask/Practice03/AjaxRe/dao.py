import cx_Oracle

class EmpDAO:

    def empone(self, empno):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from emp01 where empno = :v", v = empno)
                row = cur.fetchone()

                data = '{"ename":"' + row[1] + '", "sal":' + str(row[2]) +'}'

            except Exception as e:
                print(e)

        finally:
            cur.close()
            conn.close()

        return data