current_users = ['admin', 'tal', 'ofri', 'yahel', 'sky']
new_users = ['tofi', 'bobot', 'sky', 'kadur', 'ofri']
for new_user in new_users:
    if new_user in current_users:
        print(f'{new_user} username alredy have been used, choose new one')
    else:
        print(f'{new_user} is available')    
