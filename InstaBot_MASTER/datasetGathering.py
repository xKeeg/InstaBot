import config
import fileHandling as fh
import instaloader
from itertools import islice
from sanitize import SanitaryTargets
import printOperations as printOps


def get_ghost_followings():
    L = instaloader.Instaloader()
    USER = config.USERNAME

    # Profile to Analyse
    PROFILE = USER
    L.login(config.USERNAME, config.PASSWORD)

    profile = instaloader.Profile.from_username(L.context, PROFILE)
    likes = set()
    # Retrieve Likes
    print('Fetching likes of {} most recent posts of profile {}.'.format(str(config.INACTIVE_POST_TOLERANCE),
                                                                         profile.username))
    for post in islice(profile.get_posts(), config.INACTIVE_POST_TOLERANCE):
        tmp = set(post.get_likes())
        likes = likes | tmp

    followers = set(profile.get_followees())

    ghosts = followers - likes

    fh.write_to_file(config.INACTIVE_FOLLOWINGS_PATH, ghosts)


def get_new_targets():
    L = instaloader.Instaloader()

    # Init
    PROFILE = input("What User would you like to retrieve targets from?\n"
                    ">> ")

    L.login(config.USERNAME, config.PASSWORD)

    profile = instaloader.Profile.from_username(L.context, PROFILE)

    # Like Retrieval
    likes_first = set()
    likes_second = set()
    likes_third = set()
    count = 0
    try:
        print('Fetching likes of 3 recent posts in the past 12 of profile {}.'.format(profile.username))
        for post in islice(profile.get_posts(), 1, 13, 4):
            if count == 0:
                likes_first = likes_first | set(post.get_likes())
                print("Found {} likes on post one.".format(len(likes_first)))
            if count == 1:
                likes_second = likes_second | set(post.get_likes())
                print("Found {} likes on post two.".format(len(likes_second)))
            if count == 2:
                likes_third = likes_third | set(post.get_likes())
                print("Found {} likes on post three.".format(len(likes_third)))
            count += 1
    except Exception as e:
        if config.DEBUG:
            print(e)
        print("User has insufficient posts")
        pass

    # Count Total Unique Profiles Analysed
    total_unique_users = set.union(likes_third, likes_second, likes_first)
    print("{} Total Unique Followers found".format((str(len(total_unique_users)))))

    # Get Intersecting Likes
    reliable_followers = set.intersection(likes_first, likes_second, likes_third)
    print("{} Total Reliable Followers found".format(str(len(reliable_followers))))

    fh.add_set_to_file(config.NEW_TARGETS_PATH, reliable_followers)

    SanitaryTargets()
    print("{} of which we have not previously interacted with".format(printOps.get_target_list_length()))
