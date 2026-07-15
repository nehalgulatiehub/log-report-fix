import json
from pathlib import Path

REPORT = Path("/app/report.json")

EXPECTED = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def test_success_criterion_1_report_exists():
    """Success Criterion 1: report.json exists."""
    assert REPORT.exists()


def test_success_criterion_2_valid_json():
    """Success Criterion 2: report.json contains valid JSON."""
    json.loads(REPORT.read_text())


def test_success_criterion_3_required_fields():
    """Success Criterion 3: required fields are present."""
    data = json.loads(REPORT.read_text())

    assert set(data.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }


def test_success_criterion_4_correct_values():
    """Success Criterion 4: values are correct."""
    data = json.loads(REPORT.read_text())

    assert data == EXPECTED