import datetime


class Logger:
    def __init__(self):
        self.log_file = 'logfile.txt'
        self.clear_log_file()

    def log(self, message):
        with open(self.log_file, 'a') as log:
            timestamp = datetime.datetime.now().strftime("%m-%d %H:%M:%S")
            log.write(f'{timestamp}:{message}/n')

    def clear_log_file(self):
        open(self.log_file, 'w').close()
