from datetime import datetime
from dateutil.tz import gettz


def epoch_to_datetime(epoch, timezone='GMT'):
    try:
        # Convert epoch to datetime
        # localise the datetime object to the timezone

        dt = datetime.fromtimestamp(int(epoch))
        local_timezone = gettz(timezone)
        localized_datetime = dt.replace(tzinfo=local_timezone)
        return localized_datetime.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return "Invalid epoch value."
