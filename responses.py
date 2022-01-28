import re


def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[. -!?;]", message.lower())
    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        process_message(message, ['hello', 'hi', 'hey'], 'hey..there!'),
        process_message(message, ['bye', 'goodbye'], 'goodbye buddy!'),
        process_message(message, ['how', 'are', 'you'] , 'I\'m doing fine thanks!'),
        process_message(message, ['your', 'name'], 'My name santhosh, nice to meet you!'),
        process_message(message, ['help', 'me'], 'I will do my best to assit you!'),
        # Add more responses here
    ]

    # Checks all the response scores ande returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # get the max value for the best response and store it into a variable
    winning_response = max(response_scores)


    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = ' I didn\'t understand what you wrote...'
    else:
        bot_response = matching_response

    print('Bot response:', bot_response)
    return bot_response


# Test your system
get_response('what is your name?')

