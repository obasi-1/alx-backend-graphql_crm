#!/bin/bash
# Script to delete inactive customers (no orders in the last year)

# Navigate to project directory
cd /c/Users/OBA/Documents/alx-backend-graphql_crm || exit

# Run Django shell command
deleted_count=$(echo "
from django.utils import timezone
from datetime import timedelta
from crm.models import Customer

one_year_ago = timezone.now() - timedelta(days=365)
qs = Customer.objects.filter(orders__isnull=True, created_at__lt=one_year_ago)
count = qs.count()
qs.delete()
print(count)
" | /c/Users/OBA/Documents/alx-backend-graphql_crm/venv/Scripts/python manage.py shell)

# Log result with timestamp
echo \"$(date '+%Y-%m-%d %H:%M:%S') - Deleted $deleted_count inactive customers\" >> /tmp/customer_cleanup_log.txt
