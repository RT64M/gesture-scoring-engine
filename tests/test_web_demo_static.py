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


def test_inverse_page_uses_tau_compressed_adaptive_score():
    app_source = (ROOT / "web_demo" / "app.js").read_text(encoding="utf-8")

    assert "inverse_adaptive_score" in app_source
    assert "scoreFromDistanceAndTau" in app_source
    assert "tighter tau compresses adaptive score" in app_source
    assert "item.inverse_adaptive_score" in app_source


def test_inverse_page_copy_explains_raw_adaptive_inverse_relationship():
    app_source = (ROOT / "web_demo" / "app.js").read_text(encoding="utf-8")

    assert "Fixed raw score rises as the Palm attempt improves" in app_source
    assert "adaptive score stays flatter because tau tightens" in app_source
    assert "inverse progress rises because strictness is counted" in app_source


def test_feature_explanation_lists_all_dimensions_and_marks_top_five():
    app_source = (ROOT / "web_demo" / "app.js").read_text(encoding="utf-8")
    styles_source = (ROOT / "web_demo" / "styles.css").read_text(encoding="utf-8")

    assert "renderFeatureExplanation" in app_source
    assert "topDeviationFeatures" in app_source
    assert "topFeatureBadge" in app_source
    assert "feature-row impact" in app_source
    assert "feature_deviations.slice(0, 5)" not in app_source
    assert ".feature-row.impact" in styles_source


def test_live_classifier_camera_and_snapshot_are_rotated():
    app_source = (ROOT / "web_demo" / "app.js").read_text(encoding="utf-8")
    styles_source = (ROOT / "web_demo" / "styles.css").read_text(encoding="utf-8")

    assert "transform: scaleX(-1) rotate(180deg)" in styles_source
    assert "drawRotatedCameraFrame" in app_source
    assert "context.translate(width, height)" in app_source
    assert "context.rotate(Math.PI)" in app_source
    assert "context.moveTo(start.x * width, start.y * height)" in app_source
    assert "context.arc(point.x * width, point.y * height" in app_source
