class EmpDTO:
    def __init__(self, newempno, newename, newsal):
        self.empno = newempno
        self.ename = newename
        self.sal = newsal

    def getEmpno(self):
        return self.empno

    def setEmpno(self, newempno):
        self.empno = newempno

    def getEname(self):
        return self.ename
    
    def setEname(self, newename):
        self.ename = newename

    def getSal(self):
        return self.sal
    
    def setSal(self, newsal):
        self.sal = newsal

    def __str__(self):
        return 'EMPNO : ' + self.empno + ' / ENAME : ' + self.ename + ' / SAL : ' + self.sal
