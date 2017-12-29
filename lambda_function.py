import os
from datetime import datetime
from exchanges.blockchain import currentprice

#SITE = os.environ['site']  # URL of the site to check, stored in the site environment variable


def lambda_handler(event, context):
    print('Checking bitcoin price at {}...'.format(event['time']))
    try:
        print('Current bitcoin price in GBP is: ', currentprice(currency='GBP'))
    except:
        print('Check failed!')
        raise
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))

