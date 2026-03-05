# EQX Decision Engine Service

Service for calculating Propensity, Affluence, and Intent scores for customers.

## API Endpoint

### POST /scores

Calculate scores for a customer based on bureau data.

#### Request Body

```json
{
  "Id": 123,
  "customer_id": 2345,
  "bureau_path": "s3://bucket/path/to/bureau/data.json",
  "bureau_type": "CRIF",
  "end_user": "1",
  "Create_date": "2024-01-15"
}
```

#### Response

```json
{
  "Id": 123,
  "customer_id": 2345,
  "Propensity_score": {
    "PL": 1,
    "CC": 1,
    "LAMF": 1,
    "CCBP": 1,
    "CHR": 0,
    "Digital Gold": 0,
    "Insurance": 1
  },
  "Affluence_score": 86,
  "Intent_score": {
    "PL": 97,
    "CC": 22,
    "LAMF": 1,
    "CCBP": 1,
    "CHR": 0,
    "Digital Gold": 0
  }
}
```

## Installation

```bash
pip install -r requirements.txt
```

## Running the Service

### Local Development

```bash
# Using uvicorn directly
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Or using Python
python -m app.main
```

### Docker

#### Build and run with Docker

```bash
# Build the Docker image
docker build -t eqx-de-service .

# Run the container
docker run -p 8000:8000 eqx-de-service
```

#### Using Docker Compose

```bash
# Build and start the service
docker-compose up --build

# Run in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the service
docker-compose down
```

#### Environment Variables

You can set environment variables in docker-compose.yml or create a `.env` file:

```bash
# Example .env file
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
S3_BUCKET=your_bucket_name
LOG_LEVEL=INFO
```

Then update docker-compose.yml to use the .env file:
```yaml
env_file:
  - .env
```

## Testing

You can test the API using curl:

```bash
curl -X POST "http://localhost:8000/scores" \
  -H "Content-Type: application/json" \
  -d '{
    "Id": 123,
    "customer_id": 2345,
    "bureau_path": "s3://bucket/path/to/data.json",
    "bureau_type": "CRIF",
    "end_user": "1",
    "Create_date": "2024-01-15"
  }'
```

Or visit http://localhost:8000/docs for interactive API documentation.

## Project Structure

```
app/
├── __init__.py
├── main.py           # FastAPI application and endpoints
├── models.py         # Pydantic models for request/response and score classes
├── services.py       # Business logic classes for score calculations
└── config.py         # Configuration settings
```

## Score Classes

### PropensityScore
Calculates binary propensity scores (0/1) for products:
- PL (Personal Loan)
- CC (Credit Card)
- LAMF
- CCBP
- CHR
- Digital Gold
- Insurance

### AffluenceScore
Calculates affluence score (0-100) based on customer financial profile.

### IntentScore
Calculates intent scores (0-100) for products:
- PL (Personal Loan)
- CC (Credit Card)
- LAMF
- CCBP
- CHR
- Digital Gold

## Notes

- The current implementation uses placeholder logic. Replace the calculation methods in `services.py` with actual business logic.
- Bureau data loading from S3 needs to be implemented in the calculator classes.
- `bureau_type` is currently hardcoded to "CRIF".
- `end_user` is currently hardcoded to "1".

