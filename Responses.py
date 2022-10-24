from datetime import datetime
import Currency as currency


def sample_responses(input_text):
    user_message = str(input_text)
    return currency.getCurrency(user_message)



