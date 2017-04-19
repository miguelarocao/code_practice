# Interview Cake: In-Flight Entertainment
# https://www.interviewcake.com/question/python/inflight-entertainment
# Miguel Aroca-Ouellette
# 29/03/2017

def in_flight(flight_length, movie_length):
    # Finds two movies to watch to maximize run time

    # Iterate and check set
    times = set() # movie lengths

    for length in movie_length:
        goal = flight_length - length
        if goal in times:
            return True
        times.add(length)

    return False

flight_length = 10
movies = [5,4,2,6,1]
print in_flight(flight_length, movies)