#!/usr/bin/env python
#coding=utf-8
from twisted.python import log
from pyrad import packet
from store import store
from settings import *
import logging
import datetime
import utils

"""记账开始包处理"""
def process(req=None,user=None):
    if not req.get_acct_status_type() == STATUS_TYPE_START:
        return
        
    if not user:
        return log.err('user %s not exists'%req.get_user_name())
        
    online = utils.Storage(
        account_number = user['account_number'],
        nas_addr = req.get_nas_addr(),
        acct_session_id = req.get_acct_sessionid(),
        acct_start_time = datetime.datetime.now().strftime( "%Y-%m-%d %H:%M:%S"),
        framed_ipaddr = req.get_framed_ipaddr(),
        mac_addr = req.get_mac_addr(),
        nas_port_id = req.get_nas_portid(),
        start_source = STATUS_TYPE_START
    )

    store.add_online(online)

    log.msg('%s Accounting start request, add new online'%req.get_user_name(),level=logging.INFO)