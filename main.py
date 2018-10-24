import praw


Keywords = ['karma', 'Karma' 'Upvote' 'upvote']

def main():
    reddit = praw.Reddit(user_agent='Karma bot V 1.0',
                         client_id='9rIVsBx6n1azCA', client_secret='uYSr_DBMQgcbI_aw__t2aJr9Usw',
                         username='karma__bot', password='odl36d5n')

    subreddit = reddit.subreddit('freekarma4u')
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):

    normalized_title = submission.title.lower()
    for question_phrase in Keywords:
        if question_phrase in normalized_title and not submission.saved:
            print("Found " + str(submission.author))
            submission.save()
            submission.upvote()
            submission.reply("I have automatically upvoted your submission as per your request for free Karma. Please return if possible. \n \n \n *I am a bot and this action is performed automatically, please PM me if you have any queries*")
            print("Finished")
            break


if __name__ == '__main__':
    main()
