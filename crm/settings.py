INSTALLED_APPS = [
    # ... your other apps
    "django_crontab",
    "crm",
]

CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
]
