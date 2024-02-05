from datetime import datetime, timedelta


def get_birthdays_per_week(users):

    current_date = datetime.now()

    monday_current_week = current_date - timedelta(days=current_date.weekday())

    start_last_week = monday_current_week - timedelta(weeks=1)

    birth_per_day = {}

    for user in users:
        name = user['name']
        birthday = user['birth']
        str_birthday = birthday.strftime('%d %B')
        str_start_last_week = start_last_week.strftime('%d %B')
        str_monday_current_week = monday_current_week.strftime('%d %B')

        format_birthday = datetime.strptime(str_birthday, '%d %B')
        format_start_last_week = datetime.strptime(
            str_start_last_week, '%d %B')
        format_monday_current_week = datetime.strptime(
            str_monday_current_week, '%d %B')

        if format_start_last_week <= format_birthday < format_monday_current_week + timedelta(days=7):
            birthday_day = format_birthday.strftime('%A')

            if birthday_day in ['Saturday', 'Sunday']:
                birthday_day = 'Monday'
                
            if birthday_day not in birth_per_day:
                birth_per_day[birthday_day] = [name]
            else:
                birth_per_day[birthday_day].append(name)

    for day, names in birth_per_day.items():
        print(f"{day}: {', '.join(names)}")

def main():
    users = [
    {'name': 'Paweł', 'birth': datetime(2022, 1, 20)},
    {'name': 'Jan', 'birth': datetime(2024, 1, 20)},
    {'name': 'Piotr', 'birth': datetime(2024, 1, 19)},
    {'name': 'Mikołaj', 'birth': datetime(2024, 1, 31)},
    {'name': 'Aleksander', 'birth': datetime(2024, 1, 10)}]

    print(get_birthdays_per_week(users))
if __name__ == '__main__':
    main()
