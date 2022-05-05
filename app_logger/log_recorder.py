from datetime import datetime
class log_log:
    def __init__(self):
        pass
    def logger(self,file_name,message):
        self.file = file_name
        self.msg = message
        self.date = datetime.today()
        file_name.write(message+str(self.date))
