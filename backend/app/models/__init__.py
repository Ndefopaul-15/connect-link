from .user import User
from .domain import Domain
from .link import Link
from .qr_code import QRCode
from .targeting_rule import TargetingRule
from .click import Click
from .link_daily_stats import LinkDailyStats
from .reward import Reward
from .points_ledger import PointsLedger

# This makes all models available when importing from app.models
__all__ = [
    'User',
    'Domain',
    'Link',
    'QRCode',
    'TargetingRule',
    'Click',
    'LinkDailyStats',
    'Reward',
    'PointsLedger'
]