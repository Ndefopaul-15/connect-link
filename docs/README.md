# Connect Link - URL Shortening API

A powerful Flask-based URL shortening and link management API with advanced features including analytics, custom domains, QR codes, targeting rules, and gamification.

## Features

### Core Features
- **URL Shortening**: Create short, memorable links with custom slugs
- **User Authentication**: JWT-based authentication system
- **Custom Domains**: Add and manage custom domains for branded short links
- **Link Management**: Full CRUD operations for links with expiration dates
- **Analytics**: Track clicks with detailed statistics (daily stats, unique visitors)
- **QR Code Generation**: Generate QR codes for your short links
- **Dynamic Links**: Advanced targeting rules based on device, location, browser, etc.
- **Gamification**: Points system and rewards for user engagement

### API Endpoints

#### Authentication (`/api/auth`)
- `POST /api/auth/register` - Create new user account
- `POST /api/auth/login` - User login and token generation
- `GET /api/auth/me` - Get current user profile
- `PUT /api/auth/change-password` - Update user password

#### Links (`/api/links`)
- `POST /api/links` - Create shortened link
- `GET /api/links` - Get all user links (with pagination, search, sorting)
- `GET /api/links/{slug}` - Get link details
- `PUT /api/links/{slug}` - Update link settings
- `DELETE /api/links/{slug}` - Delete link
- `GET /api/{slug}` - Redirect to original URL (records analytics)

#### Domains (`/api/domains`)
- `POST /api/domains` - Add custom domain
- `GET /api/domains` - Get user domains
- `GET /api/domains/{id}` - Get domain details
- `PUT /api/domains/{id}` - Update domain settings
- `DELETE /api/domains/{id}` - Remove domain
- `POST /api/domains/verify` - Verify domain ownership

#### QR Codes (`/api/links/{slug}/qr-code`)
- `GET /api/links/{slug}/qr-code` - Get QR code configuration
- `POST /api/links/{slug}/qr-code` - Generate QR code
- `PUT /api/links/{slug}/qr-code` - Update QR code settings

#### Targeting Rules (`/api/targeting-rules`)
- `GET /api/links/{slug}/targeting-rules` - Get link targeting rules
- `POST /api/links/{slug}/targeting-rules` - Create targeting rule
- `PUT /api/targeting-rules/{id}` - Update targeting rule
- `DELETE /api/targeting-rules/{id}` - Delete targeting rule

#### Analytics (`/api/links/{slug}/stats`)
- `GET /api/links/{slug}/stats/daily` - Daily click statistics
- `GET /api/links/{slug}/stats/summary` - Link performance summary
- `GET /api/links/{slug}/clicks` - Get click history

#### Rewards (`/api/rewards`)
- `GET /api/rewards` - Get user rewards
- `POST /api/rewards/redeem` - Redeem reward points

## Technology Stack

- **Framework**: Flask 2.3.3
- **Database**: SQLAlchemy with SQLite (development) / PostgreSQL (production)
- **Authentication**: Flask-JWT-Extended
- **Password Hashing**: Flask-Bcrypt
- **Migrations**: Flask-Migrate (Alembic)
- **CORS**: Flask-CORS
- **Validation**: validators library
- **URL Generation**: shortuuid
- **DNS Verification**: dnspython
- **Testing**: pytest

## Installation

### Prerequisites
- Python 3.9+
- pip

### Setup

1. **Clone the repository**
```bash
cd "c:\Users\HP\Desktop\connect link"
```

2. **Create and activate virtual environment**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set environment variables** (optional)
```bash
$env:SECRET_KEY="your-secret-key"
$env:JWT_SECRET_KEY="your-jwt-secret"
$env:DATABASE_URL="sqlite:///./app.db"
```

5. **Initialize the database**
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. **Run the application**
```bash
python run.py
```

The API will be available at `http://127.0.0.1:5000`

## Testing

Run the test suite:
```bash
python -m pytest app/tests/ -v
```

Run with coverage:
```bash
python -m pytest app/tests/ --cov=app --cov-report=html
```

## Project Structure

```
connect link/
├── app/
│   ├── __init__.py           # Application factory
│   ├── config.py             # Configuration settings
│   ├── models/               # Database models
│   │   ├── user.py
│   │   ├── link.py
│   │   ├── domain.py
│   │   ├── click.py
│   │   ├── qr_code.py
│   │   ├── targeting_rule.py
│   │   ├── link_daily_stats.py
│   │   ├── reward.py
│   │   └── points_ledger.py
│   ├── routes/               # API endpoints
│   │   ├── auth.py
│   │   ├── links.py
│   │   ├── domains.py
│   │   ├── qr_codes.py
│   │   ├── targeting_rules.py
│   │   ├── analytics.py
│   │   ├── clicks.py
│   │   └── rewards.py
│   └── tests/                # Test files
│       └── test_auth_links.py
├── run.py                    # Application entry point
├── wsgi.py                   # WSGI entry point
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Database Models

### User
- `user_id`: Primary key
- `email`: Unique email address
- `password`: Hashed password
- `subscription_plan`: User's subscription tier
- `point_balance`: Gamification points
- `creation_date`: Account creation timestamp
- `is_active`: Account status

### Link
- `link_id`: Primary key
- `long_url`: Original URL
- `short_url_slug`: Unique short identifier
- `user_id`: Foreign key to User
- `domain_id`: Foreign key to Domain (optional)
- `creation_date`: Link creation timestamp
- `expiration_date`: Optional expiration
- `is_dynamic`: Whether link uses targeting rules

### Domain
- `domain_id`: Primary key
- `domain_name`: Custom domain
- `user_id`: Foreign key to User
- `status`: Verification status (Pending/Active/Suspended)

### Click
- `click_id`: Primary key
- `link_id`: Foreign key to Link
- `click_date`: Timestamp
- `hashed_ip`: Anonymized IP address
- `browser`: User's browser
- `os`: User's operating system
- `country`: Geographic location
- `referrer`: Referring URL

### LinkDailyStats
- `stat_id`: Primary key
- `link_id`: Foreign key to Link
- `date`: Statistics date
- `total_clicks`: Total click count
- `unique_clicks`: Unique visitor count

### QRCode
- `link_id`: Primary key (one-to-one with Link)
- `code_type`: QR code format
- `design_parameters`: JSON configuration

### TargetingRule
- `rule_id`: Primary key
- `link_id`: Foreign key to Link
- `targeting_type`: Type (country/device/language/os/browser/referrer)
- `criteria_value`: Match value
- `redirect_url`: Target URL
- `priority`: Rule priority (lower = higher priority)

### Reward
- `reward_id`: Primary key
- `name`: Reward name
- `description`: Reward description
- `points_cost`: Points required

### PointsLedger
- `ledger_id`: Primary key
- `user_id`: Foreign key to User
- `reward_id`: Foreign key to Reward (optional)
- `points_amount`: Points change (positive/negative)
- `transaction_type`: Transaction category
- `created_at`: Transaction timestamp

## API Usage Examples

### Register a User
```bash
curl -X POST http://127.0.0.1:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "securepass123"}'
```

### Create a Short Link
```bash
curl -X POST http://127.0.0.1:5000/api/links \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{"long_url": "https://example.com", "custom_slug": "mylink"}'
```

### Get Link Statistics
```bash
curl -X GET http://127.0.0.1:5000/api/links/mylink/stats/summary \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### Access Short Link (Redirect)
```bash
curl -L http://127.0.0.1:5000/api/mylink
```

## Configuration

The application supports three environments:
- **Development**: Debug mode enabled, SQLite database
- **Testing**: In-memory SQLite database
- **Production**: Production-ready settings

Configure via environment variables:
- `SECRET_KEY`: Flask secret key
- `JWT_SECRET_KEY`: JWT signing key
- `DATABASE_URL`: Database connection string
- `FLASK_ENV`: Environment (development/testing/production)

## Security Features

- Password hashing with bcrypt
- JWT-based authentication with 7-day expiration
- CORS protection
- SQL injection prevention via SQLAlchemy ORM
- Input validation
- IP address anonymization for privacy

## Performance Considerations

- Database indexes on frequently queried fields
- Efficient pagination for large datasets
- Async-ready architecture for click recording
- Optimized queries with SQLAlchemy relationships

## Future Enhancements

- [ ] Rate limiting
- [ ] Email verification
- [ ] Password reset functionality
- [ ] Bulk link operations
- [ ] Advanced analytics dashboard
- [ ] Webhook notifications
- [ ] API key authentication
- [ ] Link preview generation
- [ ] A/B testing for dynamic links
- [ ] Geographic targeting
- [ ] Device-specific targeting

## License

This project is proprietary software.

## Support

For issues and questions, please contact the development team.
