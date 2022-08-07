def add_time(start, duration, day=None):

    # The start time will have 'AM' or 'PM' after it,
    # so we separate this from the actual time.
    start_time = start.split(" ")

    # The time is stored in a 'hh:mm' format, so we retrieve
    # the hour and minutes, which is stored in a list where
    # the hour and minutes have index values of 0 and 1
    # respectively.
    start_hr_min = start_time[0].split(":")
    # Get the hours and minutes of the duration time, in the
    # same format as start_hr_min
    duration_hr_min = duration.split(":")


    # We need to know whether the initial time was at AM or PM,
    # so that we know whether or not a day has passed when the
    # time reaches 12 o'clock.
    old_am_pm = start_time[1]

    # NOTE: Stores minutes first, then the hour.
    # We store it in this format so that it is easier to increment
    # the time. We need to account for the fact that the hour
    # increases if the added minutes are greater than 59.
    min_hr = list()
    min_hr.append(int(start_hr_min[1]) + int(duration_hr_min[1]))
    min_hr.append(int(start_hr_min[0]) + int(duration_hr_min[0]))

    # Holds the values for the new time
    new_minutes = 0
    new_hour = 0
    new_am_pm = old_am_pm
    # Holds the new day of the week
    new_day = day
    # We need to know the initial hour. If the initial time
    # is already in the 12th hour, then AM does not suddenly
    # become PM and vice-versa.
    hour_before = min_hr[1]
    # We need to know how many hours have passed when we add
    # the start minutes to the duration minutes.
    hours_passed_from_minutes = 0
    # We can use the number of days passed to calculate the
    # new day of the week.
    days_passed = 0


    for index, num in enumerate(min_hr):
        # We look at the minute first, as we need to account
        # for the fact that the hour can increase if the
        # minutes reach greater than 60.

        # If the program is looking at the minutes.
        if index == 0:
          # Store the initial number of minutes.
          new_minutes = num
          # If the minutes are greater than or equal to 60.
          if num >= 60:
            # This will get the current minute.
            new_minutes = num % 60
            # This will get the number of hours passed as a
            # result of the minutes
            hours_passed_from_minutes = int(num / 60)

        # If the program is looking at the hour
        elif index == 1:
          # First we get the hours when the hours of the start
          # and duration times were added, then we add this
          # to the hours passed as a result of the minutes.
          new_hour = num + hours_passed_from_minutes

          # If the program has reached the 12th hour AND it was
          # not on the 12th hour to begin with.
          if new_hour >= 12 and hour_before != 12:
            # We retrieve the number of switches from AM to PM
            # and vice-versa. (int truncates the decimal.)
            am_pm_count = int(new_hour / 12)
            # If the count is odd, then there would be a switch
            # from AM to PM or from PM to AM. If the count is
            # even, then AM would stay as AM and PM would stay as
            # PM.
            if am_pm_count % 2 == 1:
              if old_am_pm == "AM":
                new_am_pm = "PM"
              else:
                new_am_pm = "AM"

            # We retrieve the hour (in clock format).
            new_hour = new_hour % 12
            # If the result is 0, then the hour is 12.
            if new_hour == 0:
              new_hour = 12

            # If AM has changed to PM or vice-versa.
            if am_pm_count > 0:
              # Depending on whether the time was initially
              # AM or PM, the program uses some maths to
              # calculate the days passed.
              if old_am_pm == "AM":
                days_passed = int(am_pm_count / 2)
              else:
                days_passed = int((am_pm_count + 1) / 2)

              # If the user has specified a day
              if day != None:
                
                days = {
                  "monday": 1,
                  "tuesday": 2,
                  "wednesday": 3,
                  "thursday": 4,
                  "friday": 5,
                  "saturday": 6,
                  "sunday": 7
                }

                # We get the day number from the dictionary.
                day_num = days[day.lower()]
                # We then add the number of days passed to
                # the current day number
                new_day_num = day_num + days_passed
                # The program then converts this to a number
                # corresponding to a day of the week (if required).
                if new_day_num > 7:
                  new_day_num = new_day_num % 7
                  if new_day_num == 0:
                    new_day_num = 7

                # Iterate through the days dictionary and get
                # each day and its corresponding day number.
                # If the day number matches the new day number,
                # retrieve the day of the week from the
                # dictionary and exit the loop.
                for day, day_num in days.items():
                  if day_num == new_day_num:
                    new_day = day
                    break

    # The hour and minutes are integers, so they are
    # converted into strings
    new_hour = str(new_hour)
    new_minutes = str(new_minutes)

    # If the minute is less than ten, it will have a
    # single digit. In a clock format, it will have a
    # '0' before it.
    if len(new_minutes) == 1:
        new_minutes = "0" + new_minutes

    # We put the time (and day) in a format that is
    # required, and then return it

    new_time = new_hour + ":" + new_minutes + " " + new_am_pm + ((", " + new_day.capitalize()) if day != None else "") + ("" if days_passed == 0 else (" (next day)" if days_passed == 1 else (" (" + str(days_passed) + " days later)")))

    return new_time


# EXAMPLES

#print(add_time("3:30 PM", "2:12"))
#print(add_time("11:55 AM", "3:12"))
#print(add_time("9:15 PM", "5:30"))
#print(add_time("11:40 AM", "0:25"))
#print(add_time("2:59 AM", "24:00"))
#print(add_time("11:59 PM", "24:05"))
#print(add_time("8:16 PM", "466:02"))
#print(add_time("5:01 AM", "0:00"))
#print(add_time("3:30 PM", "2:12", "Monday"))
#print(add_time("2:59 AM", "24:00", "saturDay"))
#print(add_time("11:59 PM", "24:05", "Wednesday"))
#print(add_time("8:16 PM", "466:02", "tuesday"))
