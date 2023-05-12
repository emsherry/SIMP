
from mailchimp3 import MailChimp
from string import Template

def mailingListSignup(email):
    
    audience_id = "26ca7191a8"
    api_key = "0711e5f351b49c6f1b5991f9bc63b70d-us13"
    client = MailChimp(mc_api=api_key, mc_user="fizo-neechan1")

    try:
        data = {
            "status": "subscribed",
            "email_address": email
        }

        client.lists.members.create(list_id=audience_id, data=data)
        print('{} has been successfully added to the {} audience'.format(email, audience_id))
        
        return 1
    except Exception as error:
        print(error)
        
        return 0