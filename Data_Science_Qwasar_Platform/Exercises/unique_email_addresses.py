def unique_email_addresses(param_1):
    mails = set()

    for email in param_1:
        plus = False
        try:
            index = email.index('+')
            plus = True
        except:
            pass

        at = email.index('@')
        if not plus:
            index = at

        mail = email[:index].replace(".", "") + "@" + email[at + 1:]
        mails.add(mail)

    return len(mails)

print(unique_email_addresses(["test.email+alex@qwasar.io","test.e.mail+bob.cathy@qwasar.io","testemail+david@lee.tcode.com"]))