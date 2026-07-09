from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "site"


def load_json(relative: str) -> dict:
    return json.loads((SITE / relative).read_text(encoding="utf-8"))


def test_manual_gallery_slide_is_portrait_with_cv_and_contact_routes():
    site = load_json("content/site.json")
    route_paths = {item["path"] for item in site["routes"]}
    gallery = site.get("gallery", [])

    assert len(gallery) == 1
    first = gallery[0]
    assert first["image"] == "assets/img/me.png"
    assert (SITE / first["image"]).is_file()

    link_routes = {link.get("route") for link in first.get("links", [])}
    assert {"/cv/ml", "/contact"} <= link_routes
    assert link_routes <= route_paths


def test_gallery_project_slides_are_generated_from_project_items_contract():
    site = load_json("content/site.json")
    projects = load_json("content/projects.json")
    route_paths = {item["path"] for item in site["routes"]}
    gallery = site.get("gallery", [])

    assert len(gallery) == 1
    manual = gallery[0]
    assert manual["image"] == "assets/img/me.png"
    assert manual.get("kind") != "project"
    assert "projectId" not in manual

    project_routes = {project["route"] for project in projects["items"]}
    assert manual.get("route") not in project_routes
    assert all(link.get("route") not in project_routes for link in manual.get("links", []))

    for project in projects["items"]:
        assert project["route"] in route_paths
        assert (SITE / project["image"]).is_file()


def test_gallery_runtime_uses_shared_project_projection_and_route_links():
    helper = (SITE / "assets" / "js" / "gallery-model.js").read_text(encoding="utf-8")
    components = (SITE / "assets" / "js" / "components.js").read_text(encoding="utf-8")
    widgets = (SITE / "assets" / "js" / "widgets.js").read_text(encoding="utf-8")

    assert "content.site.gallery" not in components
    assert "content.site.gallery" not in widgets
    assert "buildGallerySlides(content)" in components
    assert "buildGallerySlides(content)" in widgets
    assert "content?.projects?.items" in helper
    assert "project.image" in helper
    assert "project.title" in helper
    assert "project.route" in helper
    assert "project.subtitle" in helper
    assert "project.tags" in helper
    assert "routeHref(item.route)" in widgets
    assert "dataRoute" in components
    assert "dataset.route" in widgets
    assert "hashHref" not in helper
    assert "hashHref" not in components
    assert "hashHref" not in widgets
