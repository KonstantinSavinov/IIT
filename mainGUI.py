from kivy.config import Config

Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '1440')
Config.set('graphics', 'height', '900')

import kivy

from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
import sqlite3 as lite

kivy.require("1.9.0")

from kivy.app import App
from kivy.properties import NumericProperty, StringProperty, ObjectProperty, Property, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter
import pymysql.cursors
from pymysql.connections import Connection
import employee
import finance as fl

MAX_TABLE_COLS = 3

connection: Connection = pymysql.connect(host='localhost',
                                         port=8889,
                                         user='root',
                                         password='root',
                                         db='hrdb')
cursorObject = connection.cursor()


class Edit(Screen):
    col_data = ListProperty(["?", "?", "?"])
    data_list = ListProperty(
        ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?",
         "?", "?", "?", "?", "?", "?"])

    def __init__(self, **kwargs):
        super(Edit, self).__init__(**kwargs)

    def hell0(self):
        attempt = employee.CheckInfo(self.col_data[0], self.col_data[1], self.col_data[2])
        self.result = attempt.find()

        for x in range(0, 28):
            self.data_list[x] = self.result[x]

    def package_changes(self, employeeid, address, addresscity, addressstate, addresszip, mob, dob, yob, healthCare,
                        married,
                        hireMonth, hireDay, hireYear, kParticipate, kContribution, pensionP, pensionC, unionP, payType,
                        payAmount, healthcareIns, dentalIns, opticalIns, healthTier):

        self.data_list[2] = address
        self.data_list[3] = addresscity
        self.data_list[4] = addressstate
        self.data_list[5] = addresszip
        self.data_list[6] = mob
        self.data_list[7] = dob
        self.data_list[8] = yob
        self.data_list[9] = healthCare
        self.data_list[11] = married
        self.data_list[12] = hireMonth
        self.data_list[13] = hireDay
        self.data_list[14] = hireYear
        self.data_list[16] = kParticipate
        self.data_list[17] = kContribution
        self.data_list[18] = pensionP
        self.data_list[19] = pensionC
        self.data_list[20] = unionP
        self.data_list[21] = payType
        self.data_list[22] = payAmount
        self.data_list[24] = healthcareIns
        self.data_list[25] = dentalIns
        self.data_list[26] = opticalIns
        self.data_list[27] = healthTier

        cursorObject.execute(
            "UPDATE `employeeprofile` SET `addressStreet`=%s,`addressCity`=%s,`addressState`=%s,`addressZip`=%s,`birthMonth`=%s,`birthDay`=%s,`birthYear`=%s,`healthcare`=%s,`married`=%s,`hireMonth`=%s,`hireDay`=%s,`hireYear`=%s WHERE `employeeID` = %s",
            (address, addresscity, addressstate, addresszip, mob, dob, yob, healthCare, married, hireMonth, hireDay,
             hireYear, employeeid))
        cursorObject.execute(
            "UPDATE `financeprofile` SET `kParticipate`=%s,`kContribution`=%s,`pensionParticipate`=%s,`pensionContribution`=%s,`unionParticipate`=%s,`payType`=%s,`payAmount`=%s WHERE `employeeID` = %s",
            (kParticipate, kContribution, pensionP, pensionC, unionP, payType, payAmount, employeeid))
        cursorObject.execute(
            "UPDATE `insuranceprofile` SET `healthcareInsurance`=%s,`dentalInsurance`=%s,`opticalInsurance`=%s,`healthTier`=%s WHERE `employeeID` = %s",
            (healthcareIns, dentalIns, opticalIns, healthTier, employeeid))
        connection.commit()
    def clear_edit(self):
        self.ids["address"].text = ""
        self.ids["addresscity"].text = ""
        self.ids["addressstate"].text = ""
        self.ids["addresszip"].text = ""
        self.ids["mob"].text = ""
        self.ids["dob"].text = ""
        self.ids["yob"].text = ""
        self.ids["healthCare"].text = ""
        self.ids["married"].text = ""
        self.ids["hireMonth"].text = ""
        self.ids["hireDay"].text = ""
        self.ids["hireYear"].text = ""
        self.ids["kParticipate"].text = ""
        self.ids["kContribution"].text = ""
        self.ids["pensionP"].text = ""
        self.ids["pensionC"].text = ""
        self.ids["unionP"].text = ""
        self.ids["payType"].text = ""
        self.ids["payAmount"].text = ""
        self.ids["healthcareIns"].text = ""
        self.ids["dentalIns"].text = ""
        self.ids["opticalIns"].text = ""
        self.ids["healthTier"].text = ""

    def on_click(self):
        self.clear_edit()
        self.manager.current = "main"




class PayRoll(Screen):
    col_data = ListProperty(["?", "?", "?"])
    data_list = ListProperty(
        ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?", "?",
         "?", "?", "?", "?", "?", "?"])

    def __init__(self, **kwargs):
        super(PayRoll, self).__init__(**kwargs)

    def hello(self):
        attempt = employee.CheckInfo(self.col_data[0], self.col_data[1], self.col_data[2])
        self.result = attempt.find()

        for x in range(0, 28):
            self.data_list[x] = self.result[x]

    def execute(self):
        app = App.get_running_app()
        empcheck = app.root.get_screen("employeecheck")
        empcheck.check_list = [
            self.result[22],
            self.result[11],
            self.result[4],
            self.result[10],
            self.result[0],
            self.result[1],

        ]

        empcheck.set_attempts()
        app.root.current = 'employeecheck'


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


choosed = None


class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    rv_data = ObjectProperty(None)
    start_point = NumericProperty(0)
    color = [0, 0, 0, 1]

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.background_color = [.98, .99, .98, 0]
        self.selected = not is_selected
        self.rv_data = rv.data

    def on_press(self):

        self.start_point = 0
        end_point = MAX_TABLE_COLS
        rows = len(self.rv_data) // MAX_TABLE_COLS
        for row in range(rows):
            if self.index in list(range(end_point)):
                break
            self.start_point += MAX_TABLE_COLS
            end_point += MAX_TABLE_COLS

        global choosed
        if not choosed:
            choosed = self
            choosed.background_color = [.30, .84, .84, .5]
        else:
            choosed.background_color = [.98, .99, .98, 0]
            choosed = self
            choosed.background_color = [.30, .84, .84, .5]

        buttons = self.parent.parent.parent.parent.parent.parent.children[0].children
        for i in buttons:
            i.disabled = False
            if i.text == 'just space':
                i.on_press = App.get_running_app()
                info_emp = i.on_press.root.get_screen('payroll')
                info_emp1 = i.on_press.root.get_screen('edit')
                info_emp.col_data = [
                    self.rv_data[self.start_point]['text'],
                    self.rv_data[self.start_point + 1]['text'],
                    self.rv_data[self.start_point + 2]['text']
                ]
                info_emp1.col_data = [
                    self.rv_data[self.start_point]['text'],
                    self.rv_data[self.start_point + 1]['text'],
                    self.rv_data[self.start_point + 2]['text']
                ]

                info_emp.hello()
                info_emp1.hell0()



            # here we can add functions that we wanna call
            # i.on_press = func


class LoginP(Screen):

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

    def check_attempt(self):

        userN = self.ids["login"].text
        passW = self.ids["password"].text

        while (userN != ""):
            attempt = employee.Login(userN, passW)
            attempt.databaseSearchId(attempt.get_temp_id())
            result = attempt.check_login()

            if (result == 1):
                self.manager.current = "main"
                self.resetForm()
                break
            elif (result == 0):
                Alert(title='Wrong Username and/or Password', text='Wrong Username and/or Password')
                self.resetForm()
                break


class MainMenu(Screen):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):
        cursorObject.execute(
            'SELECT `employeeID`, `lastName`, `firstName` from `employeeprofile` order by `employeeID` asc')
        rows = cursorObject.fetchall()

        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)



class Alert(Popup):

    def __init__(self, title, text):
        super(Alert, self).__init__()
        Config.set('graphics', 'resizable', '0')  # 0 being off 1 being on as in true/false
        Config.set('graphics', 'width', '1440')
        Config.set('graphics', 'height', '900')
        content = AnchorLayout(anchor_x='center', anchor_y='bottom')
        content.add_widget(
            Label(text=text, halign='left', valign='top')
        )
        ok_button = Button(text='Ok', size_hint=(0.3, 0.2))
        content.add_widget(ok_button)

        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.3, 0.2),
            auto_dismiss=True,
        )
        ok_button.bind(on_press=popup.dismiss)
        popup.open()


class EmployeeCheck(Screen):
    check_list = ListProperty(["?", "?", "?"])
    finance_info = ListProperty(["?", "?", "?", "?", "?","?", "?", "?","?"])

    def __init__(self, **kwargs):
        super(EmployeeCheck, self).__init__(**kwargs)

    def set_attempts(self):
        self.finance_info[0] = fl.get_federal_income_tax_deduction(int(self.check_list[0]), self.check_list[1])
        self.finance_info[1] = fl.get_medicare_deduction(int(self.check_list[0]))
        self.finance_info[2] = fl.get_state_income_tax_deduction(self.check_list[2], int(self.check_list[0]))
        self.finance_info[3] = fl.get_social_security_deduction(int(self.check_list[0]))
        self.finance_info[4] = fl.total_salary_deduction(int(self.check_list[0]), self.check_list[1],
                                                         self.check_list[2])
        self.finance_info[5] = self.check_list[3]
        self.finance_info[6] = self.check_list[4]
        self.finance_info[7] = self.check_list[5]
        self.finance_info[8] = self.check_list[0]


class AddPage(Screen):
    def addEmp(self):
        name = self.ids["fn"].text
        lastname = self.ids["ln"].text
        addressStreet = self.idf["streetadd"]
        addressCity = self.ids["cityadd"]
        addressState = self.ids["stateaddadd"]
        addresszip = self.ids["zipadd"]
        birthday = self.ids["bd"]
        birthmonth = self.ids["bm"]
        birthyear = self.ids["by"]
        healthcare = self.ids["healthc"]
        married = self.ids["marry"]
        hiremonth = self.ids["hirem"]
        hireday = self.ids["hired"]
        hireyear = self.ids["hirey"]

        kPar = self.ids["kpar"]
        kcon = self.ids["kcon"]
        penpar = self.ids["penpar"]
        pencon = self.ids["pencon"]
        upar = self.ids["upar"]
        payt = self.ids["payType"]
        pay = self.ids["pay"]

        hcare = self.ids["hcare"]
        dcare = self.ids["dcare"]
        ocare = self.ids["ocare"]
        htier = self.ids["htier"]


class ScreenManagement(ScreenManager):
    pass


class samplegui(App):
    def builder(self):
        return LoginP()


if __name__ == "__main__":
    samplegui().run()
