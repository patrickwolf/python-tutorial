import datetime

def log_warning(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print "%s, '%s'" % (now, msg)

if __name__ == '__main__':
    log_warning("test now")