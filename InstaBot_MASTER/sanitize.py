import config
import fileHandling


class SanitaryTargets:
    def __init__(self):
        self.priorTargets = set()
        self.newTargets = set()
        self.currentTargets = set()
        self.allTargets = set()
        self.targets = set()
        self.priorUnfollows = set()
        self.currentUnfollows = set()
        self.unfollows = set()
        self.sanitize()

    def read_files(self):
        self.newTargets = self.newTargets | fileHandling.get_set_from_file(config.NEW_TARGETS_PATH)
        self.priorTargets = self.priorTargets | fileHandling.get_set_from_file(config.PRIOR_TARGETS_PATH)
        self.currentTargets = self.currentTargets | fileHandling.get_set_from_file(config.TARGETS_PATH)
        self.priorUnfollows = fileHandling.get_set_from_file(config.PRIOR_UNFOLLOWS_PATH)
        self.currentUnfollows = fileHandling.get_set_from_file(config.INACTIVE_FOLLOWINGS_PATH)

    def sanitise_sets(self):
        self.allTargets = self.newTargets | self.currentTargets
        self.targets = self.allTargets - self.priorTargets
        self.unfollows = self.currentUnfollows - self.priorUnfollows

    def sanitize(self):
        self.read_files()
        self.sanitise_sets()
        fileHandling.write_to_file(self.targets, config.TARGETS_PATH)
        fileHandling.write_to_file(self.unfollows, config.INACTIVE_FOLLOWINGS_PATH)
