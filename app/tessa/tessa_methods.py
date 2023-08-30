from . import schemas

def say_hello(str, tessa_obj : schemas.tessa_obj):
    modified_message = "Replied --" + tessa_obj.message
    my_dict = {
        "From:" : str,
        "Message" : modified_message
    }
    return my_dict