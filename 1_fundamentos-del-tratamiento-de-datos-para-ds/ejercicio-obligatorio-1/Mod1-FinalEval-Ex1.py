# MÁSTER EN BIG DATA Y BUSINESS ANALYTICS
# MOD 1 - EJERCICIO OBLIGATORIO - 1: dado un archivo que contiene en cada línea
# Se pide calcular para cada Tweet el sentimiento del Tweets, que viene dado por
# la suma de los "sentimientos" que tenemos en el archivo data/Sentimientos.txt“

import pandas as pd


def process_json(filename):
    """ Process a json file using pandas read_json
        @:return List
    """
    try:
        df_tweets = pd.read_json(filename, lines=True)
        df_tweets = df_tweets[df_tweets.text.notnull()]['text']
        return df_tweets.to_list()
    except:
        print("Something went wrong parsing the file " + filename)


def get_sentiments(filename):
    """ Processes Sentiments.txt creating a dictionary from a set
        of words and it's numerical value
        @:return Dictionary {Term, Sentiment}
    """
    valores = {}
    for linea in open(filename, 'r'):
        termino, valor = linea.split('\t')
        valores[termino] = int(valor)
    return valores


if __name__ == "__main__":

    tweets_file = 'data/Tweets.txt'
    sentiments_file = 'data/Sentimientos.txt'

    # Reading tweets
    list_of_tweets = process_json(tweets_file)

    # Reading sentiments
    values = get_sentiments(sentiments_file)

    # Get Sentiment
    for tweet in list_of_tweets:
        tweet_sentiment = sum([values.get(word.lower(), 0) for word in tweet.split(" ")])
        # Return only Tweets with content
        if tweet_sentiment > 0:
            print("Tweet: '" + tweet + "' \nSentimiento asociado: " + str(tweet_sentiment) + "\n")
