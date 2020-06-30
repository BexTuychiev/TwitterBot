import tweepy
from twitter_scraper import get_tweets
import csv
import os


def save_tweets_or_profile(generator, username):
    """
    Given the username and a generator object containing either tweets or a user profile data, the function saves the contents to a scv file
    :param generator: A generator object containing either tweets or a profile information
    :param username: Username of a profile in question
    :return: Action > Save the contents of the generator object to a CSV.
    """
    # Identify the type of the generator object
    # items_list = [item for item in generator]
    # if 'tweetId' in [items_list[0].keys()]:
    #     generator_type = 'tweets'
    # else:
    #     generator_type = 'profile'
    generator_type = type(generator)

    # Check the path for the DATA directory. If does not exist create the folder
    # in the top level directory
    if not os.path.exists('data'):
        os.mkdir('data')
        print('Saving into "data" directory')
    else:
        print('Saving into "data" directory')

    with open(f'./data/{username.lower()}_tweets.csv', 'wb') as csv_file:
        if generator_type == 'generator':
            to_csv = [tweet for tweet in generator]
            keys = to_csv[0].keys()
            dict_writer = csv.DictWriter(csv_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(to_csv)
        elif generator_type == 'class':
            to_csv = generator.to_dict()
            keys = to_csv.keys()
            dict_writer = csv.DictWriter(csv_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(to_csv)
