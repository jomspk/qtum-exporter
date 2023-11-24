#!/usr/bin/env python3

from prometheus_client import (
    Gauge, Counter
)

# Staking info
QTUM_STAKINGINFO_ENABLE: Gauge = Gauge(
    "qtum_stakinginfo", "Enable or not"
)
QTUM_STAKINGINFO_STAKING: Gauge = Gauge(
    "qtum_stakinginfo", "Staking or not"
)
QTUM_STAKINGINFO_POOLEDTX: Gauge = Gauge(
    "qtum_stakinginfo", "pooled transaction"
)
QTUM_STAKINGINFO_DIFFICULTY: Gauge = Gauge(
    "qtum_stakinginfo", "Difficulty"
)
QTUM_STAKINGINFO_SEARCHINTERVAL: Gauge = Gauge(
    "qtum_stakinginfo", "search interval"
)
QTUM_STAKINGINFO_WEIGHT: Gauge = Gauge(
    "qtum_stakinginfo", "weight"
)
QTUM_STAKINGINFO_DELEGATEWEIGHT: Gauge = Gauge(
    "qtum_stakinginfo", "delegate weight"
)
QTUM_STAKINGINFO_NETSTAKEWEIGHT: Gauge = Gauge(
    "qtum_stakinginfo", "netstake weight"
)
QTUM_STAKINGINFO_EXPECTEDTIME: Gauge = Gauge(
    "qtum_stakinginfo", "expected time"
)

# Qtum exporters metrics
EXPORTER_ERRORS: Counter = Counter(
    "qtum_exporter_errors", "Number of errors encountered by the exporter", labelnames=["type"]
)
PROCESS_TIME: Counter = Counter(
    "qtum_exporter_process_time", "Time spent processing metrics from qtum node"
)
