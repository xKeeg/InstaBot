from sleeper import sleeper
from selenium import webdriver
import random
from time import sleep
import config
from login import login
import fileHandling as fh
from sanitize import SanitaryTargets


def unfollow_loop():
    driver = webdriver.Chrome(executable_path=config.CHROMEDRIVER_PATH)
    login(driver)
    count = 0
    not_following = 0
    fail_count = 0
    limit_regulator = 0
    stats = SanitaryTargets()
    followings_list = stats.unfollows
    for follower in followings_list:
        if limit_regulator == 12:
            seconds = random.randint(660, 3600)
            sleeper(seconds, "Precautionary Sleep | 12 Follows per run")
            limit_regulator = 0
        if fail_count == 3:
            seconds = random.randint(660, 3600)
            sleeper(seconds, "Precautionary Sleep | 12 Follows per run")
            fail_count = 0
        try:
            # Open profile page
            driver.get('https://www.instagram.com/' + follower)
            # Open first post
            first_post = driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > '
                                                             'article > div:nth-child(1) > div > div:nth-child(1) > '
                                                             'div:nth-child(1)')
            first_post.click()
            sleep(1)
            # Find following button
            following = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/'
                                                     'div[1]/div[2]/button')
            # If not following do nothing
            if not following.text == 'Following':
                print("Not currently following user: {}".format(follower))
                fh.add_to_file(config.PRIOR_UNFOLLOWS_PATH, follower)
                not_following += 1
                sleep(1)
                pass
            # Click following and then click unfollow
            else:
                following.click()
                sleep(1)
                unfollow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
                unfollow.click()
                count += 1
                sleep(1.5)
                print("Unfollow Count : {} | Unfollowed {}".format(count, follower))
                fh.add_to_file(config.PRIOR_TARGETS_PATH, follower)
                fh.add_to_file(config.PRIOR_UNFOLLOWS_PATH, follower)
                fail_count = 0
                limit_regulator += 1
        except Exception:
            fail_count += 1
            print("Failed at user {} | Continuing at next user".format(follower))
            continue

    print("Successfully unfollowed {} Accounts!\n"
          "Was not following {} Accounts".format(count, not_following))
