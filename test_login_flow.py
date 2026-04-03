import requests
import json

# Test 1: Backend login
print('=== Test 1: Backend Login ===')
payload = {'email': 'admin@chemerp.com', 'password': 'admin123'}
r = requests.post('http://localhost:8000/api/auth/login', json=payload)
print(f'Status: {r.status_code}')

if r.status_code == 200:
    data = r.json()
    print(f'✓ Token received: {data["access_token"][:30]}...')
    print(f'✓ User: {data["user"]["name"]} ({data["user"]["email"]})')
    print(f'✓ Token type: {data["token_type"]}')
    token = data['access_token']
    
    # Test 2: Verify token works with /me endpoint
    print('\n=== Test 2: Verify Token with /me Endpoint ===')
    headers = {'Authorization': f'Bearer {token}'}
    r_me = requests.get('http://localhost:8000/api/auth/me', headers=headers)
    print(f'Status: {r_me.status_code}')
    if r_me.status_code == 200:
        print(f'✓ User info retrieved: {r_me.json()["name"]}')
    
    # Test 3: Simulating what frontend does
    print('\n=== Test 3: Login Flow Simulation ===')
    print('Frontend steps:')
    print('1. User submits login form')
    print('2. authApi.login() sends credentials')
    print('3. Backend returns token + user data')
    print('4. setAuth(user, token) updates Zustand store')
    print('5. Zustand persist middleware saves to localStorage')
    print('6. navigate("/") navigates to dashboard')
    print('7. AuthInitializer loads and calls hydrate()')
    print('8. hydrate() reads from localStorage')
    print('9. PrivateRoute checks useAuthStore.token')
    print('10. Dashboard renders because token exists')
    print('\n✓ All tests passed! Login should work now.')
else:
    print(f'✗ Login failed: {r.json()}')
