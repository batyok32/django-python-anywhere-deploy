

curl \
    -X GET \
    -H "Content-Type: application/json" \
    -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNTYzMzI4NiwianRpIjoiMjdmZTE4MGQ5YzVhNGIzZDhmZGMyYzdmNzAxNTI3OWUiLCJ1c2VyX2lkIjoxfQ.jN7fYh3Zi3J1aAIkjavUOz7vNk-mhAOrNlG_U__qGmE" \
    http://localhost:8000/api/v0/account/info/

curl \
    -X GET \
    -H "Content-Type: application/json" \
    -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0NDI5NzU5LCJqdGkiOiIyNDJiZjE3MjdkOGM0YWZlYTFiY2ViZTRkNGJkMTAzMCIsInVzZXJfaWQiOjF9.gZJ0rdWjhZPqEf_REo2yfJ34T0u4uOE7QdYsTbWV2jI" \
    http://localhost:8000/api/v0/account/info/


# curl \
#     -X GET \
#     -H "Content-Type: application/json" \
#     http://localhost:8000/api/v0/comments/1/



# curl \
#     -X POST \
#     -H "Content-Type: application/json" \
#     -d '{"email": "betoglan042@gmail.com","name":"batyr", "password": "batyrbet", "re_password":"batyrbet"}' \
#     http://localhost:8000/auth/users/
# curl \
#     -X POST \
#     -H "Content-Type: application/json" \
#     -d '{"email": "betoglan042@gmail.com", "password": "batyrbet"}' \
#     http://localhost:8000/auth/jwt/create/
# curl \
#     -X POST \
#     -H "Content-Type: application/json" \
#     -d '{"uid": "Mg", "token": "alf3p6-5cbb3add23866ce654c22c7059c0524a"}' \
#     http://localhost:8000/auth/activation/
# http://example.com/activate/Mg/alf3p6-5cbb3add23866ce654c22c7059c0524a
#     -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4OTUyNTEyLCJqdGkiOiIxZjIwMmM4NzcxMTc0NjhjODRjZDdlZDczNzgzNzM3NCIsInVzZXJfaWQiOjF9.Mf3xgO-MGMNrP54gCRDOvE7HuyWF-l0KmD5-gpEcsME" \
#     {"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMDE1NDkxMiwianRpIjoiYjczNGUxOTZkZjY2NGY0Y2IzNTJlMmJjYjI0ZTkxYTgiLCJ1c2VyX2lkIjoxfQ.n4rnVci5RtHZYaRhKJePPZ34ERtdU8cy4uF5gLFNvbI",
#     "access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4OTUyNTEyLCJqdGkiOiIxZjIwMmM4NzcxMTc0NjhjODRjZDdlZDczNzgzNzM3NCIsInVzZXJfaWQiOjF9.Mf3xgO-MGMNrP54gCRDOvE7HuyWF-l0KmD5-gpEcsME"}
# # curl \
# #   -X PATCH \
# #   -H "Content-Type: application/json" \
# #   -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NzMwODM5LCJqdGkiOiI5NzZhMjBkMjIxNTM0OThmYWUyOTUzM2ZmM2ZkMGIyMSIsInVzZXJfaWQiOjEsInBob25lX251bWJlciI6bnVsbH0.Gpvb0OOryW2pPv_MIFtCkdE-KmLBA1E02AKQ-wWs6Hk" \
# #   -d '{"address": "cehow"}' \
# #   http://localhost:8000/api/auth/user/me/
curl \
  -X PATCH \
  -H "Content-Type: multipart/form-data" \
  -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI1ODA2OTE3LCJqdGkiOiIwNjgyNmZiMDMzM2Q0YThkYjY2NTBjMjhkZmQyMjAwYSIsInVzZXJfaWQiOjF9.gnSX0YGQin3_vCUT3wJe_F7UuBG499bI40Jwa7lCrvw" \
  -d '{"username": "batyr", "phone_number": 99362535294,"address": "asfasf","email": "cookgoc@gmail.com", "city":"Ag", "profile_img":"http://127.0.0.1:8000/media/CACHE/images/users/2021/07/06/candy_car_tmDPVeh/51bb9fa24230c9af31a9427ad7b436bc.webp"}' \
  http://localhost:8000/auth/users/me/

  

# curl \
#   -X GET \
#   -H "Content-Type: application/json" \
#   -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4OTUyOTY5LCJqdGkiOiJlMjAxZmNlZDE4Mjg0MjMzYWM0YjRiOTMxYjdjOTk1OCIsInVzZXJfaWQiOjJ9.xnaE3-5BmuS9xsrP6q6u3b-io54-XMG3zLahbcWJaWw" \
#   http://localhost:8000/auth/users/2/

# #   -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NzMwODM5LCJqdGkiOiI5NzZhMjBkMjIxNTM0OThmYWUyOTUzM2ZmM2ZkMGIyMSIsInVzZXJfaWQiOjEsInBob25lX251bWJlciI6bnVsbH0.Gpvb0OOryW2pPv_MIFtCkdE-KmLBA1E02AKQ-wWs6Hk" \
  
# # curl \

# #   -X OPTIONS \
# #   -H "Content-Type: application/json" \
# #   -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NzMwODM5LCJqdGkiOiI5NzZhMjBkMjIxNTM0OThmYWUyOTUzM2ZmM2ZkMGIyMSIsInVzZXJfaWQiOjEsInBob25lX251bWJlciI6bnVsbH0.Gpvb0OOryW2pPv_MIFtCkdE-KmLBA1E02AKQ-wWs6Hk" \
# #   http://localhost:8000/api/auth/user/me/



# # curl --header "Content-Type: application/json" - X POST http://127.0.0.1:8000/api/auth/token/obtain/ -- data '{"username":"admin","password":"batyrbet"}'
# # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTM4MjI1OCwianRpIjoiNmFjYWY2ZDdlODQ2NDQzYjhhYjY0YTA2YWU3ZTVmMjkiLCJ1c2VyX2lkIjoyfQ.XGc3NZS0wgiFcCZJKiwj-Qu1i0k6T6E8kQGo-Xg7pbg
# # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTM4MjMzOSwianRpIjoiOGIyZWI2NTAzMWVlNDk3MmI3MjY0YjRhMTIwOTIyOGIiLCJ1c2VyX2lkIjoyfQ.UbE1iZGmNhEzCrmOcDwSY99RL_yVJdE5ARe2mz33lDM
# # curl \
# #   -X POST \
# #   -H "Content-Type: application/json" \
# #   -d '{"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTM4MjM4NiwianRpIjoiMmY1NTMwNmVkZWNjNGQyYWIyZmVlYjNhYzMxNTZlNDEiLCJ1c2VyX2lkIjoyfQ.trm9v_i4aJ3HKZJnVF4Axs201nBMaXidSC1S0zYn95k"}' \
# #   http://localhost:8000/api/auth/token/refresh/


# # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTM4MjM4NiwianRpIjoiMmY1NTMwNmVkZWNjNGQyYWIyZmVlYjNhYzMxNTZlNDEiLCJ1c2VyX2lkIjoyfQ.trm9v_i4aJ3HKZJnVF4Axs201nBMaXidSC1S0zYn95k

# # "{
# #     "username":"pk",
# #     "password":"batyrbet",
# # }"

# # {"username": "admin", "password": "batyrbet", "phone_number":63000000}

# -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwMjQzMDkzLCJqdGkiOiJhMTMyYTI1ZTRiZTI0ZjVhYTUzN2M3YmQ5MzMzMTE5NyIsInVzZXJfaWQiOjF9.KTaljwD4sFSsMVmTg5pU69By4PDlZas1vAekdt8IMeI" 
#     {"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMDE1NDkxMiwianRpIjoiYjczNGUxOTZkZjY2NGY0Y2IzNTJlMmJjYjI0ZTkxYTgiLCJ1c2VyX2lkIjoxfQ.n4rnVci5RtHZYaRhKJePPZ34ERtdU8cy4uF5gLFNvbI",
#      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4OTUyNTEyLCJqdGkiOiIxZjIwMmM4NzcxMTc0NjhjODRjZDdlZDczNzgzNzM3NCIsInVzZXJfaWQiOjF9.Mf3xgO-MGMNrP54gCRDOvE7HuyWF-l0KmD5-gpEcsME"}
# curl \
#   -X PATCH \
#   -H "Content-Type: application/json" \
#   -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NzMwODM5LCJqdGkiOiI5NzZhMjBkMjIxNTM0OThmYWUyOTUzM2ZmM2ZkMGIyMSIsInVzZXJfaWQiOjEsInBob25lX251bWJlciI6bnVsbH0.Gpvb0OOryW2pPv_MIFtCkdE-KmLBA1E02AKQ-wWs6Hk" \
#   -d '{"address": "cehow"}' \
#   http://localhost:8000/api/auth/user/me/
# curl \
#   -X PUT \
#   -H "Content-Type: application/json" \
#   -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4OTUyNTEyLCJqdGkiOiIxZjIwMmM4NzcxMTc0NjhjODRjZDdlZDczNzgzNzM3NCIsInVzZXJfaWQiOjF9.Mf3xgO-MGMNrP54gCRDOvE7HuyWF-l0KmD5-gpEcsME" \
#   -d '{"username": "batyr", "phone_number":"61000000", "city":"Ag"}' \
#   http://localhost:8000/api/auth/user/me/
# curl \
#     -X GET \
#     -H "Content-Type: application/json" \
#     -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwMjQzMDkzLCJqdGkiOiJhMTMyYTI1ZTRiZTI0ZjVhYTUzN2M3YmQ5MzMzMTE5NyIsInVzZXJfaWQiOjF9.KTaljwD4sFSsMVmTg5pU69By4PDlZas1vAekdt8IMeI" \
#     http://localhost:8000/auth/users/me/

#   -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NzMwODM5LCJqdGkiOiI5NzZhMjBkMjIxNTM0OThmYWUyOTUzM2ZmM2ZkMGIyMSIsInVzZXJfaWQiOjEsInBob25lX251bWJlciI6bnVsbH0.Gpvb0OOryW2pPv_MIFtCkdE-KmLBA1E02AKQ-wWs6Hk" \

# curl \
#   -X OPTIONS \
#   -H "Content-Type: application/json" \
#   -H Authorization: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwMjQzMDkzLCJqdGkiOiJhMTMyYTI1ZTRiZTI0ZjVhYTUzN2M3YmQ5MzMzMTE5NyIsInVzZXJfaWQiOjF9.KTaljwD4sFSsMVmTg5pU69By4PDlZas1vAekdt8IMeI" \
#   http://localhost:8000/api/auth/user/me/


# curl --header "Content-Type: application/json" - X POST http://127.0.0.1:8000/api/auth/token/obtain/ -- data '{"username":"admin","password":"batyrbet"}'
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTM4MjI1OCwianRpIjoiNmFjYWY2ZDdlODQ2NDQzYjhhYjY0YTA2YWU3ZTVmMjkiLCJ1c2VyX2lkIjoyfQ.XGc3NZS0wgiFcCZJKiwj-Qu1i0k6T6E8kQGo-Xg7pbg
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTM4MjMzOSwianRpIjoiOGIyZWI2NTAzMWVlNDk3MmI3MjY0YjRhMTIwOTIyOGIiLCJ1c2VyX2lkIjoyfQ.UbE1iZGmNhEzCrmOcDwSY99RL_yVJdE5ARe2mz33lDM
# curl \
#   -X POST \
#   -H "Content-Type: application/json" \
#   -d '{"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTM4MjM4NiwianRpIjoiMmY1NTMwNmVkZWNjNGQyYWIyZmVlYjNhYzMxNTZlNDEiLCJ1c2VyX2lkIjoyfQ.trm9v_i4aJ3HKZJnVF4Axs201nBMaXidSC1S0zYn95k"}' \
#   http://localhost:8000/api/auth/token/refresh/


# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTM4MjM4NiwianRpIjoiMmY1NTMwNmVkZWNjNGQyYWIyZmVlYjNhYzMxNTZlNDEiLCJ1c2VyX2lkIjoyfQ.trm9v_i4aJ3HKZJnVF4Axs201nBMaXidSC1S0zYn95k

# "{
#     "username":"pk",
#     "password":"batyrbet",
# }"

# {"username": "admin", "password": "batyrbet", "phone_number":63000000}
