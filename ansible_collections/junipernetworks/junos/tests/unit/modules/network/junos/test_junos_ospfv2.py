# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v2.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.junipernetworks.junos.plugins.modules import junos_ospfv2
from ansible_collections.junipernetworks.junos.tests.unit.modules.utils import set_module_args

from .junos_module import TestJunosModule, load_fixture


class TestJunosOspfv2Module(TestJunosModule):
    module = junos_ospfv2

    def setUp(self):
        super(TestJunosOspfv2Module, self).setUp()

        self.mock_lock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.lock_configuration",
        )
        self.lock_configuration = self.mock_lock_configuration.start()

        self.mock_unlock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.unlock_configuration",
        )
        self.unlock_configuration = self.mock_unlock_configuration.start()

        self.mock_load_config = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.ospfv2.ospfv2.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_commit_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.ospfv2.ospfv2.commit_configuration",
        )
        self.mock_commit_configuration = self.mock_commit_configuration.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.ospfv2.ospfv2."
            "Ospfv2Facts.get_connection",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestJunosOspfv2Module, self).tearDown()
        self.mock_load_config.stop()
        self.mock_lock_configuration.stop()
        self.mock_unlock_configuration.stop()
        self.mock_commit_configuration.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(
        self,
        commands=None,
        format="text",
        changed=False,
        filename=None,
    ):
        def load_from_file(*args, **kwargs):
            output = load_fixture("junos_ospfv2_config.cfg")
            return output

        self.execute_show_command.side_effect = load_from_file

    def sorted_xml(self, xml_string):
        temp = []
        index = 0
        while index < len(xml_string):
            temp_line = ""
            if xml_string[index] == "<":
                while index < len(xml_string) and xml_string[index] != ">":
                    temp_line += xml_string[index]
                    index += 1
                temp_line += ">"
                index += 1
                temp.append(temp_line)
            else:
                while index < len(xml_string) and xml_string[index] != "<":
                    temp_line += xml_string[index]
                    index += 1
                temp.append(temp_line)
        return sorted(temp)

    def test_junos_ospfv2_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        router_id="10.200.16.75",
                        rfc1583compatibility="False",
                        external_preference=10,
                        overload=dict(
                            allow_route_leaking=True,
                            as_external=True,
                            stub_network=True,
                            timeout=1200,
                        ),
                        spf_options=dict(
                            delay=3000,
                            holddown=4000,
                            rapid_runs=9,
                            no_ignore_our_externals=True,
                        ),
                        prefix_export_limit=30000,
                        areas=[
                            dict(
                                area_id="0.0.0.100",
                                stub=dict(default_metric=200, set=True),
                                area_ranges=[
                                    dict(
                                        address="10.200.17.0/24",
                                        exact=True,
                                        restrict=True,
                                        override_metric=2000,
                                    ),
                                ],
                                interfaces=[
                                    dict(
                                        name="so-0/0/0.0",
                                        priority=3,
                                        metric=5,
                                        flood_reduction=False,
                                        passive=True,
                                        bandwidth_based_metrics=[
                                            dict(
                                                bandwidth="1g",
                                                metric=5,
                                            ),
                                        ],
                                        timers=dict(
                                            dead_interval=4,
                                            hello_interval=2,
                                            poll_interval=2,
                                            retransmit_interval=2,
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            '<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:ospf>'
            "<nc:spf-options><nc:delay>3000</nc:delay><nc:holddown>4000</nc:holddown>"
            "<nc:rapid-runs>9</nc:rapid-runs><nc:no-ignore-our-externals/></nc:spf-options>"
            "<nc:overload><nc:timeout>1200</nc:timeout><nc:allow-route-leaking/><nc:as-external/><nc:stub-network/></nc:overload>"
            "<nc:external-preference>10</nc:external-preference>"
            "<nc:prefix-export-limit>30000</nc:prefix-export-limit>"
            "<nc:no-rfc-1583/>"
            "<nc:area><nc:name>0.0.0.100</nc:name><nc:area-range><nc:name>10.200.17.0/24</nc:name>"
            "<nc:exact/><nc:restrict/><nc:override-metric>2000</nc:override-metric></nc:area-range>"
            "<nc:interface><nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority><nc:metric>5</nc:metric>"
            "<nc:passive/><nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name><nc:metric>5</nc:metric>"
            "</nc:bandwidth></nc:bandwidth-based-metrics><nc:dead-interval>4</nc:dead-interval><nc:hello-interval>2</nc:hello-interval>"
            "<nc:poll-interval>2</nc:poll-interval><nc:retransmit-interval>2</nc:retransmit-interval></nc:interface>"
            "<nc:stub><nc:default-metric>200</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>",
            '<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:router-id>10.200.16.75</nc:router-id></nc:routing-options>",
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_ospfv2_merged_areas(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        areas=[
                            dict(
                                area_id="0.0.0.100",
                                stub=dict(default_metric=200, set=True),
                                area_ranges=[
                                    dict(
                                        address="10.200.17.0/24",
                                    ),
                                    dict(
                                        address="10.200.18.0/24",
                                    ),
                                ],
                                interfaces=[
                                    dict(
                                        name="so-0/1/0.0",
                                        bandwidth_based_metrics=[
                                            dict(
                                                bandwidth="1g",
                                                metric=5,
                                            ),
                                            dict(
                                                bandwidth="10g",
                                                metric=5,
                                            ),
                                        ],
                                    ),
                                    dict(
                                        name="so-0/1/0.0",
                                        priority=3,
                                    ),
                                ],
                            ),
                            dict(
                                area_id="0.0.0.200",
                                area_range="10.200.20.0/24",
                                interfaces=[
                                    dict(
                                        name="so-0/1/0.0",
                                        bandwidth_based_metrics=[
                                            dict(
                                                bandwidth="1g",
                                                metric=5,
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            '<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:ospf><nc:area><nc:name>0.0.0.100</nc:name><nc:area-range>"
            "<nc:name>10.200.17.0/24</nc:name></nc:area-range><nc:area-range>"
            "<nc:name>10.200.18.0/24</nc:name></nc:area-range><nc:interface>"
            "<nc:name>so-0/1/0.0</nc:name><nc:bandwidth-based-metrics><nc:bandwidth>"
            "<nc:name>1g</nc:name><nc:metric>5</nc:metric></nc:bandwidth><nc:bandwidth>"
            "<nc:name>10g</nc:name><nc:metric>5</nc:metric></nc:bandwidth></nc:bandwidth-based-metrics>"
            "</nc:interface><nc:interface><nc:name>so-0/1/0.0</nc:name><nc:priority>3</nc:priority>"
            "</nc:interface><nc:stub><nc:default-metric>200</nc:default-metric></nc:stub></nc:area>"
            "<nc:area><nc:name>0.0.0.200</nc:name><nc:area-range><nc:name>10.200.20.0/24</nc:name>"
            "</nc:area-range><nc:interface><nc:name>so-0/1/0.0</nc:name><nc:bandwidth-based-metrics>"
            "<nc:bandwidth><nc:name>1g</nc:name><nc:metric>5</nc:metric></nc:bandwidth>"
            "</nc:bandwidth-based-metrics></nc:interface></nc:area></nc:ospf></nc:protocols>",
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_ospfv2_gathered(self):
        """
        :return:
        """
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gather_list = [
            {
                "areas": [
                    {
                        "area_id": "0.0.0.100",
                        "area_range": "['10.200.17.0/24', '10.200.15.0/24']",
                        "area_ranges": [
                            {
                                "address": "10.200.17.0/24",
                                "exact": True,
                                "override_metric": 2000,
                                "restrict": True,
                            },
                            {
                                "address": "10.200.15.0/24",
                                "exact": True,
                                "override_metric": 2000,
                                "restrict": True,
                            },
                        ],
                        "interfaces": [
                            {
                                "bandwidth_based_metrics": [
                                    {
                                        "bandwidth": "1g",
                                        "metric": 5,
                                    },
                                    {
                                        "bandwidth": "10g",
                                        "metric": 40,
                                    },
                                ],
                                "metric": 5,
                                "name": "so-0/0/0.0",
                                "passive": True,
                                "priority": 3,
                                "timers": {
                                    "dead_interval": 4,
                                    "hello_interval": 2,
                                    "poll_interval": 2,
                                    "retransmit_interval": 2,
                                },
                            },
                        ],
                        "stub": {
                            "default_metric": 100,
                            "set": True,
                        },
                    },
                    {
                        "area_id": "0.0.0.200",
                        "area_range": "['10.200.19.0/24']",
                        "area_ranges": [
                            {
                                "address": "10.200.19.0/24",
                                "exact": True,
                                "override_metric": 2000,
                                "restrict": True,
                            },
                        ],
                        "interfaces": [
                            {
                                "authentication": {
                                    "password": "$9$eX2vMLoaUH.5bsgJZjPf369",
                                    "type": {
                                        "simple_password": "$9$eX2vMLoaUH.5bsgJZjPf369",
                                    },
                                },
                                "name": "so-0/1/0.0",
                                "priority": 3,
                            },
                            {
                                "authentication": {
                                    "md5": [
                                        {
                                            "key": "$9$vBL87Vg4ZiqfDi/t0OSy7-V",
                                            "key_id": 10,
                                        },
                                    ],
                                },
                                "name": "so-0/2/0.0",
                                "priority": 2,
                            },
                        ],
                    },
                    {
                        "area_id": "0.0.0.120",
                        "area_range": "['10.200.20.0/24']",
                        "area_ranges": [
                            {
                                "address": "10.200.20.0/24",
                                "exact": True,
                                "override_metric": 2000,
                                "restrict": True,
                            },
                        ],
                        "interfaces": [
                            {
                                "authentication": {
                                    "md5": [
                                        {
                                            "key": "$9$IIShrvx7V2oGs2mTF3purev",
                                            "key_id": 10,
                                        },
                                    ],
                                },
                                "name": "so-0/2/0.1",
                                "priority": 2,
                            },
                        ],
                    },
                ],
                "overload": {
                    "allow_route_leaking": True,
                    "as_external": True,
                    "stub_network": True,
                    "timeout": 1200,
                },
                "reference_bandwidth": "10g",
                "rfc1583compatibility": False,
                "router_id": "10.200.16.75",
            },
        ]

    def test_junos_ospfv2_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        router_id="10.200.16.75",
                        rfc1583compatibility="False",
                        external_preference=10,
                        overload=dict(
                            allow_route_leaking=True,
                            as_external=True,
                            stub_network=True,
                            timeout=1200,
                        ),
                        spf_options=dict(
                            delay=3000,
                            holddown=4000,
                            rapid_runs=9,
                            no_ignore_our_externals=True,
                        ),
                        prefix_export_limit=30000,
                        areas=[
                            dict(
                                area_id="0.0.0.100",
                                stub=dict(default_metric=200, set=True),
                                area_ranges=[
                                    dict(
                                        address="10.200.17.0/24",
                                        exact=True,
                                        restrict=True,
                                        override_metric=2000,
                                    ),
                                ],
                                interfaces=[
                                    dict(
                                        name="so-0/0/0.0",
                                        priority=3,
                                        metric=5,
                                        flood_reduction=False,
                                        passive=True,
                                        bandwidth_based_metrics=[
                                            dict(
                                                bandwidth="1g",
                                                metric=5,
                                            ),
                                        ],
                                        timers=dict(
                                            dead_interval=4,
                                            hello_interval=2,
                                            poll_interval=2,
                                            retransmit_interval=2,
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            '<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:ospf><nc:area delete="delete">0.0.0.100</nc:area><nc:area delete="delete">0.0.0.200</nc:area>'
            '<nc:spf-options delete="delete"/><nc:reference-bandwidth delete="delete"/>'
            '<nc:no-rfc-1583 delete="delete"/><nc:overload delete="delete"/>'
            '<nc:prefix-export-limit delete="delete"/></nc:ospf><nc:ospf>'
            "<nc:spf-options><nc:delay>3000</nc:delay><nc:holddown>4000</nc:holddown><nc:rapid-runs>9</nc:rapid-runs>"
            "<nc:no-ignore-our-externals/></nc:spf-options><nc:overload><nc:timeout>1200</nc:timeout>"
            "<nc:allow-route-leaking/><nc:as-external/><nc:stub-network/></nc:overload>"
            "<nc:external-preference>10</nc:external-preference><nc:prefix-export-limit>30000</nc:prefix-export-limit>"
            "<nc:no-rfc-1583/><nc:area><nc:name>0.0.0.100</nc:name><nc:area-range><nc:name>10.200.17.0/24</nc:name>"
            "<nc:exact/><nc:restrict/><nc:override-metric>2000</nc:override-metric></nc:area-range><nc:interface>"
            "<nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority><nc:metric>5</nc:metric><nc:passive/>"
            "<nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name><nc:metric>5</nc:metric></nc:bandwidth>"
            "</nc:bandwidth-based-metrics><nc:dead-interval>4</nc:dead-interval><nc:hello-interval>2</nc:hello-interval>"
            "<nc:poll-interval>2</nc:poll-interval><nc:retransmit-interval>2</nc:retransmit-interval></nc:interface>"
            "<nc:stub><nc:default-metric>200</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>",
            '<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:router-id>10.200.16.75</nc:router-id></nc:routing-options>",
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_ospfv2_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        router_id="10.200.16.75",
                        rfc1583compatibility="False",
                        external_preference=10,
                        overload=dict(
                            allow_route_leaking=True,
                            as_external=True,
                            stub_network=True,
                            timeout=1200,
                        ),
                        spf_options=dict(
                            delay=3000,
                            holddown=4000,
                            rapid_runs=9,
                            no_ignore_our_externals=True,
                        ),
                        prefix_export_limit=30000,
                        areas=[
                            dict(
                                area_id="0.0.0.100",
                                stub=dict(default_metric=200, set=True),
                                area_ranges=[
                                    dict(
                                        address="10.200.17.0/24",
                                        exact=True,
                                        restrict=True,
                                        override_metric=2000,
                                    ),
                                ],
                                interfaces=[
                                    dict(
                                        name="so-0/0/0.0",
                                        priority=3,
                                        metric=5,
                                        flood_reduction=False,
                                        passive=True,
                                        bandwidth_based_metrics=[
                                            dict(
                                                bandwidth="1g",
                                                metric=5,
                                            ),
                                        ],
                                        timers=dict(
                                            dead_interval=4,
                                            hello_interval=2,
                                            poll_interval=2,
                                            retransmit_interval=2,
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            '<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:ospf><nc:area delete="delete">0.0.0.100</nc:area>'
            '<nc:area delete="delete">0.0.0.200</nc:area><nc:spf-options delete="delete"/>'
            '<nc:reference-bandwidth delete="delete"/><nc:no-rfc-1583 delete="delete"/>'
            '<nc:overload delete="delete"/>'
            '<nc:prefix-export-limit delete="delete"/></nc:ospf><nc:ospf><nc:spf-options>'
            "<nc:delay>3000</nc:delay><nc:holddown>4000</nc:holddown>"
            "<nc:rapid-runs>9</nc:rapid-runs><nc:no-ignore-our-externals/>"
            "</nc:spf-options><nc:overload><nc:timeout>1200</nc:timeout>"
            "<nc:allow-route-leaking/><nc:as-external/><nc:stub-network/>"
            "</nc:overload><nc:external-preference>10</nc:external-preference>"
            "<nc:prefix-export-limit>30000</nc:prefix-export-limit><nc:no-rfc-1583/>"
            "<nc:area><nc:name>0.0.0.100</nc:name><nc:area-range>"
            "<nc:name>10.200.17.0/24</nc:name><nc:exact/><nc:restrict/>"
            "<nc:override-metric>2000</nc:override-metric></nc:area-range><nc:interface>"
            "<nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority><nc:metric>5</nc:metric>"
            "<nc:passive/><nc:bandwidth-based-metrics><nc:bandwidth>"
            "<nc:name>1g</nc:name><nc:metric>5</nc:metric></nc:bandwidth></nc:bandwidth-based-metrics>"
            "<nc:dead-interval>4</nc:dead-interval><nc:hello-interval>2</nc:hello-interval>"
            "<nc:poll-interval>2</nc:poll-interval><nc:retransmit-interval>2</nc:retransmit-interval>"
            "</nc:interface><nc:stub><nc:default-metric>200</nc:default-metric>"
            "</nc:stub></nc:area></nc:ospf></nc:protocols>",
            '<nc:routing-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:router-id>10.200.16.75</nc:router-id></nc:routing-options>",
        ]
        result = self.execute_module(changed=True, commands=commands)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_ospfv2_deleted(self):
        set_module_args(
            dict(
                config=[],
                state="deleted",
            ),
        )
        commands = [
            '<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:ospf>'
            '<nc:area delete="delete">0.0.0.100</nc:area><nc:area delete="delete">0.0.0.200</nc:area>'
            '<nc:spf-options delete="delete"/><nc:reference-bandwidth delete="delete"/>'
            '<nc:no-rfc-1583 delete="delete"/><nc:overload delete="delete"/>'
            '<nc:prefix-export-limit delete="delete"/></nc:ospf></nc:protocols>',
        ]
        result = self.execute_module(changed=True, commands=commands)

        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_ospfv2_parsed(self):
        parsed_str = """
        <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
            <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
                <protocols>
                    <ospf>
                        <spf-options>
                            <delay>3000</delay>
                            <holddown>4000</holddown>
                            <rapid-runs>9</rapid-runs>
                            <no-ignore-our-externals/>
                        </spf-options>
                        <prefix-export-limit>20000</prefix-export-limit>
                        <overload>
                            <timeout>1200</timeout>
                            <allow-route-leaking/>
                            <stub-network/>
                            <as-external/>
                        </overload>
                        <reference-bandwidth>10g</reference-bandwidth>
                        <no-rfc-1583/>
                        <area>
                            <name>0.0.0.100</name>
                            <stub>
                                <default-metric>100</default-metric>
                            </stub>
                            <area-range>
                                <name>10.200.17.0/24</name>
                                <restrict/>
                                <exact/>
                                <override-metric>2000</override-metric>
                            </area-range>
                            <area-range>
                                <name>10.200.15.0/24</name>
                                <restrict/>
                                <exact/>
                                <override-metric>2000</override-metric>
                            </area-range>
                            <interface>
                                <name>so-0/0/0.0</name>
                                <passive>
                                </passive>
                                <bandwidth-based-metrics>
                                    <bandwidth>
                                        <name>1g</name>
                                        <metric>5</metric>
                                    </bandwidth>
                                    <bandwidth>
                                        <name>10g</name>
                                        <metric>40</metric>
                                    </bandwidth>
                                </bandwidth-based-metrics>
                                <metric>5</metric>
                                <priority>3</priority>
                                <retransmit-interval>2</retransmit-interval>
                                <hello-interval>2</hello-interval>
                                <dead-interval>4</dead-interval>
                                <poll-interval>2</poll-interval>
                            </interface>
                        </area>
                    </ospf>

                </protocols>
            </configuration>
        </rpc-reply>
        """
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_dict = [
            {
                "areas": [
                    {
                        "area_id": "0.0.0.100",
                        "interfaces": [
                            {
                                "name": "so-0/0/0.0",
                                "priority": 3,
                                "metric": 5,
                                "timers": {
                                    "hello_interval": 2,
                                    "dead_interval": 4,
                                    "retransmit_interval": 2,
                                    "poll_interval": 2,
                                },
                                "passive": True,
                                "bandwidth_based_metrics": [
                                    {
                                        "metric": 5,
                                        "bandwidth": "1g",
                                    },
                                    {
                                        "metric": 40,
                                        "bandwidth": "10g",
                                    },
                                ],
                            },
                        ],
                        "area_range": "['10.200.17.0/24', '10.200.15.0/24']",
                        "area_ranges": [
                            {
                                "address": "10.200.17.0/24",
                                "override_metric": 2000,
                                "exact": True,
                                "restrict": True,
                            },
                            {
                                "address": "10.200.15.0/24",
                                "override_metric": 2000,
                                "exact": True,
                                "restrict": True,
                            },
                        ],
                        "stub": {
                            "set": True,
                            "default_metric": 100,
                        },
                    },
                ],
                "overload": {
                    "allow_route_leaking": True,
                    "as_external": True,
                    "stub_network": True,
                    "timeout": 1200,
                },
                "prefix_export_limit": 20000,
                "reference_bandwidth": "10g",
                "rfc1583compatibility": False,
                "spf_options": {
                    "delay": 3000,
                    "holddown": 4000,
                    "rapid_runs": 9,
                    "no_ignore_our_externals": True,
                },
            },
        ]

    def test_junos_ospfv2_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        router_id="10.200.16.75",
                        rfc1583compatibility="False",
                        external_preference=10,
                        overload=dict(
                            allow_route_leaking=True,
                            as_external=True,
                            stub_network=True,
                            timeout=1200,
                        ),
                        spf_options=dict(
                            delay=3000,
                            holddown=4000,
                            rapid_runs=9,
                            no_ignore_our_externals=True,
                        ),
                        prefix_export_limit=30000,
                        areas=[
                            dict(
                                area_id="0.0.0.100",
                                stub=dict(default_metric=200, set=True),
                                area_ranges=[
                                    dict(
                                        address="10.200.17.0/24",
                                        exact=True,
                                        restrict=True,
                                        override_metric=2000,
                                    ),
                                ],
                                interfaces=[
                                    dict(
                                        name="so-0/0/0.0",
                                        priority=3,
                                        metric=5,
                                        flood_reduction=False,
                                        passive=True,
                                        bandwidth_based_metrics=[
                                            dict(
                                                bandwidth="1g",
                                                metric=5,
                                            ),
                                        ],
                                        timers=dict(
                                            dead_interval=4,
                                            hello_interval=2,
                                            poll_interval=2,
                                            retransmit_interval=2,
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="rendered",
            ),
        )
        rendered = (
            '<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:ospf>'
            "<nc:spf-options><nc:delay>3000</nc:delay><nc:holddown>4000</nc:holddown>"
            "<nc:rapid-runs>9</nc:rapid-runs><nc:no-ignore-our-externals/></nc:spf-options>"
            "<nc:overload><nc:timeout>1200</nc:timeout><nc:allow-route-leaking/><nc:as-external/>"
            "<nc:stub-network/></nc:overload>"
            "<nc:external-preference>10</nc:external-preference>"
            "<nc:prefix-export-limit>30000</nc:prefix-export-limit>"
            "<nc:no-rfc-1583/><nc:area><nc:name>0.0.0.100</nc:name><nc:area-range>"
            "<nc:name>10.200.17.0/24</nc:name><nc:exact/><nc:restrict/>"
            "<nc:override-metric>2000</nc:override-metric></nc:area-range><nc:interface>"
            "<nc:name>so-0/0/0.0</nc:name>"
            "<nc:priority>3</nc:priority><nc:metric>5</nc:metric><nc:passive/>"
            "<nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name>"
            "<nc:metric>5</nc:metric></nc:bandwidth></nc:bandwidth-based-metrics>"
            "<nc:dead-interval>4</nc:dead-interval><nc:hello-interval>2</nc:hello-interval>"
            "<nc:poll-interval>2</nc:poll-interval>"
            "<nc:retransmit-interval>2</nc:retransmit-interval></nc:interface><nc:stub>"
            "<nc:default-metric>200</nc:default-metric></nc:stub></nc:area></nc:ospf>"
            "</nc:protocols>"
        )
        result = self.execute_module(changed=False)
        self.assertEqual(
            self.sorted_xml(result["rendered"]),
            self.sorted_xml(rendered),
        )
