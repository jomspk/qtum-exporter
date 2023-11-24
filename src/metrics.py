#!/usr/bin/env python3

from prometheus_client import (
    Gauge, Counter
)

# Staking info
QTUM_STAKINGINFO_ENABLE: Gauge = Gauge(
    "qtum_stakinginfo_enable", "Enable or not"
)
QTUM_STAKINGINFO_STAKING: Gauge = Gauge(
    "qtum_stakinginfo_staking", "Staking or not"
)
QTUM_STAKINGINFO_POOLEDTX: Gauge = Gauge(
    "qtum_stakinginfo_pooledtx", "pooled transaction"
)
QTUM_STAKINGINFO_DIFFICULTY: Gauge = Gauge(
    "qtum_stakinginfo_difficulty", "Difficulty"
)
QTUM_STAKINGINFO_SEARCHINTERVAL: Gauge = Gauge(
    "qtum_stakinginfo_searchinterval", "search interval"
)
QTUM_STAKINGINFO_WEIGHT: Gauge = Gauge(
    "qtum_stakinginfo_weight", "weight"
)
QTUM_STAKINGINFO_DELEGATEWEIGHT: Gauge = Gauge(
    "qtum_stakinginfo_delegateweight", "delegate weight"
)
QTUM_STAKINGINFO_NETSTAKEWEIGHT: Gauge = Gauge(
    "qtum_stakinginfo_netstakeweight", "netstake weight"
)
QTUM_STAKINGINFO_EXPECTEDTIME: Gauge = Gauge(
    "qtum_stakinginfo_expectedtime", "expected time"
)

# Qtum exporters metrics
EXPORTER_ERRORS: Counter = Counter(
    "qtum_exporter_errors", "Number of errors encountered by the exporter", labelnames=["type"]
)
PROCESS_TIME: Counter = Counter(
    "qtum_exporter_process_time", "Time spent processing metrics from qtum node"
)
