# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_login_api_snapshots 1'] = GenericRepr('<Response [200]>')

snapshots['test_register_api_snapshots 1'] = GenericRepr(u'<Response [200]>')
