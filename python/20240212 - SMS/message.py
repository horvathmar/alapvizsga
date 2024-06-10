class Message:
    def __init__(self, hour:int, minute:int, phone:str, text:str) -> None:
        self.hour = hour
        self.minute = minute
        self.phone = phone
        self.text = text    

        self.total_minutes = self.hour*60 + self.minute