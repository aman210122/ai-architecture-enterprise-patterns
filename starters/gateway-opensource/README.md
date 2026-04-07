# Gateway Starter - Kong with AI Plugin (Pattern 01)

Minimal Kong configuration for routing LLM traffic with rate limiting and content filtering.

## Prerequisites
- Kong Gateway 3.6+ (OSS or Enterprise)
- Kong AI Gateway plugin enabled
- Docker (for local testing)

## Docker Compose (Local Testing)

```yaml
version: '3.8'
services:
  kong:
    image: kong:3.6
    environment:
      KONG_DATABASE: "off"
      KONG_DECLARATIVE_CONFIG: /kong/kong.yml
      KONG_PROXY_LISTEN: "0.0.0.0:8000"
      KONG_ADMIN_LISTEN: "0.0.0.0:8001"
    volumes:
      - ./kong.yml:/kong/kong.yml
    ports:
      - "8000:8000"
      - "8001:8001"
```

## Declarative Config (kong.yml)

```yaml
_format_version: "3.0"

services:
  - name: openai-service
    url: https://api.openai.com
    routes:
      - name: llm-route
        paths:
          - /ai/chat
        methods:
          - POST

plugins:
  # Rate limiting
  - name: rate-limiting
    service: openai-service
    config:
      minute: 100
      policy: local

  # Request size limiting (prevent prompt injection via large payloads)
  - name: request-size-limiting
    service: openai-service
    config:
      allowed_payload_size: 128  # KB

  # Logging for governance metrics
  - name: file-log
    service: openai-service
    config:
      path: /tmp/ai-gateway.log
      reopen: true

  # AI Gateway plugin (Kong Enterprise)
  # - name: ai-proxy
  #   service: openai-service
  #   config:
  #     route_type: llm/v1/chat
  #     model:
  #       provider: openai
  #       name: gpt-4o
```

## Usage

```bash
curl -X POST http://localhost:8000/ai/chat \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```
