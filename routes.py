from flask import render_template, request, jsonify, flash, redirect, url_for
from app import app, db
from models import User, WeatherData, Avatar
import logging
import os

logger = logging.getLogger(__name__)


@app.route('/')
def index():
    """Splash screen landing page for WeatherAvatar"""
    return render_template('splash.html', title='Welcome to WeatherAvatar')


@app.route('/dashboard')
def dashboard():
    """Main dashboard page for WeatherAvatar"""
    return render_template('index.html', title='WeatherAvatar')


@app.route('/mockups')
def mockups():
    """Route for previewing uploaded mockups and designs"""
    return render_template('mockups.html', title='Design Mockups - WeatherAvatar')


@app.route('/weather')
def weather():
    """Weather data display route - will be implemented based on mockups"""
    # This route will be expanded based on UI mockups
    weather_data = WeatherData.query.order_by(WeatherData.timestamp.desc()).limit(10).all()
    return render_template('weather.html', weather_data=weather_data, title='Weather - WeatherAvatar')


@app.route('/avatar')
def avatar():
    """Avatar customization route - will be implemented based on mockups"""
    # This route will be expanded based on UI mockups
    avatars = Avatar.query.all()
    return render_template('avatar.html', avatars=avatars, title='Avatar - WeatherAvatar')


@app.route('/api/weather/<location>')
def api_weather(location):
    """API endpoint for weather data - placeholder for future implementation"""
    # This will be implemented to fetch real weather data
    # For now, return a structured response for frontend development
    return jsonify({
        'location': location,
        'status': 'placeholder',
        'message': 'Weather API integration will be implemented based on UI requirements'
    })


@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('404.html', title='Page Not Found - WeatherAvatar'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    db.session.rollback()
    logger.error(f'Internal server error: {error}')
    return render_template('500.html', title='Server Error - WeatherAvatar'), 500


# Context processor to make common variables available in all templates
@app.context_processor
def inject_common_vars():
    """Inject common variables into all templates"""
    return {
        'app_name': 'WeatherAvatar',
        'version': '1.0.0'
    }
