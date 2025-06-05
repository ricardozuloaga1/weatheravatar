# WeatherAvatar

A mobile-first Flask web application that generates personalized avatars with dynamic weather-based styling and outfit recommendations.

## Features

- **Dynamic Avatar Generation**: SVG-based avatars that adapt clothing based on current weather conditions
- **Real-time Weather Integration**: Live weather data from OpenWeatherMap API
- **Location Services**: GPS geolocation and manual city/ZIP code lookup
- **Personalized Profiles**: User height, gender, and body type customization
- **Weather-Adaptive Outfits**: Intelligent clothing suggestions based on temperature and conditions
- **Mobile-First Design**: Responsive interface optimized for smartphones
- **Dark Theme**: Modern Bootstrap-based UI with custom styling

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5 with custom dark theme
- **Icons**: Feather Icons
- **Server**: Gunicorn WSGI server
- **External APIs**: OpenWeatherMap

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd weatheravatar
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
export DATABASE_URL="postgresql://username:password@localhost/weatheravatar"
export SESSION_SECRET="your-secret-key-here"
export OPENWEATHER_API_KEY="your-openweather-api-key"
```

4. Initialize the database:
```bash
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

5. Run the application:
```bash
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

## Usage

1. **Welcome**: Start at the splash screen
2. **Sign Up/Login**: Create account or log in with existing credentials
3. **Profile Setup**: Enter your height, gender, and body type preferences
4. **Avatar Preview**: View and customize your personal avatar
5. **Weather Check**: Allow location access or manually enter your city
6. **Outfit Recommendations**: Get weather-appropriate clothing suggestions

## API Endpoints

- `GET /` - Splash screen landing page
- `GET|POST /login` - User authentication
- `GET|POST /profile` - Profile creation and editing
- `GET /avatar` - Avatar preview and customization
- `GET|POST /weather` - Weather selection interface
- `GET /outfit` - Weather-based outfit recommendations
- `GET /api/weather/coords/<lat>/<lon>` - Weather data by coordinates
- `GET /api/weather/city/<city>` - Weather data by city name

## Database Schema

### Users Table
- `id`: Primary key
- `username`: Unique username
- `email`: User email address
- `password_hash`: Hashed password
- `created_at`: Account creation timestamp

### User Profiles Table
- `id`: Primary key
- `user_id`: Foreign key to users table
- `height`: Height in centimeters
- `gender`: Gender selection
- `body_type`: Body type preference
- `created_at`, `updated_at`: Timestamps

### Weather Data Table
- `id`: Primary key
- `location`: Location name
- `temperature`: Temperature in Celsius
- `description`: Weather description
- `humidity`: Humidity percentage
- `wind_speed`: Wind speed
- `timestamp`: Data retrieval time

## Configuration

### Required Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
- `SESSION_SECRET`: Flask session secret key
- `OPENWEATHER_API_KEY`: OpenWeatherMap API key

### OpenWeatherMap API Setup

1. Visit [OpenWeatherMap API](https://openweathermap.org/api)
2. Create a free account
3. Generate an API key
4. Add the key to your environment variables

## File Structure

```
weatheravatar/
├── app.py              # Flask application factory
├── main.py             # Application entry point
├── models.py           # Database models
├── routes.py           # URL routing and views
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── splash.html
│   ├── login.html
│   ├── profile.html
│   ├── avatar.html
│   ├── weather.html
│   └── outfit.html
├── static/            # Static assets
│   ├── css/
│   ├── js/
│   └── assets/
└── README.md          # This file
```

## Weather Logic

The application uses intelligent logic to recommend outfits based on:

- **Temperature ranges**: Different clothing for cold, mild, warm, and hot weather
- **Weather conditions**: Rain gear for precipitation, sun protection for sunny days
- **User profile**: Recommendations adapted to body type and preferences
- **Seasonal factors**: Consideration of typical weather patterns

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues or questions, please create an issue in the GitHub repository.