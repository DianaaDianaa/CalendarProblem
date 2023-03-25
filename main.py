from datetime import datetime, timedelta


"""
The parse_time function converts a string in the format "HH:MM" to a datetime object, and format_time does the reverse.
"""
def parse_time(s):
    return datetime.strptime(s, '%H:%M')

def format_time(dt):
    return datetime.strftime(dt, '%H:%M')

"""
The get_free_time function takes a list of booked time slots (calendar), 
a minimum time (min_time) and a maximum time (max_time) and returns a list of free time slots.
"""
def get_free_time(calendar, min_time, max_time):
    free_slots = []
    start_time = parse_time(min_time)
    end_time = parse_time(max_time)
    for start, end in calendar:
        start = parse_time(start)
        end = parse_time(end)
        if start > start_time:
            free_slots.append((start_time, start))
        start_time = max(start_time, end)
    if end_time > start_time:
        free_slots.append((start_time, end_time))
    return free_slots


"""
The find_meeting_time function takes two calendars (calendar1 and calendar2), their limits (limits1 and limits2), 
and a meeting time (meeting_time), and returns a list of available meeting times. 
It first uses get_free_time to get the free time slots for each calendar, and then checks for overlapping slots of at 
least the required meeting time.
"""
def find_meeting_time(calendar1, limits1, calendar2, limits2, meeting_time):
    free_time1 = get_free_time(calendar1, limits1[0], limits1[1])
    free_time2 = get_free_time(calendar2, limits2[0], limits2[1])
    available_time = []
    for start1, end1 in free_time1:
        for start2, end2 in free_time2:
            start = max(start1, start2)
            end = min(end1, end2)
            if (end - start) >= timedelta(minutes=meeting_time):
                available_time.append((format_time(start), format_time(end)))
    return available_time


calendar1 = [['9:00','10:30'], ['12:00','13:00'], ['16:00','18:00']]
limits1 = ['9:00','20:00']
calendar2 = [['10:00','11:30'], ['12:30','14:30'], ['14:30','15:00'], ['16:00','17:00']]
limits2 = ['10:00','18:30']
meetingTime = 30

availableTime = find_meeting_time(calendar1, limits1, calendar2, limits2, meetingTime)

print(availableTime)