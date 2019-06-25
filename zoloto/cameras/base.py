from itertools import groupby

import cv2

from zoloto.calibration import parse_calibration_file
from zoloto.exceptions import MissingCalibrationsError
from zoloto.marker import Marker


class BaseCamera:
    def __init__(self, **kwargs):
        self.marker_dictionary = cv2.aruco.getPredefinedDictionary(
            kwargs["marker_dict"]
        )
        self.calibration_file = kwargs.get("calibration_file")
        self.detector_params = self.get_detector_params(
            cv2.aruco.DetectorParameters_create()
        )

    def get_calibrations(self):
        if self.calibration_file is None:
            return None
        return parse_calibration_file(self.calibration_file)

    def get_detector_params(self, params):
        return params

    def get_marker_size(self, marker_id: int) -> int:  # pragma: no cover
        raise NotImplementedError()

    def capture_frame(self):  # pragma: no cover
        raise NotImplementedError()

    def save_frame(self, filename, annotate=False, frame=None):
        if frame is None:
            frame = self.capture_frame()
        if annotate:
            self._annotate_frame(frame)
        cv2.imwrite(filename, frame)
        return frame

    def _annotate_frame(self, frame):
        ids, corners = self._get_raw_ids_and_corners(frame)
        if corners:
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)

    def _get_raw_ids_and_corners(self, frame):
        corners, ids, _ = cv2.aruco.detectMarkers(
            frame, self.marker_dictionary, parameters=self.detector_params
        )
        return ids, corners

    def _get_ids_and_corners(self, frame=None):
        if frame is None:
            frame = self.capture_frame()
        ids, corners = self._get_raw_ids_and_corners(frame)
        if ids is None:
            return [], []
        return [id[0] for id in ids], [c[0] for c in corners]

    def _get_marker(self, id, corners, calibration_params):
        return Marker(id, corners, self.get_marker_size(id), calibration_params)

    def _get_eager_marker(self, id, corners, size, calibration_params, tvec, rvec):
        return Marker(id, corners, size, calibration_params, (rvec, tvec))

    def process_frame(self, frame=None):
        ids, corners = self._get_ids_and_corners(frame)
        calibration_params = self.get_calibrations()
        for corners, id in zip(corners, ids):
            yield self._get_marker(id, corners, calibration_params)

    def process_frame_eager(self, frame=None):
        calibration_params = self.get_calibrations()
        if not calibration_params:
            raise MissingCalibrationsError()
        ids, corners = self._get_ids_and_corners(frame)

        def get_marker_size(id_and_corners):
            return self.get_marker_size(id_and_corners[0])

        sorted_corners = sorted(zip(ids, corners), key=get_marker_size)
        for size, ids_and_corners in groupby(sorted_corners, get_marker_size):
            ids, corners = zip(*ids_and_corners)
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
                corners, size, *calibration_params
            )
            for id, corners, rvec, tvec in zip(ids, corners, rvecs[0], tvecs[0]):
                yield self._get_eager_marker(
                    id, corners, size, calibration_params, tvec, rvec
                )

    def get_visible_markers(self, frame=None):
        ids, _ = self._get_ids_and_corners(frame)
        return ids

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.close()

    def __del__(self):
        self.close()
