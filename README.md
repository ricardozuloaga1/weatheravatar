# WeatherAvatar

A Flask app that turns the weather into a daily outfit, illustrated on a customizable full-body avatar.

## Daily outfit experience

Open `/today` (also the destination of `/` and `/outfit`). No account or API key is needed to try it.

- Full-body vector avatar with facial features, four hair styles, five skin tones, four hair colors, three builds, and adjustable height.
- Layered tees, button-downs, knits, overshirts, rain shells, insulated coats, shorts/trousers, sneakers/boots. Four coordinated color palettes.
- Recommendations use hourly **apparent temperature**, rain probability/conditions, wind, personal warmth preference, and activity. Apparent temperature already includes environmental effects; wind is not subtracted a second time.
- Choose the next twelve forecast hours or remaining morning/afternoon/evening hours. Elapsed periods are disabled. Weather uses the selected location's timezone.
- Search and select a city, or explicitly request browser geolocation. Forecasts are returned directly for those coordinates, never read from another user's weather history.
- Four clearly labeled sample forecasts support exploration without network access. Live forecast failures remain explicit rather than silently substituting sample data.
- Avatar appearance is saved in this browser's local storage. Canceling the editor restores the previous appearance. The last selected location, comfort, activity, units, and palette are also saved locally; a returning visit refreshes the last location. Nothing is synced to an account.

This first iteration uses generic illustrated clothing. It does **not** implement a personal wardrobe, retailer catalogues, selfie generation, virtual try-on, or garment fit prediction. The original account/profile pages remain available but are not required for the new experience; their saved profiles do not sync with the browser avatar yet.

## Run locally

Python 3.11+ and [uv](https://docs.astral.sh/uv/) are required.

```sh
uv sync
# Use an isolated development database rather than the legacy tracked database.
DATABASE_URL=sqlite:////tmp/weatheravatar-dev.db uv run flask --app main run --port 5074
```

Open http://127.0.0.1:5074/today. Sample mode works immediately. Internet access is needed for live weather and optional Google Fonts; system font fallbacks are provided.

Set `SESSION_SECRET` for any shared environment. Debug is off by default; set `FLASK_DEBUG=1` only for local development. For a deployed service, use Gunicorn, not Flask's development server.

## Weather sources and endpoints

New daily experience:

- `GET /api/locations?q=Caracas`: Open-Meteo geocoding, up to five results for explicit location selection.
- `GET /api/daily-weather?lat=10.5&lon=-66.9`: Open-Meteo current weather and two days of hourly forecasts. Celsius, km/h, and the location's local time.

Weather attribution: [Open-Meteo](https://open-meteo.com/). The public endpoints are for noncommercial use; review [their pricing and usage terms](https://open-meteo.com/en/pricing) before a commercial release. Production hardening should add rate limits and caching keyed by coordinates. The endpoint currently makes a request per explicit location selection.

Legacy weather endpoints still use `OPENWEATHER_API_KEY`. They are not used by the new daily view.

## Validate

```sh
uv run python -m unittest discover -s tests -v
node --test tests/outfit-engine.test.mjs
```

Tests cover forecast input validation, provider failures, location isolation, cold/rain/heat/wind behavior, comfort and activity adjustments, and forecast windows crossing midnight.

## Main files

- `daily.py`: daily view and weather adapter.
- `templates/daily.html`, `static/css/daily.css`: responsive daily interface.
- `static/js/outfit-engine.mjs`: deterministic outfit selection and forecast windows.
- `static/js/avatar.mjs`: vector avatar and garment layers.
- `static/js/daily.mjs`: UI, location selection, and local appearance preferences.

Next: user-owned garments and persistence, then optional selfie likeness. Keep outfit selection separate from rendering so both can evolve independently.
