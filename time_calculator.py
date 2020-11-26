weekdays = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]


def get_modifiers(start_time):
    modifier = start_time[-2:]  # extract AM/PM from string
    initial_modifier = modifier  # backup the initial AM/PM
    AMPM_count = 0  # store the number of AM/PM changes
    return modifier, initial_modifier, AMPM_count


def calculate_interval(start_time, duration):  # + remove AM/PM from string
    hour = int(start_time[:-2].split(":")[0]) + int(duration.split(":")[0])
    minute = int(start_time[:-2].split(":")[1]) + int(duration.split(":")[1])
    if minute > 59:
        hour += 1
        minute -= 60
    return hour, minute


def set_modifiers(modifier, AMPM_count, hour_count):
    modifier = "AM" if modifier == "PM" else "PM"
    AMPM_count += 1
    hour_count -= 12
    return modifier, AMPM_count, hour_count


def process_AMPM_count(initial_modifier, AMPM_count):
    if AMPM_count % 2 != 0:  # round up the modifier
        if initial_modifier == "AM":
            AMPM_count -= 1
        elif initial_modifier == "PM":
            AMPM_count += 1
    return AMPM_count


def check_day(day, days_count, time):
    if day:  # if day parameter exists, update new time with the new weekday
        time += f", {weekdays[int((weekdays.index(day.title()) + days_count) % 7)]}"
    if days_count == 1:
        time += " (next day)"
    elif days_count > 1:
        time += f" ({int(days_count)} days later)"
    return time


# gets 3 parameters (2 required, 1 optional)
def add_time(start_time, duration, day=None):
    modif, init_modif, AMPM_count = get_modifiers(start_time)
    hour, minute = calculate_interval(start_time, duration)
    h_count = hour  # save the hours total

    while hour > 12:  # keep the time in the 12-hour clock format
        hour -= 12

    while h_count > 11:  # readjust the modifiers to the correct values
        modif, AMPM_count, h_count = set_modifiers(modif, AMPM_count, h_count)

    days_later = process_AMPM_count(init_modif, AMPM_count) / 2  # days counter
    new_time = f"{hour}:{str(minute).zfill(2)} {modif}"  # rebuild the time str

    return check_day(day, days_later, new_time)
