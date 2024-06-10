from message import Message
import math

messages : list[Message] = []

def main():
    load_from_file('sms.txt')
    if len(messages) >= 10:
        print(f'2. feladat: A legfrissebb üzelet szövege: {messages[9].text}')
    else:
        print(f'2. feladat: A legfrissebb üzelet szövege: {messages[-1].text}')
 
    print('3.a feladat a leghosszabb üzenet:')
    longest = longest_message()
    print(f'\tÓra: {longest.hour}')
    print(f'\tPerc: {longest.minute}')
    print(f'\tTelefonszám: {longest.phone}')
    print(f'\tÜzenet: {longest.text}')

    print('3.b feladat a legrövidebb üzenet:')
    shortest = shortest_message()
    print(f'\tÓra: {shortest.hour}')
    print(f'\tPerc: {shortest.minute}')
    print(f'\tTelefonszám: {shortest.phone}')
    print(f'\tÜzenet: {shortest.text}')

    print('Karakterszám statisztika:')
    stat = number_of_chars_stat()
    for key, value in stat.items():
        match key:
            case 1: cat = '1-20'
            case 2: cat = '21-40'
            case 3: cat = '41-60'
            case 4: cat = '61-80'
            case 5: cat = '81-100'

        print(f'\t{cat}: {value} db')

    print(f'{unread_messages()} olyan üzenet van, amelynek elolvasásához fel kellene hívnia a szolgáltatót.')

    max_gap = longest_time_between_messages_of_girlfriend()
    if max_gap == 0:
        print('Nincs elegendő üzenet.')
    else:
        print(f'A leghosszabb néma időszak a barátnő üzenetei között: {max_gap} perc')

    messages.append(get_new_message())

def load_from_file(filename: str):
    file = open(filename, 'r', encoding='utf-8')    
    rows = file.readlines()
    for i in range(0, len(rows), 2):
        # splitted = rows[i].strip().split(' ')
        # messages.append(Message(int(splitted[0]), int(splitted[1]), splitted[2], rows[i+1].strip()))
        ora, perc, phone = rows[i].strip().split(' ')
        messages.append(Message(int(ora), int(perc), phone, rows[i+1].strip()))
    file.close()

def longest_message() -> Message:
    longest = messages[0]
    for m in messages:
        if len(m.text) > len(longest.text):
            longest = m
    return longest

def shortest_message() -> Message:
    shortest = messages[0]
    for m in messages:
        if len(m.text) < len(shortest.text):
            shortest = m
    return shortest

def number_of_chars_stat() -> dict:
    stat = {}
    for m in messages:
        hossz = len(m.text)
        category = math.ceil(hossz / 20)
        if category in stat.keys():
            stat[category] += 1
        else:
            stat[category] = 1
    return stat

def unread_messages() -> int:
    unread_counter = 0
    for hour in range(1, 25):
        message_counter = messages_of_hour(hour)
        if message_counter > 10:
            unread_counter += message_counter - 10
    return unread_counter

def messages_of_hour(hour: int) -> int:
    counter = 0
    for m in messages:
        if m.hour == hour:
            counter += 1
    return counter

def longest_time_between_messages_of_girlfriend():
    max_gap = 0
    prev_message = None
    for m in messages:
        if m.phone == '123456789':
            if prev_message == None:
                prev_message = m
            else:
                gap = m.total_minutes - prev_message.total_minutes
                prev_message = m
                if gap > max_gap:
                    max_gap = gap
    return max_gap

def get_new_message() -> Message:
    print('Új üzenet adatai:')
    hour = int(input('Óra: '))
    minute = int(input('Perc: '))
    phone = input('Telefonszám: ')
    text = input('Üzenet szövege: ')
    return Message(hour, minute, phone, text)



main()