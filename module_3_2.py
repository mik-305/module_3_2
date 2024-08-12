def send_email(message, recipient, *,sender = 'university.help@gmail.com'):
    if not ('@' in recipient and '@' in sender):
        print('Невозможно отправить письмо с адреса ',sender,' на адрес ', recipient)   # Неверный формат адреса
        return
    else:
        if recipient == sender:                                                      # Совпадение отправителя и получателя
            print('Нельзя отправить письмо самому себе! ')
            return
        else:
            if sender == 'university.help@gmail.com':
                print('Письмо успешно отправлено с адреса ',sender, ' на адрес ', recipient)
                return
            else:
                print('Нестандартный отправитель - ',sender)



print('---------------------------------------------------------------------------')
#send_email('Это сообщение для проверки связи!', 'ABBB@CCC.ru')
send_email('Это сообщение для проверки связи!', 'university.help@gmail.ru',sender = 'university.help@gmail.com')


