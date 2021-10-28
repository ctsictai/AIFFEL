import pytz
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def utc_to_asia_seoul_to_str(utc_dt):

    if not utc_dt:
        return None

    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    converted_utc_dt = datetime.strptime(utc_dt, date_format)

    local_tz = pytz.timezone("Asia/Seoul")
    local_dt = converted_utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)

    local_dt.strftime("%Y-%m-%d")
    local_dt_gte = local_dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    local_dt_lt = local_dt + relativedelta(months=1)
    local_dt_lt = local_dt_lt.replace(day=1, hour=0, minute=0, second=0, microsecond=0) - timedelta(microseconds=1)

    return local_dt_gte, local_dt_lt
