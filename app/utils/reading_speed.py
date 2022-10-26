AVG_READING_SPEED = 250

def calculate_read_time(number_of_words):
    return round(number_of_words / AVG_READING_SPEED)

def get_word_count(string):
    return len(string.split(' '))

def read_time_from_string(string):
    word_count = get_word_count(string)
    return calculate_read_time(word_count)