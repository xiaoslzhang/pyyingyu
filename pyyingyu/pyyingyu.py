# coding=utf-8

import asyncio
import random
import json
import hashlib

import aiohttp
import async_timeout
import sys


class BaiduTranslate:
    lang_auto = 'auto'
    lang_zh = 'zh'
    lang_en = 'en'

    timeout = 20
    api_addr = 'http://fanyi-api.baidu.com/api/trans/vip/translate'

    def __init__(self, loop=None):
        self.appid = '20171009000086968'
        self.secret = 'vZ36FjnZ91FoLJwe5NrF'
        if loop is None:
            self.async = False
            self.loop = asyncio.get_event_loop()
        else:
            self.async = True
            self.loop = loop

    def translate(self, text, from_lang, to_lang):
        if self.async:
            return self._request(text, from_lang, to_lang)
        else:
            return self.loop.run_until_complete(self._request(text, from_lang, to_lang))

    async def _request(self, text, from_lang, to_lang):
        salt = random.randint(0, 2147483647)
        sign = self.appid + text + str(salt) + self.secret
        sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
        params = {'q': text, 'from': from_lang, 'to': to_lang, 'appid': self.appid, 'salt': salt, 'sign': sign}
        async with aiohttp.ClientSession(loop=self.loop) as session:
            with async_timeout.timeout(self.timeout, loop=self.loop):
                async with session.post(self.api_addr,
                                        data=params) as resp:
                    body = await resp.read()
                    res = json.loads(body.decode('utf-8'))
        if 'error_code' in res and res['error_code'] != '52000':
            raise RuntimeError(res['error_msg'])
        return res['trans_result'][0]['dst']

