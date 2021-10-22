import math
import datetime as dt


# a class that we can use in combination with observations in a dataset
# to instantiate new objects
class Respondent():
    respondentcnt=0
# respondentcnt incremented at each instantiation
# a dictionary of the observations information held in self.resp_dict
    def __init__(self,resp_dict):
        self.resp_dict = resp_dict
        Respondent.respondentcnt+=1
# calculates the number of children that they have
    def child_num(self):
        return self.resp_dict['childathome'] + self.resp_dict['childnotathome']
# calculates average weeks worked while accounting for null values
    def avgweeksworked(self):
        workdict = {k: v for k, v in self.resp_dict.items() if k.startswith('weeksworked') and not math.isnan(v)}
        nweeks = len(workdict)
        if (nweeks>0):
            avgww = sum(workdict.values())/nweeks
        else:
            avgww = 0
        return avgww
# calculates the age of the observation by a certain date
    def ageby(self, bydatestring):
        bydate = dt.datetime.strptime(bydatestring, '%Y%m%d') # parses the date from the string
        birthyear = self.resp_dict['birthyear']
        birthmonth = self.resp_dict['birthmonth']
        age = bydate.year - birthyear
        if (bydate.month<birthmonth or (bydate.month==birthmonth and bydate.day<15)):
            age = age -1
        return age
# shows whether or not observation has participated in college
    def baenrollment(self):
        colenrdict = {k: v for k, v in self.resp_dict.items() if k.startswith('colenr') and v=="3. 4-year college"}
        if (len(colenrdict)>0):
            return "Y"
        else:
            return "N"



