"""
You are building a running podcast playlist generator.

Long-distance runners love listening to podcasts on their runs. Their second podcast episode often gets
cut off as they are ending their run. They want to be able to listen to two entire episodes during their
long runs. You are building a feature that would choose two podcast episodes that will equal the exact
length of their planned run.

Write a function that takes an integer run_length (in minutes) and a list of integers podcast_episode_lengths
(in minutes) and returns a boolean whether there are two numbers in podcast_episode_lengths whose sum equals
run_length. Remember that the runners will listen to precisely two episodes, and they will not want to listen 
to the same episode twice.
"""



def pod(total, podcasts):
    """
    podcast_len = {}

    for p in podcasts:
        podcast_len[p] = True
    """
    podcast_len = set() # set has O(1) look up

    for p0 in podcasts:
        other_podcast_len = total - p0
        # is there a podcast of total - p0 minutes?
        if other_podcast_len in podcast_len:
            return True

    return False

"""
total == 60
p0 == 27
p1 == 60 - 27 == total - p0 == 33
"""