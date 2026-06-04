from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def test_step1_snapshot_landmarker_uses_image_mode():
    app_source = (ROOT / "web_demo" / "app.js").read_text(encoding="utf-8")

    assert 'runningMode: "IMAGE"' in app_source
    assert ".detect(canvas)" in app_source


def test_step1_renders_selected_gesture_2d_description():
    index_source = (ROOT / "web_demo" / "index.html").read_text(encoding="utf-8")
    app_source = (ROOT / "web_demo" / "app.js").read_text(encoding="utf-8")

    assert 'id="target-gesture-skeleton"' in index_source
    assert 'id="target-gesture-description"' in index_source
    assert "renderTargetGestureDescription" in app_source
    assert "gesture_skeletons" in app_source
