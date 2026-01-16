{
  "functions": {
    "api/index.py": { "runtime": "vercel-python@v3" }
  },
  "routes": [
    { "src": "/api/time", "dest": "/api/index.py" }
  ]
}