import config
import fileHandling as fh
import instaloader


def get_ghost_followings():
    L = instaloader.Instaloader()
    USER = "come_fillet_with_me"

    # Profile to Analyse
    PROFILE = USER
    L.login("come_fillet_with_me", "Keegan010198")

    profile = instaloader.Profile.from_username(L.context, PROFILE)

    followings = set(profile.get_followees())
    followers = set(profile.get_followers())

    ghosts = followings - followers

    fh.write_to_file(config.INACTIVE_FOLLOWINGS_PATH, ghosts)


get_ghost_followings()
