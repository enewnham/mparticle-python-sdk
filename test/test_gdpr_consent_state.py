# coding: utf-8

"""
    mParticle

    mParticle Event API

    OpenAPI spec version: 1.0.1
    Contact: support@mparticle.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from __future__ import absolute_import

import os
import sys
import unittest
import calendar
import time

import mparticle
from mparticle.rest import ApiException
from mparticle.models.gdpr_consent_state import GDPRConsentState


class TestGDPRConsentState(unittest.TestCase):
    """ GDPRConsentState unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGDPRConsentState(self):
        """
        Test GDPRConsentState
        """

        now = calendar.timegm(time.gmtime())

        model = mparticle.models.gdpr_consent_state.GDPRConsentState(
            'document_agreement.v2',
            True,
            now,
            'dtmgbank.com/signup',
            'IDFA: a5d934n0-232f-4afc-2e9a-3832d95zc702',
        )

        self.assertEqual(model.document, 'document_agreement.v2')
        self.assertEqual(model.consented, True)
        self.assertEqual(model.timestamp_unixtime_ms, now)
        self.assertEqual(model.location,  'dtmgbank.com/signup')
        self.assertEqual(model.hardware_id,
                         'IDFA: a5d934n0-232f-4afc-2e9a-3832d95zc702')

    def testGDPRConsentStateMembers(self):
        """
        Test GDPRConsentState Members
        """

        now = calendar.timegm(time.gmtime())

        model = mparticle.models.gdpr_consent_state.GDPRConsentState
        model.document = 'document_agreement.v2'
        model.consented = True
        model.timestamp_unixtime_ms = now
        model.location = 'dtmgbank.com/signup'
        model.hardware_id = 'IDFA: a5d934n0-232f-4afc-2e9a-3832d95zc702'

        self.assertEqual(model.document, 'document_agreement.v2')
        self.assertEqual(model.consented, True)
        self.assertEqual(model.timestamp_unixtime_ms, now)
        self.assertEqual(model.location,  'dtmgbank.com/signup')
        self.assertEqual(model.hardware_id,
                         'IDFA: a5d934n0-232f-4afc-2e9a-3832d95zc702')


if __name__ == '__main__':
    unittest.main()
