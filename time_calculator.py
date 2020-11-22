weekdays = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
days_later = 0


def calculate_time(start, duration, position):
    return int(start.split(":")[position]) + int(duration.split(":")[position])


def calculate_hours(minute, hour):
    if minute > 59:
        minute -= 60
        hour += 1
    return minute, hour


def update_modifs(hour_modifier, modifier, modifiers_later):
    hour_modifier -= 12
    modifier = "PM" if modifier == "AM" else "AM"
    modifiers_later += 1
    return hour_modifier, modifier, modifiers_later


def am_pm_switch(initial_modifier, modifiers_later):
    if initial_modifier == "PM":
        modifiers_later += 1
    else:
        modifiers_later -= 1
    return initial_modifier, modifiers_later


def check_new_day(days_later, new_time):
    if days_later == 1:  # check if it's next day
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({int(days_later)} days later)"
    return days_later, new_time


# gets 3 parameters (2 required, 1 optional)
def add_time(start_time, duration, day=None):
    modifs_l8r = 0  # the number of AM/PM changes
    start_time = start_time.split(" ")  # retrieve the time
    modif = start_time[1]  # get the initial AM/PM
    init_modif = modif  # save the initial AM/PM

    start_time.pop(1)  # remove AM/PM
    start_time = ''.join(start_time)  # get time without AM/PM

    hour = calculate_time(start_time, duration, 0)  # retrieve the hour
    minute = calculate_time(start_time, duration, 1)  # retrieve the minutes

    minute, hour = calculate_hours(minute, hour)  # calculate the hours
    h_modif = hour

    while hour > 12:  # keep the hour in the AM/PM format
        hour -= 12

    while h_modif > 11:  # update the modifiers
        h_modif, modif, modifs_l8r = update_modifs(h_modif, modif, modifs_l8r)

    if modifs_l8r % 2 != 0:  # switch between AM and PM
        init_modif, modifs_l8r = am_pm_switch(init_modif, modifs_l8r)

    days_later = modifs_l8r / 2  # check how many days later it is
    new_time = f"{hour}:{str(minute).zfill(2)} {modif}"

    # check if day parameter exists
    if day:
        weekday = weekdays.index(day.title())
        new_weekday = int((weekday + days_later) % 7)
        new_time += f", {weekdays[new_weekday]}"

    # check if it's next day
    days_later, new_time = check_new_day(days_later, new_time)

    return new_time
