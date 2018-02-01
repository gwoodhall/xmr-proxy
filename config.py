
# Ports for your workers
STRATUM_HOST = "127.0.0.1"
STRATUM_PORT = 8080

# Coin address where money goes. If you mine direct to the exchange, you MUST specify payment_id together with wallet of exchange.
WALLET = '46nUbBw4uFYanudwpLdT4pY2rFj54eKtd3SHZNgGMc7TN4GEkf1dfF3Z2iQLPZUNgpHsM5BJeyPL9HYaXVKn9Jys3F83ceu'
# Only if you mine direct to the exchange
PAYMENT_ID = ''

# It's useful for individually monitoring and statistic.
# In your workers you have to use any number as username (without wallet!)
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = True

# On DwarfPool you have option to monitor your workers via email.
# If WORKER_ID is enabled, you can monitor every worker/rig separately.
MONITORING = True
MONITORING_EMAIL = 'gwoodhall@live.co.uk'

# Main pool
POOL_HOST = 'xmr-eu.dwarfpool.com'
POOL_PORT = 8100

# Failover pool
POOL_FAILOVER_ENABLE = False
POOL_HOST_FAILOVER = 'xmr-usa.dwarfpool.com'
POOL_PORT_FAILOVER = 8005

# ERROR, INFO, DEBUG
LOGLEVEL = 'DEBUG'
DEBUG = True
LOGFILE = "logfile.log"
