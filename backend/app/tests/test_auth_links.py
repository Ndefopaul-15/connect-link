import pytest

from app import create_app, db
from app.models import Link, LinkDailyStats


@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def register_user(client, email="test@example.com", password="password123"):
    response = client.post(
        "/api/auth/register",
        json={"email": email, "password": password},
    )
    return response


def login_user(client, email="test@example.com", password="password123"):
    response = client.post(
        "/api/auth/login",
        json={"email": email, "password": password},
    )
    return response


def test_register_and_login(client):
    response = register_user(client)
    assert response.status_code == 201
    data = response.get_json()
    assert "access_token" in data
    assert "user" in data

    login_response = login_user(client)
    assert login_response.status_code == 200
    login_data = login_response.get_json()
    assert "access_token" in login_data


def test_create_and_get_link(client, app):
    response = register_user(client)
    data = response.get_json()
    token = data["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    create_response = client.post(
        "/api/links",
        json={"long_url": "https://example.com"},
        headers=headers,
    )
    assert create_response.status_code == 201
    created = create_response.get_json()["link"]
    slug = created["short_url_slug"]

    get_response = client.get(f"/api/links/{slug}", headers=headers)
    assert get_response.status_code == 200
    link_data = get_response.get_json()
    assert link_data["long_url"] == "https://example.com"


def test_redirect_records_click_and_stats(client, app):
    response = register_user(client)
    data = response.get_json()
    token = data["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    create_response = client.post(
        "/api/links",
        json={"long_url": "https://example.com"},
        headers=headers,
    )
    assert create_response.status_code == 201
    created = create_response.get_json()["link"]
    slug = created["short_url_slug"]
    link_id = created["link_id"]

    redirect_response = client.get(f"/api/{slug}", follow_redirects=False)
    assert redirect_response.status_code in (301, 302)

    with app.app_context():
        link = Link.query.get(link_id)
        assert link is not None
        assert len(link.clicks) == 1
        assert len(link.daily_stats) == 1
        stats = link.daily_stats[0]
        assert stats.total_clicks == 1
        assert stats.unique_clicks == 1
