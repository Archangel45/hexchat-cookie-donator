import hexchat

__module_name__ = 'cookie-donator'
__module_version__ = '0.9.0-beta'
__module_description__ = 'A Hexchat script that let\'s users donate cookies to you.'

print("You have loaded", __module_name__, __module_version__)
# How many cookies were donated.
cookie_count = 0

# The cookie donators.
cookie_donators = {}

def donate_cookie(word, word_eol, userdata):
    global cookie_count, cookie_donators
    # If someone gives you a cookie, increment the cookie_count variable by 1.
    if 'gives ' + hexchat.get_info('nick') + ' a cookie' in word[1]:
        cookie_count += 1

        if word[0] not in cookie_donators:
            cookie_donators[word[0]] = 1
        else:
            cookie_donators[word[0]] += 1

        # Respond to the donator.
        hexchat.command('me Hugs {}. "Thank you for your generous donation! ^^"'.format(word[0]))
    return hexchat.EAT_NONE

# Checks how many cookies you have in total.
def check_cookies(word, word_eol, userdata):
    print("You have {} cookies.".format(cookie_count))

    print("Your donator(s):")
    for donator, donator_cookies in cookie_donators.items():
        print(donator + '...........' + str(donator_cookies))
    return hexchat.EAT_NONE

hexchat.hook_print("Channel Action Hilight", donate_cookie)
hexchat.hook_command("COOKIE", check_cookies, help='SYNTAX: /COOKIE\nChecks the total amount of cookies and lists the donators.')
