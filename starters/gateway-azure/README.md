# Gateway Starter - Azure API Management (Pattern 01)

Minimal API Management policy for routing and governing LLM traffic through Azure.

## Prerequisites
- Azure API Management instance (Developer tier or higher)
- Azure OpenAI Service deployed
- Managed identity configured between APIM and Azure OpenAI

## Policy Configuration

Apply this policy to your Azure OpenAI API in APIM:

```xml
<policies>
  <inbound>
    <!-- Rate limiting per subscription -->
    <rate-limit-by-key
      calls="100"
      renewal-period="60"
      counter-key="@(context.Subscription.Id)" />

    <!-- Token budget per subscription (approximate) -->
    <quota-by-key
      calls="10000"
      renewal-period="86400"
      counter-key="@(context.Subscription.Id)" />

    <!-- Log request for governance metrics -->
    <set-variable name="request-start" value="@(DateTime.UtcNow)" />

    <!-- Content safety check on input -->
    <set-variable name="input-content"
      value="@(context.Request.Body.As<JObject>()["messages"]?.Last?["content"]?.ToString() ?? "")" />

    <!-- Block requests containing obvious PII patterns -->
    <choose>
      <when condition="@(System.Text.RegularExpressions.Regex.IsMatch(
        (string)context.Variables["input-content"],
        @"\b\d{3}-\d{2}-\d{4}\b"))">
        <return-response>
          <set-status code="400" reason="PHI Detected" />
          <set-body>{"error": "Request blocked: potential PHI detected in input"}</set-body>
        </return-response>
      </when>
    </choose>

    <!-- Route to Azure OpenAI backend -->
    <set-backend-service base-url="https://your-openai.openai.azure.com" />
    <authentication-managed-identity resource="https://cognitiveservices.azure.com/" />
  </inbound>

  <outbound>
    <!-- Log response metrics -->
    <set-variable name="response-tokens"
      value="@(context.Response.Body.As<JObject>()?["usage"]?["total_tokens"]?.ToString() ?? "0")" />

    <!-- Emit to Application Insights for governance tracking -->
    <trace source="ai-gateway" severity="information">
      <message>@{
        return new JObject(
          new JProperty("subscription", context.Subscription.Id),
          new JProperty("tokens", context.Variables["response-tokens"]),
          new JProperty("latency_ms",
            ((DateTime.UtcNow - (DateTime)context.Variables["request-start"]).TotalMilliseconds)),
          new JProperty("status", context.Response.StatusCode)
        ).ToString();
      }</message>
    </trace>
  </outbound>
</policies>
```

## GAIF-4 Integration

Query Application Insights for T1PR:

```kusto
customEvents
| where name == "ai-gateway"
| where timestamp > ago(7d)
| extend blocked = tobool(customDimensions.phi_blocked)
| summarize
    total = count(),
    blocked = countif(blocked == true),
    t1pr = round(1.0 * countif(blocked == true) / count(), 4)
```
