#!/usr/bin/env python3
""" Flask app module """
import requests

URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """test"""
    data = {"email": email, "password": password}
    response = requests.post(f"{URL}/users", data=data)
    assert response.status_code == 200, "Test fail"
    print("Task validate: 'register_user'")


def log_in_wrong_password(email: str, password: str) -> None:
    """test"""
    data = {"email": email, "password": password}
    response = requests.post(f"{URL}/sessions", data=data)
    assert response.status_code == 401, "Test fail"
    print("Task validate: 'log_in_wrong_password'")


def profile_unlogged() -> None:
    """test"""
    data = {"session_id": ""}
    response = requests.get(f"{URL}/profile", data=data)
    assert response.status_code == 403, "Test fail"
    print("Task validate: 'profile_unlogged'")


def log_in(email: str, password: str) -> str:
    """test"""
    data = {"email": email, "password": password}
    response = requests.post(f"{URL}/sessions", data=data)
    assert response.status_code == 200, "Test fail"
    print("Task validate: 'log_in'")
    session_id = response.cookies.get("session_id")
    return session_id


def profile_logged(session_id: str) -> None:
    """test"""
    data = {"session_id": session_id}
    response = requests.get(f"{URL}/profile", cookies=data)
    assert response.status_code == 200, "Test fail"
    print("Task validate: 'profile_logged'")


def log_out(session_id: str) -> None:
    """test"""
    data = {"session_id": session_id}
    response = requests.delete(f"{URL}/sessions", cookies=data)
    assert response.status_code == 200, "Test fail"
    print("Task validate: 'log_out'")


def reset_password_token(email: str) -> str:
    """test"""
    data = {"email": email}
    response = requests.post(f"{URL}/reset_password", data=data)
    assert response.status_code == 200, "Test fail"
    print("Task validate: 'reset_password_token'")
    reset_token = response.json().get("reset_token")
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """test"""
    data = {"email": email, "reset_token": reset_token,
            "new_password": new_password}
    response = requests.put(f"{URL}/reset_password", data=data)
    assert response.status_code == 200, "Test fail"
    print("Task validate: 'update_password'")


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == '__main__':
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
