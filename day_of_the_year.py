
def dayOfYear(date: str) -> int:
        date = date.replace('-', ' ')
        date_list = date.split()
        for i in range(len(date_list)):
            date_list[i] = int(date_list[i])
        month1 = [1,3,5,7,8,10,12]
        month2 = [4,6,9,11]
        month_days = 0
        for i in range((date_list[1]-1)):
            i +=1
            if i in month1:
                month_days += 31
            elif i in month2:
                month_days +=30
            else:
                if date_list[0]%400 == 0:
                    month_days += 29
                elif  date_list[0]%4 == 0 and not date_list[0]%100 == 0:
                    month_days += 29
                else:
                    month_days += 28

        return date_list[2] + month_days



print(dayOfYear("2000-03-01"))

#class Solution:
#    def dayOfYear(self, date: str) -> int:
#        y,m,d = map(int, date.split('-'))
#        if (y%400==0 or (y%100!=0 and y%4==0)) and m>2: d+=1
#        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#        for i in range(1, m):
#            d+=months[i-1]
#        return d