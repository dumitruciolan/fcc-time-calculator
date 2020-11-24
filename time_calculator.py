weekdays = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
days_later = 0


def remove_am_pm(start_time):
    start_time.pop(1)
    start_time = ''.join(start_time)
    return start_time


def calculate_time(start, duration, position):
    return int(start.split(":")[position]) + int(duration.split(":")[position])


def update_mins_and_hours(minute, hour):
    if minute > 59:
        minute -= 60
        hour += 1
    return minute, hour


def update_modifs(modifiers_later, modifier, hour_modifier):
    modifiers_later += 1
    modifier = "AM" if modifier == "PM" else "PM"
    hour_modifier -= 12
    return modifiers_later, modifier, hour_modifier


def switch_between_am_pm(initial_modifier, modifiers_later):
    if initial_modifier == "AM":
        modifiers_later -= 1
    elif initial_modifier == "PM":
        modifiers_later += 1
    return modifiers_later


def check_if_its_next_day(days_later, new_time):
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({int(days_later)} days later)"
    return new_time


# gets 3 parameters (2 required, 1 optional)
def add_time(start_time, duration, day=None):
    modifs_l8r = 0  # stores the number of AM/PM changes

    start_time = start_time.split(" ")  # convert into list type
    modif = start_time[1]  # get the initial AM/PM
    temp_modif = modif  # save the initial AM/PM

    start_time = remove_am_pm(start_time)  # get the time without AM/PM
    minute = calculate_time(start_time, duration, 1)  # retrieve the minutes
    hour = calculate_time(start_time, duration, 0)  # retrieve the hour
    minute, hour = update_mins_and_hours(minute, hour)
    h_modif = hour  # save the hour modifier

    while hour > 12:  # keep the hour in the AM/PM format
        hour -= 12

    while h_modif > 11:  # recalculate the modifiers
        modifs_l8r, modif, h_modif = update_modifs(modifs_l8r, modif, h_modif)

    if modifs_l8r % 2 != 0:  # switch between AM and PM
        modifs_l8r = switch_between_am_pm(temp_modif, modifs_l8r)

    days_later = modifs_l8r / 2  # check how many days later it is
    new_time = f"{hour}:{str(minute).zfill(2)} {modif}"  # prepare return value

    if day:  # if day parameter exists, update the return value with the new weekday
        new_time += f", {weekdays[int((weekdays.index(day.title()) + days_later) % 7)]}"

    new_time = check_if_its_next_day(days_later, new_time)

    return new_time
