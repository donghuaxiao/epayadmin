class SQLException(Exception):
    def __init__(self, message):
        super(SQLException, self).__init__(message)



class DateTimeFormatException(Exception):
    def __init__(self, message):
        super(DateTimeFormatException, self).__init__(message)