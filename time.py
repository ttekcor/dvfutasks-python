class Time:
    # Конструктор, принимающий четыре целых числа: часы, минуты, секунды и миллисекунды.
    # В случае, если передан отрицательный параметр, вызвать исключение ValueError.
    # После конструирования, значения параметров времени должны быть корректными:
    # 0 <= GetHour() <= 23
    # 0 <= GetMinute() <= 59
    # 0 <= GetSecond() <= 59
    # 0 <= GetMillisecond() <= 999
    hours = 0
    def __init__(self, hours=0, minutes=0, seconds=0, milliseconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.milliseconds = milliseconds
    def GetHour(hours):
        if hours>=24:
            hours = hours%24
    def GetMinute(self,minutes,hours):
        if minutes>60:
            hours += minutes/60
            minutes = minutes%60
    def GetSecond(self,seconds,minutes):
        if seconds>60:
            minutes += seconds/60
            seconds = seconds%60
    def GetMillisecond(self,milliseconds,seconds):
        if milliseconds>1000:
            seconds += milliseconds/1000
            milliseconds = seconds%1000
    # Прибавляет указанное количество времени к текущему объекту.
    # После выполнения этой операции параметры времени должны остаться корректными.
    def Add(self, time):
        pass
    # Оператор str должен представлять время в формате
    # HH:MM:SS.milliseconds
    def __str__(self):
        print(({Time.GetHour(self)}+':'+{Time.GetMinute(self)}+':'+{Time.GetSecond(Time.seconds)}+'.'+{Time.GetMillisecond(Time.milliseconds)}))

time = Time(25, 11, 12, 1)
print(str(time))