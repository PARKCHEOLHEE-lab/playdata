import cx_Oracle
from dto import EmpDTO
import json
import collections

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

    def empinsert(self, dto):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("insert into emp01 values (:empno, :ename, :sal)", \
                empno = dto.getEmpno(), ename = dto.getEname(), sal = dto.getSal()) 
            conn.commit()

        except Exception as e:
            print(e)
        
        finally:
            cur.close()
            conn.close()


    def empupdate(self, dto):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        cur.execute("update emp01 set ename=:ename, sal=:sal where empno=:empno", \
                    ename=dto.getEname(), empno=dto.getEmpno(), sal=dto.getSal())
        conn.commit()

        cur.close()
        conn.close()


    def empdelete(self, dto):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        cur.execute("delete from emp01 where empno=:empno", empno=dto.getEmpno())
        conn.commit()

        cur.close()
        conn.close()

    def empall(self):
        data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from emp01")
                rows = cur.fetchall()
                
                v = []
                for row in rows:
                    # print(row[0], row[1], row[2])
                    d = collections.OrderedDict()
                    d['empno'] = row[0]
                    d['ename'] = row[1]
                    d['sal'] = row[2]

                    v.append(d)
                    print(v)

                data = json.dumps(v, ensure_ascii=False) # auto json formatting library
                print(data)

            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data

# if __name__ == '__main__':
#     EmpDAO().emplist()

        
