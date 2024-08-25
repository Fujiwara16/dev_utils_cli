from datetime import datetime
import pytz
from utils.formatter import TerminalFormatter


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
        time = localized_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')
        formatter = TerminalFormatter()
        formatter.print_title()
        formatter.format_table([['Epoch', epoch], ['Timezone', timezone], ['Time', time]])
    except (ValueError, pytz.UnknownTimeZoneError) as e:
        return f"Error: {e}"
