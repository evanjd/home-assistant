"""Constants in Logi Circle component."""

ATTR_API = 'api'

CONF_CLIENT_ID = 'client_id'
CONF_CLIENT_SECRET = 'client_secret'
CONF_API_KEY = 'api_key'
CONF_REDIRECT_URI = 'redirect_uri'
CONF_CAMERAS = 'cameras'
CONF_FFMPEG_ARGUMENTS = 'ffmpeg_arguments'

DEFAULT_CACHEDB = '.logi_cache.pickle'

DOMAIN = 'logi_circle'
DATA_LOGI = DOMAIN

LED_MODE_KEY = 'LED'
RECORDING_MODE_KEY = 'RECORDING_MODE'

SIGNAL_LOGI_CIRCLE_UPDATE = 'logi_circle_update'

# Activity properties: hass state prop, API wrapper prop
LOGI_ACTIVITY_KEYS = [
    ['activity_id', 'activity_id'],
    ['relevance_level', 'relevance_level'],
    ['start_time', 'start_time_utc'],
    ['duration', 'duration']
]

# Sensor types: Name, unit of measure, icon per sensor key.
LOGI_SENSORS = {
    'battery_level': [
        'Battery', '%', 'battery-50'],

    'last_activity_time': [
        "Last Activity", None, 'history'],

    'signal_strength_category': [
        "WiFi Signal Category", None, 'wifi'],

    'signal_strength_percentage': [
        "WiFi Signal Strength", '%', 'wifi']
}

# Binary sensor types: Name, device_class, icon
LOGI_BINARY_SENSORS = {
    'activity': [
        'Activity', 'motion', 'walk'],

    'charging': [
        'Charging', 'connectivity', 'battery'],

    'recording': [
        'Recording', None, 'eye'],

    'streaming': [
        'Streaming', None, 'camera']
}

# Attribution
CONF_ATTRIBUTION = "Data provided by circle.logi.com"
DEVICE_BRAND = 'Logitech'