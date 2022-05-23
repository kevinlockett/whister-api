DELETE from auth_user
WHERE id > 30;

DELETE from whistlerapi_appuser
WHERE id > 30;

UPDATE whistlerapi_appuser
SET approved = 1
WHERE id <= 35 
AND role_id IS 2