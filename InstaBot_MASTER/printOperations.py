from fileHandling import get_set_from_file
import config


def already_following(iteration_count, target_list, target):
    print("[{}/{}] Already following {}. Moving on to the next user"
          "".format(iteration_count, str(len(target_list)), target))


def successful_action_chain(iteration_count, target_list, target):
    print("[{}/{}] Followed and Liked {}"
          "".format(iteration_count, str(len(target_list)), target))


def rate_limiter(iteration_count, target_list):
    print("\n[{}/{}] Encountered rate limiter"
          "".format(iteration_count, str(len(target_list))))


def account_is_private(iteration_count, target_list, target):
    print("[{}/{}] {} is private. Moving on to the next user"
          "".format(iteration_count, str(len(target_list)), target))


def get_target_list_length():
    targetList = get_set_from_file(config.TARGETS_PATH)
    return str(len(targetList))


def get_inactive_followings_length():
    inactiveFollowings = get_set_from_file(config.INACTIVE_FOLLOWINGS_PATH)
    return str(len(inactiveFollowings))
