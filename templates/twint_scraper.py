import twint

# Configure Twint
c = twint.Config()
c.Username = "utdtrey"
c.Limit = 1
c.Store_object = True

# Run the search
twint.run.Search(c)

# Get the tweet object
tweet = twint.output.tweets_list[0]

# Print the tweet text
print(tweet.tweet)
