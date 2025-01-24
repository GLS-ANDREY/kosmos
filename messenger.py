subscribers = []

def add_me_to_chat(def_subscriber):
    subscribers.append(def_subscriber)

def send_message(text, otpravitel, dop_infa=None):
    for subscribers_for in subscribers:
        subscribers_for(text,otpravitel,dop_infa)