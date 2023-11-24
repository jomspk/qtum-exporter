#!/usr/bin/env python3
from .rpc import RPC
from .config import Config
from .metrics import (
    # # Staking info
    QTUM_STAKINGINFO_ENABLE, QTUM_STAKINGINFO_STAKING, QTUM_STAKINGINFO_POOLEDTX, QTUM_STAKINGINFO_DIFFICULTY, QTUM_STAKINGINFO_SEARCHINTERVAL, QTUM_STAKINGINFO_WEIGHT, QTUM_STAKINGINFO_DELEGATEWEIGHT, QTUM_STAKINGINFO_NETSTAKEWEIGHT, QTUM_STAKINGINFO_EXPECTEDTIME
)


def collect() -> None:

    with RPC(
        url=f"http://{Config.QTUM_RPC_HOST}:{Config.QTUM_RPC_PORT}",
        rpc_user=Config.QTUM_RPC_USER,
        rpc_password=Config.QTUM_RPC_PASSWORD
    ) as rpc:

        # Set staking info values
        staking_info: dict = rpc.get_staking_info()
        if staking_info["enabled"]:
            QTUM_STAKINGINFO_ENABLE.set(1)
        else:
            QTUM_STAKINGINFO_ENABLE.set(0)
        if staking_info["staking"]:
            QTUM_STAKINGINFO_STAKING.set(1)
        else:
            QTUM_STAKINGINFO_STAKING.set(0)
        QTUM_STAKINGINFO_POOLEDTX.set(staking_info["pooledtx"])
        QTUM_STAKINGINFO_DIFFICULTY.set(staking_info["difficulty"])
        QTUM_STAKINGINFO_SEARCHINTERVAL.set(staking_info["search-interval"])
        QTUM_STAKINGINFO_WEIGHT.set(staking_info["weight"])
        QTUM_STAKINGINFO_DELEGATEWEIGHT.set(staking_info["delegateweight"])
        QTUM_STAKINGINFO_NETSTAKEWEIGHT.set(staking_info["netstakeweight"])
        QTUM_STAKINGINFO_EXPECTEDTIME.set(staking_info["expectedtime"])
