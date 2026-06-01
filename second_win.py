#tambahan p2
def timer1Event(self):
    global time
    time - time.addSecs(-1)
    self.text_timer.setText(time.toString("hh:mm:ss"))
    self.text_timer.setStyleSheet("color: rgb(0,0,0)")
    self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
    if time.toString("hh:mm:ss") == "00:00:00":
        self.timer.stop()
def timer2Event(self):
    global time
    time - time.addSecs(-1)
    self.text_timer.setText(time.toString("hh:mm:ss"))[6:8])
    self.text_timer.setStyleSheet("color: rgb(0,0,0)")
    self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
    if time.toString("hh:mm:ss") == "00:00:00":
        self.timer.stop()
def timer3Event(self):
    global time
    time - time.addSecs(-1)
    self.text_timer.setText(time.toString("hh:mm:ss"))
    if int(time.toString(hh:mm:ss")[6:8]) >= 45:
        self.text_timer.setStyleSheet("color: rgb(0,255,0)")
    elif int(time.toString(hh:mm:ss")[6:8]) <= 15:
        self.text_timer.setStyleSheet("color: rgb(0,255,0)")
    else:
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
    self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
    if time.toString("hh:mm:ss") == "00:00:00":
        self.timer.stop()
def connects(self):
    self.btn_next.clicked.connect(self.next_click)
    self.btn_test1.clicked.connect(self.timer_test) #tambahkan
    self.btn_test2.clicked.connect(self.timer_sits) #tambahkan
    self.btn_test3.clicked.connect(self.timer_final) #tambahkan

      
