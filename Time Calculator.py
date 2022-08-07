def add_time(start, duration, day=None):

    days = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
    }

    start_time = start.split(" ")

    start_hr_min = start_time[0].split(":")
    duration_hr_min = duration.split(":")
    end_min_hr = list()
    old_am_pm = start_time[1]
    #print(start_hr_min)
    #print(duration_hr_min)
    #print(old_am_pm)
    # Minutes first, then hour
    end_min_hr.append(int(start_hr_min[1]) + int(duration_hr_min[1]))
    end_min_hr.append(int(start_hr_min[0]) + int(duration_hr_min[0]))
    #print(end_min_hr)

    #print("\n\n")
    new_minutes = 0
    new_hour = 0
    new_am_pm = old_am_pm
    new_day = day
    hour_before = end_min_hr[1]
    hours_passed = 0
    days_passed = 0
    for index, num in enumerate(end_min_hr):

        if index == 0:
          new_minutes = num
          if num >= 60:
            new_minutes = num % 60
            hours_passed = int(num / 60)

        elif index == 1:
          new_hour = num + hours_passed
          if new_hour >= 12 and hour_before != 12:
            #print("new_hour:", new_hour)
            am_pm_count = int(new_hour / 12)
            if am_pm_count % 2 == 1:
              if old_am_pm == "AM":
                new_am_pm = "PM"
              else:
                new_am_pm = "AM"
              #print("AM/PM:", new_am_pm)
            #print(new_hour)
            new_hour = new_hour % 12
            if new_hour == 0:
              new_hour = 12
            #print(new_hour)

            if am_pm_count > 0:
              if old_am_pm == "AM":
                days_passed = int(am_pm_count / 2)
              else:
                days_passed = int((am_pm_count + 1) / 2)

              if day != None:
                day_num = days[day.lower()]
                new_day_num = day_num + days_passed
                if new_day_num > 7:
                  new_day_num = new_day_num % 7
                  if new_day_num == 0:
                    new_day_num = 7

                for day, day_num in days.items():
                  if day_num == new_day_num:
                    new_day = day

    new_hour = str(new_hour)
    new_minutes = str(new_minutes)
    if len(new_minutes) == 1:
        new_minutes = "0" + new_minutes



    # (Uses ternary operators)
    #print(new_hour + ":" + new_minutes + " " + new_am_pm + ((", " + new_day.capitalize()) if day != None else "") + ("" if days_passed == 0 else (" (next day)" if days_passed == 1 else (" (" + str(days_passed) + " days later)"))) )

    return new_hour + ":" + new_minutes + " " + new_am_pm + ((", " + new_day.capitalize()) if day != None else "") + ("" if days_passed == 0 else (" (next day)" if days_passed == 1 else (" (" + str(days_passed) + " days later)")))


print(add_time("3:30 PM", "2:1243453"))
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
