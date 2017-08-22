#!/usr/bin/python

# 'ab' is short for 'a'ddress'b'ook

ab = {'Swaroop':'swaroop@swaroop.com',
      'Larry':'larry@wall.org',
      'Matsumoto':'matz@ruby-lang.org',
      'Spammer':'spammer@hotmail.com'
      }

print('Swaroop\'s address is', ab['Swaroop'])

# Deleting a ket-value pair
del ab['Spammer']

print('\nThere are {0} contacts int the addrss-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))

# Adding a key-value
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab: # OR ab.has_key('Guido')
    print("\nGuido's address is", ab['Guido'])