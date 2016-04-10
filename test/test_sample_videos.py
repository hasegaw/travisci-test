import unittest
import os
import cv2

from test.video_test import VideoTestCase


class TestSampleVideos(VideoTestCase):

    def test_sample_video(self):
        ignored_events = [
            'on_game_special_gauge_update',
            'on_game_objective_position_update',
            'on_game_inklink_state_update',
            'on_game_individual_result',
            'on_result_detail_still',
        ]
        ignored_events.append(self._ignored_events)

        engine = self._test_engine(
            'https://dl.dropboxusercontent.com/u/14421778/IkaLog/ikalog_sample.mp4',
            expected_events=[
                'on_lobby_matched',
                'on_game_go_sign',
                'on_game_killed',
                'on_game_finish',
                'on_result_judge', 'on_result_detail', 'on_result_udemae',
                'on_result_gears',
                'on_game_session_end',
                'on_game_reset',
                'on_lobby_matching',
            ],
            ignored_events=ignored_events,
            ignore_unexpected_events=True
        )
