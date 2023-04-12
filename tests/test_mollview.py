from unittest.mock import patch
from typer.testing import CliRunner

from mollview import app

TEST_FILE = "tests/test_iqu_map.fits"

runner = CliRunner()


def test_app():
    with patch("mollview.plt.show") as show_patch:
        result = runner.invoke(app, [TEST_FILE])
        assert result.exit_code == 0
        assert show_patch.called


def test_app_save():
    with patch("mollview.plt.show") as show_patch:
        with patch("mollview.plt.savefig") as savefig_patch:
            result = runner.invoke(app, [TEST_FILE, "--save"])
            assert result.exit_code == 0
            assert savefig_patch.called
        assert show_patch.called


def test_app_title():
    with patch("mollview.plt.show") as show_patch:
        result = runner.invoke(app, [TEST_FILE, "--title", "test title"])
        assert result.exit_code == 0
        assert show_patch.called


def test_app_min():
    with patch("mollview.plt.show") as show_patch:
        result = runner.invoke(app, [TEST_FILE, "--min", "1"])
        assert result.exit_code == 0
        assert show_patch.called


def test_app_max():
    with patch("mollview.plt.show") as show_patch:
        result = runner.invoke(app, [TEST_FILE, "--max", "1"])
        assert result.exit_code == 0
        assert show_patch.called


def test_app_norm():
    with patch("mollview.plt.show") as show_patch:
        result = runner.invoke(app, [TEST_FILE, "--norm", "hist"])
        assert result.exit_code == 0
        assert show_patch.called


def test_app_unit():
    with patch("mollview.plt.show") as show_patch:
        result = runner.invoke(app, [TEST_FILE, "--unit", "K"])
        assert result.exit_code == 0
        assert show_patch.called


def test_app_coord():
    with patch("mollview.plt.show") as show_patch:
        result = runner.invoke(app, [TEST_FILE, "--coord", "G", "C"])
        assert result.exit_code == 0
        assert show_patch.called


def test_app_cmap():
    with patch("mollview.plt.show") as show_patch:
        result = runner.invoke(app, [TEST_FILE, "--cmap", "afmhot"])
        assert result.exit_code == 0
        assert show_patch.called


def test_app_cbar():
    with patch("mollview.plt.show") as show_patch:
        result = runner.invoke(app, [TEST_FILE, "--no-cbar"])
        assert result.exit_code == 0
        assert show_patch.called


def test_app_notext():
    with patch("mollview.plt.show") as show_patch:
        result = runner.invoke(app, [TEST_FILE, "--notext"])
        assert result.exit_code == 0
        assert show_patch.called


def test_app_xsize():
    with patch("mollview.plt.show") as show_patch:
        result = runner.invoke(app, [TEST_FILE, "--xsize", "1000"])
        assert result.exit_code == 0
        assert show_patch.called
