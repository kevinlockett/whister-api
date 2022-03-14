rm db.sqlite3
./manage.py makemigrations whistlerapi
./manage.py migrate
echo "MIGRATION COMPLETE"
./manage.py loaddata instrument_family
echo "LOAD INSTRUMENT_FAMILY DATA COMPLETE"
./manage.py loaddata instrument
echo "LOAD INSTRUMENT DATA COMPLETE"
./manage.py loaddata merchant
echo "LOAD MERCHANT DATA COMPLETE"
./manage.py loaddata music_style
echo "LOAD MUSIC_STYLE DATA COMPLETE"
./manage.py loaddata role
echo "LOAD ROLE DATA COMPLETE"
./manage.py loaddata service_type
echo "LOAD SERVICE_TYPE DATA COMPLETE"
./manage.py loaddata state
echo "LOAD STATE DATA COMPLETE"
./manage.py loaddata shop
echo "LOAD SHOP DATA COMPLETE"
./manage.py seed_db
echo "LOAD SEED_DB | AUTH_USER & APP_USER COMPLETE"
./manage.py loaddata payment_type
echo "LOAD PAYMENT_TYPE DATA COMPLETE"
./manage.py loaddata service
echo "LOAD SERVICE DATA COMPLETE"
./manage.py loaddata invoice
echo "LOAD INVOICE DATA COMPLETE"
./manage.py loaddata service_invoice
echo "LOAD SERVICE_INVOICE DATA COMPLETE"
