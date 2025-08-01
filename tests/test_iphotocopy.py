from unittest import TestCase
from unittest.mock import MagicMock, patch
from pathlib import Path
from iphotocopy.iphotocopy import ApplePhotoCopier


class TestApplePhotoCopier(TestCase):
    def setUp(self):
        self.source = Path("/mock/source")
        self.destination = Path("/mock/destination")

    @patch("iphotocopy.iphotocopy.Path.mkdir")
    @patch("iphotocopy.iphotocopy.Path.is_dir", return_value=True)
    @patch("iphotocopy.iphotocopy.shutil.move")
    @patch("iphotocopy.iphotocopy.shutil.copy2")
    @patch("iphotocopy.iphotocopy.ApplePhotoCopier.get_exif_make", return_value="Apple")
    @patch("iphotocopy.iphotocopy.Path.iterdir")
    def test_copy_mode_does_copy(self, mock_iter, mock_get, mock_copy2, mock_move, *_):
        copier = ApplePhotoCopier(self.source, self.destination, move=False)
        mock_file = MagicMock()
        mock_file.name, mock_file.is_file.return_value = "img.jpg", True
        mock_iter.return_value = [mock_file]

        copier.copy()

        mock_copy2.assert_called_once_with(mock_file, self.destination / "img.jpg")
        mock_move.assert_not_called()

    @patch("iphotocopy.iphotocopy.Path.mkdir")
    @patch("iphotocopy.iphotocopy.Path.is_dir", return_value=True)
    @patch("iphotocopy.iphotocopy.shutil.move")
    @patch("iphotocopy.iphotocopy.ApplePhotoCopier.get_exif_make", return_value="Apple")
    @patch("iphotocopy.iphotocopy.Path.iterdir")
    def test_move_mode_does_move(self, mock_iter, mock_get, mock_move, *_):
        copier = ApplePhotoCopier(self.source, self.destination, move=True)
        mock_file = MagicMock()
        mock_file.name, mock_file.is_file.return_value = "img.jpg", True
        mock_iter.return_value = [mock_file]

        copier.copy()

        mock_move.assert_called_once_with(mock_file, self.destination / "img.jpg")
