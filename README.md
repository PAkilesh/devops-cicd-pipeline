# Python Flask + PostgreSQL Docker Compose Project

A containerized IT Asset Management API built using Python Flask, PostgreSQL, Docker, and Docker Compose.

## Project Overview

This project demonstrates how to build a Python backend API, connect it to PostgreSQL, containerize the application with Docker, run multiple services using Docker Compose, persist database data using Docker volumes, and troubleshoot service-to-service communication issues.

## Architecture

Client / Browser  
↓  
Python Flask API  
↓  
Docker Network  
↓  
PostgreSQL Database  
↓  
Docker Volume

## Technologies Used

- Python 3
- Flask
- PostgreSQL 16
- psycopg2
- Docker
- Docker Compose
- Docker Networking
- Docker Volumes
- Git
- GitHub

## Project Structure

```text
docker-compose-fullstack/
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── database/
│   └── init.sql
├── docker-compose.yml
├── .gitignore
└── README.md
