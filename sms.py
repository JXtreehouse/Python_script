#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/30
# @Author : AlexZ33
# @Site : 
# @File : sms.py
# @description 发送手机短信
# @reference https://www.twilio.com/docs/libraries/python
# @Software: PyCharm

"""
为了要使用Twilio公司所提供的短信服务，需要到Twilio公司注册账号，以取得下列信息：
Account SID：Twilio API key账号。
Auth TOKEN：Twilio账号的图腾(TOKEN)。
Twilio Number：Twilio电话号码。
Verified numbers：电话号码使用地区。
上述信息我们可以称之为API key(密钥)，有了上述密钥，您就可以使用Python程序发送短信了。
"""
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console



