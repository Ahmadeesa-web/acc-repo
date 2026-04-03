#!/usr/bin/env python3
import requests
import json

# Test login response structure
payload = {'email': 'admin@chemerp.com', 'password': 'admin123'}
response = requests.post('http://localhost:8000/api/auth/login', json=payload)

print('=== BACKEND RESPONSE ===')
print(f'Status Code: {response.status_code}')
print(f'Response Body:')
data = response.json()
print(json.dumps(data, indent=2))

print('\n=== RESPONSE STRUCTURE ANALYSIS ===')
print(f'Keys in response: {list(data.keys())}')
print(f'user type: {type(data.get("user"))}')
print(f'user keys: {list(data.get("user", {}).keys())}')
print(f'access_token exists: {"access_token" in data}')
print(f'access_token type: {type(data.get("access_token"))}')
print(f'token_type: {data.get("token_type")}')

print('\n=== HOW FRONTEND ACCESSES IT ===')
print('In Login.jsx: res.data.access_token')
print(f'  Where res = axios response from api.post()')
print(f'  res.data = {list(data.keys())}')
print(f'  res.data.access_token = {data.get("access_token")[:40]}...')
print(f'  res.data.user = {data.get("user")}')
print(f'  res.data.user.email = {data.get("user", {}).get("email")}')

print('\n✓ Response structure looks correct!')
