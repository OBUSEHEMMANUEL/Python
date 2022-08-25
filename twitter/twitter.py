users = [
    {'name': 'Hadiza',
     'age': 21,
     'gender': 'Female',
     'username': 'deezah',
     'is-verified': True,
     'tweets': [
         {'content': 'PO for President', 'likes': 450, 'retweets': 233},
         {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2},

     ]},
    {'name': 'Ibrahim',
     'age': 32,
     'gender': 'male',
     'username': 'ibro',
     'is-verified': False,
     'tweets': [
         {'content': 'Programming is fun', 'likes': 34, 'retweets': 233},
     ]},
    {'name': 'James',
     'age': 25,
     'gender': 'Male',
     'username': 'amez',
     'is-verified': True,
     'tweets': [
         {'content': 'love is life', 'likes': 450, 'retweets': 233},
         {'content': 'only Racheal i know', 'likes': 4, 'retweets': 2},

     ]}, {'name': 'Racheal',
          'age': 21,
          'gender': 'Female',
          'username': 'betty',
          'is-verified': False,
          'tweets': [
              {'content': '.', 'likes': 1450, 'retweets': 2330},
              {'content': 'Thinking about Amez', 'likes': 4, 'retweets': 2},
              {'content': 'Amezing ggrace', 'likes': 4000, 'retweets': 3000},

          ]}, {'name': 'Elijah',
               'age': 17,
               'gender': 'Male',
               'username': 'el_d_si',
               'is-verified': False,
               'tweets': [
                   {'content': '#osun decides', 'likes': 450, 'retweets': 233},
                   {'content': 'imole', 'likes': 4, 'retweets': 2}
               ]},
    {
        'name': 'Dorris',
        'age': 16,
        'gender': 'Female',
        'username': 'anything',
        'is-verified': False,
        'tweets': [
            {'content': 'I love chimamanda', 'likes': 450, 'retweets': 233},
            {'content': 'Feminism is the goal', 'likes': 4, 'retweets': 2},
        ]},
    {
        'name': 'jacob',
        'age': 37,
        'gender': 'Male',
        'username': 'elder_j',
        'is_Verified': False,
        'tweets': [
            {'content': 'visualizing', 'likes': 1, 'retweets': 233},
            {'content': 'Feminism is the goal', 'likes': 4, 'retweets': 2},
        ]},
    {
        'name': 'phiqui',
        'age': 47,
        'gender': 'Male',
        'username': 'whistle',
        'is_Verified': False,
        'tweets': [

        ]},
]

no_of_user = len(users)
usernames = {user['username'] for user in users}
female_users = [user['name'] for user in users if user['gender'].lower() == 'female']
inactive_users = [user for user in users if len(user['tweets']) == 0]
age = [user['age'] for user in users]
name_and_age = [{'name': user['name'], 'age': user ['age']} for user in users]
avg_age_of_users = round(sum(user ['age'] for user in users)/len(users))

print(inactive_users)
print(female_users)
print(age)
print(name_and_age)
print(avg_age_of_users)