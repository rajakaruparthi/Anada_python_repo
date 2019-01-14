
def convert_epoch_to_time(epoch_time):
    sec = int(epoch_time % 60)
    minutes = int(epoch_time % 3600 / 60)
    hours = int(epoch_time % 86400 / 3600)
    days = int(epoch_time / 86400)
    return ("" if days == 0 else parse_time(days) + ":") + parse_time(hours) + ":" + parse_time(
        minutes) + ":" + parse_time(sec)


def parse_time(input):
    return "0" + str(input) if input < 10 else str(input)
