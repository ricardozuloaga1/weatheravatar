from flask import render_template, request, jsonify, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login and signup route"""
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validate required fields
        if not email or not password:
            flash('Email and password are required.', 'error')
            return render_template('login.html', title='Login - WeatherAvatar')
        
        if form_type == 'login':
            # Handle login
            user = User.query.filter_by(email=email).first()
            if user and user.password_hash and check_password_hash(user.password_hash, password):
                session['user_id'] = user.id
                session['user_email'] = user.email
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid email or password.', 'error')
        
        elif form_type == 'signup':
            # Handle signup
            confirm_password = request.form.get('confirm_password')
            
            if not confirm_password:
                flash('Please confirm your password.', 'error')
            elif password != confirm_password:
                flash('Passwords do not match.', 'error')
            elif User.query.filter_by(email=email).first():
                flash('Email already registered.', 'error')
            else:
                # Create new user
                username = email.split('@')[0] if '@' in email else email
                password_hash = generate_password_hash(password)
                
                new_user = User()
                new_user.username = username
                new_user.email = email
                new_user.password_hash = password_hash
                
                try:
                    db.session.add(new_user)
                    db.session.commit()
                    
                    session['user_id'] = new_user.id
                    session['user_email'] = new_user.email
                    flash('Account created successfully!', 'success')
                    return redirect(url_for('dashboard'))
                except Exception as e:
                    db.session.rollback()
                    logger.error(f'Error creating user: {e}')
                    flash('Error creating account. Please try again.', 'error')
    
    return render_template('login.html', title='Login - WeatherAvatar')


@app.route('/logout')
def logout():
    """Logout route"""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


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
