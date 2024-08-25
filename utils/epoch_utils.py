from datetime import datetime
import pytz


def epoch_to_datetime(epoch, timezone):
    try:
        if not timezone:
            timezone = "GMT"
        # Convert epoch to naive datetime (no timezone info)
        dt = datetime.fromtimestamp(int(epoch))
        # Set the desired timezone
        target_timezone = pytz.timezone(timezone)
        # Localize the datetime object to the desired timezone
        localized_datetime = dt.astimezone(target_timezone)
        return localized_datetime.strftime('%Y-%m-%d %H:%M:%S') + timezone
    except (ValueError, pytz.UnknownTimeZoneError) as e:
        return f"Error: {e}"
