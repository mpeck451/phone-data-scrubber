import re

def capture_phone_metadata(data_input, field_name):
    new_meta_data = {
        "field_name": field_name,
        'total_listings': 0,
        'integers': 0,
        'non_integer_strings': 0,
        'empty_strings': 0,
        'one_digit': 0,
        'two_digits': 0,
        'three_digits': 0,
        'four_digits': 0,
        'five_digits': 0,
        'six_digits': 0,
        'seven_digits': 0,
        'eight_digits': 0,
        'nine_digits': 0,
        'ten_digits': 0,
        'eleven_digits': 0,
        'twelve_digits': 0,
        'larger_than_twelve_digits': 0,
        'strings_with_letters': 0,
    }
    for item in data_input:
        new_meta_data['total_listings'] += 1
        phone_value = item[field_name].replace(" ", "")
            #print(phone_value)
        try:
            int(phone_value)
            new_meta_data['integers'] += 1 
            match len(phone_value):
                case 1:
                    new_meta_data['one_digit'] += 1
                case 2:
                    new_meta_data['two_digits'] += 1
                case 3:
                    new_meta_data['three_digits'] += 1
                case 4:
                    new_meta_data['four_digits'] += 1
                case 5:
                    new_meta_data['five_digits'] += 1
                case 6:
                    new_meta_data['six_digits'] += 1
                case 7:
                    new_meta_data['seven_digits'] += 1
                case 8:
                    new_meta_data['eight_digits'] += 1
                case 9:
                    new_meta_data['nine_digits'] += 1
                case 10:
                    new_meta_data['ten_digits'] += 1
                case 11:
                    new_meta_data['eleven_digits'] += 1
                case 12:
                    new_meta_data['twelve_digits'] += 1
                case other:
                    new_meta_data['larger_than_twelve_digits'] += 1     
        except:
            if re.findall("[a-zA-Z]", phone_value):
                new_meta_data['strings_with_letters'] += 1
            if len(phone_value) == 0:
                new_meta_data['empty_strings'] += 1
            else:
                new_meta_data['non_integer_strings'] += 1

    return new_meta_data