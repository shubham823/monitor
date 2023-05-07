from ldap3 import Server, Connection, ALL

# Set up the LDAP server and connection
server = Server('ldap://your-ldap-server-url.com', get_info=ALL)
conn = Connection(server, user='your-ldap-username', password='your-ldap-password')

# Bind the connection to the LDAP server
conn.bind()

# Search for the user in the LDAP directory
conn.search('dc=example,dc=com', '(sAMAccountName=username)', attributes=['dn', 'userPassword'])

if conn.entries:
    # Get the user's distinguished name (DN) and password
    user_dn = conn.entries[0].dn
    user_password = password

    # Attempt to bind the user's DN and password to the LDAP server
    user_conn = Connection(server, user=user_dn, password=user_password)
    user_conn.bind()

    if user_conn.bound:
        # The username and password are valid
        print('Valid credentials')
    else:
        # The password is incorrect
        print('Incorrect password')
else:
    # The user doesn't exist in the LDAP directory
    print('User not found')
