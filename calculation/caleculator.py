from app_logger import log_recorder
from datetime import date
class flask_cal:
    def __init__(self):
        self.log = log_recorder.log_log()
        self.path = 'log_recorder/record_' + str(date.today()) + '.txt'
        self.my_file = open(self.path,'a+')
        self.msg = 'Successfully Rakesh Done'+ str(date.today())

    def caleculation(self,opt,num1,num2):
        if opt=='add':
            res = num2+num1
        if opt =='sub':
            res = num2-num1
        self.log.logger(self.my_file,self.msg)

        return res
