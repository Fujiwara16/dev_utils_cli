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
        print(f"Error: {e}")


def curr_time(timezone):
    try:
        if not timezone:
            timezone = "GMT"
        # Get current time in epoch
        epoch = int(datetime.now().timestamp())
        # Set the desired timezone
        target_timezone = pytz.timezone(timezone)
        # Localize the datetime object to the desired timezone
        localized_datetime = datetime.now().astimezone(target_timezone)
        time = localized_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')
        formatter = TerminalFormatter()
        formatter.print_title()
        formatter.format_table([['Epoch', epoch], ['Timezone', timezone], ['Time', time]])
    except pytz.UnknownTimeZoneError as e:
        print(f"Error: {e}")


def date_time_to_epoch(datetime, timezone):
    try:
        if not timezone:
            timezone = "GMT"
        # Set the desired timezone
        target_timezone = pytz.timezone(timezone)
        # Convert the datetime string to a datetime object
        dt = datetime.strptime(datetime, '%Y-%m-%d %H:%M:%S')
        # Localize the datetime object to the desired timezone
        localized_datetime = target_timezone.localize(dt)
        # Convert the localized datetime to epoch
        epoch = int(localized_datetime.timestamp())
        time = localized_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')
        formatter = TerminalFormatter()
        formatter.print_title()
        formatter.format_table([['Datetime', datetime], ['Timezone', timezone], ['Epoch', epoch], ['Time', time]])
    except (ValueError, pytz.UnknownTimeZoneError) as e:
        print(f"Error: {e}")
