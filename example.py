#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instabot import InstaBot

bot = InstaBot(login="ricardocosta.jr", password="RCJR18",
               like_per_day=600,
               comments_per_day=0,
               tag_list=['motorsports','rallycar','motorsport'],
               max_like_for_one_tag=50,
               follow_per_day=60,
               follow_time=5*60*60,
               unfollow_per_day=0,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0)

bot.new_auto_mod()
