import pytz
from datetime import datetime


def utc_to_asia_seoul_to_str(utc_dt):

    if not utc_dt:
        return None

    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    converted_utc_dt = datetime.strptime(utc_dt, date_format)

    local_tz = pytz.timezone("Asia/Seoul")
    local_dt = converted_utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)

    return local_dt.strftime("%Y-%m")
