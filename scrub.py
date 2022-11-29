def scrub_phone_data(phone_number):
    #remove formatting and spaces
    phone_number = phone_number.replace("-", "")
    phone_number = phone_number.replace(" ", "")
    phone_number = phone_number.replace("(", "")
    phone_number = phone_number.replace(")", "")
    #remove leading 9
    if phone_number and phone_number[0] == '9' and (len(phone_number) != 7 or len(phone_number) != 10):
        phone_number = phone_number[1:]
    #remove leading 1
    if phone_number and phone_number[0] == '1' and (len(phone_number) != 7 or len(phone_number) != 10):
        phone_number = phone_number[1:]
    return phone_number

