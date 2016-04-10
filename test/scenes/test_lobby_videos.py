import unittest
import os
import cv2

from test.video_test import VideoTestCase

url_base = 'https://dl.dropboxusercontent.com/u/14421778/IkaLog/test/'

class TestLobbyVideos(VideoTestCase):

    scene_name = 'lobby'

    def test_lobby_tag_2_matching_to_matched(self):
        engine = self._test_engine(
            url_base + 'lobby_ja_tag_2_matching_to_matched.mp4',
            expected_events=[
                'on_lobby_matching',
                'on_lobby_matched',
            ]
        )

        assert engine.context['lobby']['type'] == 'tag'
        assert engine.context['lobby']['state'] == 'matched'
        assert engine.context['lobby']['team_members'] == 2

    def test_lobby_tag_2_matched(self):
        engine = self._test_engine(
            url_base + 'lobby_ja_tag_2_matched.mp4',
            game_lang='ja',
            expected_events=[
                'on_lobby_matched',
            ]
        )

        assert engine.context['lobby']['type'] == 'tag'
        assert engine.context['lobby']['state'] == 'matched'
        assert engine.context['lobby']['team_members'] == 2

    def test_lobby_tag_4_matched(self):
        engine = self._test_engine(
            url_base + 'lobby_ja_tag_4_matched.mp4',
            game_lang='ja',
            expected_events=[
                'on_lobby_matched',
            ]
        )

        assert engine.context['lobby']['type'] == 'tag'
        assert engine.context['lobby']['state'] == 'matched'
        assert engine.context['lobby']['team_members'] == 4

    def test_lobby_public_matching_to_matched(self):
        engine = self._test_engine(
            url_base + 'lobby_ja_public_matching_to_matched.mp4',
            game_lang='ja',
            expected_events=[
                'on_lobby_matching',
                'on_lobby_matched',
            ]
        )

        assert engine.context['lobby']['type'] == 'public'
        assert engine.context['lobby']['state'] == 'matched'

    def test_lobby_fes_matching_to_matched(self):
        engine = self._test_engine(
            url_base + 'lobby_ja_fes_matching_to_matched.mp4',
            game_lang='ja',
            expected_events=[
                'on_lobby_matched',
            ]
        )

        assert engine.context['lobby']['type'] == 'festa'
        assert engine.context['lobby']['state'] == 'matched'
