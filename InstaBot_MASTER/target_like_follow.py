from login import login
from sanitize import SanitaryTargets
import fileHandling as fh
from sleeper import sleeper
from time import sleep
import config
from printOperations import already_following, successful_action_chain, rate_limiter, account_is_private
from selenium import webdriver


def target_loop():
    driver = webdriver.Chrome(executable_path=config.CHROMEDRIVER_PATH)
    login(driver)

    cleanFile = SanitaryTargets()
    target_list = cleanFile.targets

    delay_count = 0
    failure_count = 0
    iteration_count = 0
    follow_count = 0
    likes = 0
    private_count = 0

    print("\nProceeding to follow {} accounts.".format(str(len(target_list))))
    for target in target_list:
        iteration_count += 1
        sleep(config.SLEEP_TIMER)
        if delay_count == 3:
            rate_limiter(iteration_count, target_list)
            sleeper(config.LIMIT_REACHED_SLEEP_TIMER)
            delay_count = 0
        try:
            # Open profile page
            driver.get(config.INSTAGRAM_URL_BASE + target)
            # Check for Private Accounts
            public_status = ''
            try:
                public_status = driver.find_element_by_css_selector(config.PUBLIC_STATUS).text
            except Exception:
                pass
            sleep(1)
            if public_status == 'This Account is Private':
                account_is_private(iteration_count, target_list, target)
                private_count += 1
                fh.add_to_file(config.PRIOR_TARGETS_PATH, target)
            else:
                # Open first post
                first_post = driver.find_element_by_css_selector(config.PROFILE_FIRST_POST)
                first_post.click()
                sleep(1)
                # Follow Them
                following = driver.find_element_by_xpath(config.PROFILE_FOLLOWING)
                # If already following do nothing
                if following.text == 'Following':
                    already_following(iteration_count, target_list, target)
                    fh.add_to_file(config.PRIOR_TARGETS_PATH, target)
                    pass
                else:
                    # Like first post
                    button_like = driver.find_element_by_xpath(config.PROFILE_LIKE_BUTTON)
                    button_like.click()
                    likes += 1
                    sleep(config.SLEEP_TIMER)
                    # Like the next 8 posts
                    for post in range(8):
                        sleep(config.SLEEP_TIMER)
                        # If Profile has less than 9 Posts
                        try:
                            next_post = driver.find_element_by_link_text('Next')
                            next_post.click()
                            sleep(1)
                            button_like = driver.find_element_by_xpath(config.BUTTON_LIKE)
                            button_like.click()
                            likes += 1
                        except Exception as e:
                            if config.DEBUG:
                                print(e)
                    following = driver.find_element_by_xpath(config.PROFILE_FOLLOWING)
                    following.click()
                    follow_count += 1
                    successful_action_chain(iteration_count, target_list, target)
                    fh.add_to_file(config.PRIOR_TARGETS_PATH, target)
        except Exception as e:
            if config.DEBUG:
                print(e)
            delay_count += 1
            failure_count += 1
            pass
