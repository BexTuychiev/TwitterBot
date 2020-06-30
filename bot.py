import tweepy
from twitter_scraper import get_tweets, Profile
import csv
import os
import types


def save_tweets_or_profile(generator, username):
    """
    Given the username and a generator object containing either tweets or a user profile data, the function saves the contents to a scv file
    :param generator: A generator object containing either tweets or a profile information
    :param username: Username of a profile in question
    :return: Action > Save the contents of the generator object to a CSV.
    """
    generator_type = type(generator)

    # Check the path for the DATA directory. If does not exist create the folder
    # in the top level directory
    if not os.path.exists('data'):
        os.mkdir('data')
        print('Saving into "data" directory')
    else:
        print('Saving into "data" directory')

    # Save as CSV
    with open(f'./data/{username.lower()}_tweets.csv', 'w') as csv_file:
        if isinstance(generator, types.GeneratorType):
            to_csv = [tweet for tweet in generator]
            keys = [key for key in to_csv[0].keys()]
            dict_writer = csv.DictWriter(csv_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(to_csv)
        else:
            to_csv = generator.to_dict()
            keys = [key for key in to_csv.keys()]
            dict_writer = csv.DictWriter(csv_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(to_csv)


def retrieve_tweets(username, num_of_pages=10, field=None, save=False):
    """
    Retrieve the tweets of the user with the given username up to specified page
    :param username: The screen name or the user id of the twitter user. # sign can be used to get tweets from a hashtag
    :param num_of_pages: Specifies the number of pages to retrieve. Default is 10
    :param field: A parameter which retrieves a specific info about a tweet. Return the whole tweet dictionary if not specified
    :param save: If true, saves each tweet as a new row in a CSV file
    :return: A list of tweets in a dictionary format.
    """
    # Get the tweets in a generator object
    statuses = get_tweets(username, pages=num_of_pages)

    # If save is True, create a new CSV file with the given username as a filename into a new directory
    if save:
        save_tweets_or_profile(generator=statuses, username=username)

    if field is None:
        return [tweet for tweet in statuses]
    else:
        return [f'{field} of tweet with id of {tweet["tweetId"]}: {tweet[field]}' for tweet in statuses]
