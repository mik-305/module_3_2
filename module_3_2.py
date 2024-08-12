def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if not ('@' in recipient and '@' in sender):
        print('1 Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)  # Неверный формат адреса
        return
    elif not (recipient[len(recipient) - 4:] == '.com' or recipient[len(recipient) - 3:] == '.ru' or recipient[
                                                                                                     len(recipient) - 4:] == '.net'):
        print('2 Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)  # Неверный формат адреса
        return
    elif not (sender[len(sender) - 4:] == '.com' or sender[len(sender) - 3:] == '.ru' or sender[
                                                                                         len(sender) - 4:] == '.net'):
        print('3 Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)  # Неверный формат адреса
        return
    else:
        if recipient == sender:  # Совпадение отправителя и получателя
            print('Нельзя отправить письмо самому себе! ', ' Отправитель: ', sender, '  Адресат: ', recipient)
            return
        else:
            if sender == 'university.help@gmail.com':
                print('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
                return
            else:
                print('Нестандартный отправитель - ', sender)


print('---------------------------------------------------------------------------')
send_email('Это сообщение для проверки связи!', 'abc@viva.ru')
