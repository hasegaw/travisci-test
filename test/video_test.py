import unittest
import os
import cv2

class VideoTestCase(unittest.TestCase):

    scene_name = None

    _ignored_events = [
            'on_debug_read_next_frame',
            'on_frame_read',
            'on_show_preview',
            'on_draw_preview',
            'on_mark_rect_in_preview',
    ]

    def _load_screenshot(self, filename):
        filepath = os.path.join('test_data', 'movies',
                                self.scene_name, filename)

    def noop(self, context):
        pass

    def on_frame_read_failed(self, context):
        self.engine.stop()

    def onUncatchedEvent(self, event_name, context):
        if event_name in self._ignored_events:
            return

        if len(self._expected_events) == 0:
            return

        self._observed_events.append(event_name)

        try:
            assert self._expected_events[0] == event_name,            'Unexpected event'
            self._expected_events.pop(0)
        except AssertionError:
            if not self._ignore_unexpected_events:
                raise

    def _test_engine(self, mp4_filename,expected_events, game_lang=None, ignored_events=None, ignore_unexpected_events=True, framerate=10):
        from ikalog.utils import Localization
        from ikalog.inputs import CVFile
        from ikalog.engine import IkaEngine
        from ikalog.outputs.debug import DebugLog

        if game_lang is not None:
            Localization.set_game_languages(game_lang)

        self._ignore_unexpected_events = ignore_unexpected_events
        self._observed_events = []
        self._expected_events = expected_events
        if ignored_events is not None:
            self._ignored_events = ignored_events

        self.errors = []
        source = CVFile()
        source.start_video_file(mp4_filename)
        source.set_frame_rate(framerate)
        source.need_resize = True
        output_plugins = [
            self,
        ]

        self.engine = IkaEngine()

        self.engine.set_capture(source)
        self.engine.set_plugins(output_plugins)
        self.engine.pause(False)

        print('Engine started')
        try:
            self.engine.run()
        except EOFError:
            pass
        print('Engine stopped')

        print('events observed: ', self._observed_events)
        print('expected events remained: ', self._expected_events)
        assert len(self._expected_events) == 0

        # dereference the engine
        engine = self.engine
        self.engine = None
        return engine
