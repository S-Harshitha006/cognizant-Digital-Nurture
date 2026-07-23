# ==========================================================
# Task 1 - Understanding Django Web Framework Foundations
# ==========================================================

# 1. Request-Response Cycle
#
# Browser sends GET request to /api/courses/
#        |
# URL Router (urls.py)
#        |
# View (views.py)
#        |
# Model (models.py) queries the database
#        |
# View receives data
#        |
# Response returned to browser (HttpResponse/JSON)

# ----------------------------------------------------------

# 2. Middleware
#
# Middleware sits between the HTTP request and the view.
# It processes requests before they reach the view and
# processes responses before they are returned to the client.
#
# Two built-in middleware classes:
#
# 1. SecurityMiddleware
#    - Adds various security protections such as HTTPS support.
#
# 2. SessionMiddleware
#    - Manages user session data across requests.

# ----------------------------------------------------------

# 3. WSGI vs ASGI
#
# WSGI (Web Server Gateway Interface)
# - Supports synchronous applications.
# - Django uses WSGI by default.
#
# ASGI (Asynchronous Server Gateway Interface)
# - Supports asynchronous programming.
# - Suitable for WebSockets, real-time chat,
#   long-running connections and async APIs.
#
# Switch to ASGI when building asynchronous applications
# requiring high concurrency.

# ----------------------------------------------------------

# 4. MVC vs Django MVT
#
# MVC
# M = Model
# V = View
# C = Controller
#
# Django MVT
# Model      -> Model
# View       -> Controller (handles business logic)
# Template   -> View (UI displayed to user)
#
# Therefore:
# MVC Model      = Django Model
# MVC Controller = Django View
# MVC View       = Django Template