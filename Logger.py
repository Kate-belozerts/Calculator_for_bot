from datetime import datetime as dt


def logger(entered_number, name):
    time = dt.now()
    with open('log.csv', 'a') as file:
        file.write('{} - {}: {}'.format(time, name, entered_number))
        file.write('\n')
