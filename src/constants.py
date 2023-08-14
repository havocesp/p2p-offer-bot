AUTHENTICATION_TOKEN_CACHE_KEY = "{provider}_AUTHENTICATION_TOKEN"
AUTHENTICATION_TOKEN_VALIDITY_TIMEDELTA_HRS = 24

CMC_CURRENCY_MARKET_PRICE_CACHE_KEY = (
    "CMC_CURRENCY_MARKET_PRICE_{crypto_currency}_{conversion_fiat_currency}"
)
CMC_CURRENCY_MARKET_PRICE_CACHE_TTL = 180

CURRENCY_CONFIG_AMOUNT_TO_INCREASE_OFFER = "amount_to_increase_offer"
CURRENCY_CONFIG_SEARCH_PRICE_UPPER_MARGIN = "search_price_upper_margin"
CURRENCY_CONFIG_SEARCH_PRICE_LOWER_MARGIN = "search_price_lower_margin"
CURRENCY_CONFIG_OWNER_LAST_SEEN_MAX_TIME = "owner_last_seen_max_time"

CURRENCY_CONFIG_CACHE_NAME = '{config_name}_{currency}_{provider}'

CURRENCY_CONFIGS = [
    CURRENCY_CONFIG_AMOUNT_TO_INCREASE_OFFER,
    CURRENCY_CONFIG_SEARCH_PRICE_UPPER_MARGIN,
    CURRENCY_CONFIG_SEARCH_PRICE_LOWER_MARGIN,
    CURRENCY_CONFIG_OWNER_LAST_SEEN_MAX_TIME,
]
CACHE_MAX_TTL = 3600  # 1h
