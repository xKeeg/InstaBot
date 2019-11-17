from tkinter import *
from datasetGathering import get_ghost_followings
from datasetGathering import get_new_targets
from target_like_follow import target_loop
from unfollow import unfollow_loop
import printOperations as printops
from sanitize import SanitaryTargets


class InstabotWindow:
    def __init__(self, master):
        self.master = master
        self.inactiveFollowings = printops.get_inactive_followings_length()
        self.targets = printops.get_target_list_length()

        headerFrame = Frame(master)
        valuesFrame = Frame(master)
        buttonsFrame = Frame(master)

        headerFrame.pack()
        valuesFrame.pack()
        buttonsFrame.pack()

        self.inactiveFollowingsLabel = Label(headerFrame, text="Inactive Followings")\
            .grid(column=0, row=0)
        self.currentTargetsLabel = Label(headerFrame, text="Current Targets")\
            .grid(column=1, row=0)

        self.inactiveFollowingsCount = Label(valuesFrame, text=self.inactiveFollowings)
        self.inactiveFollowingsCount.grid(column=0, row=0, padx=40)
        self.currentTargetsCount = Label(valuesFrame, text=self.targets)
        self.currentTargetsCount.grid(column=1, row=0, padx=40)

        self.updateInactiveButton = Button(buttonsFrame, text="Update Inactive"
                                                              "\nFollowings", command=get_ghost_followings)\
            .grid(column=0, row=0, sticky=W+E+N+S, padx=5, pady=5)
        self.unfollowButton = Button(buttonsFrame, text="Unfollow Inactive\nFollowings", command=unfollow_loop)\
            .grid(column=0, row=1, sticky=W+E+N+S, padx=5, pady=5)
        self.getNewTargetsButton = Button(buttonsFrame, text="Get New Targets", command=get_new_targets) \
            .grid(column=1, row=0, sticky=W+E+N+S, padx=5, pady=5)
        self.followTargets = Button(buttonsFrame, text="Follow Targets", command=target_loop) \
            .grid(column=1, row=1, sticky=W+E+N+S, padx=5, pady=5)
        self.updateMetricsButton = Button(buttonsFrame, text="Update Count", command=self.update_metrics) \
            .grid(columnspan=2, row=2, sticky=W+E+N+S, padx=5, pady=5)

    def update_metrics(self):
        SanitaryTargets()
        self.inactiveFollowings = printops.get_inactive_followings_length()
        self.targets = printops.get_target_list_length()
        self.inactiveFollowingsCount.config(text=self.inactiveFollowings)
        self.currentTargetsCount.config(text=self.targets)
        self.currentTargetsCount.update()
        self.inactiveFollowingsCount.update()