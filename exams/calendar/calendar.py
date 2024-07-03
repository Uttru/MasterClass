def main():

    with open('calendar/events.txt', 'r') as file:
        event_dict = {}
        for lines in file:
            lines = lines.strip().split(';')
            Day = int(lines[0])
            Hour = int(lines[1])
            event = ' '.join(lines[2:]) if len(lines) > 2 else ''

            if not (1 <= Day <= 365):
                print('Error: Invalid Day')
                continue
            if not (0 <= Hour < 24):
                print('Error: Invalid Hour')
                continue

            if Day in event_dict:
                event_dict[Day].append((Hour, event))
            else:
                event_dict[Day] = [(Hour, event)]

    with open('calendar/commands.txt', 'r') as file:
        commands_dict = {}
        for line in file:
            line = line.strip().split()
            command = line[0]
            day_command = int(line[1])

            if len(line) >= 3:
                hour_command = int(line[2])
                event_command = ' '.join(line[3:])
                if command in commands_dict:
                    commands_dict[command].append((day_command, hour_command, event_command))
                else:
                    commands_dict[command] = [(day_command, hour_command, event_command)]
            else:
                if command in commands_dict:
                    commands_dict[command].append(day_command)
                else:
                    commands_dict[command] = [day_command]
    for command, details in commands_dict.items():
        if command == 'v':
            for day in details:
                if day in event_dict:
                    print(f'Events of day {day}:')
                    for sour ,event in event_dict[day]:
                        print(f'  {sour}: {event}')
                else:
                    print(f'No event found for day {day}')
        elif command == 'i':
            for detail in details:
                day_command = detail[0]
                hour_command = detail[1]
                event_command = detail[2]
                if day_command in event_dict:
                    print(f'Cannot insert event')
                else:
                    event_dict[day_command] = event_command
                    print(f'Event inserted for day {day_command}:')
                    print(f'  {hour_command}: {event_command}')

if __name__ == "__main__":
    main()



























