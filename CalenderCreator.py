import datetime

class calendar_page():
	
    def __init__(self, input_month, input_year):
		self.month = input_month
		self.year = input_year
    
    def create_calendar_page(self):
        firstday=datetime.datetime(self.year, self.month, 1)
        first_weekday=firstday.isoweekday()
        monthes_with_31=(1, 3, 5, 7, 8, 10, 12)
        monthes_with_30=(4, 6, 9, 11)
        if self.month in monthes_with_31:
            num_days_in_month=31
        if self.month in monthes_with_30:
            num_days_in_month=30
        if self.month==2 and self.year%4==0:
            num_days_in_month=29
        if self.month==2 and self.year%4 !=0:
            num_days_in_month=28
        separator='--------------------\nMO TU WE TH FR SA SU\n--------------------\n'
        weeks='00 00 00 00 00 00 00\n00 00 00 00 00 00 00\n00 00 00 00 00 00 00\n00 00 00 00 00 00 00\n00 00 00 00 00 00 00\n'
        days_in_month=('xx', 'xx', 'xx', 'xx', 'xx', 'xx', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
        first_day=first_weekday
        month_begin = 7-first_day
        month_end=days_in_month.index(str(num_days_in_month))+1
        days_in_calendar=str(days_in_month[month_begin:month_end])
        days_in_calendar=days_in_calendar.replace(',', '')
        days_in_calendar=days_in_calendar.replace("'", '')
        days_in_calendar=days_in_calendar.replace("(", '')
        days_in_calendar=days_in_calendar.replace(")", '')
        item_begin=0
        item_end=20
        days_in_calendar2=''
        while item_end<len(days_in_calendar):
            days_in_calendar2=days_in_calendar2+days_in_calendar[item_begin:item_end]+'\n'
            last=item_end
            item_begin=item_begin+21
            item_end=item_end+21
        days_in_calendar2=days_in_calendar2+days_in_calendar[last+1:]
        self.text=separator+days_in_calendar2.replace('x', ' ')
        return (self.text)
    
    def print_calendar_page(self):
        str_month = ('', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
        print ("%s %s" %(str_month[self.month], self.year))
        print (self.text)

a = calendar_page(1, 2017) 
a.create_calendar_page()
a.print_calendar_page()

input ()