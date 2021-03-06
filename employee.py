import pymysql.cursors
from pymysql.connections import Connection
import mainGUI
import uuid

class Employee:

    def __init__(self):
        print("connected")
    __id = ""
    __pass = ""
    __first_name = ""
    __last_name = ""
    __addressStreet= ""
    __addressCity = ""
    __addressState =""
    __addressZip = ""
    __day_of_birth = ""
    __month_of_birth = ""
    __year_of_birth = ""
    __health_care = ""
    __employee_id = ""
    __married = ""
    __hireDay =""
    __hireMonth=""
    __hireYear=""
    __kParticipation=""
    __kContribution = ""
    __pension = ""
    __pensionCon =""
    __union = ""
    __payType=""
    __payAmount = ""
    __hInsurance = ""
    __dInsurance = ""
    __oInsurance = ""
    __hTier = ""

    __row = ""
    __status = ""

    connection: Connection = pymysql.connect(host='localhost',
                                             port=8889,
                                             user='root',
                                             password='root',
                                             db='hrdb')

    cursorObject = connection.cursor()

    def find(self):
        result = []
        result2 = []
        result3 = []

        try:

            connection: Connection = pymysql.connect(host='localhost',
                                                     port=8889,
                                                     user='root',
                                                     password='root',
                                                     db='hrdb')

            cursorObject = connection.cursor()

            cursorObject.execute(
                'SELECT * FROM `employeeprofile` WHERE employeeID ="' + self.__employee_id + '"' + ' AND firstName ="' + self.__first_name + '"' +
                ' AND lastName ="' + self.__last_name + '"')
            numrows = cursorObject.fetchall()
            for row in numrows:
                for col in row:
                    result.append(col)

            cursorObject.execute(
                'SELECT * FROM `financeprofile` WHERE employeeID ="' + self.__employee_id + '"')
            numrows2 = cursorObject.fetchall()
            for row in numrows2:
                for col in row:
                    result2.append(col)

            cursorObject.execute(
                'SELECT * FROM `insuranceprofile` WHERE employeeID ="' + self.__employee_id + '"')
            numrows3 = cursorObject.fetchall()
            for row in numrows3:
                for col in row:
                    result3.append(col)

            finalresult = result + result2 + result3

            return finalresult
        except:
            print("Employee Not Found")






    def databaseSearchId(self, idSelect, cursorObject=cursorObject):

        try:

            cursorObject.execute('SELECT username FROM login WHERE username ="' + idSelect + '"')
            result = str(cursorObject.fetchone()[0])
            cursorObject.execute('SELECT password FROM login WHERE username ="' + idSelect + '"')
            result1 = str(cursorObject.fetchone()[0])
            self.set_id(str(result))
            self.set_pass(str(result1))
        except:
            print("Id is not found")

    def databaseInsert(self, connection=connection, cursorObject=cursorObject):
        check_name = self.get_first_name()
        check_last = self.get_last_name()
        check_d = self.get_day_of_birth()
        check_m = self.get_month_of_birth()
        check_y = self.get_year_of_birth()
        searchstatus = bool

        cursorObject.execute('SELECT employeeID FROM employeeprofile WHERE firstName ="' + check_name + '"' +
                             ' AND lastName ="' + check_last + '"' + ' AND birthDay ="' + check_d + '"' + ' AND birthMonth ="' + check_m + '"' + ' AND birthYear ="' + check_y + '"')
        row_count = cursorObject.rowcount
        if row_count == 0:
            searchstatus = False
        else:
            searchstatus = True

        if (searchstatus == False):

                with connection.cursor() as cursor:
                    # Create a new record
                    sql = "INSERT INTO `employeeprofile` (`firstName`, `lastName`, `addressStreet`,`addressCity`,`addressState`,`addressZip`,`birthMonth`," \
                          "`birthDay`,`birthYear`,`healthcare`,`employeeID`,`married`,`hireMonth`,`hireDay`,`hireYear`)" \
                          'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    sql1 = "INSERT INTO `insuranceprofile` (`employeeID`,`healthcareInsurance`," \
                           "`dentalInsurance`,`opticalInsurance`,`healthTier`)" \
                           'VALUES (%s, %s, %s, %s, %s)'
                    sql2 = "INSERT INTO `financeprofile` (`employeeID`,`kParticipate`,`kContribution`," \
                           "`pensionParticipate`,`pensionContribution`,`unionParticipate`,`payType`,`payAmount`)" \
                           'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                    cursor.execute(sql,
                                   (
                                    self.__first_name, self.__last_name, self.__addressStreet,self.__addressCity,self.__addressState, \
                                    self.__addressZip,self.__month_of_birth,self.__day_of_birth,  \
                                    self.__year_of_birth, self.__health_care, self.__employee_id, self.__married, self.__hireMonth, \
                                    self.__hireDay, self.__hireYear)
                                   )
                    cursor.execute(sql2,
                                   (self.__employee_id, self.__kParticipation, self.__kContribution, self.__pension, self.__pensionCon, \
                                    self.__union, self.__payType, self.__payAmount))
                    cursor.execute(sql1,
                                   (self.__employee_id, self.__health_care, self.__dInsurance, self.__oInsurance, \
                                    self.__hTier))
                connection.commit()

                print("Successfully inserted")
                return 1
        else:
            print("Employee Already in the system")
            return 0

    # Getters

    def get_status(self):
        return self.__status

    def get_id(self):
        return self.__id

    def get_pass(self):
        return self.__pass

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_address_street(self):
        return self.__addressStreet

    def get_address_city(self):
        return self.__addressCity

    def get_address_State(self):
        return self.__addressState

    def get_address_Zip(self):
        return self.__addressZip

    def get_day_of_birth(self):
        return self.__day_of_birth

    def get_month_of_birth(self):
        return self.__month_of_birth

    def get_year_of_birth(self):
        return self.__year_of_birth

    def get_health_care(self):
        return self.__health_care


    def get_employee_id(self):
        return self.__employee_id

    def get_married(self):
        return self.__married

    def get_hInsurance(self):
        return self.__hInsurance

    def get_dInsurance(self):
        return self.__dInsurance

    def get_oInsurance(self):
        return self.__oInsurance

    def get_hTier(self):
        return self.__hTier

    def get_kParticipation(self):
        return self.__kContribution

    def get_kContribution(self):
        return self.__kContribution

    def get_pension(self):
        return self.__pension

    def get_pension_con(self):
        return self.__pensionCon

    def get_union(self):
        return self.__union

    def get_pay_type(self):
        return self.__payType

    def get_pay_amount(self):
        return self.__payAmount

    def get_row(self):
        return self.__row

    def get_hireDay(self):
        return self.__hireDay

    def get_hireMonth(self):
        return self.__hireMonth

    def get_hireYear(self):
        return self.__hireYear

    # Setters

    def set_status(self, stat):
        self.__status = stat

    def set_id(self, id):
        self.__id = id

    def set_pass(self, password):
        self.__pass = password

    def set_first_name(self, firstName):
        self.__first_name = firstName

    def set_last_name(self, lastName):
        self.__last_name = lastName

    def set_address_street(self, addRess):
        self.__addressStreet = addRess
    def set_address_city(self, addRess):
        self.__addressCity = addRess
    def set_address_state(self, addRess):
        self.__addressState = addRess
    def set_address_zip(self, addRess):
        self.__addressZip = addRess

    def set_day_of_birth(self, birthDay):
        self.__day_of_birth = birthDay

    def set_month_of_birth(self, birthMonth):
        self.__month_of_birth = birthMonth

    def set_year_of_birth(self, birthYear):
        self.__year_of_birth = birthYear

    def set_health_care(self, healthCare):
        self.__health_care = healthCare


    def set_employee_id(self, employeeId):
        self.__employee_id = employeeId

    def set_married(self, married):
        self.__married = married

    def set_hInsurance(self, hInsurance):
        self.__hInsurance = hInsurance

    def set_dInsurance(self, dInsurance):
        self.__dInsurance = dInsurance

    def set_oInsurance(self, oInsurance):
        self.__oInsurance = oInsurance

    def set_hTier(self, hTier):
        self.__hTier = hTier

    def set_kParticipation(self, kPar):
        self.__kParticipation = kPar

    def set_kContribution(self, kContribution):
        self.__kContribution = kContribution

    def set_pension(self, pension):
        self.__pension = pension

    def set_pensionCon(self, pension):
        self.__pensionCon = pension

    def set_union(self, unionDues):
        self.__union = unionDues

    def set_pay_type(self, payType):
        self.__payType = payType

    def set_pay_amount(self, payAmount):
        self.__payAmount = payAmount

    def set_row(self, row):
        self.__row = row

    def set_hired(self, day):
        self.__hireDay = day
    def set_hirem(self, m):
        self.__hireMonth = m
    def set_hirey(self, y):
        self.__hireYear = y


class Login(Employee):
    temp_id = ""
    temp_pass = ""
    attempts = 3

    def __init__(self, loginid, loginpass):
        self.set_temp_id(loginid)
        self.set_temp_pass(loginpass)


    def set_temp_id(self, tempId):
        self.temp_id = tempId
    def set_temp_pass(self, tempPass):
        self.temp_pass = tempPass
    def get_temp_id(self):
        return self.temp_id
    def get_temp_pass(self):
        return self.temp_pass

    def check_login(self):

        if self.temp_id == self.get_id() and self.temp_pass == self.get_pass():
            self.set_status(1)
            return self.get_status()
        else:
            self.set_status(0)
            return self.get_status()


class Register(Employee):
    def __init__(self, firstName, lastName, addressStr, addressC, addressStt, addressZip, dayofbirth, monthofbirth, yearofbirth, healthcare, married, hInsur, dInsur, oInsur, hTie, kCon,kPar, pens,penCon, union, payt, paa,d,m,y):


        temp_id = self.generateID()


        self.set_employee_id(str(temp_id)[:10])
        self.set_first_name(firstName)
        self.set_last_name(lastName)
        self.set_address_street(addressStr)
        self.set_address_city(addressC)
        self.set_address_state(addressStt)
        self.set_address_zip(addressZip)
        self.set_day_of_birth(dayofbirth)
        self.set_month_of_birth(monthofbirth)
        self.set_year_of_birth(yearofbirth)
        self.set_health_care(healthcare)
        self.set_married(married)
        self.set_hInsurance(hInsur)
        self.set_dInsurance(dInsur)
        self.set_oInsurance(oInsur)
        self.set_hTier(hTie)

        self.set_kContribution(kCon)
        self.set_kParticipation(kPar)
        self.set_pension(pens)
        self.set_pensionCon(penCon)
        self.set_union(union)
        self.set_pay_type(payt)
        self.set_pay_amount(paa)

        self.set_hired(d)
        self.set_hirem(m)
        self.set_hirey(y)

    def generateID(self):
        return uuid.uuid4().fields[-1]

class CheckInfo(Employee):
    def __init__(self, employeeID, lastName, firstName):

        self.set_employee_id(employeeID)
        self.set_last_name(lastName)
        self.set_first_name(firstName)
