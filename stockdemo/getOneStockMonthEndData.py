import csv
import datetime
#from datetime import datetime
#ticker = 'ARRY'

def getHistoryDataFile(ticker):
    return 'data/IBB/'+ticker+'.csv'

# check if the date is month end
def isMonthEnd(line):
    # get each line's date
    s_date_str = line["Date"]
    #print(type(s_date_str))
    #print(s_date_str.__class__)
    s_date = datetime.datetime.strptime(s_date_str , '%Y-%m-%d').date()
    #print(type(s_date))
    #print(s_date.__class__)
    monthEndDate =  last_day_of_month(s_date)
    return s_date == monthEndDate

def last_day_of_month(any_day):
        next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
        return next_month - datetime.timedelta(days=next_month.day)

def getTickerMonthEndDataList(ticker):
    stock_m_end_data = []

    # open csv file
    his_data_file = getHistoryDataFile(ticker)
    with open(his_data_file, 'r') as f:
        readerCSV = csv.DictReader(f)
        print(readerCSV)

        # read line
        for i, line in enumerate(readerCSV):
            if isMonthEnd(line):
                # append result into list
                stock_m_end_data.append(line)

    return stock_m_end_data

result = getTickerMonthEndDataList('ARRY')
print(result)